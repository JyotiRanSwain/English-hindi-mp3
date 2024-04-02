import tkinter as tk
from tkinter import messagebox
from googletrans import Translator
from gtts import gTTS

def translate_to_hindi():
    english_text = english_entry.get()
    translator = Translator()
    translation = translator.translate(english_text, src='en', dest='hi')
    hindi_translation = translation.text
    hindi_text.insert("1.0", hindi_translation)

def save_to_mp3():
    hindi_text_value = hindi_text.get("1.0", "end-1c")
    if not hindi_text_value:
        messagebox.showerror("Error", "Hindi translation is empty")
        return
    tts = gTTS(text=hindi_text_value, lang='hi')
    output_file = output_entry.get()
    if not output_file:
        messagebox.showerror("Error", "Please enter output file name")
        return
    tts.save(f"{output_file}.mp3")
    messagebox.showinfo("Success", "Translation saved successfully")

# Create main window
root = tk.Tk()
root.title("Power Cloud ---------------English to Hindi Translator---------------")

# Load logo image
logo_image = tk.PhotoImage(file="logo.png")  # Replace "logo.png" with your actual logo file name

# Create and place logo label
logo_label = tk.Label(root, image=logo_image)
logo_label.grid(row=0, column=0, padx=5, pady=5, rowspan=4)

# Add a message alongside the logo
message_label = tk.Label(root, text="Welcome to English to Hindi Translator", font=("Helvetica", 16))
message_label.grid(row=0, column=1, columnspan=3, padx=5, pady=5)

# Create and place widgets
english_label = tk.Label(root, text="English Text:")
english_label.grid(row=1, column=1, padx=5, pady=5)

english_entry = tk.Entry(root, width=50)
english_entry.grid(row=1, column=2, padx=5, pady=5, columnspan=2)

translate_button = tk.Button(root, text="Translate", command=translate_to_hindi)
translate_button.grid(row=1, column=4, padx=5, pady=5)

hindi_label = tk.Label(root, text="Hindi Translation:")
hindi_label.grid(row=2, column=1, padx=5, pady=5)

hindi_text = tk.Text(root, height=5, width=50)
hindi_text.grid(row=2, column=2, padx=5, pady=5, columnspan=2)

output_label = tk.Label(root, text="Output File Name:")
output_label.grid(row=3, column=1, padx=5, pady=5)

output_entry = tk.Entry(root, width=50)
output_entry.grid(row=3, column=2, padx=5, pady=5, columnspan=2)

save_button = tk.Button(root, text="Save MP3", command=save_to_mp3)
save_button.grid(row=3, column=4, padx=5, pady=5)

# Run the main event loop
root.mainloop()
