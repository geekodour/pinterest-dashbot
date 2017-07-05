import os
import json
import random
import time
from core import pinBot

bot_dir = os.path.dirname(__file__)
with open(os.path.join(bot_dir,'pinterestBot.json')) as json_data:
    bot_config = json.load(json_data)

bot = pinBot()
followingUsers = bot.getFollowingUsers()
followingBoards = bot.getFollowingBoards()

# fix number of users and boards to unfollow
user_unfollow_count = bot_config['user']['unfollow']
board_unfollow_count = bot_config['user']['unfollow']

if len(followingUsers) <= user_unfollow_count:
    user_unfollow_count = len(followingUsers)

if len(followingBoards) <= board_unfollow_count:
    board_unfollow_count = len(followingBoards)

# unfollow random users
for user in random.sample(followingUsers,user_unfollow_count):
    time.sleep(1)
    bot.unfollowUser(user)

# unfollow random boards
for board in random.sample(followingBoards,board_unfollow_count):
    time.sleep(1)
    bot.unfollowBoard(board)
