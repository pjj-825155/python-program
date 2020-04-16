import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ConnectPage(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #分成n列
        self.cols=2
        #分成m行
        self.rows=4
        #读取本地查看是否为空
        f=open("data.txt","r")
        d=f.readline()
        if d:
            d=d.split(",")
            data_ip=d[0]
            data_port=d[1]
            data_name=d[2]
        else:
            data_ip=""
            data_port=""
            data_name=""
                
        self.add_widget(Label(text="IP"))
        self.ip=TextInput(text=data_ip,multiline=False)
        self.add_widget(self.ip)

        self.add_widget(Label(text="Port"))
        self.port=TextInput(text=data_port,multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text="Name"))
        self.name=TextInput(text=data_name,multiline=False)
        self.add_widget(self.name)

        #添加按钮
        self.join=Button(text="Join")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)

    def join_button(self,instance):
        ip=self.ip.text
        port=self.port.text
        name=self.name.text

        print(f"ip={ip},port={port},name={name}")
        with open("data.txt","w") as f:
            f.write(f"{ip},{port},{name}")

class EpicApp(App):
    def build(self):
        return ConnectPage()

if __name__ == "__main__":
    EpicApp().run()
