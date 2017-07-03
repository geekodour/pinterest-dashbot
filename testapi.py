#!/usr/bin/env python
# -*- coding: utf8 -*-
import requests

ACCESS_TOKEN = 'AbVZ6pBecrXC9afBG9mahRCxS8NuFM2MA50rraBEIg4xUYA_VwAAAAA'
API_URL = 'https://api.pinterest.com/v1/'
params = [ 'access_token='+ACCESS_TOKEN ]
print(API_URL+'boards/anapinskywalker/wanderlust/pins'+'?'+'&'.join(params))
r = requests.get(API_URL+'boards/anapinskywalker/wanderlust/pins'+'?'+'&'.join(params))
print(r.json())
