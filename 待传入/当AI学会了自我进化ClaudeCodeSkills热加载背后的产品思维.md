![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3o4kmdics7EGspUQejIHfBbicibOZx3agOGuC4rvWPKct4DEpOWh11GicHiaj7B7yPFN70wYrRb7VvR8nQ/0?wx_fmt=jpeg)

#  当 AI 学会了自我进化：Claude Code Skills 热加载背后的产品思维

AI Product Insights  Claude Code  产品思考  AI 进化  
---  

![内容结构图](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3o4kmdics7EGspUQejIHfBbic7wYialRj3IVDm6y6R0JoHoE1uWuh8IzInr5WaoLN0SZIVskPechrBQQ/640?wx_fmt=jpeg)

💡 **核心观点** Claude Code 2.1.0 的 Skills 热加载功能，表面上是开发体验优化，实际上开启了 AI 自我进化的可能性——AI
可以在运行时修改和优化自己的能力，无需重启。这可能是 AI 工具走向"自我进化"的第一步。  
---  

这几天我在用 Claude Code 写一个微信公众号排版工具的 skill 时，发现了一件有意思的事。

我修改了 skill 文件里的一行提示词，保存，然后直接在对话里调用——它居然立刻生效了。不需要重启，不需要刷新，甚至不需要中断当前对话。

等等，这意味着什么？

AI 可以在运行过程中，实时更新自己的能力。

这让我想了很久。表面上看，这只是一个"热加载"的技术特性。但往深了想，这可能是 AI 工具走向"自我进化"的第一步，如下图我的 Skill
根据流程自动优化更新，并直接使用。

![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3o4kmdics7EGspUQejIHfBbicEl3VSGeFxpnu7AnvY4jup6lWicP3gyeRgvyQvTDpFRrYxbmoicQm2gHA/640?wx_fmt=jpeg)

##  01\. 先说清楚：Skills 热加载是什么

Claude Code 2.1.0 版本在 2026 年 1 月 7 日发布，其中一个重要更新就是 Skills 热加载（Hot-Reload）。

简单说就是：你在 ` ~/.claude/skills ` 或 ` .claude/skills ` 目录下创建或修改的 skill
文件，会立即生效，无需重启会话。

之前的开发体验  改一行 → 重启会话  丢失对话上下文  |  现在的开发体验  改完即生效  ⬆️ 保持完整上下文   
---|---  

官方文档里轻描淡写地说："Hot-reload is automatic. Create or modify a skill in
~/.claude/skills and it's immediately available."

但我觉得这背后的意义，远不止"开发体验优化"这么简单。

##  02\. 我的观点：这是 AI 自我进化的雏形

我认为，Skills 热加载开启了一个新的可能性：  AI 可以在运行时修改和优化自己的能力  。

这不是科幻，这是正在发生的事情。让我用三个真实场景来解释。

##  03\. 三个真实场景

|  🔧  
---  
场景一：AI 自己改自己的 Skill  我对生成的文章不满意，觉得开头太啰嗦。于是直接说："你刚才用的那个 skill，开头的引导语太长了。帮我改一下
skill 文件，让开头更简洁，然后再用该 skill 写一篇。"  

Claude Code 读取了 skill 文件，修改了提示词，保存。它又立刻用修改后的版本生成了文章。  

**整个过程不到 1分钟。AI 自己改了自己的"能力定义"，然后立刻用上了新能力。**  
|  📝  
---  
场景二：自动补充缺失规则  我的代码审查 skill 漏掉了一个安全检查项。我指出来后，它主动说："我注意到这个规则在 skill
定义里没有明确说明。需要我把它加进去吗？"  

我说好，它就把这条规则追加到了 skill 文件里。下一次做代码审查时，它自动就检查这个项了。  

**这种"用着用着就变得更好"的体验，是我之前在任何 AI 工具里都没感受过的。**  
|  🔄  
---  
场景三：能力迁移  我让 Claude Code 参考一个写得好的 skill，去改进另一个写得不好的
skill。它读取了两个文件，分析了结构差异，然后把好的设计模式迁移过去了。  

**这已经不只是"热加载"了。这是能力的自我迭代和跨场景复用。**  

##  04\. 从产品角度看，这意味着什么

1\. 开发者已经在用它做什么

先看一个贴近我们的数据。

Claude Code 的核心开发者 Boris Cherny 在推特上说，他用 Claude Code **生成了 259 个 PR，超过 40000
行代码** 。这条推文获得了 440 万次浏览。

社区里已经出现了大量实用的 Skill 包：

📦 热门 Skill 生态

**Tresor** ：8 个自动化 skill + 8 个专家 agent + 4 个工作流命令

**Skill Factory** ：帮你生成针对特定领域的定制 skill

**Skills Library** ：26+ 专业领域包，覆盖营销、产品、工程、管理

2\. 但也有真实的痛点

当然，也不全是好消息。

|  😤  
---  
开发者真实吐槽  "200 美元/月的订阅，两天就把配额烧完了。"  
"节假日双倍额度取消后感觉像诱导消费。"  

