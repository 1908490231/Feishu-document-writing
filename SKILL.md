---
name: feishu-write
description: 当用户需要将本地 Markdown 文件发布到飞书文档时使用。支持写入知识库、我的空间、指定文件夹，自动上传图片和保留代码块格式。用户说"发布到飞书"、"写入飞书文档"、"上传到知识库"时触发。
allowed-tools: Read, Write, Edit, Bash
# model: (待测试后填入推荐模型)
---

# 飞书文档写入

将本地 Markdown 文件写入飞书文档。

## 前置条件

在执行本技能之前，请按以下顺序检查：

1. **检查依赖是否安装**：运行 `pip install -r requirements.txt`
2. **检查 .env 文件是否存在且配置正确**：
   - 必须包含 `FEISHU_APP_ID` 和 `FEISHU_APP_SECRET`
   - 如果用户要写入知识库，还需要 `FEISHU_DEFAULT_WIKI_NODE_TOKEN` 或通过参数传入
   - 如果用户要写入指定文件夹，还需要 `FEISHU_DEFAULT_FOLDER_TOKEN` 或通过参数传入
3. **如果用户尚未配置**，请引导用户阅读 `references/setup-guide.md` 完成飞书应用创建和权限开通

### 所需飞书应用权限

应用必须在飞书开放平台开通以下权限，并发布版本后生效：

```json
[
  {
    "scope": "docx:document",
    "description": "查看、创建、编辑和管理云空间中的新版文档",
    "required": true
  },
  {
    "scope": "drive:drive",
    "description": "查看、创建、编辑和管理云空间中的文件",
    "required": true
  },
  {
    "scope": "drive:drive:readonly",
    "description": "查看云空间中的文件",
    "required": true
  },
  {
    "scope": "wiki:wiki",
    "description": "查看、创建、编辑和管理知识库",
    "required": true,
    "note": "写入知识库时必需"
  }
]
```

> 详细权限配置步骤见 `references/setup-guide.md`

## 使用方式

```bash
python -m scripts.feishu_writer <文件路径> [选项]
```

## 参数说明

| 参数 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `path` | - | MD 文件或目录路径 | 必填 |
| `--target` | `-t` | 目标位置 (space/folder/wiki) | space |
| `--folder-token` | `-f` | 文件夹 token（也可通过 .env 配置默认值） | - |
| `--wiki-token` | `-w` | 知识库 node_token（也可通过 .env 配置默认值） | - |
| `--on-duplicate` | - | 重复处理方式 (ask/update/skip/new) | ask |
| `--no-check-duplicate` | - | 不检查重复 | false |

## 示例

```bash
# 写入到默认知识库（使用 .env 中配置的默认值）
python -m scripts.feishu_writer ./doc.md --target wiki

# 写入到指定知识库节点
python -m scripts.feishu_writer ./doc.md --target wiki --wiki-token FWn9wEcZhixVLrk2z5scBx8DnTe

# 写入到我的空间
python -m scripts.feishu_writer ./doc.md --target space

# 写入到默认文件夹（使用 .env 中配置的默认值）
python -m scripts.feishu_writer ./doc.md --target folder

# 写入到指定文件夹
python -m scripts.feishu_writer ./doc.md --target folder --folder-token LlqxfXXXXXXXXXX

# 批量处理目录下所有 MD 文件
python -m scripts.feishu_writer ./docs/ --target folder --folder-token LlqxfXXXXXXXXXX
```

## 环境变量配置

在 `.env` 文件中配置：

```dotenv
# 必需
FEISHU_APP_ID=应用ID
FEISHU_APP_SECRET=应用密钥

# 可选：默认知识库
FEISHU_DEFAULT_WIKI_NODE_TOKEN=默认知识库node_token
FEISHU_DEFAULT_WIKI_SPACE_ID=默认知识库space_id（可自动查询）

# 可选：默认文件夹
FEISHU_DEFAULT_FOLDER_TOKEN=默认文件夹folder_token
```

## Token 获取

用户可能不知道如何获取 token，请引导他们：

| Token 类型 | 获取方式 | 格式特征 |
|-----------|---------|---------|
| folder_token | 浏览器地址栏：`https://xxx.feishu.cn/drive/folder/XXX` | 字母数字混合字符串 |
| node_token | 浏览器地址栏：`https://xxx.feishu.cn/wiki/XXX` | `/wiki/` 后的字符串 |
| space_id | 程序自动通过 node_token 查询，无需手动获取 | 数字 |

> 详细获取步骤见 `references/token-guide.md`

## 支持的 Markdown 格式

- 标题 (h1-h9)
- 段落文本（加粗、斜体、行内代码）
- 代码块（支持语法高亮）
- 有序/无序列表
- 引用块
- 图片（本地图片和网络图片自动上传）
- 表格
- 链接
- 分割线

## 故障排查

执行过程中遇到错误时，请查阅 `references/troubleshooting.md` 获取解决方案。

常见问题速查：
- **"获取 token 失败"** → 检查 App ID / App Secret
- **"permission denied"** → 应用权限未开通或未添加为协作者
- **"permission denied" (folder 模式)** → 云文件夹需通过群组中介方式授权（参见 `references/setup-guide.md` 第 4.1 节）
- **"node permission denied"** → 应用未被添加为知识库协作者（参见 `references/setup-guide.md` 第 4.2 节）
- **图片上传失败** → 检查图片格式和 `drive:drive` 权限
