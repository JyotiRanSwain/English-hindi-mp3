# convert the English text into Hindi, and then use a Text-to-Speech (TTS) engine to convert the translated text into speech and save it as an MP3 file. 

First, you'll need to install the required libraries: 
```
pip install googletrans==4.0.0-rc1 gtts
```

Install pyinstaller libraries: 
```
pip install pyinstaller
```

Extract exe file: 
```
python -m PyInstaller --onefile mpui.py
```
