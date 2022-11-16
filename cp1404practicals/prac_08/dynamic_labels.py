from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty



class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Jacob', 'Ryan', 'Clark', 'Groves']

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from list and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

DynamicLabelsApp().run()
