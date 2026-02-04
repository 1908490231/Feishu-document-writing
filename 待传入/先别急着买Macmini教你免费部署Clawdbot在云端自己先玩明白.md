![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3rUBjwxMYeTVcKdAPvBZxRibbs4m0d8pYsgCahkzoVnP0llOarGwowfibsaHSFGwy02riaYYlGJuEEVg/0?wx_fmt=jpeg)

#  先别急着买Mac mini : 教你免费部署Clawdbot在云端，自己先玩明白

如果AI能主动帮你处理杂事"  ;  // 一个真正的贾维斯，会是什么样？
"不是被动等待你提问的聊天机器人，而是会主动给你发消息、帮你处理杂事、甚至自己编写代码扩展能力的AI助手"  

这两天，一个叫  Clawdbot 的开源项目在硅谷技术圈炸开了锅。GitHub星标短短几天破万，Discord社区涌入数千人，有人说，这是自ChatGPT发布以来，再一次让人真切感受到"未来已来"的震撼。  

今天，我们就来聊聊这只横空出世的"龙虾AI"——它到底是个什么东西，为什么这么多人对它着迷，以及最关键的问题：我们普通用户能怎么玩儿，如何部署？

![结构图](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rUBjwxMYeTVcKdAPvBZxRibwhgicrFN2tTO8n8oKgo7fy89GrdiaomCUTefuYaibPqTZgibWO6vks4icEw/640?wx_fmt=png)

★  文末附  手把手AWS免费部署教程  ，小白也能轻松上手！（着急的可以直接拉到最后一部分)

##  > Step_01.  到底什么是Clawdbot？

用一句话概括：  Clawdbot是一个你可以完全掌控的个人AI助手，运行在你自己的设备上，通过你日常使用的聊天软件与你交互。

它的定位非常清晰——不是另一个封装的ChatGPT套壳，而是一个真正"属于你"的AI助手。

##  > Step_02.  能帮你做什么？

当你真正开始使用Clawdbot后，你会发现它和传统AI助手完全是两个物种。以下是一些真实的用户案例：

###  主动式提醒

想象这样一个场景：你早上刚醒，Clawdbot已经在Telegram上给你发来消息：

"早上好！今天有三件事需要注意：  
1\. 下午2点和产品经理的会议，我已整理好相关文档  
2\. 你的航班值机已开放，需要我帮你办吗？  
3\. 收件箱里有12封重要邮件需要处理"  
---  

这不是科幻，而是Clawdbot用户每天都在体验的现实。它会主动监控你的日历、邮箱、航班信息，在关键时刻给你推送提醒和建议。

###  实际任务执行

Clawdbot不是那种只会"我理解你的需求，但无法直接操作"的AI。它真的能  做事  ：

**清理收件箱** 批量处理垃圾邮件、分类归档、自动回复常见问题

**管理日历** 安排会议、协调时间、发送邀请

**航班服务** 自动值机、选座、推送登机牌

**信息研究** 公司背景调查、竞品分析、资料整理

有用户分享，他让Clawdbot帮他处理保险理赔，结果AI主动写了一封有理有据的申诉邮件，最终让保险公司重新审核了原本被拒的申请。

###  持久记忆能力

和ChatGPT那种每次对话都是"一张白纸"的机制不同，Clawdbot拥有真正的记忆。它会记住：

• 你的偏好和习惯

• 之前的对话上下文

• 你交代过的长期任务

• 你的工作流程和规范

这意味着你不需要每次都重新解释背景信息。你说一次"我喜欢邮件用简洁风格"，它就会在未来的所有邮件沟通中贯彻这个风格。

###  技能自扩展系统

这可能是Clawdbot最神奇的地方——它可以让AI自己编写和安装新技能。

举个例子：你告诉Clawdbot"我想要一个能自动抓取某网站价格并提醒我的功能"。几分钟后，它会回复说："我已经为你编写了一个价格监控技能，正在运行中，目标商品降价时会第一时间通知你。"

