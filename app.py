from flask import Flask, request, send_file
from pytube import YouTube
import os


app = Flask(__name__)

@app.route('/api', methods=['GET'])
def Download():
    try:
        url = request.args.get('url')
        path = request.args.get('path')
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        output = video.download(output_path=path)
        
        base, ext = os.path.splitext(output)
        new = base + '.mp3'
        os.rename(output,new)

        return send_file(output_path, as_attachment=True)

    except Exception as e:
        return False
    

if __name__ == '__main__':
    app.run(debug=True)