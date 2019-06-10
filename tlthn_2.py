from telethon import TelegramClient, sync
from telethon import functions, types
from telethon.errors.rpcerrorlist import PeerFloodError
import time
import tlt_conf # all settings are here
import datetime

def routine_txt(id_to_send,msg_to_send,Gr):
	"""does all the routine job with txt file"""
	filee=days_file = open('examp.txt','r')
	lines=filee.readlines()
	i=1 # начинаем с 1, так как на 0 строке ссылка на группу

	prom=lines[0]
	Gr.append(prom[13:-1]) # имя группы, взятое из ссылки

	while i<len(lines):
		i+=1
		if lines[i]=='\n': # если в конце файла пустые строки - брэйк
			break
		id_to_send.append(lines[i])
		i+=1
		tmp=''
		while i!=len(lines) and lines[i]!='_\n': # сообщение не прекратит записываться, пока не произойдет перехода на след строку
			tmp+=lines[i]
			i+=1
		msg_to_send.append(tmp)

	for i in range(0,len(id_to_send)):
		promej=id_to_send[i]
		id_to_send[i]=promej[:-1]

	for i in range(0,len(msg_to_send)):
		promej=msg_to_send[i]
		msg_to_send[i]=promej[:-1]

def client_job(id_to_send,msg_to_send,gr):
	"""does a client.start and send the messages to the needed ppl"""
	client = TelegramClient(tlt_conf.sess, tlt_conf.api_id, tlt_conf.api_hash)
	client.start()
	deelay=0
	with client:
		client.get_participants(gr[0])
		for i in range(0,len(iD_to_send)):
			try:
				client.send_message(int(id_to_send[i]), str(msg_to_send[i].encode('cp1251')))
				time.sleep(deelay)
			except ValueError:
				file=open('log.txt','a') # a = append
				file.write("User"+" "+str(id_to_send[i])+" "+"is deleted"+" "+str(datetime.datetime.now())+"\n")
				file.close()
				pass
			except PeerFloodError:
				file=open('log.txt','a') # a = append
				file.write("U r having some sending problems (maybe u r currently banned for spam)"+" "+str(datetime.datetime.now())+"\n")
				file.close()
				pass

GR=[]
iD_to_send=[] # a list for ID's
msG_to_send=[] # a list for msg's
routine_txt(iD_to_send,msG_to_send,GR)
client_job(iD_to_send,msG_to_send,GR)
