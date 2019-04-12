import youtube_dl, os

def download_video(url, ops):
    with youtube_dl.YoutubeDL(ops) as ytdl:
        try:
            if 'list=' in url:
                url = delist(url)
                print('Now downloading: ' + url.strip() + '\n--------------------')
                ytdl.download([url])
            else:
                print('Now downloading: ' + url.strip() + '\n--------------------') 
                ytdl.download([url])
        except:
            print('An Error has occured.')
            return 1
    return 0


def delist(url):
    return url.split('list=')[0]


def driver():
    file_name = input("Enter your file name > ")
    with open(file_name, 'r') as f:
        lines = f.readlines()

    file_prefix = file_name.split('.')[0]
    folder_name = file_prefix + '-downloads'

    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

    ytdl_ops = {
        'format': 'bestaudio/best',
        'outtmpl': folder_name + '/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    videos_failed = 0
    for counter, line in enumerate(lines, start=1):
        print('\n\n' + str(counter) + ') ', end="")
        videos_failed += download_video(line, ytdl_ops)

    print(str(counter - videos_failed) + ' videos downloaded.')
    print(str(videos_failed) + ' videos failed to download.')

driver()