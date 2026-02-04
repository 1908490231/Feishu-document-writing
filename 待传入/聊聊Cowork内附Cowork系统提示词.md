![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3oiaWp6Wy8Oo7ibbjo9GUA6dxFAHiaOoxfJCNjaRms4bZmz13MMqkZ6xWKDBCH0DxQIHeiaUzxibvU2j7w/0?wx_fmt=jpeg)

#  聊聊Cowork：内附Cowork系统提示词

10天，从CLI到桌面应用的产品化之路  "把AI Agent从开发者的终端，带到每个人的桌面。"  

前两天Anthropic发布了个新功能叫Cowork，说是用10天做出来的。

我一开始没当回事，以为又是个小玩意儿。

结果仔细一看，有点意思。

**这不是一个简单的功能迭代，而是Anthropic在AI Agent产品化道路上的一次重要实验。**

更让我惊讶的是，据Hacker News上的讨论，Cowork的初版开发周期只有10天。

10天，把一个面向开发者的命令行工具，变成普通人也能用的桌面"同事"。这背后的技术架构和产品设计思路，值得深挖。

##  > Step_01.  产品定位：从"程序员的CLI"到"所有人的同事"

先说背景。

Claude Code
是Anthropic推出的命令行AI编程工具。它让开发者可以在终端里直接和Claude对话，让AI帮你写代码、调试、重构。对于程序员来说，这是一个效率神器。

但问题来了： **99%的人不会用命令行。**

产品经理不会、设计师不会、运营不会、财务不会。他们也有大量重复性的文件处理工作，也需要AI帮忙。但让他们打开Terminal输入命令？门槛太高了。

Cowork的定位就是解决这个问题： **把Claude Code的能力，用GUI的方式交付给非技术用户。**

**文件夹授权：** 选择一个文件夹，授权Claude访问

**自然语言交互：** 用自然语言描述任务（"帮我整理这个文件夹"）

**自动执行：** Claude自动规划步骤、执行任务、汇报进度

**异步任务队列：** 可以同时分配多个任务，无需等待

##  > Step_02.  技术架构拆解：三层安全边界

作为一个协助我们办公AI Agent产品，Cowork最核心的技术挑战是： **如何让AI在用户电脑上执行操作，同时保证安全？**

想象一下，你让AI"整理下载文件夹"，结果它误删了你的重要文档。或者更糟，AI被恶意prompt注入，把你的敏感文件上传到外部服务器。

Anthropic的解决方案是构建三层安全边界：文件系统沙箱、权限管理系统、网络隔离。

###  2.1  文件系统沙箱：虚拟机级别的隔离

Cowork的核心安全机制是 **在用户电脑上运行一个轻量级Linux虚拟机** 。

在macOS上，它使用Apple的Virtualization Framewore（具体是  VZVirtualMachine
API）启动一个定制的Ubuntu 22环境。用户选择的文件夹会被挂载到这个虚拟机中，Claude的所有操作都在这个沙箱内执行。

KEY INSIGHT:  即使Claude执行了 rm -rf /
这样的"毁灭性"命令，也只会影响虚拟机内部，不会触及用户的真实文件系统（不过我们还是要做好文件备份）  
---  

**macOS：** VZVirtualMachine + Seatbelt (sandbox-exec)

**Linux：** bubblewrap 容器隔离

这种设计的精妙之处在于：它不是简单的"限制AI能做什么"，而是 **从操作系统层面创造一个隔离环境** 。即使AI的行为完全不可预测，损害也被限制在沙箱内。

###  2.2  权限管理：Permission-First设计

沙箱解决了"最坏情况"的问题，但日常使用中，我们还需要更细粒度的权限控制。

Cowork采用了"Permission-First"设计原则： **默认只读，任何修改操作都需要显式授权。**

**分层权限配置：** settings.json定义allow/deny/ask三种规则，deny优先级最高

**工作目录限制：** 默认只能写入当前工作目录及其子目录

**网络请求审批：** 任何网络请求默认需要用户批准

这套权限系统的设计思路很清晰： **把控制权交给用户，而不是让AI自己决定什么能做什么不能做。**

###  2.3  网络隔离：代理服务器控制

网络访问是AI Agent安全的另一个关键点。如果AI可以随意访问网络，就可能被利用来泄露数据或下载恶意内容。

Cowork的解决方案是： **所有网络请求都必须通过运行在沙箱外部的代理服务器。**

**HTTP/HTTPS：** 通过HTTP代理服务器，根据白名单/黑名单过滤

**其他TCP连接：** 通过SOCKS5代理处理（SSH、数据库等）

**默认策略：** 网络访问默认被拒绝

这种架构确保了：即使沙箱内的代码尝试绕过限制，也无法直接访问网络。所有流量都必须经过代理服务器的审查。

##  > Step_03.  系统提示词设计：产品化的Prompt Engineering

技术架构只是基础，真正让Cowork"好用"的，是它的系统提示词设计。

我拿到了Cowork的系统提示  词（私信cowork领取)，发现了几个很有意思的设计细节。

###  3.1  身份定位：明确"我不是Claude Code"

系统提示词的开头就明确声明：

// application_details.txt  
"Claude is powering Cowork mode...  
Claude is NOT Claude Code and should  not refer to itself as such."  
---  

这个设计很聪明。虽然Cowork底层使用了Claude
Code的技术栈，但在用户感知层面，它是一个独立的产品。这避免了用户混淆，也为未来的产品演进留下了空间。

###  3.2  双目录架构：临时工作区 vs 用户可见区

