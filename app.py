import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os
import ffmpeg
import subprocess
import shlex
import time 
print("hi")

def download_video():
    url = entry_url.get()
    resolution = resolution_var.get()
    #file_type_checker = file_type_combobox.get() 
    file_type_checker= type_var.get()

    progress_label.pack(pady=("10p", "5p"))
    progress_bar.pack(pady=("10p", "5p"))
    status_label.pack(pady=("10p", "5p"))

    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(res=resolution).first()
        # stream.download()
        # download video into specific directory
        os.path.join("uploads", f"{yt.title}.mp4",)
        stream.download(output_path="downloads")
        #time.sleep(35)
        #file_type_checker =file_type.get()
        #path1 = "/Users/ethanwong/Desktop/YT-Downloader-v2/env/downloads/"
        path1="/../downloads/"
        #input_file = f"{path1}"+f"{yt.title}.mp4"
        #output_file = f"{path1}"+f"{yt.title}.mp3"
        input_file = f"{yt.title}.mp4"
        output_file = f"{yt.title}.mp3"
        input_file_escaped = shlex.quote(input_file)
        output_file_escaped = shlex.quote(output_file)
        command = ['ffmpeg', '-i', input_file_escaped,'-vn', '-c:a', 'libmp3lame', output_file_escaped]
        print(command)
        print("this is the path\n"+ input_file_escaped)
        # /Users/ethanwong/Desktop/YT-Downloader-v2/env/downloads/Curious George (2006-) Intro.mp4
        # ffmpeg -i "/Users/ethanwong/Desktop/YT-Downloader-v2/env/downloads/Curious George (2006-) Intro.mp4" -vn -c:a libmp3lame output.mp3
        # ffmpeg', '-i', /Users/ethanwong/Desktop/YT-Downloader-v2/env/downloads/Curious George (2006-) Intro.mp4,'-vn', '-c:a', 'libmp3lame', output_file_escaped

        subprocess.run(command)

    
        if file_type_checker == "mp3": # and os.isfile(input_file_escaped):
            print("true file exists")
            
            # https://www.youtube.com/watch?v=mOzZZf-lL3M
            # https://www.youtube.com/watch?v=bktcHsAvBI0

            #input_file = os.path.join("uploads", f"{yt.title}.mp4")
            #output_file = os.path.join("uploads", f"{yt.title}.mp3")
            #ffmpeg.input(input_file).output(output_file).run(overwrite_output=True, capture_stdout=True, capture_stderr=True)

            
            #output_file = os.path.join("downloads", f"{yt.title}.mp3")
            
            #ffmpeg.input(file_location).output(output_file).run(overwrite_output=True)
            #output_file = os.path.join("downloads", f"{yt.title}.mp3")
            ##input_file=f"{yt.title}.mp4"
            ##output_file=f"{yt.title}.mp3"
            #(
            #    ffmpeg
            #    .input(file_location)
            #    .output(output_file, format='mp3')
            #    .run(overwrite_output=True)
            #)
            #if os.path.isfile(output_file):
            #    print("MP3 file successfully created")
            ##command = ['ffmpeg', '-i', input_file,'-vn', '-c:a', 'libmp3lame', output_file]
            ##subprocess.run(command)
            


            #ffmpeg.input(f"{file_location}").output(f"downloads/{yt.title}.mp3").run()

            #stream_inp = ffmpeg.input(f"{file_location}")
            #stream_inp = ffmpeg.output(stream_inp, '{yt.title}.mp3')

        status_label.configure(text=f"Success", text_color="white", fg_color="green")

    except Exception as e:
        status_label.configure(text=f"Error{str(e)}", text_color="white", fg_color="red")
    


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = bytes_downloaded / total_size * 100

    progress_label.configure(text=str(int(percentage_completed))+"%")
    progress_label.update()
    progress_bar.set(float(percentage_completed/100))


# create root window

root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# title of window
root.title("Youtube Downloader")

# set min max
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

# create a frame to hold the content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

# create a label and the entry widget
url_label = ctk.CTkLabel(content_frame, text="Enter the youtube url here:")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=("10p", "5p"))
entry_url.pack(pady=("10p", "5p"))

# create a download button

download_button = ctk.CTkButton(content_frame, text="Download", command=download_video)

download_button.pack(pady=("10p", "5p"))

# create resolutions combo box
resolutions = ["720p", "360p", "240p"]
resolution_var = ctk.StringVar()
resolution_combobox = ctk.CTkComboBox(content_frame, values=resolutions)
resolution_combobox.pack(pady=("10p", "5p"))
resolution_combobox.set("720p")

#create mp4 or mp3 option combo box
file_type = ["mp4", "mp3"]
type_var= ctk.StringVar()
file_type_combobox = ctk.CTkComboBox(content_frame, values=file_type)
file_type_combobox.pack(pady=("10p", "5p"))
file_type_combobox.set("mp4")

# create a label and the progress bar ti display download progress
progress_label = ctk.CTkLabel(content_frame, text="0%")
progress_label.pack(pady=("10p", "5p"))

progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0.6)

# status label
status_label = ctk.CTkLabel(content_frame, text="Downloaded")

# start the app
root.mainloop()