整个过程中，你不需要写一行代码，不需要了解API，甚至不需要知道这背后发生了什么。AI自己完成了需求分析、代码编写、功能测试、部署上线的全流程。

###  多Agent协同

对于高级用户，Clawdbot还支持同时运行多个AI实例。你可以有一个专门处理邮件的"邮件助手"、一个负责编程的"代码助手"、一个管理家庭的"生活助手"——这些Agent之间可以互相通信、协同工作，形成一个完整的"AI团队"。

##  > Step_03.  技术架构：为什么它能做到这些？

如果你对技术感兴趣，可能会好奇Clawdbot是怎么实现的。

###  Gateway架构

Clawdbot的核心是一个  WebSocket控制平面  ，称为Gateway。这个Gateway扮演着"中央指挥部"的角色，协调各个组件：

**通讯层** 连接WhatsApp、Telegram等聊天平台的接口

**Agent层** 实际的AI推理和决策模块

**工具层** 浏览器控制、文件读写、日历API等操作工具

**节点层** 手机、电脑等执行设备端动作的节点

这种架构的好处是灵活性极强——你可以把Gateway跑在一台廉价的云服务器上，而把需要执行具体操作的节点放在家里的Mac mini上。

###  模型支持

Clawdbot理论上支持任何大语言模型，但作者强烈推荐使用  Claude Pro/Max订阅配合Opus 4.5模型  。原因很简单：

• 长上下文优势：Claude支持20万token的上下文窗口，足够容纳大量的对话历史和文档内容

• 更安全的指令注入防护：对恶意提示词有更强的抵抗力

• 更好的代码能力：在编写和调试技能代码时表现更出色

###  运行环境

Clawdbot使用  Node.js 22+
编写，这意味着它可以运行在几乎所有主流操作系统上：macOS、Linux、Windows（通过WSL2）。你可以在树莓派上跑，可以在Mac
mini上跑，也可以在云端VPS上跑。

##  > Step_04.  使用Clawdbot需要注意什么？

虽然Clawdbot很强大，但它不是一个"开箱即用"的消费级产品。在决定部署之前，有几点需要清楚：

###  技术门槛

这不是夸大其词——你需要有一定的技术基础才能顺利部署Clawdbot：

• 基本的命令行操作能力

• 了解如何配置环境变量和API密钥

• 可能需要处理网络代理和端口问题

• 遇到问题时能阅读日志、排查故障

对于完全没有技术背景的用户来说，直接上手Clawdbot可能会有一定挑战。不过，社区正在努力降低这个门槛，比如提供更友好的安装向导。

###  安全策略

Clawdbot连接的是真实的聊天平台，这意味着理论上存在被滥用的风险。为此，项目默认启用了  DM配对策略  ：

• 陌生用户发来的消息不会被处理

• 系统会生成一个配对码，需要你手动批准

• 你可以设置允许列表，只信任特定的联系人

对于更高安全需求的场景，Clawdbot还支持  沙盒模式
：非主会话（比如群聊）中的操作会在隔离的Docker容器中执行，即使AI做了什么出格的事，也不会影响你的主系统。

##  ⚠️  重要提醒：Clawdbot无法在微信中使用

这是很多国内用户会问的第一个问题："我能用微信和Clawdbot对话吗？"

WARNING:  答案是：目前不能。  
---  

Clawdbot支持的聊天平台包括：

• WhatsApp、Telegram、Slack、Discord

• Google Chat、Signal、iMessage、Microsoft Teams

• Matrix、Zalo、WebChat

但  不支持微信  。原因很简单：微信没有公开的机器人API，任何尝试接入微信的行为都可能违反其服务条款。

###  国内用户的替代方案

如果你想在中国使用Clawdbot，可以选择：

**Telegram** 需要科学上网，但用户体验最好

**Discord** 同样需要网络工具，但社区活跃

