import os
import re

def html_extract(text):
    
    url_index = [m.start() for m in re.finditer('---sn-cnoa-w5pe', text)]
    url_index = int(url_index[0]) - 1
    search_term = 'https://r' + text[url_index] + '---sn-cnoa-w5pe.googlevideo.com/'        
    listt = [m.start() for m in re.finditer(search_term, text)]
    temp = []
    for i in range(len(listt)):
        if i == len(listt)-1:
            break
        temp.append(text[int(listt[i]):int(listt[i+1])])
    return (temp, text[url_index])

def urls_extract(list):
    video_urls = []
    audio_urls = []

    if open("files/video_urls.txt", 'w'):
        os.remove("files/video_urls.txt")
    if open("files/audio_urls.txt", 'w'):
        os.remove("files/audio_urls.txt")

    for i in list:
        if "mime=video" in i and "quality_label" in  i:
            with open("files/video_urls.txt", 'a') as file:
                file.write(i+"\n")
                video_urls.append(i)
        elif "mime=audio" in i:
            with open("files/audio_urls.txt", "a") as file:
                file.write(i+"\n")
                audio_urls.append(i)
    return (video_urls, audio_urls)

def video_urls_format_extract(video_urls, audio_urls):
    video_urls_webm = []
    video_urls_mp4 = []
    for i in video_urls:
        if "type=video/webm" in i:
            video_urls_webm.append(i)
        if "type=video/mp4" in i:
            video_urls_mp4.append(i)
    return (video_urls_mp4, video_urls_webm)

def main():
    print("hi")
if __name__ == "__main__":
    main()