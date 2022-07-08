from flask import Flask
from flask import request
from flask import Response
import requests

TOKEN = "5393889257:AAH11FtoYCFyFdBem5Kk9C1EaAf6ntA1Qmk"
app = Flask(__name__)


def parse_message(message):
    print("message-->", message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id, txt


def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    r = requests.post(url, json=payload)
    return r


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id, txt = parse_message(msg)
        if txt == "/start":
            tel_send_message(chat_id,
                             "Привет!\nТы нашел меня!\nЯ - новый проект по торговле BTC и ETH методом P2P - твой бот "
                             "'Марк'")
            main_menu(chat_id)
        elif txt == "button":
            main_menu(chat_id)
        elif txt == "Кто Мы?":
            tel_send_button2(chat_id)
        elif txt == "Че там на рынке?":
            tel_send_message(chat_id, "В данный момент цена BTC равняется " + str(get_data("BTC", "price")) + " USD")
            tel_send_message(chat_id, "А за один ETH придется отдать " + str(get_data("ETH", "price")) + " USD")
            tel_send_message(chat_id, "Что же касается SOL, то в данный момент цена составляет " + str(
                get_data("SOL", "price")) + " USD")
            tel_send_button_universal(chat_id, text="Что дальше?", button2="Назад", button1="Присылай мне уведомления!")
            # tel_send_message(chat_id, "Стоит также заметить, что за 24 часа цена BTC изменилась на " + get_data("BTC","change_day") + "%")
        elif txt == "Пожертвовать":
            tel_send_message(chat_id,
                             "BTC:\nbc1q72auymr3pcqmgygpqh73y555pslwv8swam9m9a")
            tel_send_message(chat_id,
                             "ETH:\n0x3ac8632B6702749232CDcB1Aa9d2c166e317C30f")
            return_to_main_menu(chat_id)
        elif txt == "Главное меню":
            main_menu(chat_id)
        elif txt == "Назад":
            main_menu(chat_id)
        elif txt == "Торговля":
            tel_send_button_buyorsell(chat_id)
        elif txt == "Продать":
            tel_send_button_eth_or_btc(chat_id)
        elif txt == "Присылай мне уведомления!":
            tel_send_button_universal3(chat_id, text="Как часто?", button1="Каждый час", button2="Каждый день",
                                       button3="Назад")
        elif txt == "Каждый час":
            tel_send_message(chat_id,
                             "Поздравляю, теперь Вы будете каждый час получать сводки новостей крипторынков ")
            tel_send_button_universal1(chat_id, "Больше тут делать нечего", "Назад")
        else:
            tel_send_message(chat_id, 'from webhook')

        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"


def main_menu(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': "Навигация",
        'reply_markup': {
            'keyboard': [[{'text': 'Кто Мы?'}, {'text': 'FAQ'}, {'text': 'Че там на рынке?'}, {'text': 'Торговля'}]]}
    }

    r = requests.post(url, json=payload)

    return r


def tel_send_button2(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': "Мы - студенты, которые верят в будущее криптовалют.\nПоэтому, в качестве наработки собственного портфолио, была придумана идея бота, помогающего людям купить или продать криптовалюту.\nМы очень серьезно относимся к приватности наших пользователей, поэтому будьте уверены: мы не храним никакие наши данные на сервере, включая историю активности и транзакции.\nТакже, если вдруг очень хочется, можете поддержать нас пожертвованием.",
        'reply_markup': {'keyboard': [[{'text': 'Пожертвовать'}, {'text': 'Назад'}]]}
    }

    r = requests.post(url, json=payload)

    return r


def tel_send_button_buyorsell(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': "Хотите купить или продать криптовалюту?",
        'reply_markup': {'keyboard': [[{'text': 'Купить'}, {'text': 'Продать'}]]}
    }

    r = requests.post(url, json=payload)

    return r


def tel_send_button_eth_or_btc(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': "BTC, ETH, SOL?",
        'reply_markup': {'keyboard': [[{'text': 'BTC'}, {'text': 'ETH'}, {'text': 'SOL'}]]}
    }

    r = requests.post(url, json=payload)

    return r


def tel_send_button_universal(chat_id, text, button1, button2):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': {'keyboard': [[{'text': button1}, {'text': button2}]]}
    }

    r = requests.post(url, json=payload)

    return r


def tel_send_button_universal1(chat_id, text, button1):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': {'keyboard': [[{'text': button1}]]}
    }

    r = requests.post(url, json=payload)

    return r


def tel_send_button_universal3(chat_id, text, button1, button2, button3):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': {'keyboard': [[{'text': button1}, {'text': button2}, {'text': button3}]]}
    }

    r = requests.post(url, json=payload)

    return r


def return_to_main_menu(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': "Перейти в главное меню?",
        'reply_markup': {'keyboard': [[{'text': 'Главное меню'}]]}
    }

    r = requests.post(url, json=payload)

    return r


def get_data(coin1, parameter):
    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(coin1)).json()[
        "RAW"]
    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "price": crypto_data[i]["USD"]["PRICE"],
            "change_day": crypto_data[i]["USD"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_data[i]["USD"]["CHANGEPCTHOUR"],

        }
    return data[coin1][parameter]


if __name__ == '__main__':
    app.run(debug=True)
