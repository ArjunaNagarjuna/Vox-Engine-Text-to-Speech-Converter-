from gtts import gTTS
from tkinter import *
from tkinter import messagebox, filedialog, ttk
from playsound import playsound
import tempfile
import os
import PyPDF2

# --- Emoji Dictionary (Fun Mode) ---
emoji_dict = {
    "happy": "😊", "love": "❤️", "idea": "💡", "food": "🍕", "sad": "😢",
    "laugh": "😂", "hello": "👋", "bye": "👋", "fire": "🔥", "cool": "😎",
    "angry": "😡", "music": "🎵", "book": "📖", "computer": "💻", "phone": "📱",
    "dog": "🐶", "cat": "🐱", "star": "⭐", "money": "💰", "party": "🎉",
    "sun": "☀️", "moon": "🌙", "car": "🚗", "train": "🚆", "plane": "✈️",
    "rain": "🌧️", "coffee": "☕", "school": "🏫", "game": "🎮", "win": "🏆",
    "heart": "💖", "robot": "🤖"
}

# --- Functions ---
def add_emojis(text):
    words = text.split()
    new_words = []
    for w in words:
        lw = w.lower().strip(",.!?")
        if lw in emoji_dict and fun_mode_var.get():
            new_words.append(emoji_dict[lw])
        else:
            new_words.append(w)
    return " ".join(new_words)

def textTospeech():
    global last_text
    text = text_area.get("1.0", END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter or upload some text!")
        return

    # Apply emoji replacements if Fun Mode is on
    display_text = add_emojis(text)
    text_area.delete("1.0", END)
    text_area.insert("1.0", display_text)

    language = lang_var.get()
    slow = speed_var.get() == "Slow"
    last_text = text

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            temp_path = fp.name
        tts = gTTS(text=text, lang=language, slow=slow)
        tts.save(temp_path)
        playsound(temp_path)
        os.remove(temp_path)
        show_completion_popup()
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

def saveAudio():
    text = text_area.get("1.0", END).strip()
    if not text:
        messagebox.showwarning("No Audio", "Please enter or upload some text first!")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                             filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        try:
            tts = gTTS(text=text, lang=lang_var.get(), slow=(speed_var.get()=="Slow"))
            tts.save(file_path)
            messagebox.showinfo("Saved", f"Audio saved successfully:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")

def uploadFile():
    global last_text
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf")])
    if not file_path:
        return
    
    try:
        file_text = ""
        if file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                file_text = file.read()
        elif file_path.endswith(".pdf"):
            with open(file_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    if page.extract_text():
                        file_text += page.extract_text() + "\n"

        if not file_text.strip():
            messagebox.showwarning("Empty File", "The selected file has no readable text.")
            return

        text_area.delete("1.0", END)
        text_area.insert("1.0", file_text)
        last_text = file_text
        messagebox.showinfo("File Uploaded", "File loaded successfully!\nClick 'Convert & Play' or 'Save Audio'.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not read file:\n{e}")

def show_completion_popup():
    popup = Toplevel(root)
    popup.title("Reading Complete!")
    popup.geometry("400x300")
    popup.config(bg="#f5f5f5")

    Label(popup, text="🤖", font=("Arial", 120), bg="#f5f5f5").pack(pady=10)
    Label(popup, text="Reading Completed!", font=("Arial", 16, "bold"), bg="#f5f5f5").pack(pady=5)

    def read_again():
        popup.destroy()
        textTospeech()

    Button(popup, text="🔁 Read Again", command=read_again,
           font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=10)
    Button(popup, text="❌ Close", command=popup.destroy,
           font=("Arial", 12, "bold"), bg="#F44336", fg="white", padx=10, pady=5).pack()

# --- Main App UI ---
root = Tk()
root.title("🔊 VoxEngine – Engineered Speech")
root.geometry("700x500")
root.config(bg="#f5f5f5")

last_text = ""

# Title
Label(root, text="VoxEngine – Text to Speech Converter",
      font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#333").pack(pady=10)

# Language & Speed Frame
frame = Frame(root, bg="#f5f5f5")
frame.pack(pady=5)

Label(frame, text="Language:", font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=0, padx=5)
lang_var = StringVar(value="en")
lang_dropdown = ttk.Combobox(frame, textvariable=lang_var,
                             values=["en", "hi", "fr", "es", "ta", "te"],
                             width=7, state="readonly")
lang_dropdown.grid(row=0, column=1, padx=5)

Label(frame, text="Speed:", font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=2, padx=5)
speed_var = StringVar(value="Normal")
speed_dropdown = ttk.Combobox(frame, textvariable=speed_var,
                              values=["Normal", "Slow"],
                              width=8, state="readonly")
speed_dropdown.grid(row=0, column=3, padx=5)

# Fun Mode Checkbox
fun_mode_var = BooleanVar(value=True)
Checkbutton(frame, text="🎭 Fun Mode (Emojis)", variable=fun_mode_var,
            font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=4, padx=10)

# Text Area
text_area = Text(root, font=("Arial", 12), width=80, height=12, bd=2, relief="solid")
text_area.pack(pady=10)

# Buttons
btn_frame = Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=10)

Button(btn_frame, text="📂 Upload File", command=uploadFile,
       font=("Arial", 12, "bold"), bg="#FF9800", fg="white", activebackground="#F57C00",
       padx=12, pady=5).grid(row=0, column=0, padx=10)

Button(btn_frame, text="▶ Convert & Play", command=textTospeech,
       font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", activebackground="#45a049",
       padx=12, pady=5).grid(row=0, column=1, padx=10)

Button(btn_frame, text="💾 Save Audio", command=saveAudio,
       font=("Arial", 12, "bold"), bg="#2196F3", fg="white", activebackground="#1976D2",
       padx=12, pady=5).grid(row=0, column=2, padx=10)

root.mainloop()
