import telegram
from environs import Env


def main():
    env = Env()
    env.read_env()
    TELEGRAM_API_TOKEN = env('TELEGRAM_API_TOKEN')
    bot = telegram.Bot(token=TELEGRAM_API_TOKEN)
    print(bot.get_me())
    bot.send_message(text='Hello from tb_bot.py!', chat_id='@andreysSpacePics')


if __name__ == '__main__':
    main()
