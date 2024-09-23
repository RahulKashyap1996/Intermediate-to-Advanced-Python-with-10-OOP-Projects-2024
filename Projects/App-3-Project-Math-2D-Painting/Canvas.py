import time

from PIL import Image


class Canvas():
    def __init__(self,radius=0):
        self.radius=radius

    def create_image(self):
        p=Image.new(mode="RGB",size=[1000,1000],color="White")
        filename="Output Files/"+str(time.time())+".jpg"
        p.save(fp="Output Files/"+str(time.time())+".jpg")
        return filename


canvas=Canvas()
canvas.create_image()