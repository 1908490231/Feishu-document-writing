![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3r8evzYfeINd8etuaA1D745BS9tFOK3vfTZApPVic3j1VUmtx3oZXXekdv8DhWicnficXEx7KaAHNmvg/0?wx_fmt=jpeg)

#  CC Hooks：再也不用盯着屏幕等 AI 干活了，完成后主动通知。

##  > Step_01.  什么是 Hooks？

🏠 用生活场景来理解

假设你有一个智能家居系统，可以设置一些"自动触发的规则"：

**🚪 门铃响了** → 自动推送监控画面到手机  
---  

**📦 快递柜有包裹** → 自动发短信通知你

**🌙 晚上11点** → 自动关闭客厅灯光

这些"当某事发生时，自动做另一件事"的规则，就是  Hooks  的概念！

💻 Claude Code 中的 Hooks

在 Claude Code 里，Hooks 的工作方式完全一样： **当某个特定事件发生时，自动执行你预设的脚本或命令。**

##  > Step_02.  Hooks 需要安装吗？

✅ 答案  不需要！Hooks 是 Claude Code 的内置功能  开箱即用，你只需要：① 编写想执行的脚本 ② 在配置文件中告诉 Claude
Code 何时执行。不需要安装任何插件或扩展！  
---  

##  > Step_03.  支持哪些 Hook 事件？

Claude Code 官方支持  9 种  Hook 事件：

**SessionStart** 会话启动或恢复时 → 加载配置

**UserPromptSubmit** 提交问题时 → 注入上下文

**PreToolUse** 工具执行前 → 拦截危险操作

**PermissionRequest** 需要授权时 → 自动审批/拒绝

**PostToolUse** 工具执行后 → 记录日志

**Notification** 发送通知时 → 自定义渠道

**Stop ⭐** 完成响应时 → **发送完成通知**  
---  

**SubagentStop** 子代理完成时 → 监控子任务

**PreCompact** 压缩上下文前 → 保存重要信息

##  > Step_04.  如何制作自己的 Hook？

制作一个 Hook 只需要 **3 个步骤** ：

**步骤 1：明确需求**  
想清楚：什么时候触发？触发后做什么？

**步骤 2：编写脚本**  
创建 Shell 或 Python 脚本，添加执行权限（chmod +x）

**步骤 3：配置 settings.json**  
在 ~/.claude/settings.json 中添加 hooks 配置

配置模板：

{  
"hooks"  : {  
"事件名称"  : [{  
"matcher"  :  ""  ,  
"hooks"  : [{  
"type"  :  "command"  ,  
"command"  :  "你的脚本路径"  
}]  
}]  
}  

}  

##  > Step_05.  实战：任务完成自动通知

现在动手实现： **当 Claude Code 完成响应后，自动发送通知提醒你。（不想写配置的同学可以私信：[hooks]获取仓库链接）**

核心流程  Claude Code 完成响应  
⬇️  
触发 Stop Hook  
⬇️  
执行 notify.sh /notify.ps1 脚本。  
⬇️  
发送通知提醒你  
---  
步骤 1  创建通知脚本  在  ~/.claude/  目录下创建
notify.sh/notify.ps1。注意，下方是Linux的配置，windows的配置需要在GitHub上获取。  
---  
#!/bin/bash  
# Claude Code 任务完成通知脚本  

TITLE  =  "Claude Code"  
MESSAGE  =  "任务执行完成"  

# 飞书 Webhook（本地开发不用配置飞书，云端需要）  
FEISHU_WEBHOOK  =  ""  

# 本地通知  
send_local_notification  () {  
if  command -v notify-send &> /dev/null;  then  
notify-send  "$TITLE"  "$MESSAGE"  
elif  [[  "$OSTYPE"  ==  "darwin"  * ]];  then  
osascript -e  "display notification \"$MESSAGE\" with title \"$TITLE\""  
fi  
}  

# 飞书推送  
send_feishu_notification  () {  
[ -z  "$FEISHU_WEBHOOK"  ] && return  0  
curl -s -X POST  "$FEISHU_WEBHOOK"  \  
-H  "Content-Type: application/json"  \   
-d  '{"msg_type":"text","content":{"text":"'"$TITLE: $MESSAGE"'"}}'    
}  

