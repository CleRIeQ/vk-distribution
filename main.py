import time

import vk_api
import schedule

from config import *

# Счётчик для отправки сообщений пользователям последовательно
users_offset = 0

# Информация об отправленных комментариев к постам
table_info = {}

# Функция для отправки поста в группу
def post_to_group(api):
    api.wall.post(owner_id=-GroupID, message=AdvertisingText, random_id=123456)


# Функция для отправки комментария в пост
def post_comment(api, group_id, post_id):
    api.wall.createComment(owner_id=-group_id, post_id=post_id, message="Привет")


# Функция для отправки рассылки подписчикам группы
def send_group_messages(api, offset):
    members = api.groups.getMembers(group_id=GroupID, v='5.131')['items']

    for member_id in members[offset:]:
        api.messages.send(user_id=member_id, message=SubscribersAdText, random_id=123456)
        time.sleep(120)

    offset += 10


# Функция для вывода таблицы с информацией о группах
def update_table():
    print('-----------------------------------------------------')
    print('|   Номер группы   |   ID Группы   |    ID Поста    |')
    print('-----------------------------------------------------')
    for index, (key, value) in enumerate(table_info.items(), start=1):
        print(f'|     {index}     |     {value}    |     {key}     |')
    print('-----------------------------------------------------')

# Функция для получения последнего поста группы
def get_last_post(vk, group_id):
    response = vk.wall.get(owner_id=-group_id, count=1, offset=0)

    post = response['items']

    return post[0]['id']

# Функция для отправки комментариев в группы
def send_commentaries(vk):
    for group_id in CommentsGroup:
        post_id = get_last_post(vk, group_id)
        post_comment(vk, group_id, post_id)

        table_info[post_id] = group_id

        update_table()



# Основная функция для запуска бота
def main():

    vk_session = vk_api.VkApi(token=Token)
    vk = vk_session.get_api()

    # Здесь задаются запланированные события отправки сообщений, постов и тд

    # Отправка постов
    schedule.every(2).hours.do(
        post_to_group, vk
    )

    # Отправка комментариев в группы
    schedule.every(3).hours.do(
        send_commentaries, vk
    )

    # Рассылка сообщений подписчикам групп
    schedule.every(2).hours.do(
        send_group_messages, vk, users_offset
    )

    while True:
        schedule.run_pending()


# Запуск бота
if __name__ == '__main__':
    main()
