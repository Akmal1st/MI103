from telethon.sync import TelegramClient, events
from random import randrange as rr
import re
from time import sleep
import asyncio

def check(a):
	if a is not None:
		return a
	else:
		return '  '

api_id = 2688818
api_hash = 'c94b3f8c66f2584b3cafc55d6556bae8'
s=''
client = TelegramClient('name', api_id, api_hash)
client.start()   

@client.on(events.NewMessage(pattern="/start"))
async def start(event):
	pass	

@client.on(events.NewMessage(pattern='^[Mm]ode.$'))
async def emojies(event):
	chat = await event.get_chat()
	mid = event.id
	text = event.message.text
	mode = re.match('^[mM]ode.$',text).group()
	e = [
			['1f641','1f615','1f610','1f611','1f610','1f642','1f600','1f604','1f603','1f601','1f606','1f602','1f923'],
			['2601','1f329','2601','26c8','1f327','2601','1f327','1f326','1f325','26c5','1f324','2600'],
			['2600','1f324','26c5','1f325','2601','1f329','26c8','1f329','26c8','1f327'],
			['1f615','1f641','2639','1f61f','1f614','1f61e','1f614','1f623','1f616','1f62b','1f629','1f97a','1f622','1f62d'],
			['1f625','1f630','1f628','1f631','1f480','2620'],
			['1f567','1f550','1f55c','1f551','1f55d','1f552','1f55e','1f553','1f55f','1f554','1f560','1f555','1f561','1f556','1f562','1f557','1f563','1f558','1f564','1f559','1f565','1f55a','1f566','1f55b','1f973']
		]

	k = int(mode[4])
	l=len(e)
	if k<l:
		for x in e[k]:
			a = '\\U{:0>8}'.format(x)
			xx = a.encode()
			await client.edit_message(chat,mid,"."+xx.decode("unicode_escape")+".")
			sleep(0.19)
@client.on(events.NewMessage(pattern="^([Aa]ss|[Ss])alom"))
async def salom(event):
	chat = await event.get_chat()
	me = await client.get_me()
	kirish = ['Assalom','Salom',]
	chiqish = ['Va alaykum assalom','Salom']
	text = event.message.text.split(' ')
	text = text[0].capitalize()
	b = re.match('^([Aa]ss|[Ss])alom',text)
	if b!=None and me.id!=event.from_id.user_id and event.fwd_from==None:
		if event.is_reply==False:
			b=b.group()
			if b in kirish:
				async with client.action(chat, 'typing'):
					await asyncio.sleep(2)
					await event.reply(chiqish[kirish.index(b)])
				await client.action(chat, 'cancel')

@client.on(events.NewMessage(pattern='^[Aa]l*o*$'))
async def alo(event):
	chat = await event.get_chat()
	async with client.action(chat, 'typing'):
		await asyncio.sleep(2)
		await event.reply("Eshitaman")
	await client.action(chat, 'cancel')
@client.on(events.NewMessage(pattern='^/[Gg]et$'))
async def users(event):
	chat = await event.get_chat()
	k = await client.get_participants(chat.title)
	count = 0
	for x in range(len(k)):
		if k[x].deleted:	
			count+=1
			#await client.kick_participant(chat, k[x].id)
	print(chat.title,"|=| deleted accounts {}".format(count))
	info = f"Guruhda o\'chirilgan profillar soni {count} ta" 
	#await client.edit_message(chat,event.id,info)
	await event.reply(info)

