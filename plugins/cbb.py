# (©)Codexbotz
# Recode by @ReszXD

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import CHANNEL, CHANNELBC, GROUP, OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>Tentang Bot ini:\n\n • Creator : @{OWNER}\n • 💦Channel Asupan : @{CHANNEL}\n • 💦Channel Backup : @{CHANNELBC}\n • 🌟Group Asupan : @{GROUP}\n • Source Code : <a href='https://github.com/restuap17/FileSharing-Restu'>Klik Disini</a></b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴜᴛᴜᴘ •", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
