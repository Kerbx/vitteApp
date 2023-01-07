from kivy.tests.common import GraphicUnitTest, UnitTestTouch


class TestLoginScreen(GraphicUnitTest):
    def testScreen(self):
        from main import MyApp        
        
        self.render(MyApp)
        
        from kivy.base import EventLoop
        
        EventLoop.ensure_window()
        window = EventLoop.window
        
        touchMain = UnitTestTouch(
            *window.children[0].children[0].ids.main.pos
        )
        touchTasks = UnitTestTouch(
            *window.children[0].children[0].ids.tasks.pos
        )
        touchCalendar = UnitTestTouch(
            *window.children[0].children[0].ids.calendar.pos
        )
        touchSettings = UnitTestTouch(
            *window.children[0].children[0].ids.settings.pos
        )
        touchLogout = UnitTestTouch(
            *window.children[0].children[0].ids.logout.pos
        )
        
        touchSettings.touch_down()
        touchSettings.touch_up()
        self.assertTrue(window.children[0].children[0].manager.current == 'settings')

        touchMain.touch_down()
        touchMain.touch_up()
        self.assertTrue(window.children[0].children[0].manager.current == 'main')
        
        touchCalendar.touch_down()
        touchCalendar.touch_up()
        self.assertTrue(window.children[0].children[0].manager.current == 'calendar')
        
        touchTasks.touch_down()
        touchTasks.touch_up()
        self.assertTrue(window.children[0].children[0].manager.current == 'tasks')
        
        touchLogout.touch_down()
        touchLogout.touch_up()
        self.assertTrue(window.children[0].children[0].manager.current == 'logout')
        
        
if __name__ == '__main__':
    import unittest
    unittest.main()