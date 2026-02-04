![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3rDtTibZ29N2CPNicFSqhKBic6ETXvJvrCIkrnCvKfX09LKmtibQ0URhSjUPN084NEVeL6xic4tRqLxXqg/0?wx_fmt=jpeg)

#  从 Chat 到 Agent：Claude Agent SDK 才是 AI 真正的生产力开关

如果你曾经使用过 Claude Code CLI，一定会被它强大的代码理解和编辑能力所震撼。但你是否想过，能不能把这种能力集成到自己的应用中？能不能让 AI
智能体在 CI/CD 流程中自动修复 Bug？能不能构建一个全自动化的代码审查系统？  Claude Agent SDK
就是为此而生的。它让开发者能够以程序化的方式使用 Claude 的能力，将交互式的开发体验转化为生产级的自动化工具。  

##  > 01\.  Claude Agent SDK 是什么？

Claude Agent SDK 是 Anthropic 官方提供的框架，用于构建生产级的 AI 智能体。简单来说，它让你能够：

• **编写自主代理** ：自动读取文件、运行命令、搜索网页、编辑代码

• **生产自动化** ：构建 CI/CD 流程、任务自动化、批量处理

• **应用集成** ：嵌入到现有应用或 API 中

• **自定义工作流** ：通过 hooks、权限和会话管理实现复杂场景

与 Claude Code CLI 的交互式体验不同，Claude Agent SDK 提供的是完全可编程的
API，让你能够在代码中精确控制智能体的每一个行为。

###  核心功能一览

Claude Agent SDK 提供了丰富的内置工具和特性：

**文件操作：** Read(读文件)、Write(写文件)、Edit(编辑文件)

**命令执行：** Bash(运行命令)、后台任务管理

**代码搜索：** Glob(文件匹配)、Grep(内容搜索)

**网络功能：** WebSearch(网络搜索)、WebFetch(获取网页)

**高级特性：** Hooks(拦截器)、权限系统、会话管理、子代理、MCP 集成

##  > 02\.  快速开始：5 分钟创建第一个智能体

###  第一步：安装

首先安装 Claude Code（SDK 的运行时）：

# macOS/Linux/WSL  
curl -fsSL https://claude.ai/install.sh | bash   

# 或者使用 Homebrew  
brew install --cask claude-code  

# 或者使用 npm  
npm install -g @anthropic-ai/claude-code  
---  

然后安装 SDK：

# Python  
pip install claude-agent-sdk  

# TypeScript/Node.js  
npm install @anthropic-ai/claude-agent-sdk  
---  

###  第二步：配置 API 密钥

# 设置环境变量  
export  ANTHROPIC_API_KEY=your-api-key  

# 在 https://console.anthropic.com/ 获取 API 密钥  
---

###  第三步：编写第一个智能体

Python 版本：

import  asyncio  
from  claude_agent_sdk  import  query, ClaudeAgentOptions  

async  def  main  ():  
async  for  message  in  query  (  
prompt=  "列出当前目录的所有 Python 文件"  ,  
options=  ClaudeAgentOptions  (  
allowed_tools=[  "Glob"  ,  "Read"  ],  
permission_mode=  "acceptEdits"  
)  
):  
if  hasattr  (message,  'content'  ):  
for  block  in  message.content:  
if  hasattr  (block,  'text'  ):  
print  (block.text)  

asyncio.  run  (main())  
---  

TypeScript 版本：

import  { query }  from  "@anthropic-ai/claude-agent-sdk"  ;  

async  function  main  () {  
for  await  (  const  message  of  query  ({  
prompt:  "列出当前目录的所有 Python 文件"  ,  
options: {  
allowedTools: [  "Glob"  ,  "Read"  ],  
permissionMode:  "acceptEdits"  
}  
})) {  
if  (message.type ===  "assistant"  && message.message?.content) {  
for  (  const  block  of  message.message.content) {  
if  (  "text"  in  block) {  
console.  log  (block.text);  
}  
}  
}  
}  
}  

main().  catch  (console.error);  
---  

运行这个简单的例子，你就创建了第一个智能体！

##  > 03\.  核心概念深度解析

###  1\. 智能体执行循环

Claude Agent SDK 实现了一个完整的智能体决策循环：

用户提示  
↓  
Claude 分析并决定使用哪个工具  
↓  
SDK 执行工具（内置工具由 SDK 自动处理）  
↓  
将执行结果反馈给 Claude  
↓  
Claude 分析结果并决定继续或完成  
↓  
返回最终结果给用户  
---  

