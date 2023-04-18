import ftplib
import os
import time
from tkinter import filedialog
import tkinter
import tabulate

def init():
    # оичистка экрана и объявление глобальных переменных
    os.system('CLS')
    global ftp
    global root

    # tkinter нужен для диалоговых окон
    root=tkinter.Tk()
    root.withdraw()

    # ввод Ip адреса ftp сервера, имени пользователя и пароля
    SERVER = str(input("IP: "))
    USER = str(input("User: "))
    PASS = str(input("Password: "))

    # попытка подключения к серверу
    try:
        ftp = ftplib.FTP(SERVER)
        ftp.login(USER, PASS)
        print()
        print(f"[OK] Соединение с {SERVER} установлено!")
        print()
        time.sleep(5)
        # в случае удачного соединения вызывается основная функция
        maindef()
    except:
        print()
        print(f"[ERROR] Ошибка соединения с {SERVER}!")
        print(f"[ERROR] Проверьте правильность введеных данных!")
        print()
        time.sleep(5)
        # в случае ошибки функция init() повторится
        init()

def fil_size():
    filenames = []
    ftp.retrlines('LIST', lambda line: filenames.append(line.split()))
    data = [
        ['Имя', 'Размер', 'Дата изменения'],
    ]

    for file in filenames:
        te=float(file[2])
        cont=0
        while te>=1024:
            te/=1024
            cont+=1
        if cont==0:
            dat="Байт"
        if cont==1:
            dat="Кб"
        if cont==2:
            dat="Мб"
        if cont==3:
            dat="Гб"
        dat2=[
            file[3], str(float('{:.3f}'.format(te)))+dat, file[1]+" "+file[0]
        ]
        data.append(dat2)
    print()
    results = tabulate.tabulate(data)
    return results

def maindef():
    # цикл для выбора действий
    choose=-1
    while choose!=0:
        # Очистка консоли и вывод "меню"
        os.system('CLS')
        print("1. Вывести список файлов и каталогов")
        print("2. Загрузить файл на сервер")
        print("3. Скачать файл с сервера")
        print("0. Выход")
        choose = int(input("Выбирите действие: "))

        if choose == 1:
            print()
            # Вывод списка файлов и каталогов на сервере
            print(fil_size())
            print()
            time.sleep(5)
        elif choose == 2:
            # Выбор файла для отправики на сервер
            file = filedialog.askopenfilename()
            # открытие файла, после чтения и отправки его закрытие
            with open(file, 'rb') as upload_file:
                ftp.storbinary('STOR ' + os.path.basename(file), upload_file)
            print()
            print(f"[OK] Файл: {file} был загружен на сервер")
            print()
            time.sleep(5)
        elif choose == 3:
            print()
            # Выбор файла для отправики на сервер
            print(fil_size())
            print()
            file = str(input('Какой файл скачаем с сервера: '))
            # Выбор дериктории для сохранения файла
            dir = filedialog.askdirectory()
            # открытие файла и запись файла
            with open(dir+"\\"+file, 'wb') as f:
                ftp.retrbinary('RETR ' + file, f.write)
            print()
            print(f"[OK] Файл: {file} был скачан в {dir}/{file}")
            print()
            time.sleep(5)
        elif choose == 0:
            # выход
            return
        else:
            # если выбрали того что нет в списке
            print("[ERROR] Нет даннного действия")
            time.sleep(5)
            maindef()

    # Закрываем FTP соединение
    ftp.close

# начало выполнения
if __name__ == "__main__":
    init()
