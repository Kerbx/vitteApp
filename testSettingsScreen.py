from kivy.tests.common import GraphicUnitTest, UnitTestTouch


class TestLoginScreen(GraphicUnitTest):
    def testScreen(self):
        from kivy.uix.screenmanager import ScreenManager
        from settingsScreenTeacher import SettingsScreenTeacher
        
        manager = ScreenManager()
        settingsScreen = SettingsScreenTeacher(name='settings')
        manager.add_widget(settingsScreen)
        manager.current = 'settings'
        
        self.render(manager)
        
        from kivy.base import EventLoop
        
        EventLoop.ensure_window()
        window = EventLoop.window
        
        touchSettings = UnitTestTouch(
            *window.children[0].children[0].ids.change_theme.pos
        )
        
        touchSettings.touch_down()
        touchSettings.touch_up()
        self.assertTrue(window.children[0].children[0].theme_cls.theme_style == 'Light')
        self.assertTrue(window.children[0].children[0].theme_cls.primary_palette == 'Red')

        touchSettings.touch_down()
        touchSettings.touch_up()
        self.assertTrue(window.children[0].children[0].theme_cls.theme_style == 'Dark')
        self.assertTrue(window.children[0].children[0].theme_cls.primary_palette == 'Orange')
        
if __name__ == '__main__':
    import unittest
    unittest.main()