import tkinter as tk
from tkinter import messagebox
import yt_dlp
import webbrowser

def play_video(url, quality):
    if not url:
        messagebox.showerror('Error', 'Please enter a valid URL')
        return
    
    ydl_opts = {}
    if quality == 'high':
        ydl_opts = {'format': 'best'}
    elif quality == 'low':
        ydl_opts = {'format': 'worst'}
    elif quality == 'audio':
        ydl_opts = {'format': 'bestaudio'}

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_url = info_dict['url']
            webbrowser.open(video_url)
            messagebox.showinfo('Playing', f'Opening video in {quality} quality')
    except Exception as e:
        messagebox.showerror('Error', f'Failed to open video: {e}')

def play_high_quality():
    url = entry.get()
    play_video(url, 'high')

def play_low_quality():
    url = entry.get()
    play_video(url, 'low')

def play_audio_only():
    url = entry.get()
    play_video(url, 'audio')

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title('Video Player')

# إنشاء حقل إدخال
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# إنشاء الأزرار
button_high = tk.Button(root, text='Play High Quality', command=play_high_quality)
button_high.pack(pady=5)

button_low = tk.Button(root, text='Play Low Quality', command=play_low_quality)
button_low.pack(pady=5)

button_audio = tk.Button(root, text='Play Audio Only', command=play_audio_only)
button_audio.pack(pady=5)

# تشغيل النافذة
root.mainloop()