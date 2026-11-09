# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase
import webbrowser

# 注册Windows自带的微软雅黑字体，解决中文方框问题
LabelBase.register(name='YaHei', fn_regular='C:/Windows/Fonts/msyh.ttc')
FONT = 'YaHei'


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        # 标题
        self.add_widget(Label(
            text='我的手机小工具',
            size_hint_y=None, height=50,
            bold=True, font_size=22,
            font_name=FONT
        ))

        # 输入框
        self.url_input = TextInput(
            hint_text='粘贴视频链接到这里',
            multiline=False,
            size_hint_y=None, height=45,
            font_name=FONT
        )
        self.add_widget(self.url_input)

        # 打开按钮
        btn_open = Button(
            text='打开视频',
            size_hint_y=None, height=50,
            background_color=(0.1, 0.47, 1, 1),
            font_name=FONT
        )
        btn_open.bind(on_press=self.open_video)
        self.add_widget(btn_open)

        # 分隔
        self.add_widget(Label(size_hint_y=None, height=10))

        # 三个快捷按钮
        row1 = BoxLayout(size_hint_y=None, height=45, spacing=10)
        btn_iqy = Button(text='爱奇艺', font_name=FONT)
        btn_tx = Button(text='腾讯视频', font_name=FONT)
        btn_yk = Button(text='优酷', font_name=FONT)
        btn_iqy.bind(on_press=lambda x: self.open_site('https://www.iqiyi.com'))
        btn_tx.bind(on_press=lambda x: self.open_site('https://v.qq.com'))
        btn_yk.bind(on_press=lambda x: self.open_site('https://www.youku.com'))
        row1.add_widget(btn_iqy)
        row1.add_widget(btn_tx)
        row1.add_widget(btn_yk)
        self.add_widget(row1)

        # 提示
        self.add_widget(Label(
            text='提示：复制链接后点"打开视频"',
            size_hint_y=None, height=30,
            font_size=12, color=(0.5, 0.5, 0.5, 1),
            font_name=FONT
        ))

    def open_video(self, instance):
        url = self.url_input.text.strip()
        if url:
            webbrowser.open(url)

    def open_site(self, url):
        webbrowser.open(url)


class MyApp(App):
    def build(self):
        self.title = '我的小工具'
        return MainLayout()


if __name__ == '__main__':
    MyApp().run()
