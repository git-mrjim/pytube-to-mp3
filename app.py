from flask import Flask, request, send_file, jsonify
from pytube import YouTube
import os
import shutil


app = Flask(__name__)

@app.route('/api', methods=['GET'])
def Download():
    try:
        url = request.args.get('url')

        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        output = video.download()
        
        base, ext = os.path.splitext(output)
        new = base + '.mp3'
        shutil.move(output, new)

        return send_file(new, as_attachment=True)

    except Exception as e:
        return jsonify(error=str(e)), 500

    

if __name__ == '__main__':
    app.run(debug=True)