Cowork定义了两个关键目录：

**{{cwd}}：** 临时工作目录，用户不可见，Claude的"草稿纸"

**{{workspaceFolder}}：** 最终输出目录，持久化到用户电脑

系统提示词明确要求： **所有最终交付物必须保存到workspaceFolder，否则用户看不到。**
这个设计解决了一个常见问题：AI在执行任务时会产生大量中间文件，但用户只关心最终结果。

###  3.3  强制使用TodoList：进度可视化

系统提示词中有一条硬性要求：

// todo_list_tool.txt  
"Claude MUST use TodoWrite for  
virtually ALL tasks that involve  
tool calls."  
---  

为什么？因为TodoList会被渲染成用户可见的进度widget。这是一个很好的产品设计： **让用户始终知道AI在做什么。**
对于可能需要几分钟甚至更长时间的任务，进度可视化大大降低了用户的焦虑感。

###  3.4  AskUserQuestion工具：先澄清再执行

另一个强制要求是： **在开始任何多步骤任务之前，必须先用AskUserQuestion工具澄清需求。**

**"Create a presentation about X"**  
→ 先问受众、长度、风格、重点

**"Put together some research on Y"**  
→ 先问深度、格式、具体角度、用途

这个设计背后的逻辑是： **大多数用户请求都是underspecified的。** 与其让AI猜测用户意图然后做错，不如先花30秒澄清需求。

###  3.5  Skills系统：预置最佳实践

Cowork内置了一套"Skills"系统——本质上是针对不同任务类型的最佳实践文档。

比如创建Word文档时，系统会要求Claude先读取  skills/docx/SKILL.md  ；创建PPT时，先读取
skills/pptx/SKILL.md  。这些Skill文档包含了大量经过验证的技巧和注意事项，是Anthropic团队"踩坑"后的经验总结。

###  3.6  computer://协议：文件分享的特殊处理

Cowork使用了一个特殊的  computer://  协议来分享文件：

[  View your report  ](  computer://{{workspaceFolder}}/report.docx  )  
---  

这个协议让桌面应用可以直接打开对应的文件，而不是显示一个普通的文件路径。小细节，但大大提升了用户体验。

##  > Step_04.  产品设计哲学：安全与体验的平衡

从Cowork的设计中，我总结出几个值得借鉴的产品设计原则：

###  4.1  安全是底线，但不能牺牲体验

Cowork的三层安全边界（沙箱、权限、网络隔离）确保了最坏情况下的安全。但在日常使用中，用户几乎感知不到这些安全机制的存在。这是一个很好的平衡：
**安全机制应该是"隐形"的，只在需要时才出现。**

###  4.2  透明可控：用户始终是主人

TodoList进度显示、AskUserQuestion澄清需求、Permission-First权限设计——这些功能的共同点是：
**让用户始终知道AI在做什么，并保持控制权。** 这对于AI Agent产品尤其重要。用户把任务交给AI，但不意味着放弃控制。

###  4.3  渐进式授权：按需请求权限

Cowork不会在一开始就要求用户授予所有权限。而是在需要时才请求：需要写入文件时请求写入权限，需要访问网络时请求网络权限。这种设计降低了用户的心理负担，也符合最小权限原则。

##  > Step_05.  对AI产品经理的启示

Cowork给我的最大启发是： **AI Agent的产品化，不只是套一个GUI那么简单。**

它需要：

**重新设计安全边界：** 从操作系统层面思考隔离方案

**重新设计交互模式：** 从"一问一答"变成"任务分配+进度追踪"

**重新设计提示词：** 把Prompt Engineering变成产品设计的一部分

Anthropic用10天做出了Cowork的初版，但背后是Claude Code多年的技术积累，以及对AI Agent安全问题的深入思考。对于想要做AI
Agent产品的团队，Cowork提供了一个很好的参考架构。但更重要的是理解它背后的设计原则： **安全优先、用户可控、渐进授权。**

TAKEAWAY:  这些原则，可能比具体的技术实现更有价值。  
---  

写在最后

Cowork目前还是research preview，只对Claude
Max用户开放，且仅支持macOS。Anthropic表示未来会支持Windows，并扩大用户范围。

作为一个产品经理，我很期待看到Cowork的演进。它代表了AI Agent产品化的一个重要方向：
**不是让AI替代人，而是让AI成为人的"同事"——一个可以信任、可以协作、可以控制的数字助手。**

这个方向，比起 vibe coding 更接近普通用户的真实需求。

📖 往期推荐：

[ vibe coding：6个月零基础，我用 AI 编程改变了工作方式](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247485379&idx=1&sn=e172c302ee4950ca62c5478986dc480c&scene=21#wechat_redirect)

[ AI IDE里出现广告了，但这次我不反感](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247485173&idx=1&sn=9af52af237ffeb52799d536b2578354c&scene=21#wechat_redirect)  

[ Vibe Easily Everywhere：随时随地Vibe Coding 的完整指南](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247485081&idx=1&sn=b0d3b20da08bac2ec35e4057f2a13c1f&scene=21#wechat_redirect)  

[ 我用 Claude Code 写 PRD，评审通过率从 40% 提升到 85%](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484929&idx=1&sn=bcccb450310e9db83f848a5c3d9f1d07&scene=21#wechat_redirect)  

[ 从70分钟到9分钟：微信公众号自动化Skills！提效狂魔！](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484628&idx=1&sn=db1ccd7bf7a243dd13ad77785f04f7a9&scene=21#wechat_redirect)  
