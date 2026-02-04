![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3p21mfQhCxEw4GOOCqmh3TxBekKsOQpJA5Vz2EeSD9yscw7TJE6qePAahM8EWk14fvTpkQI3XXWaA/0?wx_fmt=jpeg)

#  Claude Code 零基础指南：不会写代码也能做开发？看这一篇就够了，效率翻倍！

在小说阅读器中沉浸阅读

你从来没写过代码，但想：

  * 📱 做一个自己的网站？ 
  * 🤖 自动处理Excel表格？ 
  * 📊 批量重命名几百个文件？ 
  * 🎨 批量调整图片大小？ 
  * 📝 自动生成工作周报？ 

 以前   ：这些事要么花钱找人做，要么啃几百页教程...

 现在   ：用 Claude Code，   说人话   就能让AI帮你完成！

* * *

##  什么是 Claude Code？（用人话说）

 简单理解   ：Claude Code 就是一个能听懂   人话   的AI助手，你用中文告诉它要做什么，它就帮你写代码、完成任务。

 重点   ：  
\- ❌ 不需要学编程  
\- ❌ 不需要懂英语  
\- ✅ 只会用键盘打字就行  
\- ✅ 说中文就能完成复杂任务

* * *

##  第一步：检查系统环境（1分钟）

###  1.1 检查是否安装 Node.js

Claude Code 需要 Node.js 环境（版本 ≥ 18.0）。

 打开终端（保持终端窗口打开，后面我们会用到）   ：  
\- Windows：按  ` Win + R  ` ，输入  ` cmd  ` ，回车  
\- macOS：按  ` Command + 空格  ` ，输入  ` 终端  ` ，回车

 检查命令   ：



    node -v

 情况A：如果看到版本号（比如  ` v20.11.0  ` ）
\- ✅ 恭喜！你已经安装了 Node.js  
\- 可以直接进入第二步：下载 Claude Code

 情况B：如果提示"command not found"或"不是内部或外部命令"
\- ❌ 你的系统还没有安装 Node.js  
\- 需要先安装 Node.js，然后再安装 Claude Code

###  1.2 如果没有安装 Node.js

 下载 Node.js   ：https://nodejs.org/

 安装步骤   ：  
1\. 点击上面的链接，会打开下载页面  
2\. 选择 LTS 版本（长期支持版，更稳定）  
3\. 点击下载按钮  
4\. 下载完成后，双击安装包  
5\. 一路点击"下一步"即可安装

 验证安装   ：



    node -v

如果看到版本号，说明安装成功！

* * *

##  第二步：下载安装 Claude Code（2分钟）

###  2.1 使用安装脚本（推荐小白使用提示中的的npm进行安装）

 官方下载链接   ：https://code.claude.com/install.sh

 安装步骤   ：

  1. \- Windows：按  ` Win + R  ` ，输入  ` cmd  ` ，回车 

  2. \- macOS：按  ` Command + 空格  ` ，输入  ` 终端  ` ，回车 

  3. 复制粘贴以下命令：

npm install -g @anthropic -ai/claude-code

  

  4. 按回车，等待安装完成（大约30秒） 

###  2.2 验证安装

在终端中输入：



    claude --version

看到版本号就OK了！

 💡 提示   ：如果登录过程中遇到问题，可以尝试使用 npm 安装低版本，后续在升级高版本，需要先卸载之前安装，使用：npm uninstall
-g @anthropic -ai/claude-code ：



    npm install -g  @anthropic -ai/claude-code@2.0.18

* * *

##  第三步：注册账号并获取 API Key（2分钟）

Claude Code 需要连接到AI服务才能工作，你需要一个 API Key。

###  3.1 推荐使用智谱AI（新手友好）

 优势   ：  
\- ✅ 有免费额度  
\- ✅ 中文理解最好  
\- ✅ 价格便宜（每月20元起）  
\- ✅ 国内服务器，速度快

 注册步骤   ：

  1. 打开智谱AI开放平台：  https://bigmodel.cn/glm-coding?utm_source=bigModel&utm_medium=Frontend%20Group&utm_content=glm%20code&utm_campaign=Platform_Ops&_channel_track_key=WW2t6PJI 
  2. 点击右上角"注册/登录" 
  3. 使用手机号注册（或微信扫码登录）并且输入身份证号进行实名认证 
  4. 回到购买页面进行订阅，  建议大家先购买20元包月的套餐，非常实惠，而且个人学习使用可以随便造！没有token焦虑！！ 
  5. ![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3p21mfQhCxEw4GOOCqmh3Tx2vXk6h5jjWZaKxliaUsGTmw7FeqBMQy8DUT6hiaDHZg36lapD6JhXODg/640?wx_fmt=png&from=appmsg) 点击右上角进入API key中心 
  6. ![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3p21mfQhCxEw4GOOCqmh3TxAIopQHVLouzEVSWLmOH1LVO3Fs1iba9JDibIIw3OdlicRLNUedpG2LRUg/640?wx_fmt=png&from=appmsg)

