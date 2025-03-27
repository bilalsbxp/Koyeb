from flask import Flask, render_template_string
import subprocess

app = Flask(__name__)

def get_version(command):
    try:
        result = subprocess.check_output(
            command.split(),
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        return result.strip()
    except Exception as e:
        return f"Gagal: {str(e)}"

@app.route('/')
def home():
    ffmpeg_version = get_version("ffmpeg -version")
    ytdlp_version = get_version("yt-dlp --version")
    
    return render_template_string('''
        <h1>Status Instalasi</h1>
        <p>FFmpeg: {{ ffmpeg }}</p>
        <p>yt-dlp: {{ ytdlp }}</p>
    ''', ffmpeg=ffmpeg_version, ytdlp=ytdlp_version)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
