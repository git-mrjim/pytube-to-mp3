from flask import Flask, request
from pytube import YouTube
import os


app = Flask(__name__)

@app.route('/api', methods=['GET'])
def Download():
    url = request.args.get('url')
    path = request.args.get('path')
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    output = video.download(output_path=path)
    
    base, ext = os.path.splitext(output)
    new = base + '.mp3'
    os.rename(output,new)
    
    if output:
        return {
            'title': yt.title,
            'thumbnailUrl': yt.thumbnail_url,
            'videoUrl': url,
            'failed': False
        }
    else:
        return {
            'failed': True
        }

if __name__ == '__main__':
    app.run(debug=True)