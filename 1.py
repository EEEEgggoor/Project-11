from kivy.lang import Builder

from kivymd.uix.scrollview import MDScrollView
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase

KV = '''
    MDBoxLayout:
        orientation: "vertical"
    
        MDTopAppBar:
            title: "Example Tabs"
    
        MDTabs:
            id: tabs
    
    
    <Tab>
    
        MDList:
    
            MDBoxLayout:
                adaptive_height: True
    
                MDFlatButton:
                    text: "ADD TAB"
                    on_release: app.add_tab()
    
                MDFlatButton:
                    text: "REMOVE LAST TAB"
                    on_release: app.remove_tab()
    
                MDFlatButton:
                    text: "GET TAB LIST"
                    on_release: app.get_tab_list()
'''


class Tab(MDScrollView, MDTabsBase):
    '''Class implementing content for a tab.'''


class Example(MDApp):
    index = 0

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def on_start(self):
        self.add_tab()

    def get_tab_list(self):
        '''Prints a list of tab objects.'''

        print(self.root.ids.tabs.get_tab_list())

    def add_tab(self):
        self.index += 1
        self.root.ids.tabs.add_widget(Tab(title=f"{self.index} tab"))

    def remove_tab(self):
        if self.index > 1:
            self.index -= 1
            self.root.ids.tabs.remove_widget(
                self.root.ids.tabs.get_tab_list()[-1]
        )


Example().run()