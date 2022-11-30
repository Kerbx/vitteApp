import kivy
kivy.require('2.1.0')

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_string("""
<TasksScreen>:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "Электронная среда"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        elevation: 1
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '10dp'
                MDLabel:
                    size_hint_y: None
                    height: self.texture_size[1]
                    text: "Текст"
                    color: "black"
                    font_style: "Subtitle1"
                MDLabel:
                    size_hint_y: None
                    height: self.texture_size[1]
                    text: "Текст2"
                    color: "black"
                    font_style: "Caption"
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "Главная"
                            on_press:root.openMain()
                            IconLeftWidget:
                                icon: "home"
                        OneLineIconListItem:
                            text: "Расписание"
                            on_press:root.openCalendar()
                            IconLeftWidget:
                                icon: "calendar"
                        OneLineIconListItem:
                            text: "Задания"
                            on_press:root.openTasks()
                            IconLeftWidget:
                                icon: "lead-pencil"
                        OneLineIconListItem:
                            text: "Выйти"
                            on_press:root.logout()
                            IconLeftWidget:
                                icon: "logout"
""")

class TasksScreen(Screen):
    def openMain(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'main'
        
    def openCalendar(self):
        self.manager.current = 'calendar'
        self.ids.nav_drawer.set_state("close")
        
    def openTasks(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'tasks'
        
    def logout(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'login'
