import threading
import time
import speech_recognition as sr
import requests
from gtts import gTTS
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from plyer import audio, notification
from kivy.clock import mainthread
from io import BytesIO
import os
import tempfile
import platform

# Ваш API-ключ для ChatGPT
API_KEY = "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"
HEADPHONES_CONNECTED = False
CHECK_INTERVAL = 5  # Интервал проверки в секундах

class HeadphoneRecorderApp(App):
    def build(self):
        self.label = Label(text="Подключите наушники для записи", font_size=20)
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(self.label)
        
        threading.Thread(target=self.periodic_check).start()
        
        return layout

    def periodic_check(self):
        while True:
            self.check_headphones()
            time.sleep(CHECK_INTERVAL)

    def check_headphones(self):
        global HEADPHONES_CONNECTED
        try:
            if platform.system() == "Android":
                HEADPHONES_CONNECTED = audio.is_headset_connected()
            else:
                HEADPHONES_CONNECTED = True  # Для тестирования на ПК

            if HEADPHONES_CONNECTED:
                self.update_label("Наушники подключены. Начинается запись...")
                self.record_and_send()
            else:
                self.update_label("Наушники не подключены. Подключите их и попробуйте снова.")
        except Exception as e:
            self.update_label(f"Ошибка проверки наушников: {e}")

    def record_and_send(self):
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                self.update_label("Говорите... Идет запись")
                audio_data = recognizer.listen(source, timeout=10)
                self.update_label("Идет распознавание...")
                text = recognizer.recognize_google(audio_data, language="ru-RU")
                self.update_label(f"Распознанный текст: {text}")
                self.send_to_chatgpt(text)
        except sr.MicrophoneException as e:
            self.update_label(f"Ошибка доступа к микрофону: {e}")
        except sr.WaitTimeoutError:
            self.update_label("Время записи истекло.")
        except sr.UnknownValueError:
            self.update_label("Не удалось распознать речь.")
        except Exception as e:
            self.update_label(f"Ошибка записи: {e}")

    def send_to_chatgpt(self, user_text):
        self.update_label("Отправка запроса в ChatGPT...")
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": user_text}
            ]
        }

        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()
            chat_response = result["choices"][0]["message"]["content"]
            self.update_label(f"Ответ ChatGPT: {chat_response}")

            # Озвучивание ответа
            self.speak_response(chat_response)

        except requests.RequestException as e:
            self.update_label(f"Ошибка запроса: {e}")
        except Exception as e:
            self.update_label(f"Ошибка обработки ответа: {e}")

    def speak_response(self, text):
        try:
            tts = gTTS(text, lang="ru")
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts.save(temp_file.name)
            os.system(f"mpv {temp_file.name}")  # Используем mpv для воспроизведения
            os.remove(temp_file.name)
        except Exception as e:
            self.update_label(f"Ошибка озвучивания: {e}")

    @mainthread
    def update_label(self, text):
        self.label.text = text

if __name__ == '__main__':
    HeadphoneRecorderApp().run()
