import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType



class VkBot:
    def __init__(self, token):
        token = token

    _events = ['Вызвать всех']

    vk_session = vk_api.VkApi(token=token)
    session_api = vk_session.get_api()
    longpool = VkBotLongPoll(vk_session)

    while True:
        for event in longpool.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                print('i am here')