send_local_notification  
send_feishu_notification  
---  
步骤 2  添加执行权限  
---  
chmod +x ~/.claude/notify.sh  
---  
步骤 3  配置飞书机器人（云端配置，本地可选）  • 打开飞书 → 进入一个群聊  
• 群设置 → 群机器人 → 添加机器人  
• 选择「自定义机器人」，复制 Webhook 地址  
• 将地址填入脚本的 FEISHU_WEBHOOK 变量  
---  
步骤 4（关键！）  配置 Hook  编辑  ~/.claude/settings.json  
---  
{  
"hooks"  : {  
"Stop"  : [{  
"matcher"  :  ""  ,  
"hooks"  : [{  
"type"  :  "command"  ,  
"command"  :  "/你的用户目录/.claude/notify.sh"  
}]  
}]  
}  

}  

配置说明  •  "Stop"  — 在 Claude 完成响应时触发  
•  "matcher": ""  — 空字符串表示所有情况都触发  
•  "command"  — 脚本的 **绝对路径**  
---  
步骤 5  测试效果  重启 Claude Code，随便问它一个问题。回复完成后，你应该能收到通知啦！🎉  
---  

📱 实际效果展示

**Windows 桌面通知：**

![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3r8evzYfeINd8etuaA1D74506CBEBp9ibLKVheVvFE4SibbTbF883MKNg4ia91IKWNt3libpVOytiakmTg/640?wx_fmt=other)

**飞书消息通知：**

![](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3r8evzYfeINd8etuaA1D745uF3AM3854BkTdQ6aAzq3YJvXaN4MeHqPVVyXmqGxIanK6GlDZs5ibpQ/640?wx_fmt=jpeg)

> Step_06.  更多 Hook 创意

**🛡️ 危险命令拦截**  
使用 PreToolUse + Bash matcher，检查是否包含 rm -rf 等危险操作

**✨ 自动代码格式化**  
使用 PostToolUse + Write|Edit matcher，写完文件后自动运行 Prettier

**📝 会话日志记录**  
使用 SessionStart Hook，每次会话开始时记录时间戳到日志文件

##  > Step_07.  常见问题

**Q: Hook 执行失败怎么办？**  
A: 用  claude --debug  启动，查看详细日志

**Q: 修改配置后不生效？**  
A: Hooks 在启动时加载，修改后需重启或使用  /hooks  命令重新加载

**Q: matcher 怎么用？**  
A: matcher 用于过滤触发条件。如设为 "Bash"，则只有执行 Bash 命令时才触发

##  > Summary.  总结

KEY POINTS  Claude Code 的 Hooks 是一个强大的 **内置功能** ：  ✅ **无需安装** — 开箱即用，只需配置
settings.json  
✅ **灵活定制** — 9 种事件类型，覆盖完整工作流  
✅ **简单易用** — 写个脚本 + 改个配置，即可实现自动化  
---  

Hooks 的玩法远不止通知提醒——安全审计、自动格式化、上下文注入……只要发挥想象力，你可以让 Claude Code 变得更加智能！

现在就去试试吧！🚀

🔗 相关资源：

官方文档：  code.claude.com/docs/en/hooks

📖  相关文章：

[ Claude Code Skills 资源库全面盘点：12 个必收藏仓库](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484810&idx=1&sn=852f8e4fd2bfce3778894e4ceb3c00bc&scene=21#wechat_redirect)

[ Claude Code 零基础指南：不会写代码也能做开发？看这一篇就够了，效率翻倍！](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484748&idx=1&sn=ee97a00b3eaae45e66466642d67f2008&scene=21#wechat_redirect)

[ 从70分钟到9分钟：微信公众号自动化Skills！提效狂魔！](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484628&idx=1&sn=db1ccd7bf7a243dd13ad77785f04f7a9&scene=21#wechat_redirect)

[ 从 Chat 到 Agent：Claude Agent SDK 才是 AI 真正的生产力开关](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484632&idx=1&sn=f9eb9abbbed6095099e04e655eda5d4a&scene=21#wechat_redirect)  

[ Claude Skill：为什么它会取代 Dify、n8n 和 Coze？
](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247484218&idx=1&sn=64d4bf66c2a66d1d45be208c02e44a3d&scene=21#wechat_redirect)









****



****



****





__









