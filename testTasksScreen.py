from kivy.tests.common import GraphicUnitTest, UnitTestTouch


class TestLoginScreen(GraphicUnitTest):
    def testScreen(self):
        from kivy.uix.screenmanager import ScreenManager
        from tasksScreenTeacher import TasksScreenTeacher
        
        manager = ScreenManager()
        tasksScreen = TasksScreenTeacher(name='tasks')
        manager.add_widget(tasksScreen)
        manager.current = 'tasks'
        
        self.render(manager)
        
        from kivy.base import EventLoop
        
        EventLoop.ensure_window()
        window = EventLoop.window
        
        touchAdd = UnitTestTouch(
            *window.children[0].children[0].ids.add.pos
        )
        
        window.children[0].children[0].ids.add.bind(on_release=lambda instance: setattr(instance, 'passed', True))

        touchAdd.touch_down()
        touchAdd.touch_up()
        self.assertTrue(window.children[0].children[0].ids.add.passed)

        
if __name__ == '__main__':
    import unittest
    unittest.main()