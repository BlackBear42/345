import speech_recognition as sr
# 創建一個Recognizer對象
r = sr.Recognizer()
questions = {
    "訂單狀態": "您可以在我們的網站上查看您的訂單狀態。",
    "退貨流程": "您可以在我們的網站上查看退貨流程，或者聯繫我們的客服人員進行退貨。",
    "支付問題": "您可以在我們的網站上查看支付方式，或者聯繫我們的客服人員進行支付。",
    "產品信息": "您可以在我們的網站上查看產品信息，或者聯繫我們的客服人員瞭解更多詳情。",
}
with sr.Microphone(device_index=0, sample_rate=44100, chunk_size=512) as source:
    r.adjust_for_ambient_noise(source, duration=1) # 不用 adjust_for_ambient_noise() 方法
    r.energy_threshold = 4000 # 加入 energy_threshold 參數
while True:
    with sr.Microphone() as source:
        print("Please speak:")
        audio = r.listen(source, timeout=5)
        
    try:
        text = r.recognize_google(audio, language='zh-TW')
        print("You said: {}".format(text))
       
         
        
        if "客服" in text:
            print("Connecting to customer service...")
            print("Connection succeeded.")
            while True:
                with sr.Microphone() as source:
                    print("Please speak:")
                    
                    audio = r.listen(source, timeout=10)

                
                try:
                    text = r.recognize_google(audio, language='zh-TW')
                    print("You said: {}".format(text))
                    if "拜拜" in text:
                        print("Goodbye!")
                        break
                    with open('file1.txt', 'w') as f:
                         f.write(text)

                         
                        
                except sr.UnknownValueError:
                    print("Sorry, I couldn't understand you. Please try again.")
                except sr.WaitTimeoutError:
                    print("Sorry, we didn't hear anything. Please try again.")
    except sr.UnknownValueError:
         print("Sorry, I couldn't understand you. Please try again.")
    except sr.WaitTimeoutError:
        print("Sorry, we didn't hear anything. Please try again.")
    if "拜拜" in text:
                        print("Goodbye!")
                        break

