import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType



class VkBot:
    token = ''
    group_id = ''
    def __init__(self, token, group_id):
        self.token = token
        self.group_id = group_id

    _events = ['Вызвать всех']

    vk_session = vk_api.VkApi(token=token)
    session_api = vk_session.get_api()
    longpool = VkBotLongPoll(vk_session)

    while True:
        for event in longpool.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                print('i am here')