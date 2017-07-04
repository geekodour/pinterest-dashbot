import json
import random
import time
from core import pinBot

bot = pinBot()

with open('pinterestBot.json') as json_data:
    bot_config = json.load(json_data)
with open('done_pins.json') as json_data:
    done_pins = json.load(json_data)

# generate posts to post
available_posts = list(filter(lambda x: x['imageUrl'] in done_pins ,bot_config['posts']))

for post in random(available_posts,bot_config['periods']['post_to_post_per_day']):
    bot.createPost(post['imageUrl'],post['note'])
    done_pins.append(post['imageUrl'])

with open('done_pins.json', 'w') as outfile:  
    json.dump(done_pins, outfile)