**WebChat** Clawdbot自带的一个Web界面，不需要第三方平台

虽然这些方案都不如微信方便，但考虑到Clawdbot带来的价值，这点额外成本是值得的。

##  > Tutorial.  手把手教程：AWS免费部署Clawdbot

NEWBIE FRIENDLY:  看到这里你可能已经跃跃欲试了——别担心，下面这份教程专门为小白准备。
我会手把手带你完成从注册AWS到成功运行Clawdbot的全过程。不需要你有任何技术背景，跟着截图一步步操作就行！  
---  

###  前置准备

在开始之前，你需要准备：

• + 86手机号（用于接收验证码）

• 一张国内的银行卡或信用卡（用于AWS验证，不会扣费）

###  第一步：注册AWS账号

访问  https://aws.amazon.com/cn/
点击"创建AWS账户"。注册过程一共五步，按照提示填写个人信息、银行卡信息和身份验，填写国内的就行，我这里不一一展示了。

![AWS注册](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rUBjwxMYeTVcKdAPvBZxRibmkafaMicYSyqbTZQR9bbMFUicmicaoLr6WO4jGNItwJUHMgrP0QgyrrLA/640?wx_fmt=png)

注册成功后，你会进入AWS控制台界面：

![注册后界面](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rUBjwxMYeTVcKdAPvBZxRibR3BtFoP7mVyNiat8kYG61TDzOXCWUe6gicpicllgNI4qa81PKe08sMlhw/640?wx_fmt=png)

###  第二步：启动EC2实例

在右上角搜索框输入"ec2"，点击进入EC2服务：

![进入EC2](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rUBjwxMYeTVcKdAPvBZxRibAV3P7tSXiae6YUWFXqtDtJtcgWbW92IjHpNKib2pE5JkChFOGWbpOfoQ/640?wx_fmt=png)

点击橙色的"启动实例"按钮：

![启动实例](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rUBjwxMYeTVcKdAPvBZxRib50ZicRqNT0GyAmuR94qPy5J5qcfvL5lCj63FhRtianZtId1sRNJMd1Cg/640?wx_fmt=png)

接下来是关键配置步骤：

**1\. 命名实例** ：随便起个名字，比如"clawdbot-server"

**2\. 选择操作系统** ：选择Ubuntu

**3\. 选择实例类型** ：  重要！搜索"free"，选择的套餐必须要选择与我截图一样的配置，不然会卡住！！！

![配置实例](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rUBjwxMYeTVcKdAPvBZxRib2wTFqTfY00bZa5NobGEts2CtQLbkQJicghiaShDpeG1y4wicYt0hscdWA/640?wx_fmt=png)

###  第三步：完成实例创建

在密钥对设置中，选择"在没有密钥对的情况下继续"：

![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3rUBjwxMYeTVcKdAPvBZxRibYneKF83YooiaibIG5RTZV4IdKYdrp8ymKpT4y2cmzFosJjt0Rz8UeVOA/640?wx_fmt=jpeg)

点击"启动实例"，等待几分钟让实例创建完成。创建成功后，点击"连接到实例"：

![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3rUBjwxMYeTVcKdAPvBZxRibBdbwzWSN1lFgLVOA4bw5Izz582dicvWDPAOJfNeFvibFlJQgLoSBYPYQ/640?wx_fmt=jpeg)

然后点击"连接"按钮：

![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3rUBjwxMYeTVcKdAPvBZxRibVKriaia3ls84Yh3NE3Mff1ANwMTpIaiaoDe9TiaXusAY2zw4icFxbYHKsmA/640?wx_fmt=jpeg)

###  第四步：连接服务器并安装Clawdbot

点击连接后，会打开一个基于浏览器的SSH终端，你就成功连接到你的服务器了：

![连接服务器](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rUBjwxMYeTVcKdAPvBZxRiblSQ9WEanjlBJWZGmQJYHrhUJd6pRLpLKQxZOORbrnI16Unb5gQ1haw/640?wx_fmt=png)

