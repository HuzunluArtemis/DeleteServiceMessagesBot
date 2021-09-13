# HuzunluArtemis

from pyrogram import Client, filters
import pyrogram
from pyrogram.types import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from pyrogram.types.messages_and_media.message import Message
from config import Config

app = Client(
	"DeleteServiceMessagesBot",
	api_id=Config.APP_ID,
	api_hash=Config.API_HASH,
	bot_token=Config.BOT_TOKEN
)

app.start()
print("Bot Started!")

@app.on_message(filters.command(["start", "help", "about", "yardım", "h", "y"]))
async def helps(client, message: Message):
	tumad = message.from_user.first_name
	if message.from_user.last_name != None:
		tumad += f" {message.from_user.last_name}"
	if Config.UPDATES_CHANNEL is not None and Config.UPDATES_CHANNEL is not "" and Config.UPDATES_CHANNEL is not " ":
		channel = "https://t.me/" + Config.UPDATES_CHANNEL
		reply_markup=InlineKeyboardMarkup(
			[
				[InlineKeyboardButton(
				text = "🔥 Güncellemeler / Updates",
				url = channel)
				]
			])
	else:
		reply_markup=None
	#
	tamisim = Message.from_user.first_name
   if Message.from_user.last_name is not None: tamisim += f" {Message.from_user.last_name}"
	DONATESTARTTEXT = f"Esenlikler / Hi {tamisim}\n\n"
	DONATESTARTTEXT += "🇹🇷 Servis mesajlarını silen reklamsız, basit bir botum.\n(üye eklendi, üye katıldı, şu bunu ekledi vb. mesajlar)"
	DONATESTARTTEXT += "\nYapman gereken beni grubuna yönetici olarak ekleyip\nsilme yetkisi vermek. Sonrasını bana bırak."
	DONATESTARTTEXT += "\nBu bot genellikle telegram\'ın silme limitlerine ulaşır.\nBu botla birlikte klonlarını da eklerseniz sorun çözülür.\n\n"
	DONATESTARTTEXT += "🇬🇧 I am an ad-free, simple bot that deletes service messages.\n(member added, member joined, this added this, etc. messages)"
	DONATESTARTTEXT += "\nAll you have to do is add me to your group as an administrator\nwith delete permission. Leave the rest to me."
	DONATESTARTTEXT += "\nThis bot often reaches telegrams delete limits.\nIf you add clones of this bot too, the problem will be solved."

	await message.reply_text(text=DONATESTARTTEXT,
		reply_markup=reply_markup,
		disable_web_page_preview=True,
		parse_mode="md"
	)

@app.on_message(filters.service)
async def service(client, Message):
   try:
      	await Message.delete(True)
   except:
      	pass

pyrogram.idle()
app.stop()
print("Bot Stopped!")
