Как запустить бота?
1) Установите Pyhton (нужно перейти на https://www.python.org/downloads/ и оттуда скачать, нажав на "Download Python 3.11.4")
2) Создайте вируальное окружение: python -m venv venv
3) Активируйте вируальное окружение: .\venv\Scripts\activate (если у вас Linux, то source venv/bin/activate)
4) Установите зависимости: pip install -r requirements.txt
5) Получите api токен (см. ниже)
6) Запустите бота (из корневой папки проекта): python bot/main.py

Как получить access токен?
1) Зайдите на сайт https://vkhost.github.io/, и выберите приложение vk.com
2) После подтверждения, скопируйте токен из поисковой строки после access_token
3) Вставьте его в файл bot/config.py в строку Token