现在，复制下面这条命令，粘贴到终端中按回车：

`curl -fsSL https://clawd.bot/install.sh | bash`

![输入命令](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rUBjwxMYeTVcKdAPvBZxRibX7UrictJ2nPic8fLyTgdlPwb3aJ6kkNc12iarU6wQryrJoyToYOysjh1Q/640?wx_fmt=png)

安装过程可能需要几分钟，请耐心等待。安装完成后会自动进入配置向导。

###  第五步：配置Clawdbot

1\. 同意风险声明

安装完成后，系统会显示风险声明。因为我们将给AI访问文件系统和执行命令的权限，需要你明确同意。输入"yes"继续：

![同意安装](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rUBjwxMYeTVcKdAPvBZxRiboyS9I2trNWnMKEsPKVraoM33QmgVqQiaAOlRIXk5aY2K0XYn8TcV63w/640?wx_fmt=png)

2\. 选择快速开始

系统会问你想要哪种配置方式。选择"Quick Start"快速开始模式。

3\. 配置AI模型

接下来需要配置AI模型。系统会要求你设置Token：

![配置模型](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rUBjwxMYeTVcKdAPvBZxRib6rAvuX3MgEcyGlEuHXMosF09HiaBg7gp7YN2SYLYLGyvCibP0lXu4Ftw/640?wx_fmt=png)

你可以选择：

**Claude Pro/Max** 推荐，效果最好，需要订阅

**Gemini API** 性价比高，可以使用Gemini Flash免费版

**其他模型** OpenAI GPT-4等

按照提示在本地终端运行命令获取Token，然后粘贴回来。

4\. 选择模型版本

如果使用Claude，选择最新版的  Opus 4.5  （最聪明的那个）。

###  第六步：配置Telegram（推荐）

Clawdbot会引导你配置Telegram连接。首先获取Telegram Bot Token：

![配置Telegram](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rUBjwxMYeTVcKdAPvBZxRibjNvSzHiaUjgBricAgnvyzrhm5JbKz26GL8ib8JTZvCItTHzdCTWq5hBIA/640?wx_fmt=png)

获取Bot Token步骤：

1\. 在Telegram中搜索 @BotFather

2\. 发送 /newbot 命令

3\. 按提示设置机器人名称

4\. BotFather会给你一个Token，复制并粘贴到Clawdbot配置中

![获取Token](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rUBjwxMYeTVcKdAPvBZxRibicsXR2QribMKLSyiagFd9SFRxcI4aIvyZhcJbXy6SkQpA0oTBO26jqicpw/640?wx_fmt=png)

###  第七步：配置技能（可选）

系统会询问你要安装哪些技能。对于小白，建议先跳过这一步，等熟悉后再添加：

![配置Skills](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rUBjwxMYeTVcKdAPvBZxRibCck9PBcaalhCO01Mk2jJJqMv1cAQlkDVFrELb6j7tBZfno49QODONQ/640?wx_fmt=png)

常用的技能包括，后面可以添加：

**Exa MCP** 网页搜索和深度搜索

**Homebrew/MCP** 各种开发工具集成

**GitHub** 代码仓库操作

###  第八步：给机器人建立身份

最后，系统会问你一些关于机器人身份的问题：

• 你想叫它什么名字？（比如"小虾米"、"JARVIS"）

• 它的目的是什么？（比如"帮我处理日常琐事"、"辅助我编程"）

• 你的名字是什么？

• 你的时区是多少？（中国选择UTC+8或Asia/Shanghai）

配置完成后，Clawdbot会开始"孵化"（Hatch）——这是它建立自己人格的过程。

###  第九步：开始使用！

一切就绪后，打开Telegram，找到你创建的机器人，给它发送一条消息：

