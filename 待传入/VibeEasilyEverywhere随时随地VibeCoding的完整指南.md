![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3oPgZfkwFLocdRKChRlic3G3dlgfUMvT0TgUxww3JibLTm6HGY8DnnzTVmxtyfRBFFfJicrQzQLAXAcA/0?wx_fmt=jpeg)

#  Vibe Easily Everywhere：随时随地Vibe Coding 的完整指南

你有没有想过，没有电脑也能完成需求，我用手机完成了一个完整的功能开发"从需求分析到代码实现，全程没有打开电脑。旁边的乘客可能以为我在看电子书，其实我正在和 Claude Code 结对编程。"  

先给大家看效果，vibe on 地铁 ：

![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3p0TiaicozzLSCfdXd0jax3blTMRYE2XSWZIjVPkr0quuicrU84sRHWY55DfMAJulo5t95vsZhL26rQg/640?wx_fmt=jpeg)
这篇文章，我想分享一下这套「移动端 Vibe Coding」工作流是怎么搭建出来的。
![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3oPgZfkwFLocdRKChRlic3G33WklKm25T9Yciays0E5utLRPmCZn7XrOzaLWydgGQPVBTPBjKJ36gWw/640?wx_fmt=jpeg)

##  > Step_01.  为什么我需要这套流程

作为 AI 产品经理，我的工作状态很分裂：白天开各种会，对前后端与业务端需求，真正能静下心写代码、做 Demo 的时间，往往只有晚上和周末。

但问题是，每天通勤加起来差不多 2 小时。坐地铁的时候，脑子里经常冒出想法：「这个功能如果加个 XX 会不会更好？」「刚才那个 Bug 是不是因为 XX？」

以前只能打开备忘录记下来，回家再处理。但很多时候，到家一忙就忘了，或者当时的灵感已经没那么清晰了。

我就想： **能不能在手机上直接写代码？**

试过很多方案：

• GitHub 的网页编辑器：能改代码，但没法运行

• Code-Server：太重了，手机屏幕体验很差

• 各种云 IDE：要么收费贵，要么延迟高

直到  Claude Code  出现，一切都变了。

Claude Code 是对话式的——你不需要一行行敲代码，而是用自然语言描述你要什么，它帮你写。这种交互方式，天然适合移动端：
**读多于写，用语音代替打字。**

WORKFLOW  云服务器 + Termius + tmux + Claude Code + 语音输入法
经过几周的折腾，我摸索出了这套工作流。下面一步步来。  
---  

##  > Step_02.  准备云服务器

你需要一台能跑 Claude Code 的服务器。可以是：

• 云服务器（阿里云、腾讯云、AWS 等）

• 自己的电脑 + 内网穿透

• 带公网 IP 的 NAS

我是将大学时买的笔记本重装成 Linux 服务器使用，配置不需要太高，2 核 4G 足够。

**关键是要确保能通过 SSH 连接。**

以 Linux 服务器为例，检查 SSH 服务是否运行：

sudo systemctl status sshd  
---  

如果没启动：

sudo systemctl start sshd  
sudo systemctl enable sshd  
---  

**端口转发配置**

如果你的服务器在内网，需要配置端口转发。以常见的路由器为例：

**1.** 登录路由器管理页面

**2.** 找到「端口转发」或「虚拟服务器」

**3.** 将外部端口 22（或自定义端口）映射到服务器的内网 IP

如果用的是云服务器，记得在安全组里放行 SSH 端口。

##  > Step_03.  Termius 下载与配置

Termius  是我用过体验最好的移动端 SSH 客户端。界面现代，操作流畅，最重要的是——免费版就够用。

**下载地址：**

• iOS：App Store 搜索「Termius」

• Android：Google Play 或官网 https://termius.com/

**配置连接**

打开 Termius，右上角找到➕添加新主机：

**地址：** 你的服务器 IP 或域名

**端口：** 22（或你自定义的端口）

**用户名：** 你的登录用户名

**认证方式：** 密码或 SSH 密钥（推荐用密钥，更安全）

PRO TIP:  重要设置：保持连接不断开  手机网络不稳定，默认配置下很容易断连。需要调整两个参数：  1\. 进入 Host 设置  
2\. 找到 **Keepalive interval** ，设为 **30 秒**  
3\. 开启 **Expect answer** 选项  
---  
![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3oPgZfkwFLocdRKChRlic3G391Hak8J3QH6uI9qMh8t7JSVZdzA5YzajJ1wQbicOmOXxTw5bnIHZWXA/640?wx_fmt=jpeg)

##  > Step_04.  tmux —— 移动端 Coding 的灵魂

这里要介绍一个神器：  tmux

tmux 是什么？简单说，它能让你的终端会话「永生」。

**没有 tmux 的时候：**

• 你在手机上开了 Claude Code

• 地铁进隧道，网断了

• 重新连上服务器，发现 Claude Code 没了，之前的对话全丢了

**有了 tmux：**

• 会话跑在服务器上，和你的连接无关

• 断网重连后，输入 ` tmux a ` ，一切都还在

• Claude Code 该怎么跑还怎么跑

**安装 tmux**

大多数 Linux 发行版都可以直接安装：

# Ubuntu/Debian  
sudo apt install tmux  

# CentOS/RHEL  
sudo yum install tmux  

# macOS  
brew install tmux  
---  

**基本使用流程**

上地铁后，两个动作就够了：

# 第一次启动  
tmux  

# 在 tmux 里启动 Claude Code  
claude  
---  

如果中途断连了：

# 重新连接后，恢复会话  
tmux a  
---  

就这么简单。

###  在 tmux 中使用 Claude Code 的常见问题

**问题一：我想往上翻看 Claude 之前的回答，但划不动？**

