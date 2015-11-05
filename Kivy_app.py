#Kivy
#Soroiu Teodora

from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.uix.switch import Switch
import sys

class Website(App):

    def build(self):
        self.icon = 'E:/PROGRAMMIN/Curs/Pentru examen/fisiere proiect/python1.ico'
        return Screen()
        
class Screen(FloatLayout):

    def build(self):
        self.object1 = BoxLayout()
        return self.object1
       
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
#Fundal image
        with self.canvas.before:
            self.fundal_image = Image(source = "E:/PROGRAMMIN/Curs/Pentru examen/fisiere proiect/fundal.jpg")
            self.fundal_image.opacity = 0.7
            self.add_widget(self.fundal_image)
            self.rect = Rectangle(size = self.size, pos = self.pos)

        self.bind(size = self._update_rect, pos = self._update_rect)

        self.layout = FloatLayout()
        self.layout.size_hint = (None, None)
        self.layout.size = (600, 500)
        self.layout.padding = 20
        self.fundal_image.add_widget(self.layout)
        
        self.sound = SoundLoader.load("E:/PROGRAMMIN/Curs/Pentru examen/fisiere proiect/JO_-_09_-_Fortitude.ogg")
        self.sound.play()
        self.sound.loop = True
        self.sound.volume = 0.5
               
        self.Menu(None)

    def Menu(self, buton):

        self.layout.clear_widgets()
        
        self.button1 = Button(text = 'Carousel', bold = True, background_color =(0, 0, 1, 1))
        self.button1.pos = (290, 380)
        self.button1.size_hint = (0.3, 0.1)
        self.layout.add_widget(self.button1)

        self.button2 = Button(text = 'Optiuni', bold = True, background_color =(0, 0, 1, 1))
        self.button2.pos = (290, 280)
        self.button2.size_hint = (0.3, 0.1)
        self.layout.add_widget(self.button2)

        self.button3 = Button(text = 'About', bold = True, background_color =(0, 0, 1, 1))
        self.button3.pos = (290, 180)
        self.button3.size_hint = (0.3, 0.1)
        self.layout.add_widget(self.button3)

        self.button4 = Button(text = 'Iesi', bold = True, background_color =(0, 0, 1, 1))
        self.button4.pos = (290, 80)
        self.button4.size_hint = (0.3, 0.1)
        self.layout.add_widget(self.button4)

        self.button1.bind(on_press = self.Carousel)
        self.button2.bind(on_press = self.Options)
        self.button3.bind(on_press = self.About)
        self.button4.bind(on_press = self.Exit)

    def Carousel(self, buton):

        self.layout.clear_widgets()
        
        self.carousel = Carousel(direction = 'right')
        self.carousel.anim_move_duration = 1
        self.carousel.loop = True
        self.carousel.size_hint = (0.7, 0.7)
        self.carousel.pos = (200, 120)
        self.layout.add_widget(self.carousel)

        self.image1 = Image(source = 'E:/PROGRAMMIN/Curs/Pentru examen/fisiere proiect/nature1.jpg')
        self.carousel.add_widget(self.image1)
        self.image2 = Image(source= 'E:/PROGRAMMIN/Curs/Pentru examen/fisiere proiect/nature2.jpg')
        self.carousel.add_widget(self.image2)
        self.image3 = Image(source = 'E:/PROGRAMMIN/Curs/Pentru examen/fisiere proiect/nature3.jpg')
        self.carousel.add_widget(self.image3)
        self.image4 = Image(source = 'E:/PROGRAMMIN/Curs/Pentru examen/fisiere proiect/nature4.jpg')
        self.carousel.add_widget(self.image4)

        self.label = Label(text = 'This is the end of the list!', font_size = 30)
        self.carousel.add_widget(self.label)

        self.backbutton = Button(text = 'Back', bold = True, background_color = (0, 0, 1, 1))
        self.backbutton.pos = (200, 100)
        self.backbutton.size_hint = (0.7, 0.1)
        self.layout.add_widget(self.backbutton)
        
        self.backbutton.bind(on_press = self.Menu)

    def Options(self, buton):
        
        self.layout.clear_widgets()

        self.switch = Switch(text = 'Music')
        self.switch.active = True
        self.switch.size_hint = (0.3, 0.2)
        self.switch.pos = (300, 360)
        self.layout.add_widget(self.switch)

        self.show_volume = Label(text = 'Volume = 50')
        self.layout.add_widget(self.show_volume)

        self.music_slide = Slider(min = 0, max = 100, value = 50)
        self.music_slide.step = 5
        self.music_slide.size_hint = (0.3, 0.1)
        self.music_slide.pos = (300, 180)
        self.music_slide.orientation = 'horizontal'
        self.layout.add_widget(self.music_slide)

        self.button = Button(text = 'Back', bold = True, background_color = (0, 0, 1, 1))
        self.button.pos = (300, 120)
        self.button.size_hint = (0.3, 0.1)
        self.button.opacity = 0.7
        self.layout.add_widget(self.button)
        
        self.switch.bind(active = self.mute)
        self.music_slide.bind(value = self.volume_value)
        self.button.bind(on_press = self.Menu)
       

    def volume_value(self,x,y):
        self.show_volume.text = 'Volume ' + str(int(self.music_slide.value))
        self.sound.volume = self.music_slide.value / 100

    def mute(self,x,y):
        if (self.switch.active == False):
            self.music_slide.disabled = True
            self.sound.stop()
        else:
            self.music_slide.disabled = False
            self.music_slide.value = 0
            self.sound.play()

    def About(self, buton):
        
        self.layout.clear_widgets()
        
        self.backbutton = Button(text = 'Back', background_color = (0, 0, 1, 1))
        self.backbutton.size_hint = (1, 0.1)
        
        self.label = Label(text = 'Thanks InfoAcademy!', bold = True, font_size = 24)
        self.blayout = BoxLayout()
        self.blayout.orientation = 'vertical'
        self.blayout.padding = 40
        
        self.blayout.add_widget(self.backbutton)
        self.blayout.add_widget(self.label)
        self.backbutton.bind(on_press = self.Menu)
        
        self.popup = Popup(background = 'E:/PROGRAMMIN/Curs/Pentru examen/fisiere proiect/fundal4_tema.jpg')
        self.popup.size_hint =(None, None)
        self.popup.size = (400, 400)
        self.popup.title = 'Who made this aplication?'
        self.popup.content = self.blayout
        self.popup.open()
        self.popup.bind(on_press = self.close_popup)
        self.backbutton.bind(on_press = self.close_popup)

    def close_popup(self, buton):
        self.popup.dismiss()

    def Exit(self, buton):
        sys.exit()
               
                                           
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
            
    
if __name__ == '__main__':
    Website().run()