![开始聊天](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rUBjwxMYeTVcKdAPvBZxRiboXibEqcgiaHicDFyHf40BiaHwnbPpSIwMfRONzesNVKu3keRao2DicwCtVQ/640?wx_fmt=png)

如果你配置了相应skills或者mcp,试试这些命令：

• "早上好"

• "帮我查一下今天的天气"

• "提醒我下午3点开会"

你会惊讶地发现，它真的像一个贴身助手一样回应你！

###  常见问题

Q: AWS真的免费吗？

A: AWS提供12个月免费套餐，使用t2/t3实例完全免费。记得选择标注"Free tier eligible"的实例类型。

Q: 实例卡住了怎么办？

A: 在AWS控制台选择实例，点击"重启"即可。

Q: 可以用其他模型吗？

A: 可以，Clawdbot支持多种模型。推荐使用Claude Opus 4.5获得最佳体验。

Q: 不用的时候要关机吗？

A:可以7✖️24小时开机

aws部署教程就到这里了，如果你完全是小白，对自己的个人ai助理感兴趣，我强烈建议你看完以下内容：

##  > Step_05.  从Clawdbot到Claude Code：一条更接地气的学习路径

###  Claude Code是什么？

Claude Code是Anthropic官方推出的AI编程助手。它和Clawdbot有很多相似之处：

• 都可以理解你的自然语言指令

• 都可以执行实际的代码操作

• 都支持长上下文记忆

• 都可以集成到你的工作流中

不同的是，Claude Code专注于编程场景，使用门槛更低，而且有官方支持。

###  为什么推荐从Claude Code入手？

**第一，更平滑的学习曲线。** Claude Code有完整的文档和教程，遇到问题有官方支持。对于AI新手来说，这是更好的起点。

**第二，实用价值立竿见影。** 即使你不想搭建什么"个人AI助手"，学会用Claude
Code也能大幅提升你的编程效率——自动生成代码、解释复杂逻辑、调试错误、重构代码……这些都是日常开发中的刚需。

**第三，为Clawdbot做准备。** 当你熟悉了Claude
Code的工作方式后，再转向Clawdbot会容易很多。你会发现很多概念是相通的：agent会话、技能系统、工具调用……这不就是Clawdbot的核心架构吗？

###  实践建议

如果你对Clawdbot感兴趣，我建议你这样规划学习路径：

**1\. 先掌握Claude Code的基础用法**  
学会用自然语言描述编程需求  
熟悉代码审查和调试的工作流  
理解AI如何处理上下文和记忆

**2\. 尝试构建自动化工作流**  
用Claude Code编写脚本自动化日常任务  
探索API集成和数据处理  
体验"让AI帮你写代码"的快感

**3\. 逐步过渡到Clawdbot**  
在本地搭建一个简单的Clawdbot实例  
从Telegram或Discord开始体验  
一步步添加你需要的技能和功能

**4\. 打造属于你的AI助手**  
根据自己的需求定制技能  
让AI真正融入你的工作和生活  
成为别人羡慕的"有AI助理"的人

相关资源:

• Clawdbot官网：https://clawd.bot/  
• Clawdbot GitHub仓库：https://github.com/clawdbot/clawdbot  

• Claude Code官方文档：https://docs.anthropic.com/claude-code  

今天的文章就到这里啦，如果觉得不错，可以点个赞、在看、转发，三连支持我～

也可以私信公众号添加作者微信，拉你进 AI 学习交流群。

🔗 往期推荐：

[ claude code skills](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4352965036143722500#wechat_redirect)

[ AI时代的产品经理](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4331246827556487182&scene=305#wechat_redirect)

[ AI编程效率提升](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4316065742149353480&scene=305#wechat_redirect)

[ Claude code全系列从小白到专家](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4323976194007154694&scene=305#wechat_redirect)

[ 技术趋势与行业观察](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4316069104655761409&scene=305#wechat_redirect)

[ AI大模型热点追踪](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4316074155000430604&scene=305#wechat_redirect)
