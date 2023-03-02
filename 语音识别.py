import pyttsx3 as pyttsx
from comtypes.client import CreateObject
from comtypes.gen import SpeechLib
from win32com.client import Dispatch
import speech_recognition as sr

# 文本转化为语音
"""engine = pyttsx.init()
engine.say('好好学习')
engine.runAndWait()"""

# 文本转化为语音
"""speaker = Dispatch('SAPI.SpVoice')
speaker.Speak("好好学习")
del speaker"""

# 将文本转化为语音
engine = CreateObject('SAPI.SpVoice')
stream = CreateObject('SAPI.SpFileStream')
infile = 'demo.txt'  # 事先创建文本文件
outfile = 'demo_audio.wav'  # 生成音频文件
stream.open(outfile, SpeechLib.SSFMCreateForWrite)
engine.AudioOutputStream = stream
f = open(infile, 'r', encoding='utf-8')
theText = f.read()
f.close()
engine.speak(theText)
stream.close()

# 将语音转换为文本
audio_file = 'demo_audio.wav'
r = sr.Recognizer()
# 打开语音文件
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)
# print('文本内容：',r.recognize_sphinx(audio))
print('文本内容：', r.recognize_sphinx(audio, language='zh-CN'))
