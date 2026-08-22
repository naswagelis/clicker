from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.clock import Clock
import threading
import time

class ClickerApp(App):
    def build(self):
        self.is_clicking = False
        self.cps = 10.0

        # Основной контейнер
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        # Заголовок
        self.title_label = Label(
            text='Android AutoClicker', 
            font_size='24sp', 
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.title_label)

        # Статус
        self.status_label = Label(
            text='Статус: Остановлен', 
            font_size='18sp', 
            size_hint=(1, 0.2),
            color=(1, 0.3, 0.3, 1)
        )
        layout.add_widget(self.status_label)

        # Вывод текущего CPS
        self.cps_label = Label(
            text=f'Скорость: {int(self.cps)} CPS', 
            font_size='16sp', 
            size_hint=(1, 0.1)
        )
        layout.add_widget(self.cps_label)

        # Слайдер настройки CPS
        self.slider = Slider(min=1, max=30, value=self.cps, size_hint=(1, 0.2))
        self.slider.bind(value=self.on_slider_change)
        layout.add_widget(self.slider)

        # Кнопка Старт/Стоп
        self.toggle_btn = Button(
            text='ЗАПУСТИТЬ', 
            font_size='20sp', 
            size_hint=(1, 0.3),
            background_color=(0.1, 0.7, 0.2, 1)
        )
        self.toggle_btn.bind(on_press=self.toggle_clicker)
        layout.add_widget(self.toggle_btn)

        return layout

    def on_slider_change(self, instance, value):
        self.cps = value
        self.cps_label.text = f'Скорость: {int(self.cps)} CPS'

    def toggle_clicker(self, instance):
        if not self.is_clicking:
            self.is_clicking = True
            self.toggle_btn.text = 'ОСТАНОВИТЬ'
            self.toggle_btn.background_color = (0.8, 0.1, 0.1, 1)
            self.status_label.text = 'Статус: Работает!'
            self.status_label.color = (0.2, 1, 0.2, 1)
            
            # Запускаем кликер в отдельном потоке
            threading.Thread(target=self.click_loop, daemon=True).start()
        else:
            self.is_clicking = False
            self.toggle_btn.text = 'ЗАПУСТИТЬ'
            self.toggle_btn.background_color = (0.1, 0.7, 0.2, 1)
            self.status_label.text = 'Статус: Остановлен'
            self.status_label.color = (1, 0.3, 0.3, 1)

    def click_loop(self):
        while self.is_clicking:
            # Здесь будет логика кликов по экрану (требует Android Accessibility Service)
            print(f"Клик! Скорость: {self.cps} CPS")
            
            # Пауза между кликами на основе CPS
            time.sleep(1.0 / self.cps)

if __name__ == '__main__':
    ClickerApp().run()
          