这个循环是完全自主的，Claude 会根据任务需求自动选择合适的工具，无需人工干预。

###  2\. 工具系统架构

SDK 提供了丰富的内置工具：

**文件操作工具**

•  Read  ：读取任何格式的文件（支持图片、PDF、Jupyter 笔记本等）

•  Write  ：创建新文件

•  Edit  ：精确修改现有文件的特定部分

**命令执行工具**

•  Bash  ：运行终端命令

•  BashOutput  ：获取后台任务输出

•  KillBash  ：终止后台进程

**搜索工具**

•  Glob  ：文件模式匹配（如  **/*.py  ）

•  Grep  ：基于正则表达式的内容搜索

**网络工具**

•  WebSearch  ：网络搜索（仅限美国）

•  WebFetch  ：获取网页内容

**高级工具**

•  Task  ：委派给子代理处理特定任务

•  TodoWrite  ：跟踪任务进度

###  3\. 权限系统

权限系统是 Claude Agent SDK 的核心安全特性。它按照以下优先级进行检查：

1\. PreToolUse Hook（前置拦截）  
2\. Deny 规则（拒绝优先）  
3\. Allow 规则（明确允许）  
4\. Ask 规则（需要确认）  
5\. 权限模式检查  
6\. canUseTool 回调  
7\. PostToolUse Hook（后置处理）  
---  

示例：实现文件保护

async  def  protect_sensitive_files  (tool_name, input_data):  
"""禁止修改敏感文件"""  
if  tool_name  in  [  "Write"  ,  "Edit"  ]:  
file_path = input_data.  get  (  "file_path"  ,  ""  )  
# 保护 .env 和配置文件  
if  any  (pattern  in  file_path  for  pattern  in  [  ".env"  ,
"config.json"  ,  "secrets"  ]):  
return  {  
"behavior"  :  "deny"  ,  
"message"  :  "不允许修改敏感配置文件"  
}  
return  {  "behavior"  :  "allow"  ,  "updatedInput"  : input_data}  

async  for  message  in  query  (  
prompt=  "重构代码库"  ,  
options=  ClaudeAgentOptions  (  
allowed_tools=[  "Read"  ,  "Write"  ,  "Edit"  ],  
can_use_tool=protect_sensitive_files  
)  
):  
print  (message)  
---  

###  4\. Hooks：拦截和扩展

Hooks 允许你在工具执行的关键点插入自定义逻辑。支持的 Hook 类型：

•  PreToolUse  ：工具执行前

•  PostToolUse  ：工具执行后

•  Stop  ：智能体停止时

•  PreUserPromptSubmit  ：用户输入提交前

•  PreAgentMessageSubmit  ：智能体消息提交前

示例：实现审计日志

import  asyncio  
from  datetime  import  datetime  

async  def  audit_logger  (input_data, tool_use_id, context):  
"""记录所有文件修改操作"""  
tool_name = input_data.  get  (  'tool_name'  ,  'unknown'  )  
file_path = input_data.  get  (  'tool_input'  , {}).  get  (  'file_path'  ,
'unknown'  )  

with  open  (  './audit.log'  ,  'a'  )  as  f:  
timestamp = datetime.  now  ().  isoformat  ()  
f.  write  (  f"  {  timestamp  }  |  {  tool_name  }  |  {  file_path  }  \n"  )   

return  {}  

async  for  message  in  query  (  
prompt=  "重构身份验证模块"  ,  
options=  ClaudeAgentOptions  (  
allowed_tools=[  "Read"  ,  "Edit"  ],  
permission_mode=  "acceptEdits"  ,  
hooks={  
"PostToolUse"  : [  
HookMatcher  (  
matcher=  "Edit|Write"  ,  # 只监控修改操作  
hooks=[audit_logger]  
)  
]  
}  
)  
):  
print  (message)  
---  

###  5\. 会话管理

会话管理让你能够维护持续的对话上下文：

async  def  continuous_conversation  ():  
# 第一次查询  
session_id =  None  
async  for  message  in  query  (  
prompt=  "读取 authentication.py 文件"  ,  
options=  ClaudeAgentOptions  (allowed_tools=[  "Read"  ])  
):  
if  hasattr  (message,  'subtype'  )  and  message.subtype ==  'init'  :  
session_id = message.session_id  

# 恢复会话，Claude 记得之前读取的内容  
if  session_id:  
async  for  message  in  query  (  
prompt=  "找出所有调用这个文件的地方"  ,  # Claude 知道"这个文件"是什么  
options=  ClaudeAgentOptions  (resume=session_id)  
):  
print  (message)  
---  

还可以分叉会话进行实验：

# 创建会话分支，不影响原会话  
async  for  message  in  query  (  
prompt=  "尝试另一种重构方案"  ,  
options=  ClaudeAgentOptions  (  
resume=session_id,  
fork_session=  True  # 创建新分支  
)  
):  
print  (message)  
---  

##  > 04\.  实战场景

###  场景 1：自动化代码审查

async  def  code_review_agent  ():  
"""完整的代码审查智能体"""  
async  for  message  in  query  (  
prompt=  """  
对整个代码库进行全面审查：  
1\. 查找安全漏洞（SQL 注入、XSS、CSRF 等）  
2\. 识别性能问题（N+1 查询、内存泄漏等）  
3\. 检查代码风格一致性  
4\. 生成详细的审查报告  
"""  ,  
options=  ClaudeAgentOptions  (  
allowed_tools=[  "Read"  ,  "Glob"  ,  "Grep"  ],  
system_prompt=  "你是一位资深代码审查专家，专注于安全性和性能优化"  
)  
):  
if  hasattr  (message,  'content'  ):  
for  block  in  message.content:  
if  hasattr  (block,  'text'  ):  
print  (block.text)  
---  

###  场景 2：自动化测试和修复

async  def  auto_test_fix  ():  
"""自动编写测试并修复失败"""  
async  for  message  in  query  (  
prompt=  """  
为 utils.py 编写完整的单元测试：  
1\. 分析函数逻辑  
2\. 编写测试用例  
3\. 运行测试  
4\. 如果有失败，分析原因并修复  
5\. 重新运行确保全部通过  
"""  ,  
options=  ClaudeAgentOptions  (  
allowed_tools=[  "Read"  ,  "Write"  ,  "Edit"  ,  "Bash"  ,  "Glob"  ],  
permission_mode=  "acceptEdits"  
)  
):  
print  (message)  
---  

###  场景 3：自定义 MCP 工具

MCP（Model Context Protocol）允许你创建自定义工具：

from  claude_agent_sdk  import  tool, create_sdk_mcp_server  

@tool  (  "calculate"  ,  "执行数学运算"  , {  "expression"  :  str  })  
async  def  calculate  (args):  
"""自定义计算器工具"""  
try  :  
# 安全地评估数学表达式  
result =  eval  (args[  "expression"  ], {  "__builtins__"  : {}})  
return  {  
"content"  : [{  "type"  :  "text"  ,  "text"  :  f"计算结果：  {  result  }  "  }]  
}  
except  Exception  as  e:  
return  {  
"content"  : [{  "type"  :  "text"  ,  "text"  :  f"计算错误：  {  str  (e)  }  "
}],  
"is_error"  :  True  
}  

# 创建 MCP 服务器  
calculator_server = create_sdk_mcp_server(  
name=  "calculator"  ,  
version=  "1.0.0"  ,  
tools=[calculate]  
)  

# 在智能体中使用  
async  for  message  in  query  (  
prompt=  "计算 123 * 456 + 789"  ,  
options=  ClaudeAgentOptions  (  
mcp_servers={  "calc"  : calculator_server},  
allowed_tools=[  "mcp__calc__calculate"  ]  
)  
):  
print  (message)  
---  

###  场景 4：子代理委派

将复杂任务分解给专门的子代理：

async  def  subagent_delegation  ():  
"""使用专门的代码审查子代理"""  
async  for  message  in  query  (  
prompt=  "使用代码审查代理检查整个代码库"  ,  
options=  ClaudeAgentOptions  (  
allowed_tools=[  "Read"  ,  "Glob"  ,  "Grep"  ,  "Task"  ],  
agents={  
"code-reviewer"  :  AgentDefinition  (  
description=  "专业代码审查专家"  ,  
prompt=  "分析代码质量并提出改进建议"  ,  
tools=[  "Read"  ,  "Glob"  ,  "Grep"  ]  
)  
}  
)  
):  
print  (message)  
---  

##  > 05\.  最佳实践

###  1\. 最小化权限原则

# ✅ 好的做法：只授予必要的权限  
options =  ClaudeAgentOptions  (  
allowed_tools=[  "Read"  ,  "Glob"  ],  # 只读操作  
permission_mode=  "default"  
)  

# ❌ 避免：过度授权  
options =  ClaudeAgentOptions  (  
permission_mode=  "bypassPermissions"  # 仅在完全可信环境中使用  
)  
---  

###  2\. 实现分层权限检查

async  def  layered_security  (tool_name, input_data):  
"""多层安全检查"""  
if  tool_name ==  "Bash"  :  
cmd = input_data.  get  (  "command"  ,  ""  )  

# 黑名单：危险命令  
dangerous_patterns = [  "rm -rf /"  ,  "sudo"  ,  "dd if="  ,  "mkfs"  ]  
if  any  (pattern  in  cmd  for  pattern  in  dangerous_patterns):  
return  {  "behavior"  :  "deny"  ,  "message"  :  "检测到危险命令"  }  

# 白名单：仅允许特定命令  
allowed_commands = [  "git"  ,  "npm"  ,  "pytest"  ,  "ls"  ,  "cat"  ]  
if  not  any  (cmd.  startswith  (allowed)  for  allowed  in
allowed_commands):  
return  {  "behavior"  :  "ask"  ,  "message"  :  f"是否允许执行：  {  cmd  }  "  }  

return  {  "behavior"  :  "allow"  ,  "updatedInput"  : input_data}  
---  

###  3\. 错误处理

from  claude_agent_sdk  import  (  
CLINotFoundError,  
ProcessError,  
CLIJSONDecodeError  
)  

try  :  
async  for  message  in  query  (prompt=  "执行任务"  ):  
process_message  (message)  
except  CLINotFoundError:  
print  (  "请先安装 Claude Code：npm install -g @anthropic-ai/claude-code"  )  
except  ProcessError  as  e:  
print  (  f"进程失败，退出码：  {  e.exit_code  }  "  )  
print  (  f"错误信息：  {  e  }  "  )  
except  CLIJSONDecodeError  as  e:  
print  (  f"JSON 解析错误：  {  e  }  "  )  
except  Exception  as  e:  
print  (  f"未预期的错误：  {  e  }  "  )  
---  

###  4\. 性能优化

# ✅ 设置合理的最大轮次  
options =  ClaudeAgentOptions  (  
max_turns=  10  # 防止无限循环  
)  

# ✅ 限制工具集合  
options =  ClaudeAgentOptions  (  
allowed_tools=[  "Read"  ,  "Grep"  ]  # 比允许所有工具更快  
)  

# ✅ 在 CI/CD 中跳过权限检查  
options =  ClaudeAgentOptions  (  
permission_mode=  "bypassPermissions"  ,  # 仅在可信环境  
allowed_tools=[  "Read"  ,  "Write"  ,  "Edit"  ,  "Bash"  ]  
)  
---  

###  5\. 安全注意事项

# ✅ 限制文件访问范围  
options =  ClaudeAgentOptions  (  
add_dirs=[  "/safe/project/directory"  ],  # 仅允许特定目录  
cwd=  "/safe/project/directory"  
)  

# ✅ 掩盖日志中的敏感信息  
def  sanitize_log  (message):  
"""清理敏感信息"""  
sensitive_patterns = [  "password"  ,  "api_key"  ,  "token"  ,  "secret"  ]  
sanitized =  str  (message)  
for  pattern  in  sensitive_patterns:  
if  pattern  in  sanitized.  lower  ():  
sanitized = sanitized.  replace  (pattern,  "***"  )  
return  sanitized  

# 在记录日志时使用  
logging.  info  (  sanitize_log  (message))  
---  

##  > 06\.  Claude Agent SDK vs Claude Code CLI

两者是什么关系？何时使用哪个？

###  核心区别

**使用方式：**  
• Claude Code CLI：交互式命令行  
• Claude Agent SDK：程序化 API

**主要场景：**  
• Claude Code CLI：开发调试、一次性任务  
• Claude Agent SDK：生产自动化、CI/CD

**权限管理：**  
• Claude Code CLI：UI 提示或配置文件  
• Claude Agent SDK：代码级控制

**会话管理：**  
• Claude Code CLI：自动保存历史  
• Claude Agent SDK：显式管理

**集成方式：**  
• Claude Code CLI：IDE 插件  
• Claude Agent SDK：应用内嵌入

###  配置共享

两者可以共享配置文件（CLAUDE.md 和 .claude/ 目录）：

# 加载项目的 CLAUDE.md 配置  
options =  ClaudeAgentOptions  (  
system_prompt={  
"type"  :  "preset"  ,  
"preset"  :  "claude_code"  
},  
setting_sources=[  "project"  ]  # 加载 .claude/settings.json  
)  
---  

###  使用建议

**使用 Claude Code CLI：**

• 交互式开发和调试

• 一次性任务

• 与代码库进行对话式开发

• IDE 集成开发

**使用 Claude Agent SDK：**

• CI/CD 自动化

• 生产环境部署

• 集成到现有应用

• 批量处理任务

• 需要精细权限控制

###  完整工作流示例

# 典型工作流：开发 → 验证 → 自动化  

# 第一步：在 CLI 中交互式开发  
# $ claude --prompt "创建新功能 X"  
# 手动测试、调整、验证  

# 第二步：将验证过的工作流转换为 SDK 代理  
async  def  deploy_feature_x  ():  
async  for  message  in  query  (  
prompt=  "按照既定模式创建功能 X"  ,  
options=  ClaudeAgentOptions  (  
allowed_tools=[  "Read"  ,  "Write"  ,  "Edit"  ,  "Bash"  ],  
permission_mode=  "acceptEdits"  ,  
setting_sources=[  "project"  ]  # 使用项目配置  
)  
):  
# 在 CI/CD 中自动运行  
handle_message  (message)  
---  

##  > 07\.  常见问题

###  Q1: Claude Agent SDK 需要安装 Claude Code 吗？

是的。Claude Agent SDK 依赖 Claude Code CLI 作为运行时环境。你需要先安装 Claude Code。

###  Q2: 如何控制成本？

• 使用  max_turns  限制最大轮次

• 通过  allowed_tools  限制可用工具

• 使用更小的模型（通过 model 参数）

• 设置合理的超时时间

###  Q3: 可以在生产环境中使用吗？

完全可以！但需要注意：

• 实现完善的错误处理

• 使用权限系统限制工具访问

• 添加审计日志

• 设置超时和重试机制

• 在沙箱环境中运行敏感操作

###  Q4: 如何调试智能体？

# 打印所有消息  
async  for  message  in  query  (prompt=  "..."  ):  
print  (  f"消息类型：  {  message.type  }  "  )  
print  (  f"消息内容：  {  message  }  "  )  

# 使用 Hooks 记录工具调用  
async  def  debug_hook  (input_data, tool_use_id, context):  
print  (  f"工具调用：  {  input_data[  'tool_name'  ]  }  "  )  
print  (  f"参数：  {  input_data[  'tool_input'  ]  }  "  )  
return  {}  
---  

##  > 08\.  总结

Claude Agent SDK 为开发者提供了一个强大而灵活的框架，让 AI 智能体能够真正走进生产环境。通过：

• **丰富的内置工具** ：覆盖文件操作、命令执行、网络搜索等常见需求

• **强大的权限系统** ：确保安全可控的自动化

• **灵活的 Hooks 机制** ：在关键点插入自定义逻辑

• **会话管理** ：维护持续的对话上下文

• **MCP 集成** ：扩展自定义工具

无论是构建 CI/CD 自动化、代码审查系统，还是智能开发助手，Claude Agent SDK 都能提供坚实的基础。

现在就开始你的 AI 智能体之旅吧！

🔗 参考资源：

官方文档：  https://docs.anthropic.com/en/docs/agents

GitHub 仓库：  https://github.com/anthropics/anthropic-sdk-typescript

Claude API 控制台：  https://console.anthropic.com/

社区讨论：  https://github.com/anthropics/claude-code/discussions

📖 往期内容：

[ 从70分钟到9分钟：微信公众号自动化Skills！提效狂魔！](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484628&idx=1&sn=db1ccd7bf7a243dd13ad77785f04f7a9&scene=21#wechat_redirect)

[ Claude Skill：为什么它会取代 Dify、n8n 和 Coze？](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484218&idx=1&sn=64d4bf66c2a66d1d45be208c02e44a3d&scene=21#wechat_redirect)  

[ Claude Skills:让AI助手秒变领域专家的"技能包"系统](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247483729&idx=1&sn=b622701e7ab1c8c27424d71b254a16b8&scene=21#wechat_redirect)

[ 国产AI编程双雄对决：MiniMax 2.1 vs 智谱GLM-4.7，谁更适合你？](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247483701&idx=1&sn=420c5741ce56f6d2fdc36b71c057436e&scene=21#wechat_redirect)

[ Google 开源 A2UI：让 AI 智能体会"说"UI 的革命性协议](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247483964&idx=1&sn=b2d26325dad972670e2ed4c7f34e843f&scene=21#wechat_redirect)
