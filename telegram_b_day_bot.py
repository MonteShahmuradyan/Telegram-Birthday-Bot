# Import telebot to connect with the Telegram API
import telebot

# Request a Bot Token via BothFather in Telegram to get atoken, and then copy and paste it as Bot_token
Bot_token = 'PLease use here the token of telegram, that you can get it from BotFather'
bot = telebot.TeleBot(Bot_token)

# 
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Welcome! 🎉\nWho is the happy soul to celebrate a birthday today?\nPlease write '/bday' followed by the  name."
    )

# This handler processes the /ծ command and sends a personalized birthday message
@bot.message_handler(commands=['bday'])
def birthday_message(message):
    # Extract the name from the command text
    name = message.text[len('/bday '):].strip()

    if name:
        # Send a personalized birthday message
        bot.send_message(
            message.chat.id,
            f"🎂 HAPPY BIRTHDAY TO YOU, DEAR {name}! 🎉 "
            "WISH YOU ALL THE BEST FOR ETERNITY."
        )

        # Replace 'photo_path' with the path of the picture you want as an output, can be cake pictures as well.
        photo_path = 'photo_path'

        # Open and send the photo
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    else:
        # If no name is provided, prompt the user to give a name
        bot.send_message(
            message.chat.id,
            "Please provide the name by typing '/bday' followed by the name. Example: >> /bday Alex << "
        )

# Start the bot and keep it running
bot.infinity_polling()
