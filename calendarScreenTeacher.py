import kivy
kivy.require('2.1.0')

from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.screen import MDScreen


class CalendarScreenTeacher(MDScreen):
    def onSave(self, instance, value, date_range):
        day = value.weekday()
        while self.ids.schedule.children:
            for i in self.ids.schedule.children:
                self.ids.schedule.remove_widget(i)
            
        schedule = open(f'{day}.txt').read().split('\n')
        
        for i in schedule:
            lessons = i.split('|')
            self.ids.schedule.add_widget(ThreeLineListItem(text=lessons[0], secondary_text=lessons[1], tertiary_text=lessons[2]))
        
    def openDate(self):
        date = MDDatePicker()
        date.bind(on_save=self.onSave)
        date.open()
        
    def openMainTeacher(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'mainTeacher'
        
    def openCalendarTeacher(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'calendarTeacher'
        
    def openTasksTeacher(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'tasksTeacher'
        
    def logout(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'login'

    def openSettingsTeacher(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'settingsTeacher'
        