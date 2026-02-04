![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/onUpicncef3rjOIIP4GnfjDkFTCx9mOYKQBanjibznuQ9nSlGbd65KlrIJByGrpjX8E3ORwZL2TW76HWS1WUd3Mw/0?wx_fmt=jpeg)

#  打通国内生态，教你把Clawdbot接入飞书

打通国内生态"把Clawdbot接入飞书，无需翻墙，秒速体验AI贾维斯"  

上一篇教程 [ 先别急着买Mac mini : 教你免费部署Clawdbot在云端，自己先玩明白](https://mp.weixin.qq.com/s?__biz=MzYzNDU0OTE5Nw==&mid=2247486135&idx=1&sn=26345bb01b1a581586fd555b9c62dae6&scene=21#wechat_redirect)
我们手把手在AWS上免费部署了Clawdbot，那只横空出世的"AI 助手"让不少朋友直呼"未来已来"。

但有一个问题一直困扰着国内用户——Clawdbot支持的那么多IM系统，全是国外的，每次对话都得先"翻个墙"，实在不够优雅。

能不能把Clawdbot接到飞书上？我捣鼓了几个小时，有了以下结论。

答案是：完全可以，而且用的是飞书的  长连接模式  ，不需要公网服务器，不需要内网穿透，只要你的机器能上网就能用。

##  > 整体思路：这个方案是怎么工作的？

先搞清楚我们要做的事情：

你在飞书发消息  
↓  
飞书通过WebSocket推送给Python脚本  
↓  
脚本调用Clawdbot CLI生成回复  
↓  
脚本通过飞书API把回复发回去  
↓  
你收到AI的回复  
---  

整个过程实时进行，体验和飞书原生机器人几乎没有区别。

**核心技术点：**

• 用Python脚本主动连接飞书WebSocket服务器

• 监听 ` im.message.receive_v1 ` 事件接收消息

• 调用Clawdbot的agent模式生成回复（保持上下文记忆）

• 消息去重防止重复回复

• 异步处理防止阻塞事件循环

• 自动重连保证稳定性

##  > 准备工作

开始之前，确认你手里有这些东西：

项目  |  说明   
---|---  
飞书企业账号  |  个人企业号也可以   
Clawdbot已部署  |  按照上篇教程在AWS上跑起来   
服务器终端访问  |  能SSH到你的AWS服务器   
Python 3.8+  |  服务器上一般都有   

如果Clawdbot还没部署，建议先去看上一篇教程，把基础环境搭好再回来。

##  > Step_01.  飞书开放平台：创建你的机器人应用

1.1 进入飞书开放平台  打开浏览器，访问飞书开放平台，用你的飞书账号登录：  
---  

![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rjOIIP4GnfjDkFTCx9mOYKgVznuhny6Z8OsUL52TEc13s0afY8HtWqiaSpcZ3ft22ydZHgAGFVuZQ/640?wx_fmt=png)

1.2 创建企业自建应用  点击左侧导航栏的"应用开发"，然后点击"创建应用"：  
---  

![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rjOIIP4GnfjDkFTCx9mOYKNxRg03cNl1xYd8nRrz6jJCjiaMR0xNebgV1iaW5PUFxyHX7iaSibibobIyw/640?wx_fmt=png)

选择"创建企业自建应用"，填写基本信息：

• **应用名称** ：比如"Clawdbot助手"

• **应用描述** ：个人AI助手

• **应用图标** ：上传一个你喜欢的图标

![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rjOIIP4GnfjDkFTCx9mOYK3tME2H0aBSTq8z6sicibtFAqu0icZR498egUYOQXEEmhg3p06RlCzy4Dg/640?wx_fmt=png)

点击"创建"后，你就拥有了一个属于自己的飞书应用。

##  > Step_02.  开启机器人能力

应用创建好后，进入应用详情页。

在左侧导航找到"功能" → "机器人"，点击"添加机器人"：

![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rjOIIP4GnfjDkFTCx9mOYKaueYbnANicgwEoSgibX02dZyiaCgeEeBXFILTBQZjUvuX0mZZnBhPuFPg/640?wx_fmt=png)

##  > Step_05.  获取4个关键参数

现在，我们需要从控制台复制几个关键参数。

进入"凭证与基础信息"页面。

**你需要获取以下4个参数：**

参数名称  |  位置  |  用途   
---|---|---  
**App ID** |  凭证与基础信息  |  应用唯一标识   
**App Secret** |  凭证与基础信息  |  应用密钥，点击"查看"才能看到   
**Verification Token** |  事件与回调  |  验证请求来源   
**Encrypt Key** |  事件与回调  |  消息加密密钥（如果没开启加密就是空的）   

![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rjOIIP4GnfjDkFTCx9mOYKUOqH5wm10p36dpicgzvGveiarGMLuzjl1UWF2Kb5nHmm3E7qYo6W5www/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rjOIIP4GnfjDkFTCx9mOYKeES5TyCLtmBZKcdo2hRx8H7PibnzCEdTx8ibMABtibyU2XUY5vrte3mEQ/640?wx_fmt=png)

⚠️ 重要提醒  这4个参数相当于你机器人的"身份证"，一定要妥善保管，不要泄露给别人。  
---  

##  > Step_06.  安装飞书Python SDK

现在切换到你的AWS服务器终端。

6.1 确认Python版本  python3 --version  

---
6.2 安装lark-oapi SDK  飞书官方提供了Python SDK叫 ` lark-oapi ` ，安装很简单：  pip install
lark-oapi -U  

---

安装完成后，你的Python环境就具备了和飞书通信的能力。

##  > Step_07.  编写连接脚本（核心代码）

到了最关键的环节了——编写连接飞书和Clawdbot的Python脚本。

7.1 创建脚本文件  在你的Clawdbot工作目录（比如 ` /home/ubuntu/clawd ` ）下，创建一个新文件：  nano
feishu_ws_agent.py  

---
7.2 粘贴核心代码（格式有点问题，叫ai帮你整理一下）  把下面这段代码完整复制进去：  import  os  
import  json  
import  time  
import  lark_oapi  as  lark  
from  lark_oapi.api.im.v1  import  *  
import  subprocess  
import  threading  # 用于异步处理Clawdbot调用  

# 从环境变量读取飞书应用凭证  
APP_ID = os.environ[  "APP_ID"  ]  
APP_SECRET = os.environ[  "APP_SECRET"  ]  
VERIFICATION_TOKEN = os.environ[  "VERIFICATION_TOKEN"  ]  
ENCRYPT_KEY = os.environ.get(  "ENCRYPT_KEY"  ,  ""  )  # 没开加密就填空字符串  

# Clawdbot调用的会话名称（我们一直用的是'main'）  
CLAWDBOT_AGENT_SESSION =  "main"  

# 60秒去重，避免事件重推导致重复调用和回复  
_seen_message_ids = {}  
TTL_SECONDS =  60  


def  _is_dup  (message_id:  str  )  -> bool  :  
"""  
检查消息是否是重复事件，防止重复处理和回复。  
飞书在网络不稳定时可能会重推消息，这个函数很关键。  
"""  
now = time.time()  
# 清理过期的消息ID  
for  k, ts  in  list  (_seen_message_ids.items()):  
if  now - ts > TTL_SECONDS:  
_seen_message_ids.pop(k,  None  )  

if  message_id  in  _seen_message_ids:  
return  True  

_seen_message_ids[message_id] = now  
return  False  


def  call_clawdbot_cli  (prompt:  str  )  -> str  :  
"""  
通过CLI调用Clawdbot的agent模式，获取智能回复。  
使用agent模式可以保持上下文记忆。  
"""  
cmd = [  "clawdbot"  ,  "agent"  ,  "--agent"  , CLAWDBOT_AGENT_SESSION,  "--
message"  , prompt]  
print(  f  "[Clawdbot] 正在调用命令: {  '  .join(cmd)}  "  )  

try  :  
# 设置60秒超时，防止Clawdbot响应过慢  
p = subprocess.run(cmd, capture_output=  True  , text=  True  , timeout=  60
)  
stdout = (p.stdout  or  ""  ).strip()  
stderr = (p.stderr  or  ""  ).strip()  

print(  f  "[Clawdbot] 返回码:  {p.returncode}  "  )  
print(  f  "[Clawdbot] 输出:  {stdout}  "  )  
if  stderr:  
print(  f  "[Clawdbot] 错误:  {stderr}  "  )  

if  p.returncode !=  0  :  
error_message =  f  "Clawdbot调用失败（返回码:  {p.returncode}  ）："  {stderr  or
'未知错误'  }  "  
print(  f  "[Clawdbot]  {error_message}  "  )  
return  error_message  

# Clawdbot的回复通常包含前缀，需要清理  
例如：🦞 Clawdbot ... │ ◇ 你好！有什么可以帮助你的吗？✨  

我们只取实际的回复内容  

if  stdout:  
lines = stdout.split(  '\n'  )  
for  line  in  lines:  
if  '│ ◇'  in  line:  
return  line.split(  '│ ◇'  )[-  1  ].strip()  
return  stdout  

return  "Clawdbot暂时没有生成出内容"  

except  subprocess.TimeoutExpired:  
print(  "[Clawdbot] 调用超时"  )  
return  "抱歉，我思考的时间有点长，请再试一次"  
except  Exception  as  e:  
print(  f  "[Clawdbot] 调用异常:  {e}  "  )  
return  f  "调用Clawdbot时发生错误："  {e}  "  


def  message_event_handler  (data: P2ImMessageReceiveV1)  -> None  :  
"""  
处理飞书接收到的消息事件。  
"""  
event = data.event  
msg = event.message  
message_id = msg.message_id  

# 消息去重  
if  _is_dup(message_id):  
return  

print(  f  "[Feishu] 收到消息:  {message_id},  类型:  {msg.message_type}  "  )  

# 只处理文本消息  
if  msg.message_type !=  "text"  :  
print(  f  "[Feishu] 跳过非文本消息:  {msg.message_type}  "  )  
return  

chat_id = msg.chat_id  
text = json.loads(msg.content).get(  "text"  ,  ""  )  
print(  f  "[Feishu] 用户消息:  \"  {text}  \"  in chat_id: {chat_id}  "  )  

# 异步调用Clawdbot生成回复，避免阻塞飞书事件处理  
# 如果同步调用，Clawdbot响应慢会阻塞飞书的WebSocket循环  
# 可能导致连接断开或重复事件  
def  generate_and_send_reply  ():  
try  :  
reply_text = call_clawdbot_cli(text)  
print(  f  "[Feishu] Clawdbot回复:  \"  {reply_text}  \"  "  )  

# 构建并发送回复消息回飞书  
client = lark.Client.builder().app_id(APP_ID).app_secret(APP_SECRET).build()  
req = CreateMessageRequest.builder() \  
.receive_id_type(  "chat_id"  ) \  
.request_body(  
CreateMessageRequestBody.builder()  
.receive_id(chat_id)  
.msg_type(  "text"  )  
.content(json.dumps({  "text"  : reply_text}, ensure_ascii=  False  ))  
.build()  
)  
.build()  
resp = client.im.v1.message.create(req)  

if  not  resp.success():  
print(  f  "[Feishu] 发送失败: code=  {resp.code}, msg={resp.msg}  "  )  
else  :  
print(  f  "[Feishu] 消息已发送到 chat_id:  {chat_id}  "  )  
except  Exception  as  e:  
print(  f  "[Feishu] 处理回复时出错:  {e}  "  )  

# 使用单独线程来运行，防止阻塞主事件循环  
reply_thread = threading.Thread(target=generate_and_send_reply)  
reply_thread.start()  


def  main  ():  
"""  
主函数：初始化事件分发器和WebSocket客户端，并启动长连接。  
"""  
# 事件分发器  
event_handler = lark.EventDispatcherHandler.builder(ENCRYPT_KEY,
VERIFICATION_TOKEN, lark.LogLevel.DEBUG)  
.register_p2_im_message_receive_v1(message_event_handler)  
.build()  

# 持续运行并尝试重连  
while  True  :  
try  :  
print(  "[Feishu] 正在尝试连接飞书WebSocket..."  )  
ws_client = lark.ws.Client(APP_ID, APP_SECRET, event_handler=event_handler)  
print(  "[Feishu] WebSocket连接已启动，等待消息..."  )  
ws_client.start()  # 阻塞调用，直到连接断开  
print(  "[Feishu] WebSocket连接已关闭，正在重新连接..."  )  
except  lark.ws.WebSocketClosedError  as  e:  
print(  f  "[Feishu] WebSocket意外关闭:  {e}  ，  {TTL_SECONDS}  秒后重连..."  )  
except  Exception  as  e:  
print(  f  "[Feishu] 发生错误:  {e}  ，  {TTL_SECONDS}  秒后重连..."  )  
time.sleep(TTL_SECONDS)  


if  __name__  ==  "__main__"  :  
main()  
---  

按 ` Ctrl+O ` 保存， ` Ctrl+X ` 退出。

##  > Step_08.  设置环境变量并运行脚本

8.1 设置环境变量  在运行脚本的终端中，先设置之前获取的4个参数：  export APP_ID="你的APP_ID"  
export APP_SECRET="你的APP_SECRET"  
export VERIFICATION_TOKEN="你的VERIFICATION_TOKEN"  
export ENCRYPT_KEY="" # 如果没开启加密就留空  
---  

![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rjOIIP4GnfjDkFTCx9mOYKYUSibzZsFicnVLuxXxz4x1hecqLT1swNSiamDzRE38pC8rUPSILmMjhEw/640?wx_fmt=png)

⚠️ 注意  • 记得把上面命令中的 ` "你的xxx" ` 替换成你实际获取到的参数值。  • **关于ENCRYPT_KEY**
：如果飞书控制台没有开启加密，这里必须设置为空字符串 ` "" ` ，不能不设置。  
---  
8.2 前台测试运行  先在前台运行，看看是否正常：  python3 feishu_ws_agent.py  

---

如果一切顺利，你会看到类似这样的输出：

[Feishu WS Client] Attempting to connect...  
[Feishu WS Client] Starting WebSocket connection...  
[Lark] [2026-01-27 10:12:37,600] [INFO] connected to wss:...  
---  

##  > Step_03.  测试成功后配置事件订阅（关键步骤！）

这里是整个配置的核心。

3.1 核心配置  1\. 进入左侧导航的"功能" → "事件订阅"  
2\. 在"订阅方式"这里，选择 **"使用长连接接收事件"** ：  
---  

![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rjOIIP4GnfjDkFTCx9mOYK5HBlLnDmVDWAdpYXP34Akmtlw6zuSkQJ6CBqhoO1SXagFhQviauIVyg/640?wx_fmt=png)

💡 技术要点
长连接模式下，是我们的Python脚本主动连接飞书服务器。不需要配置公网URL，也就不用担心内网穿透的问题，刚刚的代码就是做这个事情。点击保存即可。  
---  

##  > Step_04.  配置权限并发布版本

4.1 开启必要权限  进入"权限管理"页面，你需要申请以下核心权限：  
---  

权限名称  |  作用   
---|---  
` im.message.receive_v1 ` |  接收消息事件   

![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rjOIIP4GnfjDkFTCx9mOYKpGrRLOicIQ8wic26NSx7NWAGnpye5k6ibtcN2iaKwbUnVOwAOsYrVNjFBg/640?wx_fmt=png)

4.2 发布应用版本  配置完权限后，进入"版本管理与发布"：  
---  

![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rjOIIP4GnfjDkFTCx9mOYKdePd2XNrGbtI3CqvJUQw5dGSfE2ibvSErMkMibDNLQgJd2pQWO5ibdo4Q/640?wx_fmt=png)

点击"创建版本"，填写版本号和说明，然后提交审核。对于企业内部应用，审核通常会很快通过。

审核通过后，记得点击"发布"，飞书会给你发一个消息，这样你的配置才会真正生效。

8.3 后台持久化运行  确认前台运行正常后，用 ` nohup ` 放到后台运行：  nohup python3 feishu_ws_agent.py >
feishu_bot.log 2>&1 &  

---

这样即使你退出SSH，脚本也会继续在后台运行。

8.4 查看运行状态和日志  查看脚本是否在运行：  ps aux | grep feishu_ws_agent    

---

查看实时日志：

tail -f feishu_bot.log  
---  

##  > Step_09.  飞书群里测试：和你的AI助手对话

9.1 把机器人加入群聊  打开飞书app，点击右上角➕，创建群组：  
---  

![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rjOIIP4GnfjDkFTCx9mOYKN5JeQJKpv11lF2h74evqib7fvqwbbJbiaN6GlibX7kJJ2lj8hSjKKZqibA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rjOIIP4GnfjDkFTCx9mOYKlkZ3p2jaWxUQqJDBnl2tk9EJGXOwSyFOGwzWEBDmvZngzY5iaAcjdkQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rjOIIP4GnfjDkFTCx9mOYKJyoSeibYnXUZE8ro62U82DH5494pzNiaYibbZpjHDr3iaswGKESXMpYO0g/640?wx_fmt=png)

9.2 发送第一条消息  在群里发送消息，记得 **@一下你的机器人** ：  @Clawdbot助手 你好  

---

![](https://mmbiz.qpic.cn/mmbiz_png/onUpicncef3rjOIIP4GnfjDkFTCx9mOYKCW9WnpbK6batg6bicTSEibKzEqz61jdSDhXwu3nTibtknkVgRfyAZEbPw/640?wx_fmt=png)

如果一切配置正确，几秒钟后你会收到Clawdbot的回复！

9.3 多轮对话测试  继续和它聊几句，试试多轮对话的连贯性。  
---  

##  > Step_10.  常见问题排查

**问题1：收不到消息回复**

• 确认脚本正在运行：ps aux | grep feishu_ws_agent    
• 检查日志：tail -50 feishu_bot.log  
• 确认事件订阅里im.message.receive_v1已勾选  
• 确认权限已开启并发布版本  
• 确认机器人已加入群聊

**问题2：机器人重复回复**

• 检查_is_dup函数是否正常工作  
• 确认TTL_SECONDS设置合理（60秒）

**问题3：Clawdbot调用超时**

• 手动测试：clawdbot agent --agent main --message "测试"  
• 查看日志中的超时信息  
• 如经常超时，可增加timeout参数值

**问题4：控制台提示"未建立长连接"**

• 检查环境变量是否正确设置  
• 确认ENCRYPT_KEY已设置（未加密时设为空字符串）  
• 确认服务器网络正常，能访问飞书服务器

**问题5：回复内容有乱码**

• 检查call_clawdbot_cli函数中的输出清理逻辑  
• 查看日志中Clawdbot的原始输出  
• 如输出格式有变化，需调整清理逻辑

**问题6：脚本运行一段时间后自动退出**

• 查看日志最后几行，找到退出原因  
• 确认while True循环和异常处理逻辑正确  
• 使用nohup和&后台运行，避免SSH断开影响

##  > 总结

到这里，你的Clawdbot就已经成功接入飞书了！

**现在你可以：**

✓  在飞书群里直接和AI助手对话

✓  无需科学上网，随时随地使用

✓  享受Clawdbot的强大智能能力

✓  在熟悉的国产协作平台上体验AI贾维斯

✓  保持上下文记忆，多轮对话更连贯

**相比Telegram方案的优势：**

• 国内访问速度快，延迟低

• 不需要额外的网络工具

• 飞书的群协作体验更符合国内使用习惯

• 可以和其他飞书应用无缝集成

**下一步可以探索的：**

• 为Clawdbot添加更多技能（比如联网搜索、代码执行）

• 让机器人定时主动推送消息

• 支持更多消息类型（图片、文件等）

如果你按照这篇教程成功接入或者有什么问题，欢迎分享你的使用体验！

今天的文章就到这里啦，如果觉得不错，可以点个赞、在看、转发，三连支持我～

也可以私信公众号添加作者微信，拉你进 AI 学习交流群

🔗 往期推荐：

[ claude code skills](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4352965036143722500#wechat_redirect)

[ AI时代的产品经理](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4331246827556487182&scene=305#wechat_redirect)

[ AI编程效率提升](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4316065742149353480&scene=305#wechat_redirect)

[ Claude code全系列从小白到专家](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4323976194007154694&scene=305#wechat_redirect)

[ 技术趋势与行业观察](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4316069104655761409&scene=305#wechat_redirect)

[ AI大模型热点追踪
](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzYzNDU0OTE5Nw==&action=getalbum&album_id=4316074155000430604&scene=305#wechat_redirect)
