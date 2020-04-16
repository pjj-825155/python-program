import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class ConnectPage(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #分成n列
        self.cols=2
        #分成m行
        self.rows=3
        self.add_widget(Label(text="IP"))
        self.ip=TextInput(multiline=False)
        self.add_widget(self.ip)

        self.add_widget(Label(text="Port"))
        self.Port=TextInput(multiline=False)
        self.add_widget(self.Port)

        self.add_widget(Label(text="Name"))
        self.Name=TextInput(multiline=False)
        self.add_widget(self.Name)

class EpicApp(App):
    def build(self):
        return ConnectPage()

if __name__ == "__main__":
    EpicApp().run()
