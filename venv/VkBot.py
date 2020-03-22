import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id


class VkBot:
    def __init__(self, token, group_id):
        self.token = token
        self.group_id = group_id
        self.vk_session = vk_api.VkApi(token=token)
        self.session_api = self.vk_session.get_api()
        self.longpool = VkBotLongPoll(self.vk_session, self.group_id)
        self.events = ['!everyone']

    def massage(self):
        while True:
            for event in self.longpool.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    peer_id = event.obj['peer_id']
                    _str = ''

                    if self.events.__contains__(event.object.text):
                        print('command received from peer id: ', peer_id)
                        ids = self.getConversationId(peer_id)
                        ids1 = ids['items']

                        for i in ids1:
                            _id = i['member_id']

                            if _id > 0:
                                _str += f'[id{_id}| ]'

                        self.session_api.messages.send(
                            peer_id=peer_id,
                            message=_str,
                            random_id=get_random_id()
                        )
                        print('message sent')

    def getConversationId(self, peer_id):
        ids = self.session_api.messages.getConversationMembers(peer_id=peer_id)
        return ids
