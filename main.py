#Desarrollado por @YordanDev  Canal: https://t.me/BuzzWireProject

#Librerias
import telebot
from telebot import types

#Token del bot 
TOKEN = 'Token_de_tu_bot'
bot = telebot.TeleBot(TOKEN)

fonts = {
    "Negrita": lambda text: f"**{text}**"
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message, "Hola, Bienvenido a el bot de @YordanDev")

@bot.inline_handler(lambda query: True)
def query_text(inline_query):
    results = []
    for font in fonts:
        results.append(types.InlineQueryResultArticle(
            id=font,
            title=font,
            input_message_content=types.InputTextMessageContent(
                message_text=fonts[font](inline_query.query),
                parse_mode='Markdown'
            )
        ))
    bot.answer_inline_query(inline_query.id, results)

######MAIN######
def recibir_mensajes():
    bot.infinity_polling()

if __name__ == '__main__':
    print("Iniciando el bot......")
    bot.set_my_commands([
        telebot.types.BotCommand('/start', "Inicia el bot")
    ])
    recibir_mensajes()
