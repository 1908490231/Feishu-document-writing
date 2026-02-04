![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3rDtTibZ29N2CPNicFSqhKBic6FxY8t1EicklKzBkJ0gLGDxrXZ9IlWt11xc5tgDo8KkJJibuiavUpuaX4Q/0?wx_fmt=jpeg)

#  从70分钟到9分钟：微信公众号自动化Skills！提效狂魔！

"从75分钟到9分钟，效率提升数倍的公众号写作自动化之路"  

##  > Intro.  写在前面

作为一个内容工作者，每周要产出2-3篇微信公众号文章。传统的写作流程是这样的：

**1\. 调研资料（15分钟）：** 在Google、技术博客翻来翻去找资料

**2\. 撰写文章（30分钟）：** 组织语言、改写内容、配图

**3\. 格式优化（20分钟）：** 复制到编辑器、调字体、调颜色、调行距

**4\. 上传发布（10分钟）：** 上传封面、填写摘要、预览调整

现状  总计：75分钟，还不包括中间被打断的时间。  
---  

我做公众号时不想这样，我使用Claude Code Skill（基础介绍： [ Claude Skills:让AI助手秒变领域专家的"技能包"系统](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247483729&idx=1&sn=b622701e7ab1c8c27424d71b254a16b8&scene=21#wechat_redirect)）。一个大胆的想法浮现： **能不能把整个写作流程自动化呢？**

两，三天的开发，我打造了这套"微信公众号自动化写作三件套"：

**wechat-tech-writer：** AI技术文章写作引擎

**wechat-article-formatter：** HTML格式化美化工具

**wechat-draft-publisher：** 一键推送到草稿箱

现在的流程变成了：

# 1. 生成文章（8分钟）  
"写一篇关于Claude Sonnet 4的文章"  

# 2. 格式优化（30秒）  
"美化这篇文章"  

# 3. 推送草稿（30秒）  
"推送到公众号"  
---  
效果  总计：9分钟，效率提升25倍。  
---  

今天，我将完整拆解这三个Skill的技术实现，分享我踩过的坑和设计思路。文末会开源全部代码。

##  > Part_01.  wechat-tech-writer - AI驱动的内容引擎

核心挑战

要让AI写出高质量的技术文章，需要解决三个核心问题：

**问题1：** 如何获取最新、最准确的信息？AI的知识有截止日期，新技术怎么办？

**问题2：** 如何避免"AI味"？照搬原文会被投诉抄袭，纯AI生成又太生硬

**问题3：** 如何生成吸引人的配图？微信文章没图就是"白开水"

技术方案

1\. 多轮智能搜索策略

我设计了一个4轮搜索机制，模拟人类调研的思维过程：

# 搜索策略（伪代码）  
def  research_topic  (topic:  str  ) -> List  [  Article  ]:  
# 第1轮：官方信息  
search  (  f"  {  topic  }  官方文档"  )  
search  (  f"  {  topic  }  GitHub"  )  

# 第2轮：技术解析  
search  (  f"  {  topic  }  详细介绍"  )  
search  (  f"  {  topic  }  教程"  )  

# 第3轮：对比评测  
search  (  f"  {  topic  }  vs  {  competitor  }  "  )  
search  (  f"  {  topic  }  评测"  )  

# 第4轮：补充验证（根据前3轮结果动态调整）  
missing_info =  analyze_gaps  (search_results)  
search  (missing_info)  
---  
关键设计点  • 优先官方源（权威性）  
• 技术博客验证（深度）  
• 评测文章对比（全面性）  
• 动态补充（智能调整）  
---  

2\. 内容改写引擎

直接让AI总结会产生"机器味"，照搬原文又会侵权。我的解决方案是 **结构化改写** ：

# 文章结构模板（2000-3000字）  

## 1. 引子（100-200字）  
用一个场景或问题引入话题  
❌  "今天我们来介绍XXX"  
✅  "你有没有遇到过这样的问题：..."  

## 2. 是什么（300-500字）  
产品/技术的基本介绍  
→ 用类比帮助理解核心概念  

## 3. 能做什么（500-800字）  
核心功能特性 + 实际应用场景  
→ 具体使用案例  
→ 代码示例（如果是技术类）  
---  

3\. AI配图生成系统

我集成了Gemini和DALL-E两套生图API，这里默认使用Gemini：

# generate_image.py 核心逻辑  

class  GeminiImageGenerator  (  ImageGenerator  ):  
"""Gemini Imagen API图片生成器"""  

def  generate  (  self  , prompt:  str  , output_path:  str  , **kwargs) ->
str  :  
from  google  import  genai  

# 创建客户端  
client = genai.  Client  (api_key=  self  .api_key)  

# 生成图片  
response = client.models.  generate_content  (  
model=  "gemini-3-pro-image-preview"  ,  
contents=[prompt],  
)  

return  output_path  
---  

配图策略：

**AI/科技类：**  
• 配色：蓝紫渐变 (#1a1f5c → #7c3aed)  
• 配图：1封面 + 1性能对比图

**工具类：**  
• 配色：绿橙渐变 (#10b981 → #f97316)  
• 配图：1封面 + 1架构图

**新闻类：**  
• 配色：粉紫渐变 (#ec4899 → #a855f7)  
• 配图：仅1封面

提示词关键要点  • 明确要求 "simplified Chinese"（避免繁体或乱码）  
• 16:9横版比例（适配公众号）  
• 专业杂志风格（提升品质感）  
---  

##  >Part_02.  wechat-article-formatter - 格式优化魔法师

核心挑战

微信公众号编辑器是出了名的"难伺候"：

**1\. 不支持外部CSS：** 必须内联样式

**2\. 代码块不支持 <pre>标签： ** 必须转换为<div> \+ <br> \+ &nbsp;

**3\. 图片显示限制：** 本地图片无法显示

**4\. 样式兼容性差：** 复制粘贴后经常样式丢失

技术方案

1\. CSS内联化引擎

微信编辑器不支持  <style> 标签，所有样式必须内联到HTML元素上。

class  WeChatHTMLConverter  :  
"""微信公众号HTML转换器"""  

def  _parse_css_to_dict  (  self  ) -> Dict  [  str  ,  Dict  [  str  ,  str
]]:  
"""解析CSS为字典格式，用于内联样式"""  
css_rules = {}  

# 1. 解析CSS变量  
css_vars = {}  
var_pattern =  r'--([a-zA-Z0-9-]+):\s*([^;]+);'  
for  match  in  re.  finditer  (var_pattern,  self  .theme_css):  
var_name =  f'--  {  match.  group  (  1  )  }  '  
var_value = match.  group  (  2  ).  strip  ()  
css_vars[var_name] = var_value  

return  css_rules  
---  

2\. 三套CSS主题系统

我设计了三套专业CSS主题，覆盖90%的使用场景：

**tech主题（科技风）：** 渐变标题、代码高亮、专业配色

**minimal主题（简约风）：** 黑白色调、大留白、优雅排版

**business主题（商务风）：** 深蓝主色、表格优化、正式感

3\. 精美HTML模板库

除了基础CSS主题，我使用Gemini 3生成了9个精美的HTML模板，涵盖不同风格：

**VSCode蓝色科技风：**  
• 适用场景：技术文章、产品介绍  
• 特色组件：导语块、序号章节、功能卡片

**红蓝对决·深度测评：**  
• 适用场景：对比评测、深度分析  
• 特色组件：渐变标题、对比卡片、数据表格

**极客暗黑风：**  
• 适用场景：技术深度文章  
• 特色组件：深色背景、代码高亮、终端风格

...

4\. 代码块兼容处理

这是最大的坑！微信编辑器 **不支持 <pre><code> 标签 ** ，必须转换为特殊格式。

PRO TIP  微信唯一支持的代码块格式  使用 <div> \+ <br> \+ &nbsp; 格式  
• 用 <div> 替代 <pre>  
• 用 <br> 替代换行符  
• 用 &nbsp; 替代空格  
• 手动添加语法高亮的 <span> 标签  
---  

##  >Part_03.  wechat-draft-publisher - 一键推送神器

核心挑战

微信公众号API设计注意：

**1\. access_token有效期仅7200秒：** 需要缓存和自动刷新

**2\. IP白名单限制：** 必须提前配置

**3\. 图片必须先上传：** 获取media_id后才能关联文章

**4\. 字段长度限制严格：** 标题32字节、作者20字节、摘要120字节

**5\. 错误码多达50+种：** 需要友好的错误提示

技术方案

1\. 智能Token管理

class  WeChatPublisher  :  
"""微信公众号草稿发布器"""  

TOKEN_CACHE_FILE =  "~/.wechat-publisher/token_cache.json"  

def  get_access_token  (  self  ) -> str  :  
"""获取access_token（带缓存）"""  
# 1. 尝试从缓存读取  
if  os.path.  exists  (  self  .TOKEN_CACHE_FILE):  
# 检查是否过期（提前5分钟刷新）  
if  cache[  'expire_time'  ] > time.  time  () +  300  :  
return  cache[  'access_token'  ]  

# 2. 缓存失效，重新获取  
return  data[  'access_token'  ]  
---  
优势  • 自动缓存，减少API调用次数  
• 提前5分钟刷新，避免过期  
• 持久化存储，重启不丢失  
---  

2\. 友好的错误提示

微信API的错误码对开发者很不友好，我做了一个映射表：

ERROR_CODES = {  
40001  :  "AppSecret错误或者AppSecret不属于这个AppID"  ,  
40164  :  "调用接口的IP地址不在白名单中"  ,  
42001  :  "access_token超时，请检查缓存是否正常"  ,  
-1  :  "系统繁忙，请稍后重试"    
}  
---  

##  > Demo.  三件套组合：完整工作流演示

现在，让我们看看三个Skill如何无缝协作，完成一篇完整的技术文章：

步骤1：生成文章（wechat-tech-writer）

"写一篇关于Claude Sonnet 4的技术文章，挑选模版进行格式美化，然后推送到微信。"  

# AI执行流程：  
1\.  [WebSearch] 搜索  "Claude Sonnet 4 official announcement"  
2\.  [WebFetch] 抓取 anthropic.com 官方介绍  
3\.  [AI改写] 生成2800字原创文章  
4\.  [Gemini API] 生成封面图（蓝紫渐变）  
5\.  [Write] 保存 Claude_Sonnet_4介绍.md  

# 耗时：约8分钟  
---

步骤2：格式优化（wechat-article-formatter）

"美化这篇文章"  

# AI执行流程：  
1\.  [检测] 发现最新文章 Claude_Sonnet_4介绍.md  
2\.  [分析] 文章包含代码块 → 选择 tech 主题  
3\.  [转换] Markdown → HTML（内联CSS）  
4\.  [代码块] 转换为微信兼容格式  
5\.  [Write] 保存 Claude_Sonnet_4介绍.html  

# 耗时：30秒  
---

步骤3：推送草稿（wechat-draft-publisher）

"推送到公众号"  

# AI执行流程：  
1\.  [提取] 从HTML提取标题：  "Claude Sonnet 4深度解析"  
2\.  [提取] 生成摘要：  "最新AI大模型Claude Sonnet 4全面介绍"  
3\.  [上传] 上传 cover.png 到微信素材库  
4\.  [发布] 创建草稿文章  

✓ 封面图上传成功  
✓ 草稿创建成功！  

# 耗时：30秒  
---

##  > Benchmark.  总流程对比

传统流程（约75分钟）

**1\. 调研资料（15分钟）**  
• Google搜索官方文档  
• 阅读技术博客  
• 整理核心要点

**2\. 撰写文章（30分钟）**  
• 组织文章结构  
• 改写参考内容  
• 寻找或制作配图

**3\. 格式优化（20分钟）**  
• 复制到微信编辑器  
• 调整标题字体大小  
• 调整代码块颜色

**4\. 上传发布（10分钟）**  
• 上传封面图  
• 填写标题、摘要  
• 手机预览调整

自动化流程（约9分钟）

**1\. 生成文章（2分钟）**  
输入："写一篇关于Claude Sonnet 4的文章"  
输出：文章 + 封面图 + 配图

**2\. 格式优化（30秒）**  
输入："美化这篇文章"  
输出：精美HTML

**3\. 推送草稿（30秒）**  
输入："推送到公众号"  
输出：草稿已创建

效率对比  • 时间：75分钟 → 9分钟（ **提升数倍** ）  
• 质量：手动调整，不一致 → AI生成，风格统一  
• 可复用性：每次从零开始 → 一键复用流程  
• 心智负担：需要反复切换工具 → 全程对话式操作  
---  

##  > Challenges.  核心技术难点与解决方案

难点1：微信代码块兼容性

**问题：** 微信编辑器不支持  <pre><code> 标签，代码块显示为纯文本。

解决方案  • 用 <div> 替代 <pre>  
• 用 <br> 替代换行符  
• 用 &nbsp; 替代空格  
• 手动添加语法高亮的 <span> 标签  
---  

难点2：AI配图中文乱码

**问题：** Gemini生成的图片中，中文有时显示为乱码或繁体字。

解决方案  • 明确要求 "simplified Chinese"  
• 英文标题 + 中文副标题（分离）  
• 添加 "IMPORTANT" 强调  
• 文字不要太多（≤15个字）  
---  

难点3：CSS变量在内联样式中失效

**问题：** 微信不支持CSS变量（  var(--primary-color)  ），内联后样式丢失。

解决方案  1\. 解析CSS变量  
2\. 替换变量为实际值  
3\. 应用内联样式  

转换前：color: var(--primary-color);  
转换后：color: #007aff;  
---  

难点4：access_token缓存管理

**问题：** Token每2小时过期，频繁请求会触发限流。

解决方案  • 持久化缓存（重启不丢失）  
• 提前刷新（避免临界过期）  
• 原子写入（防止并发问题）  
---  

##  > Case_Study.  实战案例：一周产出10篇高质量文章

我用这套工具写了一周的公众号文章，记录真实数据：

12/31 -[ Claude Skill：为什么它会取代 Dify、n8n 和 Coze？](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484218&idx=1&sn=64d4bf66c2a66d1d45be208c02e44a3d&scene=21#wechat_redirect) 
• 字数：2500➕ | 传统耗时：75分钟 | 实际耗时：9分钟 | 阅读量：370 



12/29 - ：[ Claude Skills:让AI助手秒变领域专家的"技能包"系统](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247483729&idx=1&sn=b622701e7ab1c8c27424d71b254a16b8&scene=21#wechat_redirect)
• 字数：3000➕ | 传统耗时：90分钟 | 实际耗时：11分钟 | 阅读量：431 



12/28 -[ 国产AI编程双雄对决：MiniMax 2.1 vs 智谱GLM-4.7，谁更适合你？](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247483701&idx=1&sn=420c5741ce56f6d2fdc36b71c057436e&scene=21#wechat_redirect)
• 字数：2500➕ | 传统耗时：60分钟 | 实际耗时：10分钟 | 阅读量：351 



统计数据  • 平均字数：2850字  
• 平均耗时：9分钟（传统流程：78分钟）  
• 效率提升： **8倍多**  

质量反馈：  
• 90%的文章无需修改，直接发布  
• 读者反馈："排版很专业"、"配图很吸睛"  

---

##  > Roadmap.  开源计划与后续规划

当前功能清单

**wechat-tech-writer：**  
• 多轮智能搜索（4轮策略）  
• 内容自动改写（2000-3000字）  
• AI配图生成（Gemini/DALL-E）

**wechat-article-formatter：**  
• 3套CSS主题（tech/minimal/business）  
• 9套精美HTML模板  
• CSS变量内联化  
• 微信代码块兼容转换

**wechat-draft-publisher：**  
• 微信API集成  
• Token智能缓存  
• 封面图上传  
• 友好错误提示

v2.0规划（预计1月底）

**1\. 多平台支持：**  
• 知乎专栏自动发布  
• CSDN博客自动发布  
• 掘金文章自动发布

**2\. 智能优化：**  
• SEO关键词自动优化  
• 阅读量预测（基于历史数据）  
• 最佳发布时间推荐

**3\. 数据分析：**  
• 文章数据看板  
• 阅读量趋势分析  
• 读者画像分析

##  > Outro.  写在最后

这套工具从构思到完成，历时虽然寥寥几天，踩了无数坑：

• 微信API的IP白名单限制（没分清是🪜的Ip还是公网Ip😂）

• 代码块转换格式（试了7种方案才成功）

• AI配图中文乱码，以及画面风格调整（优化提示词迭代了10+次）

• CSS变量内联化（BeautifulSoup的坑）

但每次解决一个问题，看到流程又顺畅了一点，那种成就感是无与伦比的。

最大的收获  • 深度理解了微信公众号的技术限制  
•设计出三个工作流优化了质量与速度，更高产  
• 体验了从0到1打造完整配套Skills的流程  
---  

如果你也是内容创作者，如果你也被重复的格式调整折磨，如果你也想把时间花在真正重要的事情上——

那就试试这套Skills工具吧。

开源地址见文末，期待你的Star和PR！

##  > Appendix.  技术栈总览

核心依赖

# Python环境  
python >=  3.8  

# wechat-tech-writer依赖  
requests >=  2.28.0  
google-genai >=  1.0.0  # Gemini API  
openai >=  1.0.0  # DALL-E API (可选)  

# wechat-article-formatter依赖  
markdown >=  3.4.0  
beautifulsoup4 >=  4.11.0  
cssutils >=  2.6.0  
---  

系统要求

**操作系统：** macOS / Linux / Windows（WSL2）

**Claude Code：** >= 1.0.0

**Python：** >= 3.8

**网络：** 可访问Google API、OpenAI API、微信API

🔗 相关资源：

开源地址：公众号回复「微信自动化」获取

如果这篇文章对你有帮助，欢迎：

• ⭐ Star这个项目

• 🔄 转发给有需要的朋友

• 💬 留言分享你的使用体验

最后希望大家用的开心，有什么意见希望大家都可以提出来。这里我使用的是原生Claude 4.5 sonnet和 banana
pro，模型不同，效果也不尽相同！
