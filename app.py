from flask import Flask, render_template, request, send_from_directory
from gtts import gTTS
from googletrans import Translator
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    audio_file = None
    if request.method == 'POST':
        text = request.form['text']
        lang = request.form['lang']

        # Translate text if needed
        translator = Translator()
        if lang != 'en':  # Only translate if the target language is not English
            translated_text = translator.translate(text, dest=lang).text
        else:
            translated_text = text

        # Convert text to speech
        tts = gTTS(translated_text, lang=lang)
        audio_file = "speech.mp3"
        tts.save(os.path.join('static', audio_file))

    return render_template('index.html', audio=audio_file)


if __name__ == '__main__':
    app.run(debug=True)
