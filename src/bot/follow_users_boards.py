import json
import random
import time
from core import pinBot

with open('pinterestBot.json') as json_data:
    bot_config = json.load(json_data)

bot = pinBot()
# please note, user.follow and board.follow will be repeated for each search term
# so, if you have 10 user follows and 5 search terms you'll end up follwing 50 users
# and 50 boards, which might seem fish to pintrest, so adjust that accordingly
for term in bot_config.search_terms:
    boardIds,users = bot.search(term,'board',bot_config.board.scrolls)
    # follow users
    for user in random.sample(users,bot_config.user.follow):
        bot.followUser(user)
        time.sleep(1) # maybe randomize
    # follow boards
    for board in random.sample(boardIds,bot_config.board.follow):
        bot.followBoard(board)
        time.sleep(1) # maybe randomize
