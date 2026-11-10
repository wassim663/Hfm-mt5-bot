import telebot
from telebot import types

# التوكن ومعرف المحادثة الخاص بك
TOKEN = "8929649925:AAGl3qoIKKkovo20_8bOdzS6Q5g9dB99ou4"
CHAT_ID = "7917961649"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
  # إنشاء الأزرار التفاعلية أسفل الرسالة
  markup = types.InlineKeyboardMarkup(row_width=1)
  btn_analyze = types.InlineKeyboardButton(
      "✨ Analyze signal", callback_data="analyze"
  )
  btn_list = types.InlineKeyboardButton("📋 Signal list", callback_data="list")
  markup.add(btn_analyze, btn_list)

  # نص رسالة التوصية بالتنسيق المطلوب
  signal_text = (
      "**Signal**\n"
      "🔴 **Sell**\n"
      "Entry price: 4084\n\n"
      "❌ Stop loss: 4104\n"
      "✅ Take profit: 4043\n\n"
      "Risk-reward: 2.0\n\n"
      "Status: ▶️ Active\n\n"
      "👤 #kourosh_ha\n"
      "Signals: 5\n"
      "Win rate: 80%\n"
      "Avg risk-reward: 2.0\n\n"
      "⭐ **Score:**\n"
      "96.4"
  )

  # إرسال الرسالة مع الأزرار للدردشة التي أرسلت الأمر
  bot.send_message(
      message.chat.id,
      signal_text,
      parse_mode="Markdown",
      reply_markup=markup,
  )


if __name__ == "__main__":
  print("Bot is running...")
  bot.infinity_polling()