这说明什么？说明开发者真的在重度使用这个工具。  用量焦虑本身就是产品成功的证据。

2025 年 9 月市场份额  83%  |  现在市场份额  70%  Cursor、Codex 正在追赶   
---|---  

这也侧面说明，AI 编程工具已经进入真正的竞争期了。

3\. 一个技术细节揭示的产品哲学

有个技术细节我觉得特别值得说。

Claude Code 在处理长对话时，不是简单地丢弃旧信息，而是会 **"压缩"对话** ——把到目前为止的进度记录下来，类似于做笔记。

Ethan Mollick 用了一个很妙的比喻：这就像电影《记忆碎片》里的主角，用纹身来保持记忆的连续性。  
---  

为什么这很重要？因为 Skills 热加载 + 上下文压缩 + 子代理协作，组合起来就是一个  能够持续学习、持续工作的系统  。

它不再是"一问一答"的工具，而是能在长时间任务中保持状态、积累经验的系统。

##  05\. 我觉得还有哪些可能性

热加载只是第一步。根据 Claude Code 开发者 Boris Cherny 的说法，团队接下来对两个方向很感兴趣：

🚀 Claude Code 未来方向


**Long Running** ：让 AI 能够持续运行更长时间

**Swarm** ：多个 AI agent 协同工作

把这些结合起来想象一下：一群持续运行的 AI agent，它们可以实时优化自己的技能，可以互相学习和迁移能力，可以根据任务效果自动调整策略...

这不就是一个自我进化的系统吗？

"我有一种感觉，如果我能正确串联起过去一年出现的这些工具，我能变强 10 倍。"  —— Andrej Karpathy，OpenAI 联合创始人  
---  

注意他说的是"串联"——不是单个工具有多强，而是工具之间的组合和协作。

Skills 热加载正是让这种"串联"成为可能的基础设施。当 AI
可以随时学习新能力、随时优化旧能力时，它就不再是一个固定的工具，而是一个可以无限扩展的平台。

##  SOP  对我们的启示

  * **开始构建你自己的 skill 库** ：不要只是用默认功能。把你常用的工作流、提示词模板、审查规则都沉淀成 skill。它们会随着你的使用越来越好。 
  * **学会"教"AI，而不只是"用"AI** ：当 AI 做得不好时，告诉它哪里不对，让它把改进写进 skill 文件。这样下次就不会再犯同样的错误。 
  * **关注这个领域的发展** ：Claude Code 现在大约占据 AI 编程工具 70% 的市场份额。它的设计思路会影响整个行业的方向。 


---

##  写在最后

我不想过度炒作"AI 自我进化"这个概念。目前的热加载还很初级，需要人来触发，AI 不会自己主动去改 skill。

但这个方向的意义是明确的：  AI 的能力边界不再是固定的，而是可以在使用中持续扩展的。

这让我想起 2010 年代移动互联网的爆发。当时很多人觉得 App Store 只是"能装软件"而已，没意识到它开启了整个应用经济。

Skills 热加载可能就是 AI 时代的"App Store 时刻"——一个看起来很小的技术变化，但它改变了 AI 能力的分发和迭代方式。

让我们拭目以待。

相关链接

如果你还不了解claude code：

[ Claude Code 零基础指南：不会写代码也能做开发？看这一篇就够了，效率翻倍！](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484748&idx=1&sn=ee97a00b3eaae45e66466642d67f2008&scene=21#wechat_redirect)  

[ Claude Skills:让AI助手秒变领域专家的"技能包"系统](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247483729&idx=1&sn=b622701e7ab1c8c27424d71b254a16b8&scene=21#wechat_redirect)  

效率工具：

[ 从70分钟到9分钟：微信公众号自动化Skills！提效狂魔！](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484628&idx=1&sn=db1ccd7bf7a243dd13ad77785f04f7a9&scene=21#wechat_redirect)  

[ CC Hooks：再也不用盯着屏幕等 AI 干活了，完成后主动通知。](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484858&idx=1&sn=6bfed55118d2829e574d6208d28fe16c&scene=21#wechat_redirect)

[ Vibe Easily Everywhere：随时随地Vibe Coding 的完整指南](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247485081&idx=1&sn=b0d3b20da08bac2ec35e4057f2a13c1f&scene=21#wechat_redirect)

AI 产品经理相关：

[ 我用 Claude Code 写 PRD，评审通过率从 40% 提升到 85%](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484929&idx=1&sn=bcccb450310e9db83f848a5c3d9f1d07&scene=21#wechat_redirect)

[ Google 开源 A2UI：让 AI 智能体会"说"UI 的革命性协议](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247483964&idx=1&sn=b2d26325dad972670e2ed4c7f34e843f&scene=21#wechat_redirect)

[ Claude Skill：为什么它会取代 Dify、n8n 和 Coze？
](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484218&idx=1&sn=64d4bf66c2a66d1d45be208c02e44a3d&scene=21#wechat_redirect) 
