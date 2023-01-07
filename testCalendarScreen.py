from kivy.tests.common import GraphicUnitTest, UnitTestTouch


class TestLoginScreen(GraphicUnitTest):
    def testScreen(self):
        from kivy.uix.screenmanager import ScreenManager
        from calendarScreenTeacher import CalendarScreenTeacher
        
        manager = ScreenManager()
        calendarScreen = CalendarScreenTeacher(name='calendar')
        manager.add_widget(calendarScreen)
        manager.current = 'calendar'
        
        self.render(manager)
        
        from kivy.base import EventLoop
        
        EventLoop.ensure_window()
        window = EventLoop.window
        
        touchCalendar = UnitTestTouch(
            *window.children[0].children[0].ids.calendar.pos
        )
        
        window.children[0].children[0].ids.calendar.bind(on_release=lambda instance: setattr(instance, 'passed', True))

        touchCalendar.touch_down()
        touchCalendar.touch_up()
        self.assertTrue(window.children[0].children[0].ids.calendar.passed)

        
if __name__ == '__main__':
    import unittest
    unittest.main()