import json
from data.load_data import read_file
from send_message.send_message import send_message
from send_message.talk_to_user import *
from random import randint
self_qq = json.load(open("./config.json", encoding='utf-8'))["self_qq"]
ban_words = json.load(open("./config.json", encoding='utf-8'))["ban_words"]
class msg_talker():
	def __init__(self):
		self.talk_data = read_file()

	def private_msg(self,rev):
		if rev["sub_type"] != "friend":
			return send_message('你还不是我的好友呀',rev['user_id'],"private")
		return send_message(talk_to_user(rev, self.talk_data), rev["user_id"], "private")

	def group_msg(self,rev):
		if "[CQ:at,qq={}]".format(self_qq) in rev["raw_message"]:
			try:
				rev['raw_message']=rev['raw_message'].split(" ")[1]
			except:
				pass
			return send_message(talk_to_user(rev, self.talk_data), rev["group_id"], "group")

		if randint(1,10)<4 or rev['raw_message'] in ban_words:	
			return send_message(talk_to_gourp(rev, self.talk_data), rev["group_id"], "group")
		return True


		