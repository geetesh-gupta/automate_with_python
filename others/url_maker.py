import re
import requests
from bs4 import BeautifulSoup
from sys import argv
    
def url_maker(url_given, search_number):
    url_given = url_given
    
    url_to_form = 'https://r'+search_number+'---sn-cnoa-w5pe.googlevideo.com/videoplayback?sparams=aitags%2Cclen%2Cdur%2Cei%2Cgir%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Ckeepalive%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Crequiressl%2Csource%2Cexpire&c=WEB&itag=243&key=yt6&gir=yes&mime=video%2Fwebm&source=youtube&initcwndbps=246250&requiressl=yes&fvip=1&keepalive=yes&lmt=1518668918455272&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&dur=258.480&clen=13028317&expire=1531051052&mt=1531029346&mn=sn-cnoa-w5pe%2Csn-qxa7sn7r&mm=31%2C29&id=o-AMyYrQ5sgg_QPMiBQeXeQlncZB7SbLfuYg-OwX-9DiUT&fexp=23709359&ip=117.199.157.224&mv=m&pl=20&ipbits=0&ms=au%2Crdu&ei=zKdBW-nVFtO4ogO5ijQ&alr=yes&signature=C1D69F18C224BC4295BBF958A550677062D52BD1.CE5F8760A237C86790A90868E650B5641DA987B0&cpn=k-0LlFnlBuLs96Lr'


    indexlist_of_url_given = [m.start() for m in re.finditer('&', url_given)]
    indexlist_of_url_to_form = [m.start() for m in re.finditer('&', url_to_form)]

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

    url = 'https://r'+search_number+'---sn-cnoa-w5pe.googlevideo.com/videoplayback?keepalive=yes'
    for i in list_final:
        url +=  i[0] + '=' + i[1]
    return url


if __name__ == "__main__":
    if len(argv) == 2:
        url = argv[1]
    else:
        print("Usage: python3 filename url search_number")
    url_maker(url, search_number)