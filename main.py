from kivy.app import App
from kivy.uix.screenmanager import Screen


class PhotoGalleryApp(App):
    pass

class Display(Screen):
    def display_image(self):
        return images[index]

    def advance_image(self):
        global index
        if index < len(images)-1:
            index += 1
        else:
            index = 0
        self.ids.image.source = self.display_image()

    def back_image(self):
        global index
        if index > 0:
            index -= 1
        else:
            index = len(images)-1
        self.ids.image.source = self.display_image()


images = ["neff.jpg","amos.jpg","munro.jpg","podium.jpg"]
index = 0


PhotoGalleryApp().run()