点击左侧API key选项卡，点击“添加新的API Key” 然后复制该key并且 妥善保管
![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3p21mfQhCxEw4GOOCqmh3TxAYbKEVLm3ibqEgKHmtjibIrnE8ZFmUx67dKtibKXNz1CLWY5dDpe4pEzg/640?wx_fmt=png&from=appmsg)  

  * ###  3.2 其他选择（可选） 

 Minimax  （超便宜）   ：  
\- 购买链接：  https://platform.minimaxi.com/subscribe/coding-plan  
\- 优势：入门只需要9.9一个月  
\- 适合：大量使用，多语言编程，参考： [ 国产AI编程双雄对决：MiniMax 2.1 vs 智谱GLM-4.7，谁更适合你？
](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247483701&idx=1&sn=420c5741ce56f6d2fdc36b71c057436e&scene=21#wechat_redirect)

 Claude 官方（性能最强）   ：  
\- 官网：https://console.anthropic.com/  
\- 优势：最智能  
\- 价格：相对较高

* * *

##  第四步：配置 Claude Code（1分钟）

###  4.1 创建配置文件（windows用户直接去找文件地址就好）

打开终端，输入以下命令：


    mkdir-p~/.claude
    
    nano~/.claude/settings.json

这会打开一个编辑器。

Windows用户  直接在电脑文件夹中找到根目录下的.claude文件，如下图所示，找到这个json文件右键点击打开方式为记事本。

![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3p21mfQhCxEw4GOOCqmh3TxsoNwSdiaNbHj5T8lMeEPEvUXviaibj6e74aaYHFEJnBNtptSC93p8NhKA/640?wx_fmt=png&from=appmsg)

  * ###  4.2 粘贴配置内容（觉得麻烦的可以直接去看下面的cc-switch配置） 

把以下内容复制粘贴到编辑器中（   ⚠️ 把"你的API Key"替换成实际的内容   ）：

    * * * * * * * * {    "env": {        "ANTHROPIC_AUTH_TOKEN": "你的智谱API key",        "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/anthropic",        "API_TIMEOUT_MS": "3000000",        "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1    }}

 如果你用 Minimax   ：

    * * * * * * * * * * * * * {  "env": {    "ANTHROPIC_BASE_URL": "https://api.minimaxi.com/anthropic",    "ANTHROPIC_AUTH_TOKEN": "你的Minimax API key",    "API_TIMEOUT_MS": "3000000",    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1,    "ANTHROPIC_MODEL": "MiniMax-M2.1",    "ANTHROPIC_SMALL_FAST_MODEL": "MiniMax-M2.1",    "ANTHROPIC_DEFAULT_SONNET_MODEL": "MiniMax-M2.1",    "ANTHROPIC_DEFAULT_OPUS_MODEL": "MiniMax-M2.1",    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "MiniMax-M2.1"  }}

  


###  4.3 保存文件

使用 nano 编辑器配置的同学按  ` Ctrl + X  ` ，然后按  ` Y  ` ，再按回车保存。

使用记事本配置的同学按  ` Ctrl + S  ` 直接保存即可。

###  4.4 验证配置

在终端输入：


    claude

如果出现以下欢迎界面，说明配置成功！

![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3p21mfQhCxEw4GOOCqmh3TxcO0IC6wxviapO2ibPGwIBqfV70fhRgI4LnQMj8FfJTbSjsRNYjVbnbFA/640?wx_fmt=png)

  

* * *

##  第五步：开始使用！（立即上手）

###  5.1 第一次运行

在终端输入：


    claude

你会看到类似这样的欢迎信息：
![登录界面](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3p21mfQhCxEw4GOOCqmh3TxcO0IC6wxviapO2ibPGwIBqfV70fhRgI4LnQMj8FfJTbSjsRNYjVbnbFA/640?wx_fmt=png)


    Claude Code v1.x.x Type a message or press Enter to start

###  5.2 试试第一个命令

直接用中文输入：


    你好，请帮我列出当前文件夹的所有文件

Claude Code 会：  
1\. 读取当前文件夹  
2\. 列出所有文件  
3\. 告诉你有多少个文件

 恭喜你！你已经成功使用 Claude Code 完成第一个任务了！  

* * *

##  ⚡  Claude Code 自带的5件神器

![5大功能展示](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3p21mfQhCxEw4GOOCqmh3Tx2shCZ9AZmL5ppCUIejOamOHWXaAQs75ibtibzodTVycOibNFxnbx3j7qA/640?wx_fmt=jpeg)
1\. 📊 批量处理文件（不用手动一个个操作）

 场景   ：你文件夹里有500个文件要重命名

 以前   ：手动右键重命名，500次...累死

 现在   ：在终端进入你需要处理的文件夹路径，并且使用“claude”命令唤醒Claude code，输入以下内容


    把文件夹里所有照片按"拍摄日期_序号"重命名

Claude Code 自动读取文件、提取日期、批量重命名，30秒搞定！

###  2\. 🤖 自动处理Excel（不用学函数公式）

 场景   ：合并多个表格、数据筛选、计算统计

 以前   ：要学VLOOKUP、数据透视表...头大

 现在   ：


    把这10个销售表格合并，计算每个地区的总销售额，按降序排列

Claude Code 自动处理，生成结果表格！

###  3\. 🌐 做简单网站（不用学HTML/CSS）

 场景   ：做个个人简历网站、产品展示页

 以前   ：要学网页制作，或者花钱找人

 现在   ：


    帮我做一个个人简历网站，包含个人信息、工作经历、作品展示

Claude Code 自动生成网页文件，你直接用浏览器打开就能看！

###  4\. 📝 自动生成报告（不用手动复制粘贴）

 场景   ：每周要写工作汇报、数据总结

 以前   ：打开各种表格、复制数据、整理格式...1小时

 现在   ：


    读取本周销售数据，生成一份包含图表和数据分析的周报

Claude Code 自动读取数据、分析趋势、生成报告！

###  5\. 🎨 批量处理图片（不用PS）

 场景   ：100张图片要统一调整大小、加水印

 以前   ：打开PS一张张处理...2小时

 现在   ：


    把文件夹里所有图片调整到宽800像素，加上右下角水印

Claude Code 自动批量处理，1分钟完成！

##  💡  Claude Code 的5个黑科技功能

###  1\. ⏪ 检查点功能（后悔药）

 作用   ：随时保存进度，出错可回滚

 使用   ：


    /checkpoint save "操作前的状态"

 如果出错了   ：


    /checkpoint restore

 就像游戏的存档读档！  

 场景   ：  
\- 批量处理文件前保存  
\- 如果结果不满意，一键恢复  
\- 重新尝试不同的操作

###  2\. 🤖 无人值守模式（自动化）

 作用   ：让Claude Code连续执行多个操作，不用每次都问"是否继续"

 使用   ：


    claude--dangerously-skip-permissions

 适合场景   ：  
\- 批量处理大量文件  
\- 信任的任务（如重命名、调整图片）  
\- 自动化脚本

 ⚠️ 注意   ：新手建议先不使用，等熟悉后再用

###  3\. 📋 一次性模式（快速完成任务）

 作用   ：不用进入对话模式，直接完成单个任务

 使用   ：


    claude-p"读取当前文件夹所有txt文件，合并成一个文件"

 适合   ：简单、一次性任务

 示例   ：


    claude-p"列出当前文件夹所有文件"claude-p"创建一个hello.txt文件，内容是'你好世界'"

###  4\. 🧠 清除记忆（重新开始）

 作用   ：清空对话历史，让Claude Code重新理解

 使用   ：


    /clear

 适合场景   ：  
\- 切换到新任务  
\- 对话太久，Claude理解偏了  
\- 想重新开始

 示例   ：


    你：帮我处理Excel... （对话很久后） 你：/clear 你：现在帮我处理图片...

###  5\. 🔍 权限控制（安全保护）

 作用   ：控制Claude Code能做哪些操作

 查看权限   ：


    /allowedTools

 设置权限   ：  
\-   allow   \- 允许工具无需权限即可使用  
\-   ask   \- 每次使用前询问用户（默认）  
\-   deny   \- 完全禁止使用某个工具

 新手建议   ：保持默认设置（ask模式）

 示例   ：


    /allowedTools add read_file # 允许读取文件 /allowedTools remove delete_file # 移除删除文件权限

* * *

##  🎓 从零到精通：5天学习计划

###  第1天：熟悉基本操作（30分钟）

 任务1   ：让Claude Code列出当前文件夹的文件


    列出当前文件夹的所有文件，按大小排序

 任务2   ：让它帮你创建一个新文件夹


    创建一个名为"测试"的文件夹

 任务3   ：让它帮你写一个简单的文本文件


    创建一个txt文件，内容是"你好，Claude Code"

 目标   ：熟悉对话方式，了解Claude Code能做什么

###  第2天：批量处理文件（1小时）

 任务1   ：批量重命名文件


    把当前文件夹所有jpg图片按数字编号重命名

 任务2   ：筛选文件


    找出当前文件夹超过10MB的文件，列出来

 任务3   ：整理文件


    把所有图片移动到"图片"文件夹，所有文档移动到"文档"文件夹

 目标   ：学会批量处理文件，提高效率

###  第3天：处理Excel数据（1小时）

 任务1   ：读取Excel


    读取sales.xlsx文件，告诉我有哪些列

 任务2   ：计算数据


    读取sales.xlsx，计算总销售额和平均销售额

 任务3   ：生成报告


    读取sales.xlsx，生成一份包含数据分析的文本报告

 目标   ：学会用Claude Code处理数据，不用学Excel函数

###  第4天：自动化任务（1小时）

 任务   ：用检查点功能完成复杂任务


    /checkpoint save "开始前"

然后执行多个操作，如果中间出错：


    /checkpoint restore

回到起点重新来

 目标   ：学会用检查点，不怕出错

###  第5天：实际应用（根据自己需求）

 办公自动化   ：  
\- 自动生成周报  
\- 批量处理文档  
\- 整理文件

 个人用途   ：  
\- 整理照片  
\- 做个人网页  
\- 处理数据

 目标   ：把学到的用到实际工作生活中

* * *

##  💬  小白常见问题

###  Q1：我完全不懂编程，能用吗？

 答   ：   完全可以！  

Claude Code 的核心优势就是：  
\- ✅ 听懂中文指令  
\- ✅ 自动完成复杂任务  
\- ✅ 不需要你懂代码

你只需要：  
1\. 会打字  
2\. 会说中文  
3\. 知道自己要做什么

就这么简单！

###  Q2：如果Claude Code理解错了我的意思怎么办？

 答   ：直接纠正它！


    不对，我是想按文件大小排序，不是按日期

Claude Code 会重新理解你的需求，再次执行。

###  Q3：操作失误了怎么办？

 答   ：Claude Code 有"检查点"功能！


    /checkpoint save "操作前的状态"

如果后面操作错了：


    /checkpoint restore

一键回到之前的状态，就像游戏的"读档"功能！

###  Q4：我担心它会删除我的文件？

 答   ：Claude Code 默认会   询问你   ！

每次操作前，它会告诉你：  
\- 要做什么  
\- 会影响哪些文件  
\- 询问你是否继续

只有你确认后，它才会执行。

 安全提示   ：  
\- ⚠️ 第一次使用时，先在测试文件夹尝试  
\- ⚠️ 重要文件先备份  
\- ⚠️ 不确定时说"先告诉我你会做什么，不要执行"

###  Q5：需要付费吗？

 答   ：有免费和付费选项

 免费方式   ：  
\- 智谱AI：每月有免费额度  
\- DeepSeek：新用户有免费额度

 付费方式   ：  
\- 智谱AI Coding Plan：月费20元  
\- Claude官方：按使用量计费

 建议   ：先用免费额度试试，觉得好用再付费

* * *

##  ⚠️  重要注意事项（小白必看）

###  1\. 先备份重要文件！

在使用Claude Code处理文件前：  
\- ✅ 复制一份重要文件  
\- ✅ 或在测试文件夹尝试  
\- ❌ 不要直接在唯一的工作文件上操作

 示例   ：


    复制"重要文档"文件夹到"测试文件夹" 在"测试文件夹"中操作Claude Code  直接在"重要文档"文件夹操作（风险太大）

###  2\. 从简单任务开始

 推荐顺序   ：  
1\. 第1天：查看文件、创建文件  
2\. 第2天：批量重命名、移动文件  
3\. 第3天：处理Excel  
4\. 第4天：尝试更复杂的任务

 不要一上来就   ：  
\- ❌ 批量删除文件  
\- ❌ 修改系统文件  
\- ❌ 处理非常重要的工作文件

###  3\. 不确定就先问

操作前，可以说：


    先告诉我你会做什么，不要直接执行

Claude Code 会详细说明：  
\- 会读取哪些文件  
\- 会执行什么操作  
\- 会产生什么结果

你确认后再执行。

 示例   ：


    你：先告诉我你会做什么 
    
    Claude：我会： 1. 读取当前文件夹的所有文件 2. 筛选出大于10MB的文件 3. 生成一个列表文件 不会删除或修改任何文件 是否继续？(y/n)

###  4\. 利用检查点功能

重要操作前：


    /checkpoint save "操作前"

这样即使出错了，也能恢复！

 示例   ：


    /checkpoint save "批量重命名前" /checkpoint restore # 一键恢复

###  5\. 遇到问题直接问Claude Code


    我遇到了这个问题：[描述问题]，该怎么解决？

Claude Code 会：  
\- 分析问题原因  
\- 提供解决方案  
\- 指导你操作

  * 以上入门以后，我们继续来探索以下稍微进阶的操作： 

* * *

##  🚀 进阶使用：探索更多功能

当你熟悉了 Claude Code 的基本使用后，还可以探索更多强大功能：

###  1\. 🎨 使用 Skills 技能扩展

Claude Code 支持各种技能扩展，可以完成更专业的任务：

 查看可用技能   ：


    /skills

 常用技能   ：  
\-   wechat-tech-writer   ：自动生成公众号文章  
\-   wechat-article-formatter   ：美化文章格式  
\-   wechat-draft-publisher   ：发布到微信后台  
\-   dialectical-thinking   ：多维度分析问题

 使用技能   ：


    帮我使用wechat-tech-writer写一篇关于AI的文章，并且推送到微信公众号后台

###  2\. 🔌 MCP 服务器扩展

通过 MCP（Model Context Protocol）连接外部工具：

 常用 MCP 服务器   ：  
\-   Fetch   ：搜索和抓取网页内容  
\-   Filesystem   ：高级文件操作  
\-   Database   ：数据库查询  
\-   GitHub   ：GitHub 集成

 安装 MCP 服务器   ：


    claudemcpaddfetch"npx -y @modelcontextprotocol/server-fetch"

 使用示例   ：


    帮我搜索最新的AI技术资讯

###  3\. 🔄 CC Switch 模型切换器

一键切换不同的 AI 模型，实现成本与性能的最佳平衡。

 下载 CC Switch   ：  
https://github.com/farion1231/cc-switch/releases

 使用示例   ：


    解压后安装，并且根据引导配置API key即可de

 优势   ：  
\- 1秒完成切换  
\- 自动备份配置  
\- 节省成本

###  4\. 📊 性能优化技巧

 上下文压缩命令   ：


    /compact

 限制对话轮数   ：


    claude--max-turns5

 清除上下文   ：


    /clear

###  5\. 🤖 自动化脚本

将常用命令保存为脚本，一键执行：

 创建脚本文件   ` auto_task.sh  ` ：


    #!/bin/bashclaude-p"读取今天的数据，生成报告"

 执行脚本   ：


    chmod+xauto_task.sh ./auto_task.sh

* * *

##  📚  推荐学习资源

 官方文档   ：  
\- Claude Code 官方文档：https://code.claude.com/docs  
\- Anthropic 官网：https://www.anthropic.com/

 相关文章   ：  
\- [ Claude Skill：为什么它会取代 Dify、n8n 和 Coze？](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484218&idx=1&sn=64d4bf66c2a66d1d45be208c02e44a3d&scene=21#wechat_redirect)
\- [ 从70分钟到9分钟：微信公众号自动化Skills！提效狂魔！](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484628&idx=1&sn=db1ccd7bf7a243dd13ad77785f04f7a9&scene=21#wechat_redirect)

\- [ 从 Chat 到 Agent：Claude Agent SDK 才是 AI 真正的生产力开关](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484632&idx=1&sn=f9eb9abbbed6095099e04e655eda5d4a&scene=21#wechat_redirect)

 工具下载   ：  
\- Node.js 官网：https://nodejs.org/  
\- DeepSeek 平台：https://platform.deepseek.com/

 社区资源   ：  
\- CC Switch 工具：https://github.com/farion1231/cc-switch  
\- MCP 服务器列表：https://modelcontextprotocol.io/
