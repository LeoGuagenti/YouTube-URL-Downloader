import youtube_dl, os

def download_video(url, ops):
    with youtube_dl.YoutubeDL(ops) as ytdl:
        try:
            #if url is a playlist member, trim the playlist off
            if 'list=' in url:
                url = delist(url)
                print('Now downloading: ' + url.strip() + '\n--------------------')
                ytdl.download([url])
            else:
                print('Now downloading: ' + url.strip() + '\n--------------------') 
                ytdl.download([url])
        except:
            #if an exception is thrown catch and move to next video
            print('An Error has occured.')
            return 1
    return 0


#removes any playlist extension from the url
#otherwise youtube_dl will download every video in the playlist
def delist(url):
    return url.split('list=')[0]


def driver():
    file_name = input("Enter your file name > ")
    with open(file_name, 'r') as f:
        lines = f.readlines()

    #getting output folder name based on input file name
    file_prefix = file_name.split('.')[0]
    folder_name = file_prefix + '-downloads'

    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

    #youtube_dl options
    ytdl_ops = {
        'format': 'bestaudio/best',
        'outtmpl': folder_name + '/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    #attempts to download all videos in list
    videos_failed = 0
    for counter, line in enumerate(lines, start=1):
        print('\n\n' + str(counter) + ') ', end="")
        videos_failed += download_video(line, ytdl_ops)

    #final results
    print(str(counter - videos_failed) + ' videos downloaded.')
    print(str(videos_failed) + ' videos failed to download.')

driver()