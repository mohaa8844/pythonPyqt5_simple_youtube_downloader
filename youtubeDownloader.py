
from youtube_dl import YoutubeDL
class Downloader:
    def __init__(self,url):
        self.url=url

    def download(self):
        print('هلبيكسيد')
        ytdl=YoutubeDL()
        urlList=[]
        urlList.append(self.url)
        ytdl.download(urlList)
        print('بلخدمسيد')
