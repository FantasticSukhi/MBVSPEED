from telethon import events, Button
from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10
from AltronX.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("¢σммαη∂ѕ", data="help_back")
        ],
        [
        Button.url("¢нαηηєℓ", "https://t.me/MBV_NETWORK"),
        Button.url("ѕυρρσят", "https://t.me/MBV_CHATS")
        ],
        [
        Button.url("σωηєя", "https://t.me/BLACKMAMBA_HU_VRO")
        ]
        ]


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**нєу [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nι αм  [{BotName}](tg://user?id={BotId})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **✦ ∂єνєℓσρєя :~ [мвν](https://t.me/BLACKMAMBA_HU_VRO)**\n\n"
        TEXT += f"» **мαмвα ѕραм νєяѕιση :** `1.37.0`\n"
        TEXT += f"» **тєℓєтнση νєяѕιση:** `{telethon.__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                event.chat_id,
                "http://ibb.co/w6gnf7r",
                caption=TEXT, 
                buttons=PythonButton)