@client.on(events.NewMessage(pattern="^[Jj]adval..$"))
async def scheduled(event):
	txt = event.message
	text = txt.text.split(' ')
	text2 = ""
	import urllib.request as ul
	import urllib.parse as up
	from bs4 import BeautifulSoup
	chat = await event.get_chat()
	my_data = {"request":"true","auth_stud_id":"300034845","password":"O9IM-D21-62RE"}
	site = "http://talaba.tdpu.uz/student/jadval"
	data = up.urlencode(my_data)
	data = data.encode('cp1251')
	try:
		page = ul.urlopen(site,data)
		
		soup = BeautifulSoup(page, features='lxml')
		jadval = []
		for x in soup.find_all('div'):
			clas = " ".join(x.get('class')) if x.get('class')!=None else ""
			if clas=="panel panel-default col-md-3":
				h4 = x.find('h4').get_text().split()[0]
				a = [n.get('href') for n in x.find_all('a')]
				a_text = [n.get_text() for n in x.find_all('a')]
				b = [n.get_text() for n in x.find_all('b')]
				div = [n.get_text() for n in x.find_all('div') if n.get('align')=='right']
				s = ''
				s+=h4+"\n\n"
				for k in range(len(b)//4):
					s+="%s\n" % (" ".join(div[k].split()))
					s+="%s \n%s \n" % (b[4*k+2], " ".join(b[4*k+3].split()))
					try:
						s+="[%s](%s) \n\n" % (" ".join(a_text[k].split()), a[k])
					except:
						pass
				jadval.append(s)
		
		if text[1].isdigit():
			k=int(text[1])
			if k>0 and k<7:
				text2 = jadval[k-1]
			elif k==7:
				text2 = "Dam olsangizchi"
			else:
				text2 = "Dars o'tiladigan hafta kuni raqamini kiriting"
		else:
			text2 = "Xato"
		#await client.delete_messages(chat, message_ids=txt.id)
		#await client.send_message(chat, text2)
		await event.reply(text2, parse_mode='md')
	except:
		await client.send_message(chat, 'Jadvalni olishda xatolik\nKeyinroq urinib ko\'ring')
	
	


@client.on(events.NewMessage(chats=1472844170, pattern="/[Dd]ars"))
async def dars(event):
	from time import strftime
	chat = await event.get_chat()
	mid = event.id
	w = int(strftime("%w"))
	d = strftime("%d")
	m = strftime("%m")
	y = strftime("%y")
	A = ["Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba"]
	await client.delete_messages(chat, message_ids=mid)
	if w!=0:
		for x in range(1,4):
			a = f"-----\n{d}.{m}.{y}\n#{A[w-1]}\n-----\n{x}P:\nMavzu:\nUy ishi:\n\nP.S. Adminlar to\'ldirsin!!!"
			await client.send_message(chat, a)


@client.on(events.NewMessage(pattern="^/getme"))
async def changes(event):
	from telethon.tl.functions.users import GetFullUserRequest as GFUR
	chat = await event.get_chat()
	user_id = event.message.sender_id
	full = await client(GFUR(user_id))
	text = f"ID = {full.user.id}\nfirst_name = {full.user.first_name}\nlast_name = {check(full.user.last_name)}\nusername = {check(full.user.username)}\nbio = {check(full.about)}"
	await client.send_message(chat, text)


@client.on(events.NewMessage(pattern="/aboutme"))
async def abouts(event):
	chat = await event.get_chat()
	user = await event.get_sender()
	p = await client.get_permissions(chat,user)
	a = f"add_admins = {p.add_admins} \nanonymous = {p.anonymous} \nban_users = {p.ban_users} \nchange_info = {p.change_info} \ndelete_messages = {p.delete_messages} \nhas_default_permissions = {p.has_default_permissions} \ninvite_users = {p.invite_users} \nis_admin = {p.is_admin} \nis_banned = {p.is_banned} \nis_chat = {p.is_chat} \nis_creator = {p.is_creator} \npin_messages = {p.pin_messages} \npost_messages = {p.post_messages} "
	#print(a)
	#await client.delete_messages(chat, message_ids=event.id)
	#await client.send_message(chat,a)
	await event.reply(a)

@client.on(events.NewMessage(pattern='/think'))
async def thinking(event):
	chat_id = event.chat_id
	mid = event.id
	text = "O\'ylayapman..."
	await client.edit_message(chat_id,mid, text)
	for x in range(0,101,5):
		await client.edit_message(chat_id,mid, f"{text}{x}%")
	await client.edit_message(chat_id, mid, "Bilmadim")
client.run_until_disconnected()
