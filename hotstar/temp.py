url = "https://hsprepack.akamaized.net/videos/bharat/khamp/234/master_Layer8_00" 
episode = url[46:51]
episode_code = url[52:55]
path = "/Users/gg/Movies/hotstar/" + episode+ episode_code +".ts"
infile = path
outfile = path[-len(path):-11] + infile[25:30] + "_" + infile[30:33]+ ".mkv"
print(infile,outfile)