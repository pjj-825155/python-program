import kivy
from kivy.app import App
from kivy.uix.label import Label

class firstApp(App):
    def build(self):
        return Label(text="hello world")

if __name__ == "__main__":
    firstApp().run()
