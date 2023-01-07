from kivy.tests.common import GraphicUnitTest, UnitTestTouch


class TestLoginScreen(GraphicUnitTest):
    def testScreen(self):
        from kivy.uix.screenmanager import ScreenManager
        from loginScreen import LoginScreen
        
        manager = ScreenManager()
        loginScreen = LoginScreen(name='login')
        manager.add_widget(loginScreen)
        manager.current = 'login'
        
        self.render(manager)
        
        from kivy.base import EventLoop
        
        EventLoop.ensure_window()
        window = EventLoop.window
        
        touchLogin = UnitTestTouch(
            *window.children[0].children[0].ids.username.pos
        )
        touchPasswd = UnitTestTouch(
            *window.children[0].children[0].ids.passwd.pos
        )
        touchButton = UnitTestTouch(
            *window.children[0].children[0].ids.login.pos
        )
        
        touchLogin.touch_down()
        self.assertTrue(window.children[0].children[0].ids.username.focus)
        touchLogin.touch_up()
        
        touchPasswd.touch_down()
        self.assertTrue(window.children[0].children[0].ids.passwd.pos)
        touchPasswd.touch_up()
        
        window.children[0].children[0].ids.username.text = 'admin'
        window.children[0].children[0].ids.passwd.text = 'admin'
        
        window.children[0].children[0].ids.login.bind(on_release=lambda instance: setattr(instance, 'passed', True))
        
        touchButton.touch_down()
        touchButton.touch_up()
        self.assertTrue(window.children[0].children[0].ids.login.passed)
        
        
if __name__ == '__main__':
    import unittest
    unittest.main()