默认情况下，你在手机屏幕上往下滑，Termius 翻不到 tmux 里面的历史记录。

**解决方法** ：开启鼠标模式

tmux set -g mouse on  
---  

开启后，你就可以直接用手指在 Termius 屏幕上滑动来查看历史记录了，和普通界面一样丝滑。

**问题二：怎么彻底关掉 tmux？**

当你到家了，不想继续 Coding 了，如果只是关掉 Termius，tmux 还会一直在后台跑（耗费服务器内存）。

**解决方法** ：在 tmux 界面里，输入：

exit  
---  

或者按 ` Ctrl + d ` 。看到底部绿色条消失，才算真正退出了。

**问题三：每次都要输入 tmux set -g mouse on 很麻烦？**

可以一次性永久配置：

# 编辑配置文件  
nano ~/.tmux.conf  

# 在里面写上一行  
set -g mouse on  

# 按 Ctrl+O 回车保存，按 Ctrl+X 退出  
---

以后每次启动 tmux，鼠标模式都会自动开启。

###  tmux 常用命令速查

**新建会话：** ` tmux ` 或 ` tmux new -s 名字 `

**恢复会话：** ` tmux a ` 或 ` tmux attach `

**列出所有会话：** ` tmux ls `

**退出会话（保持后台）：** ` Ctrl+b ` 然后按 ` d `

**彻底关闭会话：** ` exit ` 或 ` Ctrl+d `

SUMMARY:  移动端 Coding 的标准流程  **进站（开始工作）：** ` tmux ` → ` claude `  
**断网重连（继续工作）：** ` tmux a `  
**到家（结束工作）：** ` exit `  
---  

##  > Step_05.  语音输入法 —— 解放双手

在手机上打字效率确实不高，但我发现了一个神器： **语音输入** 。

Claude Code 是对话式的，你只需要描述你要什么，它来写代码。而语音输入，正好适合这种交互。

我用的是  讯飞语音输入法  ，识别准确率很高，专业术语也能认得八九不离十。

**下载地址：**

• iOS：App Store 搜索「讯飞输入法」

• Android：各大应用商店或官网 https://srf.xunfei.cn/

⚠️ WARNING:  苹果手机用户注意  如果你用
iPhone，可能会遇到一个问题：语音输入的时候，字会被「吃掉」。比如你说「帮我写一个登录功能」，可能只显示「帮我写一个登录」，后面的字丢了。
**解决方法：**  
1\. 打开讯飞输入法的设置  
2\. 找到「语音设置」  
3\. 将「语音结果上屏方式」切换为 **「说完后上屏」**  
---  
![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3oPgZfkwFLocdRKChRlic3G3icftiaYQibyR9UXfJOUCUwNmQYQhm2asnhnae8MV7NQA9l4vvbWHA92MQ/640?wx_fmt=jpeg)

豆包语音输入法也是不错的选择，识别效果和讯飞差不多，看个人习惯。

##  > Step_06.  一些小技巧

**1\. 善用语音标点：** 说「逗号」「句号」「换行」，讯飞能识别成对应符号

**2\. 保存常用命令：** Termius 支持 Snippets，把常用命令保存起来，一键执行

**3\. 用短句沟通：** 和 Claude Code 对话时，尽量用短句，一次只说一个需求，这样更不容易出错

**4\. 先描述再确认：** 「帮我把登录按钮改成蓝色」说完，等 Claude 理解确认后再执行，避免改错

**5\. 利用碎片时间做小任务：** 修 Bug、写小功能、代码审查，这些适合在地铁上做。大型重构还是留给安静的时间

##  > END.  写在最后

这套工作流用了一个多星期，我最大的感受是： **碎片时间终于有了价值。**

以前通勤 2 小时，只能刷刷新闻、看看视频。现在，我能在地铁上完成很多「小而重要」的任务。

当然，手机屏幕毕竟小，不适合做复杂的开发工作。但 Vibe Coding 的核心是「对话式编程」，你更多是在和 AI
沟通，而不是盯着代码敲键盘。这种模式，天然就适合移动端。

如果你也想尝试，整个流程其实不复杂：

**1.** 准备一台云服务器

**2.** 下载 Termius，配置好 SSH 连接

**3.** 在服务器上安装 tmux 和 Claude Code

**4.** 装一个好用的语音输入法

然后，下次坐地铁的时候，试着完成一个小任务。

INSIGHT:  你会发现，通勤时间，也可以是创造时间。  
---  

🔗 相关链接：

如果你还不了解claude code :

[ Claude Code 零基础指南：不会写代码也能做开发？看这一篇就够了，效率翻倍！](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484748&idx=1&sn=ee97a00b3eaae45e66466642d67f2008&scene=21#wechat_redirect)

[ Claude Skills:让AI助手秒变领域专家的"技能包"系统](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247483729&idx=1&sn=b622701e7ab1c8c27424d71b254a16b8&scene=21#wechat_redirect)  

效率工具：

[ CC Hooks：再也不用盯着屏幕等 AI 干活了，完成后主动通知。](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484858&idx=1&sn=6bfed55118d2829e574d6208d28fe16c&scene=21#wechat_redirect)

[ 从70分钟到9分钟：微信公众号自动化Skills！提效狂魔！](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484628&idx=1&sn=db1ccd7bf7a243dd13ad77785f04f7a9&scene=21#wechat_redirect)  

AI产品经理相关：

[ 我用 Claude Code 写 PRD，评审通过率从 40% 提升到 85%](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484929&idx=1&sn=bcccb450310e9db83f848a5c3d9f1d07&scene=21#wechat_redirect)  

[ Google 开源 A2UI：让 AI 智能体会"说"UI 的革命性协议](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247483964&idx=1&sn=b2d26325dad972670e2ed4c7f34e843f&scene=21#wechat_redirect)  
