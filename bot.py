import logging
import pytz
from datetime import datetime
from pyrogram import Client, idle
from pyrogram.errors.exceptions.bad_request_400 import BadRequest

from config import TOKEN, disabled_plugins, log_chat, API_ID, API_HASH
from utils import get_restarted, del_restarted

# تعيين المنطقة الزمنية للبوت
timezone = pytz.timezone("Asia/Amman")  # استبدل "Asia/Amman" بالمنطقة الزمنية المناسبة
current_time = datetime.now(timezone)
print("Current Time:", current_time)

# قراءة إصدار البوت
with open("version.txt") as f:
    version = f.read().strip()

# استخدام اسم جلسة فريد
client = Client("my_unique_session_name", API_ID, API_HASH,
                bot_token=TOKEN,
                workers=24,
                parse_mode="html",
                plugins=dict(root="plugins", exclude=disabled_plugins))

# البدء بالبوت باستخدام start() بدلاً من with
try:
    client.start()
    if __name__ == "__main__":
        wr = get_restarted()
        del_restarted()
        try:
            client.send_message(log_chat, "<b>Bot started</b>\n\n"
                                          f"<b>Version:</b> {version}")
            print("Bot started\n"
                  f"Version: {version}")
            if wr:
                client.edit_message_text(wr[0], wr[1], "Restarted successfully.")
        except BadRequest:
            logging.warning("Unable to send message to log_chat.")
        idle()
except Exception as e:
    logging.error(f"Error while starting bot: {e}")
