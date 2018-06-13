
url = "https://hsprepack.akamaized.net/videos/bharat/khamp/235/master_Layer9_00" 
episode = url[46:51]
episode_code = url[52:55]
path = "/Users/gg/Movies/hotstar/" + episode+ episode_code +".ts"
with open (path, "wb") as outputf:
    for i in range(248,302,1):
        path = '/Users/gg/Movies/hotstar/master_Layer9_00' + str(i).rjust(3, '0') + ".ts"
        with open(path, "rb") as inputf:
            outputf.write(inputf.read())

