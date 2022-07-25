# creating Gui with the help of python tkinter
# tkinter the standard GUI library for python
# python with tkinter is the fastest way to create the GUI application

import tkinter as tk
import boto3
import os
import sys
from tempfile import gettempdir
from contextlib import closing

# it is the window
root = tk.Tk()
# root.geomatery("400 * 240")
root.geometry("400x240")
root.title("Text to speech converter using Amazon polly")

# height of the window
text_example = tk.Text(root,height=12)  
# pack to the text with window
text_example.pack()
def getText():
    aws_mag_col = boto3.session.Session(profile_name = 'demo_user')
    client = aws_mag_col.client(service_name = 'polly',region_name='us-east-1')
    result = text_example.get("1.0","end")
    print(result)

    # request to amazon polly
    response = client.synthesize_speech(VoiceId='Joanna',OutputFormat='mp3',Text=result,Engine='neural')
    print(response)
    if "AudioStream" in response:
        with closing(response['AudioStream']) as stream:
            output=os.path.join(gettempdir(),"speech.mp3")
            try:
                with open(output,"wb") as file:
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)
    else:
        print("cloud not find stream")
        sys.exit(-1)
    if sys.platform == 'win32':
        os.startfile(output)
btnread = tk.Button(root,height=1,width=10,text="read",command=getText)
btnread.pack()
root.mainloop()