import requests
import sys
def download():

    for i in range(12):
        
        url = "http://cdn.cs50.net/web/2018/spring/lectures/" + str(i) + "/lecture" + str(i) + ".pdf"
        print(url)
        file_name = "lecture" + str(i) + ".pdf"
        with open(file_name, "wb") as f:
            print ("Downloading %s" % file_name)
            response = requests.get(url, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None: # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                    sys.stdout.flush()


download()