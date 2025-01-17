from sys import argv

def utf_decoder(url):
    codes = {'%20': 'space', '%21': '!', '%22': '"', '%23': '#', '%24': '$', '%25': '%', '%26': '&', '%27': "'", '%28': '(', '%29': ')', '%2A': '*', '%2B': '+', '%2C': ',', '%2D': '-', '%2E': '.', '%2F': '/', '%30': '0', '%31': '1', '%32': '2', '%33': '3', '%34': '4', '%35': '5', '%36': '6', '%37': '7', '%38':'8', '%39': '9', '%3A': ':', '%3B': ';', '%3C': '<', '%3D': '=', '%3E': '>', '%3F': '?', '%40': '@', '%41': 'A', '%42': 'B', '%43': 'C', '%44': 'D', '%45': 'E', '%46': 'F', '%47': 'G', '%48': 'H', '%49': 'I', '%4A': 'J', '%4B': 'K', '%4C': 'L', '%4D': 'M', '%4E': 'N', '%4F': 'O', '%50': 'P', '%51':'Q', '%52': 'R', '%53': 'S', '%54': 'T', '%55': 'U', '%56': 'V', '%57': 'W', '%58': 'X', '%59': 'Y', '%5A': 'Z', '%5B': '[', '%5C': '\\', '%5D': ']','%5E': '^', '%5F': '_', '%60': '`', '%61': 'a', '%62': 'b', '%63': 'c', '%64': 'd', '%65': 'e', '%66': 'f', '%67': 'g', '%68': 'h', '%69': 'i', '%6A': 'j', '%6B': 'k', '%6C': 'l', '%6D': 'm', '%6E': 'n', '%6F': 'o', '%70': 'p', '%71': 'q', '%72': 'r', '%73': 's', '%74': 't', '%75': 'u', '%76': 'v','%77': 'w', '%78': 'x', '%79': 'y', '%7A': 'z', '%7B': '{', '%7C': '|', '%7D': '}', '%7E': '~'}
    # url = 'https%3A%2F%2Fr1---sn-cnoa-w5pe.googlevideo.com%2Fvideoplayback%3Ffvip%3D2%26pl%3D20%26ei%3DvpYjW9XwE8KNoQPIgYfoBA%26itag%3D137%26source%3Dyoutube%26ipbits%3D0%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%26dur%3D304.520%26expire%3D1529080606%26lmt%3D1518102746565070%26key%3Dyt6%26requiressl%3Dyes%26initcwndbps%3D212500%26gir%3Dyes%26mime%3Dvideo%252Fmp4%26pcm2cms%3Dyes%26mm%3D31%252C29%26mn%3Dsn-cnoa-w5pe%252Csn-qxa7sn7z%26id%3Do-AO3QlfPRZGlmH9IVRjqahs4FxC_4Tw8aCr9sNzIil9nS%26keepalive%3Dyes%26c%3DWEB%26clen%3D107607071%26ip%3D117.199.177.187%26gcr%3Din%26mt%3D1529058916%26mv%3Dm%26sparams%3Daitags%252Cclen%252Cdur%252Cei%252Cgcr%252Cgir%252Cid%252Cinitcwndbps%252Cip%252Cipbits%252Citag%252Ckeepalive%252Clmt%252Cmime%252Cmm%252Cmn%252Cms%252Cmv%252Cpcm2cms%252Cpl%252Crequiressl%252Csource%252Cexpire%26ms%3Dau%252Crdu\u0026itag=137\u0026projection_type=1\u0026init=0-715\u0026clen=107607071\u0026xtags=\u0026size=1920x1080\u0026s=6FB6FBF12302101EE37448402435D0C318037EE20A748.9B400D3BF3A15C95F2ABC81FC97B6DC4BB58B557\u0026type=video%2Fmp4%3B+codecs%3D%22avc1.640028%22\u0026lmt=1518102746565070\u0026quality_label=1080p,sp=signature\u0026bitrate=2733084\u0026index=201-1259\u0026fps=25\u0026url='
    
    for i, j in codes.items():
        if not (i == "%2C"):
            if i in url:
                url = url.replace(i,j)
    if "mime=video" in url:
        url = url.replace("mime=video/", "mime=video%2F")
    if "mime=audio" in url:
        url = url.replace("mime=audio/", "mime=audio%2F")
    return(url)

if __name__ == "__main__":
    if len(argv) == 2:
        url = argv[1]
    else:
        print("Usage: python3 utf_decoder.py url")