from send_message.word_detect import *
from random import choice
from data.talk_data.base_talk import others_answer

def match(msg,talk_data):
	for row in talk_data:
		if row[0] in msg:
			return [True,row[1][0]]
	return [False,choice(others_answer["no_answer"])]

def talk_to_user(rev,talk_data):#这里可以DIY对私聊和群聊中@yes酱的操作
	msg=rev["raw_message"]
	#--------------------------------------------------------------------------------------帮助页面
	if_help = help_menu(msg)
	if if_help[0] == True:
		return if_help[1]
	#--------------------------------------------------------------------------------------删除数据
	if_del = del_data(msg,talk_data)
	if if_del[0] == True:
		return if_del[1]
	#--------------------------------------------------------------------------------------添加数据
	if_add = add_data(msg,talk_data)
	if if_add[0] == True:
		return if_add[1]
	#--------------------------------------------------------------------------------------发送涩图
	if_setu = ghs_pic(msg)
	if if_setu[0] == True:
		return if_setu[1]
	#--------------------------------------------------------------------------------------发送R18
	if_setu = hs_pic(msg)
	if if_setu[0] == True:
		return if_setu[1]
    #--------------------------------------------------------------------------------------发送猫猫图
	if_setu = mao_pic(msg)
	if if_setu[0] == True:
		return if_setu[1]
	return match(msg,talk_data)[1]

def talk_to_gourp(rev,talk_data):#这里可以DIY对群聊的操作
	msg=rev["raw_message"]
	user_id=rev["user_id"]
	group_id=rev["group_id"]
	#--------------------------------------------------------------------------------------检测关键字禁言
	if_ban = detect_ban(msg,user_id,group_id)
	if if_ban[0] == True:
		return if_ban[1]

	if match(msg,talk_data)[0]==True:
		return match(msg,talk_data)[1]
	return ""

