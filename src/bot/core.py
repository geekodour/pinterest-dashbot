#!/usr/bin/env python
# -*- coding: utf8 -*-
import requests
import time
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re

# user agent settings
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
            return list(set(ids))

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
            return (list(set(ids)),list(set(users)))
        else:
            raise "something happened"

    def followUser(self,userId):
        params = [ 'access_token='+ACCESS_TOKEN, 'user='+userId]
        r = requests.post(self.apiUrl+'me/following/users/?'+'&'.join(params))

    def unfollowUser(self,userId):
        params = [ 'access_token='+ACCESS_TOKEN ]
        r = requests.delete(self.apiUrl+'me/following/users/'+userId+'?'+'&'.join(params))

    def followBoard(self,boardId):
        params = [ 'access_token='+ACCESS_TOKEN, 'board='+boardId]
        r = requests.post(self.apiUrl+'me/following/boards/?'+'&'.join(params))

    def unfollowBoard(self,boardId):
        params = [ 'access_token='+ACCESS_TOKEN ]
        r = requests.delete(self.apiUrl+'me/following/boards/'+boardId+'?'+'&'.join(params))

    def getFollowingBoards(self):
        params = [ 'access_token='+ACCESS_TOKEN ]
        r = requests.get(self.apiUrl+'me/following/boards/?'+'&'.join(params))
        extract_board_name = lambda x: '/'.join(urlparse(x['url']).path.split('/')[1:3])
        return list(map(extract_board_name ,r.json()['data']))

    def getFollowingUsers(self):
        params = [ 'access_token='+ACCESS_TOKEN ]
        r = requests.get(self.apiUrl+'me/following/users/?'+'&'.join(params))
        extract_username = lambda x: urlparse(x['url']).path.strip('/')
        return list(map(extract_username ,r.json()['data']))

    def savePin(self,pinId):
        # save pin method is not implemented yet
        params = [ 'access_token='+ACCESS_TOKEN ]
        r = requests.patch(self.apiUrl+'me/following/users/'+userId+'?'+'&'.join(params))

    def createPost(self,imageUrl,imageDesc):
        params = [ 'access_token='+ACCESS_TOKEN ]
        r = requests.post(self.apiUrl+'pins/?'+'&'.join(params),data={'board':'hrishikeshbarma/pinboard','note':imageDesc, 'image_url': imageUrl})
        print(r.status_code)
