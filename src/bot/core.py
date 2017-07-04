#!/usr/bin/env python
# -*- coding: utf8 -*-
import requests
import time
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.common.keys import Keys
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
)

ACCESS_TOKEN = 'AbVZ6pBecrXC9afBG9mahRCxS8NuFM2MA50rraBEIg4xUYA_VwAAAAA'

class pinBot():
    def __init__(self):
        self.baseUrl = 'https://in.pinterest.com'
        self.apiUrl = 'https://api.pinterest.com/v1/'

    def search(self,keyword,searchType,scrolls):
        # todo: urlquote keyword
        ids = []
        users = []
        if(searchType=='pin'):
            pinDriver = webdriver.PhantomJS(desired_capabilities=dcap)
            pinDriver.get( self.baseUrl + r'/search/pins/?q=' + keyword )
            pinEls = []

            while scrolls:
                pinDriver.execute_script("return window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)
                scrolls-=1

            pinEls.extend(pinDriver.find_elements_by_css_selector('.pinImageWrapper'))
            for pin in pinEls:
                ids.append(re.search('\d+',pin.get_attribute('href')).group())
            pinDriver.quit()
            return set(ids)

        elif(searchType=='board'):
            boardDriver = webdriver.PhantomJS(desired_capabilities=dcap)
            boardDriver.get( self.baseUrl + r'/search/boards/?q=' + keyword )
            boardEls = []

            while scrolls:
                boardDriver.execute_script("return window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)
                scrolls-=1

            boardEls.extend(boardDriver.find_elements_by_css_selector('.boardLinkWrapper'))
            for board in boardEls:
            	boardData = urlparse(board.get_attribute('href')).path.split('/')[1:3]
            	ids.append( '/'.join(boardData) )
            	users.append(boardData[0])
            boardDriver.quit()
            return (set(ids),set(users))
        else:
            raise "something happened"

    def followUser(self,userId):
        params = [ 'access_token='+ACCESS_TOKEN, 'user='+userId]
        r = requests.post(self.apiUrl+'me/following/users/?'+'&'.join(params))
        print(r.status_code)

    def unfollowUser(self,userId):
        params = [ 'access_token='+ACCESS_TOKEN ]
        r = requests.post(self.apiUrl+'me/following/users/'+userId+'?'+'&'.join(params))
        print(r.status_code)

    def followBoard(self,boardId):
        params = [ 'access_token='+ACCESS_TOKEN, 'board='+boardId]
        r = requests.post(self.apiUrl+'me/following/boards/?'+'&'.join(params))
        print(r.status_code)

    def unfollowBoard(self,boardId):
        params = [ 'access_token='+ACCESS_TOKEN ]
        r = requests.post(self.apiUrl+'me/following/boards/'+boardId+'?'+'&'.join(params))
        print(r.status_code)

    def getFollowingBoards(self):
        params = [ 'access_token='+ACCESS_TOKEN ]
        r = requests.get(self.apiUrl+'me/following/boards/?'+'&'.join(params))
        extract_board_name = lambda x: '/'.join(urlparse(x['url']).path.split('/')[1:3])
        return list(map(extract_board_name ,r.json()['data']))

    def getFollowingUsers(self):
        params = [ 'access_token='+ACCESS_TOKEN ]
        r = requests.get(self.apiUrl+'me/following/users/?'+'&'.join(params))
        #extract_username = lambda x: 
        #return list(map(extract_username ,r.json()['data']))
        print(r.json()['data'])
        print(r.status_code)

    def savePin(self,pinId):
        # save pin method is not implemented yet
        params = [ 'access_token='+ACCESS_TOKEN ]
        r = requests.patch(self.apiUrl+'me/following/users/'+userId+'?'+'&'.join(params))

    def createPost(self,imageUrl):
        pass



"""
Requirements:
    1. search a topic
    2. get 10 results
    3. follow those boards, save those pins(if pins), follow board creators
    4. if already followed, unfollow them and skip.
    repeat this 3 times in a day.
API endpoints provided :
1. fetch user data (not needed)
2. create user follow and board follow
	/v1/me/following/boards/ POST
	/v1/me/following/users/ POST
2. delete user follow and board follow
	/v1/me/following/boards/<board>/
	/v1/me/following/users/ POST
FOLLOW example
https://api.pinterest.com/v1/me/following/users/?access_token=AbVZ6pBecrXC9afBG9mahRCxS8NuFM2MA50rraBEIg4xUYA_VwAAAAA&user=rdturner31
https://api.pinterest.com/v1/me/following/boards/?access_token=AbVZ6pBecrXC9afBG9mahRCxS8NuFM2MA50rraBEIg4xUYA_VwAAAAA&board=janew/happy
UNFOLLOW
https://api.pinterest.com/v1/me/following/users/rdturner31?access_token=AbVZ6pBecrXC9afBG9mahRCxS8NuFM2MA50rraBEIg4xUYA_VwAAAAA

Search urls:
1. boards search: https://in.pinterest.com/search/boards/?q=happy
1. pin search: https://in.pinterest.com/search/pins/?q=cool
"""
