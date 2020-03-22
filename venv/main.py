import VkBot

print('Access token: ')
token = input()
print('Group id: ')
group_id = input()

try:
    bot = VkBot.VkBot(token, group_id)
    bot.massage()
except:
    print('Error! Check your token or group id')
