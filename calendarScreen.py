import kivy
kivy.require('2.1.0')

from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.screen import MDScreen


class CalendarScreen(MDScreen):
    """Данный класс представляет из себя экран с расписанием для студента.
    """
    def onSave(self, instance, value, date_range):
        """Этот метод вызывается при нажатии кнопки "ОК" на виджете календаря.
        Берется выбранный день, проверяется, какой это день недели,
        и в соответствии с этой информацией выводится расписание.
        """
        day = value.weekday()
        while self.ids.schedule.children:
            for i in self.ids.schedule.children:
                self.ids.schedule.remove_widget(i)
            
        schedule = open(f'{day}.txt').read().split('\n')
        
        for i in schedule:
            lessons = i.split('|')
            self.ids.schedule.add_widget(ThreeLineListItem(
                                                    text=lessons[0],
                                                    secondary_text=lessons[1],
                                                    tertiary_text=lessons[2]))
        
    def openDate(self):
        """Данный метод открывает виджет календаря."""
        date = MDDatePicker()
        date.bind(on_save=self.onSave)
        date.open()
        
    def openMain(self):
        """Данный метод открывает главную страницу.
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'main'
        
    def openCalendar(self):
        """Данный метод открывает страницу календаря.
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'calendar'
        
    def openTasks(self):
        """Данный метод открывает страницу с заданиями.
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'tasks'
        
    def logout(self):
        """Данный метод открывает страницу логина.
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'login'
        
    def openSettings(self):
        """Данный метод открывает страницу настроек.
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'settings'
        