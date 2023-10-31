from kivymd.uix.menu import MDDropdownMenu
from typing import Union
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.pickers import MDColorPicker
from kivy.properties import DictProperty
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.label import MDLabel





KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True


MDScreen:

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:
            
                BoxLayout:
                
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: "AiNote"
                        elevation: 10
                        id: toolbar
                        pos_hint: {"top": 1}
                        md_bg_color: [1.0, 1.0, 1.0, 1]
                        specific_text_color: "#4a4939"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                
        MDNavigationDrawer:
            id: nav_drawer
            scrim_color: 0, 0, 0, 0.5
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Header title"
                    title_color: "#4a4939"
                    text: "Header text"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Меню"

                DrawerClickableItem:
                    icon: "gmail"
                    right_text: "+99"
                    text_right_color: "#4a4939"
                    text: "Inbox"


                DrawerClickableItem:
                    icon: "send"
                    text: "Выбор цвета"
                    on_release: app.open_color_picker()


                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Labels"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"


'''



class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class MainApp(MDApp):

    def on_start(self):
        for i in range(20):
            self.root.ids.tabs.add_widget(Tab(
                    MDLabel(id="label", text="Tab 0", halign="center"),
                    title=f"Tab {i}"))

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        instance_tab.ids.label.text = tab_text

    def open_color_picker(self):
        color_picker = MDColorPicker(size_hint=(0.5, 0.8))
        color_picker.open()
        color_picker.bind(
            on_select_color=self.on_select_color,
            on_release=self.get_selected_color,
        )

    def update_color(self, color: list) -> None:
        # self.root.ids.toolbar.md_bg_color = color
        print(color)


    def get_selected_color(
            self,
            instance_color_picker: MDColorPicker,
            type_color: str,
            selected_color: Union[list, str],
    ):
        '''Return selected color.'''

        print(f"Selected color is {selected_color}")
        self.update_color(selected_color[:-1] + [1])

        return selected_color


    def on_select_color(self, instance_gradient_tab, color: list) -> None:
        '''Called when a gradient image is clicked.'''



    def build(self):
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)










MainApp().run()
