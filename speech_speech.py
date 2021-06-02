import googletrans
import speech_recognition as sr
import gtts
import playsound
recognizer=sr.Recognizer()
translator=googletrans.Translator()
input_language='ml-IN'#search in speech regonisation supported language here it is malayalam
output_language='es'
try:
    with sr.Microphone() as source:
        print('Speak Know')
        voice=recognizer.listen(source)
        text=recognizer.recognize_google(voice,language=input_language)
        print(text)
except:
    pass

translated=translator.translate(text, dest=output_language)
print(translated.text)
converted_audio=gtts.gTTS(translated.text,lang=output_language)
converted_audio.save('Translated_voice.mp3')
playsound.playsound('Translated_voice.mp3')
#print(googletrans.LANGUAGES)#for showing all language available for translation
