# Создание Telegram Bot
import telebot

# CONTENT_TYPES = ["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
#                  "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
#                  "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
#                  "migrate_from_chat_id", "pinned_message"]

TOKEN = "token"  #тут нужен токен с телеграмма
bot = telebot.TeleBot(TOKEN)


#
# @bot.message_handlers(filters)
# def function_name(message):
#     bot.reply_to(message, "This is message handler")

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
# @bot.message_handler(commands=['start', 'help'])
# def handle_start_help(message):
#     pass
#
# # Обрабатывается все документы и аудиозаписи
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     pass


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message.text)
    print(message.chat.username)
    bot.reply_to(message, f"Привет тебе, {message.chat.username}")

@bot.message_handler(content_types=['photo', ])
def handle_photo(message):
    bot.reply_to(message, "Классный МЕМ 😂")


bot.polling(none_stop=True)
