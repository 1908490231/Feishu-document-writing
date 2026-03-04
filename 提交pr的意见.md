Verify each finding against the current code and only fix it if needed.

Inline comments:
In `@src/copaw/agents/skills/feishu_write/scripts/auth.py`:
- Around line 18-36: get_token currently caches self._token forever and makes
the POST without a timeout; update get_token to store both the token and its
expiry timestamp (read expiry/expire or expires_in from the response) and
refresh the token when now + 60s >= expiry, using a timeout on requests.post
(e.g. timeout=...) and resp.raise_for_status()/resp.json() as before; ensure
thread-safety around reading/updating self._token and expiry (e.g. use a lock on
the instance) and keep the same parameters app_id/app_secret and TOKEN_URL so
callers of get_token see identical behavior but with expiry-aware refresh and a
request timeout.

In `@src/copaw/agents/skills/feishu_write/scripts/doc_writer.py`:
- Around line 116-121: The deletion loop silently ignores HTTP/API failures when
deleting blocks (for block_id in blocks...), so update the code in the method
containing that loop (referencing variables block, block_id, document_id,
delete_url and headers from self._headers()) to check the requests.delete
response: if the HTTP status is not 2xx or the API response indicates an error,
log the failure and return False (or raise an exception) instead of continuing;
include response.status_code and response.text (or parsed JSON error) in the log
to aid debugging and ensure the caller sees that clearing content failed rather
than unconditionally returning True.
- Line 40: The Feishu HTTP calls in class DocWriter lack explicit timeouts; add
a class-level constant REQUEST_TIMEOUT = 30 and update every outbound requests
call in DocWriter (e.g., create_document, get_document_block_id, append_blocks,
list_documents_in_folder, delete_document_content, move_to_wiki,
create_wiki_document, get_wiki_space_id, create_image_block,
replace_image_token, create_table, get_table_cells, fill_table_cell, fill_table)
to pass timeout=self.REQUEST_TIMEOUT to requests.get/post/patch/delete
invocations so all HTTP requests use a 30s timeout.
- Around line 85-100: The list_documents_in_folder function only fetches the
first page (page_size 200) so duplicates in larger folders are missed; modify
list_documents_in_folder to paginate through all pages by repeatedly calling
requests.get with the same URL/params and using the API’s pagination token/next
cursor from result (e.g. result["data"]["next_cursor"] or similar) until no more
pages, appending each page’s files into a single list to return; ensure you keep
using self._headers() and preserve the existing error checks
(resp.raise_for_status() and result.get("code") != 0) for each request.

In `@src/copaw/agents/skills/feishu_write/scripts/feishu_writer.py`:
- Around line 66-68: The current validation in feishu_writer.py that exits when
args.target == "wiki" only allows operation if --wiki-token or
FEISHU_DEFAULT_WIKI_SPACE_ID exists, which incorrectly rejects configurations
that provide FEISHU_DEFAULT_WIKI_NODE_TOKEN instead; update the conditional that
checks args.target, args.wiki_token and environment variables so it permits
cases where FEISHU_DEFAULT_WIKI_NODE_TOKEN is set (i.e., require exit only when
neither args.wiki_token nor FEISHU_DEFAULT_WIKI_SPACE_ID nor
FEISHU_DEFAULT_WIKI_NODE_TOKEN are present), and adjust the printed error text
to mention both FEISHU_DEFAULT_WIKI_SPACE_ID and FEISHU_DEFAULT_WIKI_NODE_TOKEN
as acceptable environment fallbacks.
- Around line 96-155: The loop over files currently lets exceptions propagate
and halt the batch; wrap the per-file processing (the body using
writer.write_file and writer.update_document, duplicate handling that parses
result["message"], and the success/fail counting logic) in a try/except around
each iteration, catch Exception as e, increment fail_count, print/log a clear
error message including file.name and str(e), and continue to the next file so
one failure does not terminate the whole run; ensure all uses of
writer.write_file and writer.update_document and the duplicate-handling branch
remain inside the try block so any unexpected error is handled.

In `@src/copaw/agents/skills/feishu_write/scripts/parser.py`:
- Line 217: Remove the unused local variable by deleting the assignment to
full_match (the match.group(0) assignment) inside the inline parser function in
parser.py; locate the code that sets full_match = match.group(0) (within the
inline parsing logic) and remove that line so the unused variable is not
created.

In `@src/copaw/agents/skills/feishu_write/scripts/uploader.py`:
- Around line 123-124: Replace the no-op f-string print call print(f"警告: 缺少
parent_node 参数") with a plain string (e.g., print("警告: 缺少 parent_node 参数")) or,
preferably, use the module's logger to emit the warning; locate the call in
uploader.py (the print in the parent_node check) and update it accordingly to
avoid F541.
- Around line 151-153: The POST upload call in uploader.py (requests.post to
self.UPLOAD_URL inside the upload flow) lacks a timeout and can block
indefinitely; modify the upload request in the uploader method that builds
headers/files/data (the block with resp = requests.post(self.UPLOAD_URL, ...))
to pass a timeout (e.g. timeout=30) consistent with the download method, and
ensure resp.raise_for_status() remains after the timed request so failures are
still raised.

In `@src/copaw/agents/skills/feishu_write/scripts/writer.py`:
- Around line 108-116: The code treats append_blocks results as ignorable so
partial failures still return success; update the create/update flows
(functions/methods using _write_content_with_images, create_doc/create_block or
update_doc/update_block and the append_blocks call) to capture and check the
boolean return of append_blocks (and any other write helpers), aggregate
per-block/write success into a final status, and if any write fails return
success: False with an error message (including doc_id/node_token where helpful)
instead of the current success response; ensure the same change is applied to
all affected paths referenced in this file (the create path around
uploaded_images assignment and the update paths noted in the comment ranges).
- Around line 242-244: The call to
self.doc_writer.delete_document_content(document_id) must have its result
checked so a failed clear doesn't let subsequent writes append to stale content;
update the code to capture the return/exception from delete_document_content and
handle failures (raise/log and abort or retry) before calling any write/append
method (e.g., whatever method you use after delete to write content), ensuring
you only proceed to write when delete_document_content indicates success.

In `@src/copaw/agents/skills/feishu_write/SKILL.md`:
- Around line 46-51: The fenced env example in SKILL.md is missing a language
tag (MD040); update the fenced block that contains the FEISHU_* environment
variables to include a language specifier (e.g., "dotenv") after the opening
triple backticks so the block becomes a proper dotenv code fence.

---

Nitpick comments:
In `@src/copaw/agents/skills/feishu_write/scripts/__init__.py`:
- Around line 12-18: The __all__ export list is unsorted which causes unstable
export order and triggers RUF022; sort the entries in the __all__ list
(FeishuAuth, FeishuDocWriter, FeishuImageUploader, FeishuWriter, MarkdownParser)
into alphabetical order and update the __all__ definition so the module exports
are stable and lint-compliant.