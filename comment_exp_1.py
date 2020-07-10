import webbrowser
import sinaweibopy3
import os
import sys
import urllib.request
import http.cookiejar
import urllib.parse
import sys
import re
import base64
import json
import math
import requests

'''mid->id'''
mymid = '4420560555806815'
id = '4420841104391612'
id = '4350597576707582'
id = '4425633985395930'
id = '4425633977279338'
# def get_id(mid):
#     url_mid = 'https://api.weibo.com/2/statuses/queryid.json'
#     values = {'access_token': '2.00taRMTDBjMdyBcb4a8f8594dA8_HC',
#      'mid': mid,
#     'isBase62': '1',
#     'type': '1'}
#     data = urllib.parse.urlencode(values)
#     data = data.encode('UTF-8')
#     url_t = 'https://api.weibo.com/2/statuses/queryid.json?access_token=2.00taRMTDBjMdyBcb4a8f8594dA8_HC&mid=4420560555806815&type=1&isBase62=1'
#     url = 'https://api.weibo.com/2/statuses/queryid.json?access_token=2.00taRMTDBjMdyBcb4a8f8594dA8_HC&type=1&isBase62=1&mid=' + mid
#     html = urllib.request.urlopen(url)
#     id = json.loads(html.read().decode('UTF-8'))
#     print(id['id'])
#     return id['id']
#
# get_id(mymid)


'''mid->id'''
# mymid = 'BrSr7g51Q'
# def get_id(mid):
#     url_mid = 'https://api.weibo.com/2/statuses/queryid.json'
#     values = {'access_token':'2.00taRMTDBjMdyBcb4a8f8594dA8_HC',
#     'mid':mid,
#     'isBase62':'1',
#     'type':'1'}
#     data = urllib.parse.urlencode(values)
#     data = data.encode('UTF-8')
#     url_t = 'https://api.weibo.com/2/statuses/queryid.json?access_token=2.00taRMTDBjMdyBcb4a8f8594dA8_HC&mid=4420560555806815&type=1&isBase62=1'
#     url = 'https://api.weibo.com/2/statuses/queryid.json?access_token=2.00taRMTDBjMdyBcb4a8f8594dA8_HC&type=1&isBase62=1&mid=' + mid
#     html = urllib.request.urlopen(url)
#     id = json.loads(html.read().decode('UTF-8'))
#     print (id['id'])
#     return id['id']



def reply(cid,id,user):
    values ={
        'access_token':'2.00taRMTDBjMdyBcb4a8f8594dA8_HC',
    # "access_token":'2.00taRMTDLZLu8C09c2094c79HChG5B',
    'cid':cid,
    'id':id,
    'comment':'我也一定会过来'}
    url_reply = 'https://api.weibo.com/2/comments/reply.json'
    data = urllib.parse.urlencode(values)
    data =data.encode('UTF-8')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    # url =urllib.request.Request(url=url_reply,data=data,headers=headers)
    # html = urllib.request.urlopen(url)
    # html = requests.post(url=url_reply,data=data,headers=headers)
    # print(html.text)
    # infomation = requests.post(url=url_reply, data=values, verify=False).text
    # print(infomation)
    information = requests.post(url=url_reply,data=values,verify=False).text
    print(information)
    # html = urllib.request.urlopen(req)

'''通过id获取某条微博的所有评论信息'''
def show(id):
    url_show = 'https://api.weibo.com/2/comments/show.json'
    values = {
        'access_token':'2.00taRMTDBjMdyBcb4a8f8594dA8_HC',
        # "access_token": '2.00taRMTDLZLu8C09c2094c79HChG5B',
    'id':id}
    data = urllib.parse.urlencode(values)
    data = data.encode('UTF-8')
    url = 'https://api.weibo.com/2/comments/show.json?access_token=2.00taRMTDBjMdyBcb4a8f8594dA8_HC&id=' + id
    html = urllib.request.urlopen(url)
    s = json.loads(html.read().decode('UTF-8'))
    j = s['total_number']

    # print(s)
    for i in range(0,j):
        print(i)
        cid = s['comments'][i]['mid']
        print(cid)
        user = s['comments'][i]['user']['screen_name']
        reply(cid,id,user)


def get_id():
    pass

def check_limit():
    limit_url = 'https://api.weibo.com/2/account/rate_limit_status.json'
    values = {"access_token":'2.00taRMTDLZLu8C09c2094c79HChG5B',}
    data = urllib.parse.urlencode(values)
    data = data.encode('UTF-8')
    information = requests.get(url=limit_url, data=values, verify=False).text
    print(information)

show(id)

def create_comment(id):
    url_comment = 'https://api.weibo.com/2/comments/create.json'
    values = {"access_token": '2.00taRMTDBjMdyBcb4a8f8594dA8_HC',
              "id":id,
              "comment":"我希望可以和你一起去啊！"}
    data = urllib.parse.urlencode(values)
    data = data.encode('UTF-8')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    information = requests.post(url=url_comment, data=values, verify=False).text
    print(information)



# check_limit()
# create_comment(id)