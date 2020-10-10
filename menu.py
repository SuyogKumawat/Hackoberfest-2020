import speech_recognition as sr
import webbrowser
print("Welcome to Hacktoberfest 2020 Here it goes")
print("enter your requiremnets: ",end='')
#ch=input()
r=sr.Recognizer()

with sr.Microphone() as source:
	print('Start say...')
	audio=r.listen(source)
	print("speech done")

ch=r.recognize_google(audio)

if "register" in ch:
	webbrowser.open("https://hacktoberfest.digitalocean.com/")
elif("Sign up Github" in ch):
	webbrowser.open("https://github.com/")
else:
	print("not understand")