# Instruction:
# What we need: A chat id, create a bot and the token to use the bot
# 1. Open Telegram
# 2. Search for @BotFather - Should be verified by Telegram
# 3. Type in /create to create a bot
# 4. Give it a name and a username
# 5. Copy the bot token
# 5. Create a new group with the bot
# 6. Go to https://api.telegram.org/bot<Insert your Token here>/getUpdates
# 7. Get the id value of the chat (could be negative)
# 8. Download the telebot library for Python
# 9. Use this code below to send a message into the chat


import telebot

bot_token = None    # Replace "None" with your bot token

bot = telebot.TeleBot(token=bot_token)

chat_id = None  # Replace "None with your chat id
bot.send_message(chat_id=chat_id, text="Hi")
