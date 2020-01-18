from telegram.ext import CommandHandler, Updater
from telegram import ChatAction, ParseMode
from datetime import datetime
import json
import os
import requests
import logging




# Load bot token
with open('token_poke.ini', 'r') as file:
   BOT_TOKEN = file.read().strip()

# Create the bot
updater = Updater(token=BOT_TOKEN, use_context=True)

# Load persistent state
if os.path.isfile('data.txt'):
    with open('data.txt', 'r') as file:
        counter_dict = json.load(file)
else:
    counter_dict = {}

# Add /start handler
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Hello {update.effective_message.chat.first_name}! Type /cat for cat pick me ups, /dogs if you are a dog lover or /poke if you have a sudden urge to learn about pokemon'
    )

# Add /quote handler
def poke(update, context):
    # Update /quote count
    user_key = str(update.effective_chat.id)
    count = counter_dict.get(user_key, 0) + 1
    counter_dict[user_key] = count

    # Send thinking message
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='What lucky pokemon will you get ? I wonder....'
    )

    # Send typing status
    context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING
    )
'''
    # Generate image url
    img_url = f'https://picsum.photos/seed/{datetime.now()}/500'

    # Fetch quote
    response = requests.get('https://quotable.dev/random')
    if response.status_code != 200:
        # Document not found
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Hmm, got nothing on me at the moment. Try again later.'
        )
        return
    random_quote = response.json()
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=img_url,
        caption=f'{random_quote["content"]}\n- _{random_quote["author"]}_\n\nYou have called /quote {count} time(s)!',
        parse_mode=ParseMode.MARKDOWN
    )
'''
updater.dispatcher.add_handler(
    CommandHandler('start', start)
)

updater.dispatcher.add_handler(
    CommandHandler('poke', poke)
)

# Start the bot
updater.start_polling()
print('Bot started!')

# Wait for the bot to stop
updater.idle()

# Dump persistent state
with open('data.txt', 'w') as file:
    json.dump(counter_dict, file)

print('Bot stopped!')



# Hoe to go about create a responsive Bot


# need another file which does the scrapping of the data from the website requested.
# cretae in a server
