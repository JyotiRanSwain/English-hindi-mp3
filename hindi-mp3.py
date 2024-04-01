from googletrans import Translator
from gtts import gTTS

def translate_to_hindi(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='hi')
    return translation.text

def save_to_mp3(text, output_file):
    tts = gTTS(text=text, lang='hi')
    tts.save(output_file)
    print(f"Translation saved as {output_file}")

if __name__ == "__main__":
    # Input text in English
    english_text = input("Enter the English text you want to translate to Hindi and save as MP3: ")
    
    # Translate to Hindi
    hindi_translation = translate_to_hindi(english_text)
    
    # Output file name for the MP3 file
    output_file_name = input("Enter the output file name (without extension): ")
    output_file = f"{output_file_name}.mp3"
    
    # Convert to speech and save as MP3
    save_to_mp3(hindi_translation, output_file)
