from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty




class TheWidgets(BoxLayout):
    def submit(self):
        Name=self.ids.name.text
        print(Name)
        Sport=self.ids.sport.text
        print(Sport)
        Age=self.ids.age.text
        print(Age)
        Clas=self.ids.Class.text
        print(Clas)

        

class TheAnchorWidget(AnchorLayout):
    pass

class TheGridWidget(GridLayout):
    texto1=StringProperty("1")
    toggle=BooleanProperty(False)
    count=1
 #   texto1="1"
    def press(self):
        print("You clicked m!!!")
  #      self.texto2="WTF U called ME"
        self.count+=1
        self.texto1=str(self.count)

    def toogled(self,widget):
        if widget.state=="normal":
            widget.text="Off"
            self.toggle=True
        else:
            widget.text="On"
            self.toggle=False


class MyFirstApp(App):
    pass

MyFirstApp().run()