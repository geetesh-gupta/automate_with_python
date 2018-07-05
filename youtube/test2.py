import re

url_given = 'https://r1---sn-cnoa-w5pe.googlevideo.com/videoplayback?fvip=2&pl=20&ei=vpYjW9XwE8KNoQPIgYfoBA&itag=137&source=youtube&ipbits=0&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&dur=304.520&expire=1529080606&lmt=1518102746565070&key=yt6&requiressl=yes&initcwndbps=212500&gir=yes&mime=video%2Fmp4&pcm2cms=yes&mm=31%2C29&mn=sn-cnoa-w5pe%2Csn-qxa7sn7z&id=o-AO3QlfPRZGlmH9IVRjqahs4FxC_4Tw8aCr9sNzIil9nS&keepalive=yes&c=WEB&clen=107607071&ip=117.199.177.187&gcr=in&mt=1529058916&mv=m&sparams=aitags%2Cclen%2Cdur%2Cei%2Cgcr%2Cgir%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Ckeepalive%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpcm2cms%2Cpl%2Crequiressl%2Csource%2Cexpire&ms=au%2Crdu&itag=137&projection_type=1&init=0-715&clen=107607071&xtags=&size=192ႀ&s=6FB6FBF12302101EE37448402435D0C318037EE20A748.9B400D3BF3A15C95F2ABC81FC97B6DC4BB58B557&type=video/mp4;+codecs="avc1.640028"&lmt=1518102746565070&quality_label=1080p,sp=signature&bitrate=2733084&index=201-1259&fps=25&url='

url_to_form = 'https://r1---sn-cnoa-w5pe.googlevideo.com/videoplayback?mime=video%2Fwebm&requiressl=yes&clen=8028108&mn=sn-cnoa-w5pe%2Csn-qxa7sn7z&mm=31%2C29&mv=m&mt=1529051300&key=yt6&ms=au%2Crdu&source=youtube&keepalive=yes&ip=117.199.177.187&sparams=aitags%2Cclen%2Cdur%2Cei%2Cgcr%2Cgir%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Ckeepalive%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpcm2cms%2Cpl%2Crequiressl%2Csource%2Cexpire&initcwndbps=240000&gcr=in&id=o-ANcYNsClSqXOORLRqWEDD3BYzfOP7IyHbnF-ewLp5yRE&ei=9ngjW9mmPJbJogPZtqfgDQ&lmt=1518106613550617&fvip=2&pcm2cms=yes&c=WEB&gir=yes&pl=20&expire=1529072983&dur=304.520&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&ipbits=0&itag=242&alr=yes&signature=E21121E766B1FC4C11D344CDB5A82B640627FA33.1A37319DC57B46FA91A596D915BC7EC876FB207C&cpn=qMi7LamZ1vWLd_Pb&cver=2.20180612&rn=27&rbuf=0'

indexlist_of_url_given = [m.start() for m in re.finditer('&', url_given)]
indexlist_of_url_to_form = [m.start() for m in re.finditer('&', url_to_form)]

print(indexlist_of_url_given)
print(indexlist_of_url_to_form)

list_of_url_given = []
list_of_url_to_form = []

for i in range(len(indexlist_of_url_given)):
	if i == len(indexlist_of_url_given)-1:
		break
	list_of_url_given.append(url_given[int(indexlist_of_url_given[i]):int(indexlist_of_url_given[i+1])])

for i in range(len(indexlist_of_url_to_form)):
	if i == len(indexlist_of_url_to_form)-1:
		break
	list_of_url_to_form.append(url_to_form[int(indexlist_of_url_to_form[i]):int(indexlist_of_url_to_form[i+1])])

indexlist_of_dict_url_given = []
indexlist_of_dict_url_to_form = []
for i in list_of_url_given:
	indexlist_of_dict_url_given.append(i.find('='))
for i in list_of_url_to_form:
	indexlist_of_dict_url_to_form.append(i.find('='))

list_of_dict_url_given = []
list_of_dict_url_to_form = []

for i in range(len(list_of_url_given)):
	j = indexlist_of_dict_url_given[i]
	tup = (list_of_url_given[i][:j], list_of_url_given[i][j+1:])
	list_of_dict_url_given.append(tup)

for i in range(len(list_of_url_to_form)):
	j = indexlist_of_dict_url_to_form[i]
	tup = (list_of_url_to_form[i][:j], list_of_url_to_form[i][j+1:])
	list_of_dict_url_to_form.append(tup)

print(list_of_dict_url_given)
print()
print(list_of_dict_url_to_form)
print()
list_final = []

flag = 0
for x, y in list_of_dict_url_to_form:
	for z, w in list_of_dict_url_given:
		if x == z:
			tup = (x, w)
			list_final.append(tup)
			flag = 1
			break
	if flag != 1:		
		tup = (x, y)
		list_final.append(tup)	
		flag = 0
	flag = 0
print(list_final)

url = 'https://r1---sn-cnoa-w5pe.googlevideo.com/videoplayback?mime=video%2Fwebm'
for i in list_final:
	url +=  i[0] + '=' + i[1]
print(url)