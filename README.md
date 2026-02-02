# 飞书文档写入工具

将本地 Markdown 文件一键发布到飞书文档。

## 功能特性

- 支持写入到我的空间、指定文件夹、知识库
- 自动上传本地图片
- 保留代码块语法高亮
- 支持单个文件或批量处理
- 重复文档检测与处理
- 支持配置默认知识库，简化命令

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置凭证

复制 `.env.example` 为 `.env`，填入飞书应用凭证：

```
FEISHU_APP_ID=your_app_id
FEISHU_APP_SECRET=your_app_secret

# 可选：配置默认知识库（配置后可直接使用 --target wiki）
FEISHU_DEFAULT_WIKI_SPACE_ID=你的知识库space_id
FEISHU_DEFAULT_WIKI_NODE_TOKEN=你的知识库node_token
```

### 3. 获取飞书凭证

1. 访问 [飞书开放平台](https://open.feishu.cn/app)
2. 创建企业自建应用
3. 获取 App ID 和 App Secret
4. 在「权限管理」中开通以下权限：
   - `docs:doc` - 云空间文件管理
   - `drive:drive` - 云空间文件访问
   - `wiki:wiki` - 知识库管理（如需写入知识库）

### 4. 将应用添加为云文档/知识库协作者

**重要**：应用需要被添加为目标文档/知识库的协作者才能写入内容。

云文档的所有者或有「可管理」权限的协作者，可按以下步骤添加应用：

1. 打开云文档或知识库
2. 点击右上角 **「···」** 图标
3. 选择 **「更多」** > **「添加文档应用」**
4. 搜索并选择目标应用
5. 为应用分配 **「可编辑」** 或 **「可管理」** 权限
6. 点击 **「添加」**

添加成功后，应用将出现在当前文档的协作者列表中。

### 5. 使用

```bash
# 写入到我的空间
python -m scripts.feishu_writer ./doc.md

# 写入到指定文件夹
python -m scripts.feishu_writer ./doc.md --target folder --folder-token fldcnxxxxxx

# 写入到知识库（使用 .env 中配置的默认知识库）
python -m scripts.feishu_writer ./doc.md --target wiki

# 写入到指定知识库
python -m scripts.feishu_writer ./doc.md --target wiki --wiki-token FWn9wEcZhixVLrk2z5scBx8DnTe

# 批量处理目录
python -m scripts.feishu_writer ./docs/ --target folder --folder-token fldcnxxxxxx
```

## 命令参数

| 参数 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `path` | - | MD 文件或目录路径 | 必填 |
| `--target` | `-t` | 目标位置 (space/folder/wiki) | space |
| `--folder-token` | `-f` | 文件夹 token | - |
| `--wiki-token` | `-w` | 知识库 node_token（可在 .env 中配置默认值） | - |
| `--on-duplicate` | - | 重复处理 (ask/update/skip/new) | ask |
| `--no-check-duplicate` | - | 不检查重复 | false |

## 如何获取 Token

### 文件夹 Token

1. 在飞书云文档中打开目标文件夹
2. 查看浏览器地址栏：`https://xxx.feishu.cn/drive/folder/fldcnXXXXXX`
3. `fldcnXXXXXX` 即为 folder-token

### 知识库 Node Token

1. 打开目标知识库页面
2. 查看地址栏：`https://xxx.feishu.cn/wiki/FWn9wEcZhixVLrk2z5scBx8DnTe`
3. `/wiki/` 后面的字符串 `FWn9wEcZhixVLrk2z5scBx8DnTe` 即为 node_token

### 知识库 Space ID

Space ID 是知识库的内部标识（数字），可通过以下方式获取：
- 程序会自动通过 node_token 查询 space_id
- 也可手动配置在 `.env` 的 `FEISHU_DEFAULT_WIKI_SPACE_ID` 中

## 支持的 Markdown 格式

| 格式 | 示例 | 支持 |
|------|------|------|
| 标题 | `# H1` ~ `###### H6` | ✓ |
| 加粗 | `**text**` | ✓ |
| 斜体 | `*text*` | ✓ |
| 行内代码 | `` `code` `` | ✓ |
| 代码块 | ` ```python ` | ✓ |
| 无序列表 | `- item` | ✓ |
| 有序列表 | `1. item` | ✓ |
| 引用 | `> quote` | ✓ |
| 链接 | `[text](url)` | ✓ |
| 图片 | `![alt](path)` | ✓ |
| 分割线 | `---` | ✓ |

## 作为 Claude Code 技能使用

在 Claude Code 中直接使用：

```
/feishu-write ./doc.md --target folder --folder-token fldcnxxxxxx
```

## 常见问题

### Q: 提示「获取 token 失败」

检查 `.env` 中的 App ID 和 App Secret 是否正确。

### Q: 提示「权限不足」或「permission denied」

1. 确认应用权限已在飞书开放平台开通并发布
2. **确认应用已被添加为目标文档/知识库的协作者**（见上方「将应用添加为协作者」步骤）
3. 确认应用的协作者权限为「可编辑」或「可管理」

### Q: 提示「node permission denied, tenant needs edit permission」

应用没有目标知识库的编辑权限。请按照上方步骤将应用添加为知识库的协作者，并授予「可编辑」权限。

### Q: 图片上传失败

- 确保图片路径正确
- 检查图片格式是否支持（jpg/png/gif/webp/bmp/tiff）
- 确认应用有云空间写入权限（`drive:drive`）
- 图片大小不超过 20MB

### Q: 网络图片无法显示

当前版本暂不支持直接使用网络图片，请先下载到本地。

### Q: block_type 相关错误

飞书 API 要求 block_type 为数字类型。本工具已正确处理，如遇到此问题请更新到最新版本。

## 开发难点与重点

### 飞书 docx 文档图片上传流程

飞书新版文档（docx）的图片上传与旧版文档不同，需要**三步操作**才能正确显示图片：

#### 步骤 1：创建空图片块

```bash
POST /docx/v1/documents/{document_id}/blocks/{block_id}/children
```

```json
{
  "children": [
    {
      "block_type": 27,
      "image": {}
    }
  ]
}
```

返回值中包含新创建的图片块 `block_id`。

#### 步骤 2：上传图片文件

```bash
POST /drive/v1/medias/upload_all
```

| 参数 | 值 | 说明 |
|------|-----|------|
| `file` | 二进制文件 | 图片文件内容 |
| `file_name` | 文件名 | 如 `cover.png` |
| `parent_type` | `docx_image` | **必须是 docx_image** |
| `parent_node` | 图片块 ID | 步骤 1 返回的 block_id |
| `size` | 文件大小 | 字节数 |

返回值中包含 `file_token`。

#### 步骤 3：更新图片块 token（关键！）

```bash
PATCH /docx/v1/documents/{document_id}/blocks/{block_id}
```

```json
{
  "replace_image": {
    "token": "上一步返回的 file_token"
  }
}
```

**重点**：必须使用 `replace_image` 字段，而不是 `update_image` 或 `image`。

#### 常见错误

| 错误码 | 错误信息 | 原因 |
|--------|----------|------|
| 403 / 1061004 | forbidden | `parent_type` 不正确或缺少权限 |
| 400 / 1061044 | parent node not exist | `parent_node` 无效或为空 |
| 400 / 1770001 | invalid param | 更新图片块时使用了错误的字段名 |

#### 为什么需要三步？

1. **上传图片不会自动关联到图片块** - 即使 `parent_node` 正确，上传后图片块的 `token` 仍为空
2. **更新块 API 只支持文本元素** - 标准的 `update_text_elements` 不支持图片
3. **必须使用 `replace_image`** - 这是飞书专门为图片块设计的更新字段

这个三步流程是飞书 docx 文档 API 的设计特点，官方文档中没有明确说明，需要通过实践摸索。

## 许可证

MIT License
