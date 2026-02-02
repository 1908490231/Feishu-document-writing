# 飞书文档写入工具

## 项目概述

这是一个 Claude Code 技能，用于将本地 Markdown 文件写入飞书文档。

## 目录结构

```
Feishu-document-writing/
├── CLAUDE.md           # 项目说明（本文件）
├── README.md           # 用户使用文档
├── skill.md            # 技能定义文件
├── requirements.txt    # Python 依赖
├── .env.example        # 环境变量示例
├── data/               # 测试数据目录
└── scripts/            # 代码目录
    ├── __init__.py     # 模块导出
    ├── feishu_writer.py # 命令行入口
    ├── writer.py       # 主入口类
    ├── auth.py         # 认证模块
    ├── uploader.py     # 图片上传模块
    ├── parser.py       # Markdown 解析模块
    └── doc_writer.py   # 文档写入模块
```

## 核心模块

### scripts/

| 文件 | 类名 | 职责 |
|------|------|------|
| `auth.py` | `FeishuAuth` | 管理飞书 API 认证，获取 tenant_access_token |
| `uploader.py` | `FeishuImageUploader` | 上传本地图片到飞书，返回 file_token |
| `parser.py` | `MarkdownParser` | 解析 MD 为飞书 Block 格式，处理内联样式 |
| `doc_writer.py` | `FeishuDocWriter` | 创建/更新文档，管理 Block 内容，写入知识库 |
| `writer.py` | `FeishuWriter` | 主入口类，整合所有功能 |
| `feishu_writer.py` | - | 命令行入口 |

## 飞书 API 端点

- 认证：`POST /auth/v3/tenant_access_token/internal`
- 上传图片：`POST /drive/v1/medias/upload_all`
- 创建文档：`POST /docx/v1/documents`
- 写入内容：`POST /docx/v1/documents/{doc_id}/blocks/{block_id}/children`
- 在知识库创建文档：`POST /wiki/v2/spaces/{space_id}/nodes`
- 获取知识库节点信息：`GET /wiki/v2/spaces/get_node?token={node_token}`

## 飞书 Block 类型映射

| block_type | 类型 |
|------------|------|
| 2 | text（文本） |
| 3-11 | heading1-heading9（标题） |
| 12 | bullet（无序列表） |
| 13 | ordered（有序列表） |
| 14 | code（代码块） |
| 15 | quote（引用） |
| 22 | divider（分割线） |
| 27 | image（图片） |
| 31 | table（表格） |
| 32 | table_cell（表格单元格，自动生成） |

## 开发注意事项

1. 飞书 API 每次最多写入 50 个 Block，代码中已做分批处理
2. 图片必须先上传获取 token 才能在文档中使用
3. 代码块语言需要映射为飞书的语言代码（数字）
4. **block_type 必须是数字类型**，不能是字符串
5. 文件读写统一使用 `encoding='utf-8'`
6. **知识库文档需要直接在知识库中创建**，而不是先创建再移动
7. **应用必须被添加为目标知识库的协作者**才有写入权限
8. **表格单元格按行优先顺序排列**，不是嵌套的行-单元格结构

## 知识库权限配置

应用需要被添加为知识库协作者才能写入：

1. 打开知识库页面
2. 点击右上角 **「···」** > **「更多」** > **「添加文档应用」**
3. 搜索应用并授予 **「可编辑」** 权限

## 环境变量配置

```
FEISHU_APP_ID=应用ID
FEISHU_APP_SECRET=应用密钥
FEISHU_DEFAULT_WIKI_SPACE_ID=默认知识库space_id（可选）
FEISHU_DEFAULT_WIKI_NODE_TOKEN=默认知识库node_token（可选）
```

## 测试方法

```bash
# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 填入凭证

# 测试运行（写入到默认知识库）
python -m scripts.feishu_writer ./data/test.md --target wiki
```

## 技能调用

通过 `/feishu-write` 命令调用，详见 skill.md。
