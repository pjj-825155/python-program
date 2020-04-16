import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen

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
        #添加几个标签       
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
        #跳转页面内容
        chat_app.info_page.update_info(f"ip={ip},port={port},name={name}")
        #跳转
        chat_app.screen_manager.current="Info"

class InfoPage(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=1
        #设置位置和大小
        self.message=Label(halign="center",valign="middle",font_size=30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)

    def update_info(self,message):
        self.message.text=message

    def update_text_width(self,*_):
        self.message.text_size=(self.message.width*0.9,None)
        
class EpicApp(App):
    def build(self):
        self.screen_manager=ScreenManager()

        self.connect_page=ConnectPage()
        screen=Screen(name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.info_page=InfoPage()
        screen=Screen(name="Info")
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == "__main__":
    chat_app=EpicApp()
    chat_app.run()
