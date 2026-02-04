![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3o0FpVXAa816icmvBODeibicmIVRPUW7gBNPArwUbjlUQVNP3evAj3LV1KsCgAu4wGedsyQiaiamSuEianQ/0?wx_fmt=jpeg)

#  教你如何让ClawdBot干事儿，也能个性陪聊

前两篇文章我分享了 [ 先别急着买Mac mini : 教你免费部署Clawdbot在云端，自己先玩明白](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247486135&idx=1&sn=26345bb01b1a581586fd555b9c62dae6&scene=21#wechat_redirect)以及 [ 打通国内生态，教你把Clawdbot接入飞书](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247486643&idx=1&sn=db9647e46e15e65cd5874c779ae46352&scene=21#wechat_redirect)的完整教程。如果你还没来得及看，建议先去翻一翻——先把环境搭起来，再来看这些实用技巧，效果会更好。

今天这篇文章，我们就来讲下Clawdbot的实用技巧。

![Clawdbot架构图](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3o0FpVXAa816icmvBODeibicmIfu1BhyDW3XzsJmd9AWDwCEXrZj3Skvib7LU8GoP9G93k90zNrfiavO3g/640?wx_fmt=jpeg)

##  > Step_01.  定时提醒：一句话的事

Clawdbot 最让人惊艳的是它的自然语言理解能力。你不需要记任何命令或代码，就像跟真人说话一样告诉它你想做什么就行。

设置睡眠提醒，你只需要说：

"帮我设置一个睡眠提醒，每天晚上12点提醒我该睡觉了。"  
---  
到晚上12点你就会收到以下内容：
![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3o0FpVXAa816icmvBODeibicmIvEKcPckYsxmO4aRkRWpDjxfZnp6HjXg1aXd4A8x6YOdjgBJA4tOPUQ/640?wx_fmt=jpeg)

设置晚间日报，也只需要一句话：

"每天晚上9点给我生成一份当天的 AI 日报，包含 AI 相关的编程/研究/产品/热门话题，等内容。"  
---  
![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3o0FpVXAa816icmvBODeibicmIjqN1gCdibcPOekicq5Lj7Gl3cgbXibuGIR73vcMrTsfXkm68NLibhPy6Lg/640?wx_fmt=jpeg)

就这样简单！Clawdbot 会理解你的意图，并且通过它的方式，例如 RSS 或者网页抓取，为你呈现日报。

我们还有做以下任务提醒：

` "明天上午10点提醒我参加产品评审会" `

` "每半小时检查一次这个github项目，有新 Realease 立刻通知我" `

` "每天晚上10点帮我查下明天的天气，推荐穿衣" `

TECH DETAILS  能做到这种程度，是因为 Clawdbot 使用的是 Cron
调度器。任务会持久化存储，即使重启也不会丢失。但作为用户，我们完全不需要了解这些——自然语言就够了。  
---  

##  > Step_02.  页面监控：自动哨兵

Clawdbot 的强大之处在于给他一个浏览器，它能像人一样浏览网页。给它一个网址，它能处理登录、Cookie、动态加载等复杂情况。

**价格监控**  
"每半个小时检查一下这个 GitHub 项目，如果有新的 release 版本，就通过飞书通知我"

**社交媒体动态**  
"每隔一小时检查 @elonmusk 的Twitter，如果提到AI就通过飞书…"

**服务健康检查**  
"每小时检查我的网站状态，有问题就通过飞书…"

**竞品追踪**  
"每天早晚各检查一次竞品的产品更新页面，汇总后通过飞书…"

##  > Step_03.  技能扩展：无限可能

Clawdbot 的核心只是一个框架，让它强大的是各种外部技能。官方技能市场clawhub.ai/skills是你获取新技能的首选目的地。

![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3o0FpVXAa816icmvBODeibicmIle1DJuSyibKESVNviasribibZGbfZszuGjT2LCfyibybIDlW63jX3J4YCDA/640?wx_fmt=jpeg)

必装技能推荐：

**Gemini生图技能**  
让Clawdbot拥有视觉创造力。直接告诉它：为你自己画张照片。
![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3o0FpVXAa816icmvBODeibicmIHrZkzBeBfxm0dHcVRm7ic2icJbU1jxRBS9TpVFoEGXxE8nSKrCyVO2Mw/640?wx_fmt=jpeg)

Gemini-Deep-reasearch  
"使用 Gemini-Deep-research 做一篇有关 Kimi k2.5 的报告"

**self-improving-agent技能**  
让AI每天自我进化。每天晚上自动分析当天的任务完成情况，优化自己的Prompt
![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3o0FpVXAa816icmvBODeibicmIr0WgnEmiaJlAlAmgmcCpcG3afg7pj479iahDjoN8QWWlKtAoUpsC9iawg/640?wx_fmt=jpeg)

**语音输入技能（不是skill）**  

通过 Telegram 或飞书发送语音消息！配置 Gemini API 后，系统会自动调用 STT 将语音转换成文字处理。
![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3o0FpVXAa816icmvBODeibicmIQlHs7r9myDYs6yQhlSjsicCvClRJbCqoee1dicjia3N30VL8uIVQyd2EQ/640?wx_fmt=jpeg)

CONFIG  1\. 获取 Gemini API Key:aistudio.google.com/apikey  
2\. 配置环境变量: export GEMINI_API_KEY="your_key"  

---

##  > Step_04.  快捷指令：瑞士军刀

Clawdbot 的 Slash Commands 是核心功能，所有命令都以 ` / ` 开头。

/skill  \- 运行技能  
/status  \- 查看状态/配额  
/model  \- 切换模型  
/think  \- 控制思考深度  
/new  \- 开启新对话  
/stop  \- 停止任务  
---  

进阶指令：

` /elevated on ` — 提升权限（谨慎使用）

` /reasoning on ` — 显示AI思考过程

` /dock-telegram ` — 切换回复到Telegram

` /whoami ` — 查看发送者ID

> Step_05.  远程登录与调试  

我最开始部署在aws上，想要隔离本地环境，但是发现做自动化和浏览网页时不太方便。因此，我发现了以下方法：当需要给 Clawdbot
登录账号，为了更方便他操作时，可以通过 SSH 隧道转发 Chrome 的调试端口到本地。

步骤一：建立 SSH 隧道

ssh -i  "key.pem"  -L  9222  :localhost:  9222  user@server_ip  
---  

步骤二：本地浏览器访问

打开 Chrome输入 chrome://inspect/#devices，确认包含 localhost:9222

步骤三：连接远程浏览器

在 Remote Target 区域点击 inspect，即可像操作本地浏览器一样登录Youtube、GitHub、Google
等账号。这时候使用就能够更加方便快捷。

![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3o0FpVXAa816icmvBODeibicmI0feNgNnDrysLXOibBiblhOia4qNyGWDaDMqnm4aNXFMllM5app4Zpbugg/640?wx_fmt=jpeg)
![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3o0FpVXAa816icmvBODeibicmI0aoT4TKsWia8dF9NkFb0iaPStlweGK9vovwWh0zyMODuEJV9CnAzVVyQ/640?wx_fmt=jpeg)

> Step_06.  灵魂注入，让你的AI拥有独特人格  

Clawdbot 让我惊喜的功能之一，是它可以通过 SOUL.md 文件不断地塑造独特的人格。

想象一下，你的 AI 机器人不再是一个冷冰冰的机器，而是一个有个性、有口癖，甚至有点“牙尖”的成都小伙儿！

![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3o0FpVXAa816icmvBODeibicmI79o6ByQRicricMoXzynCdwbDzPv98ibjQln9LNcaM7tMKYOteClldgvEg/640?wx_fmt=jpeg)

end  如果你有什么其他的玩儿法，欢迎发在评论区一起交流！  

---

今天的文章就到这里啦，如果觉得不错，可以点个赞、在看、转发，三连支持我～  

也可以私信公众号添加作者微信，拉你进 AI 学习交流群

🔗 往期推荐：  

[ claude code skills](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4352965036143722500#wechat_redirect)

[ AI时代的产品经理](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4331246827556487182&scene=305#wechat_redirect)

[ AI编程效率提升](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4316065742149353480&scene=305#wechat_redirect)

[ Claude code全系列从小白到专家](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4323976194007154694&scene=305#wechat_redirect)

[ 技术趋势与行业观察](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4316069104655761409&scene=305#wechat_redirect)

[ clawdbot实战与玩法](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4366686156185321472#wechat_redirect)
