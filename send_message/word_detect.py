import requests
import json
import os
from random import choice
group = json.load(open("./config.json", encoding='utf-8'))["group"]
apikey= json.load(open("./config.json", encoding='utf-8'))["apikey"]
ban_words = json.load(open("./config.json", encoding='utf-8'))["ban_words"]
path = json.load(open("./config.json", encoding='utf-8'))["path"]

help_base = "这里是帮助菜单：\n"
help_base += "1.发送setu or 猫猫图返回一张图\n"
help_base += "2.私聊调教对话 例如aaa+bbb \n"
help_base += "那么发送aaa就会返回bbb啦~\n"
help_base += "可以发送rmaaa+bbb删除对话哦~\n"

def help_menu(msg):
	if msg[:4]!="help":
		return [False]
	if msg == "help":
		return [True,help_base]
	
def add_data(msg,all_data):
	if msg.count("+") != 1:
		return [False]
	if "/" in msg or "|" in msg:
		return [True,"不能含有/或|呀~"]
	if msg.split("+")[1]=="":
		return [False]
	msg = msg.split("+")
	if len(msg[0])< 3:
		return [True,"长度要大于2呀~"]
	for row in all_data:
		if msg[0] == row[0]:
			if msg[1] in row[1]:
				return [True,"这句话我已经会辣，不用再教我啦~"]
			row[1].append(msg[1])
			save_data(all_data)
			return [True,"添加成功！"]
	all_data.append([msg[0], [msg[1]]])
	save_data(all_data)
	return [True,"添加成功！"]

def save_data(all_data):
	f = open("./data/talk_data/words","w",encoding='UTF-8')
	for row in all_data:
		temp = row[0]+"|"+"".join([i+"/" for i in row[1]])
		f.writelines(temp+"\n")
	f.close()

def del_data(del_data,all_data):
	if del_data[:2] != "rm":
		return [False]
	msg = del_data[2:].split("+")
	for i in range(len(all_data)):
		if msg[0] == all_data[i][0]:
			if len(all_data[i][1]) == 1:
				all_data.pop(i)
				save_data(all_data)
				return [True]
			all_data[i][1].remove(msg[1])
			save_data(all_data)
			return [True]
	return [True,"删除出错啦~"]


def ghs_pic(msg):
    if msg in ["setu"]:
        try:
            req_url="https://api.lolicon.app/setu/"
            params = {"apikey":apikey}
            res=requests.get(req_url,params=params)
            setu_title=res.json()['data'][0]['title']
            setu_url=res.json()['data'][0]['url']
            setu_pid=res.json()['data'][0]['pid']
            setu_author=res.json()['data'][0]['author']
            local_img_url = "title:"+setu_title+"[CQ:image,file="+setu_url+"]"+"pid:"+str(setu_pid)+" 画师:"+setu_author
            return [True, local_img_url]
        except Exception as e:
            print(e)
            return [True, "阿这，出了一点问题"]
    return [False]

def hs_pic(msg):
    if msg in ["huangse"]:
        try:
            req_url="https://api.lolicon.app/setu/"
            params = {"apikey":apikey,"r18":"1"}
            res=requests.get(req_url,params=params)
            setu_title=res.json()['data'][0]['title']
            setu_url=res.json()['data'][0]['url']
            setu_pid=res.json()['data'][0]['pid']
            setu_author=res.json()['data'][0]['author']


            local_img_url = "title:"+setu_title+"[CQ:image,file="+setu_url+"]"+"pid:"+str(setu_pid)+" 画师:"+setu_author
            return [True, local_img_url]
        except Exception as e:
            print(e)
            return [True, "阿这，出了一点问题"]
    return [False]

def mao_pic(msg):
    if msg in ["来张猫猫图", "来张猫图", "猫图", "喵图", "maomao","猫猫图","猫"]:
        setu_list = os.listdir(path)
        local_img_url = "[CQ:image,file=file://"+path+choice(setu_list)+"]"
        return [True, local_img_url]
    return [False]

def detect_ban(msg,user_id,group_id):
	if group_id not in group:
		return [False]
	if msg in ban_words:
		data = {
			'user_id':user_id,
			'group_id':group_id,
			'duration':60
		}
		cq_url = "http://127.0.0.1:5700/set_group_ban"
		requests.post(cq_url,data=data)
		return [True,"不要说不该说的话啦~"]
	return [False]
