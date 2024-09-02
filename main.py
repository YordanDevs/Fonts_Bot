# Desarrollado por @YordanDev  Canal: https://t.me/BuzzWireProject

# Librerías
import telebot
from telebot import types

# Token del bot 
TOKEN = '7506418745:AAFE73h3PaOqWK-5-2SH46jRDapngi3COcw'
bot = telebot.TeleBot(TOKEN)

# Mapeo de fuentes estilizadas
font_mapping = {
    # Fuente 1
    'A': '𝔸', 'B': '𝔹', 'C': 'ℭ', 'D': '𝔻', 'E': '𝔼',
    'F': '𝔽', 'G': '𝔾', 'H': 'ℍ', 'I': '𝕀', 'J': '𝕁',
    'K': '𝕂', 'L': '𝕃', 'M': '𝕄', 'N': '𝕆', 'Ñ': '𝕹',
    'O': '𝕆', 'P': 'ℙ', 'Q': 'ℚ', 'R': 'ℝ', 'S': '𝕊',
    'T': '𝕋', 'U': '𝕌', 'V': '𝕍', 'W': '𝕎', 'X': '𝕏',
    'Y': '𝕐', 'Z': 'ℤ',
    
    # Minúsculas
    'a': '𝕒', 'b': '𝕓', 'c': '𝕔', 'd': '𝕕', 'e': '𝕖',
    'f': '𝕗', 'g': '𝕘', 'h': '𝕙', 'i': '𝕚', 'j': '𝕛',
    'k': '𝕜', 'l': '𝕝', 'm': '𝕞', 'n': '𝕟', 'ñ': '𝕟',
    'o': '𝕠', 'p': '𝕡', 'q': '𝕢', 'r': '𝕣', 's': '𝕤',
    't': '𝕥', 'u': '𝕦', 'v': '𝕧', 'w': '𝕨', 'x': '𝕩',
    'y': '𝕪', 'z': '𝕫',
    
    # Números
    '0': '⓪',  '1': '①', '2': '②',
    '3': '③', '4': '④', '5': '⑤',
    '6': '⑥', '7': '⑦', '8': '⑧',
    '9': '⑨',

    # Fuente 2 (Cursiva)
    # Mayúsculas
    "A": "𝓐", "B": "𝓑", "C": "𝓒", "D": "𝓓", "E": "𝓔",
    "F": "𝓕", "G": "𝓖", "H": "𝓗", "I": "𝓘", "J": "𝓙",
    "K": "𝓚", "L": "𝓛", "M": "𝓜", "N": "𝓝", "Ñ": "𝓝",
    "O": "𝓞", "P": "𝓟", "Q": "𝓠", "R": "𝓡", "S": "𝓢",
    "T": "𝓣", "U": "𝓤", "V": "𝓥", "W": "𝓦", "X": "𝓨",
    "Y": "𝓨", "Z": "𝓩",

    # Minúsculas
    "a": "𝓪", "b": "𝓫", "c": "𝓬", "d": "𝓭", "e": "𝓮",
    "f": "𝓯", "g": "𝓰", "h": "𝓱", "i": "𝔦", "j": "𝔧",
    "k": "𝔨", "l": "𝔩", "m": "𝔪", "n": "𝔫", "ñ": "𝔫",
    "o": "𝓸", "p": "𝔭", "q": "𝔮", "r": "𝔯", "s": "𝔰",
    "t": "𝔱", "u": "𝔲", "v": "𝔳", "w": "𝔴", "x": "𝔵",
    "y": "𝔶", "z": "𝔷",

    # Fuente 3 (Gótica)
    # Mayúsculas
    "\u0041": "\u{1D504}", "\u0042": "\u{1D505}", "\u0043": "\u{1D506}",
    "\u0044": "\u{1D507}", "\u0045": "\u{1D508}", "\u0046": "\u{1D509}",
    "\u0047": "\u{1D50A}", "\u0048": "\u{1D50B}", "\u0049": "\u{1D50C}",
    "\u004A": "\u{1D50D}", "\u004B": "\u{1D50E}", "\u004C": "\u{1D50F}",
    "\u004D": "\u{1D510}", "\u004E": "\u{1D511}", "\u00D1": "\u{1D511}",
    "\u004F": "\u{1D512}", "\u0050": "\u{1D513}", "\u0051": "\u{1D514}",
    "\u0052": "\u{1D515}", "\u0053": "\u{1D516}", "\u0054": "\u{1D517}",
    "\u0055": "\u{1D518}", "\u0056": "\u{1D519}", "\u0057": "\u{1D51A}",
    "\u0058": "\u{1D51B}", "\u0059": "\u{1D51C}", "\u005A": "\u{1D51D}",
    
    # Minúsculas
    "\u0061":"\u{1D51E}","\u0062":"\u{1D51F}","\u0063":"\u{1D520}",
    "\u0064":"\u{1D521}","\u0065":"\u{1D522}","\u0066":"\u{1D523}",
    "\u0067":"\u{1D524}","\u0068":"\u{1D525}","\u0069":"\u{1D526}",
    "\u006A":"\u{1D527}","\u006B":"\u{1D528}","\u006C":"\u{1D529}",
    "\u006D":"\u{1D52A}","\u006E":"\u{1D52B}","\u006F":"\u{1D52C}",
    "\u0070":"\u{1D52D}","\u0071":"\u{1D52E}","\u0072":"\u{1D52F}",
    "\u0073":"\u{1D530}","\u0074":"\u{1D531}","\u0075":"\u{1D532}",
    "\u0076":"\u{1D533}","\u0077":"\u{1D534}","\u0078":"\u{1D535}",
    "\u0079":"\u{1D536}","\u007A":"\u{1D537}"
}

def convert_text(text):
    converted_text = ""
    for char in text:
        converted_text += font_mapping.get(char, char)  # Reemplaza o deja el carácter original
    return converted_text

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hola, Bienvenido al bot de @YordanDev")

@bot.inline_handler(lambda query: True)
def query_text(inline_query):
    if inline_query.query:
        result_text = convert_text(inline_query.query)
        bot.answer_inline_query(inline_query.id, [
            types.InlineQueryResultArticle(
                id='1',
                title='Texto Estilizado',
                input_message_content=types.InputTextMessageContent(
                    message_text=result_text,
                    parse_mode='Markdown'
                )
            )
        ])

###### MAIN ######
def recibir_mensajes():
    bot.infinity_polling()

if __name__ == '__main__':
    print("Iniciando el bot......")
    bot.set_my_commands([
        telebot.types.BotCommand('/start', "Inicia el bot")
    ])
    recibir_mensajes()