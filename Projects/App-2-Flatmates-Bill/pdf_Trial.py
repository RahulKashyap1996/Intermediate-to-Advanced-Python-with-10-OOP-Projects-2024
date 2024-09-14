# import the canvas object
from datetime import time, datetime, date
from itertools import count
from pickle import GLOBAL

from PIL.TiffImagePlugin import DATE_TIME
from reportlab.pdfgen import canvas
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0


from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))


count=0
# c = canvas.Canvas("generated pdf's/" + "Flatmate_Bill" + "_" + "v"+str(counter)+".pdf",
#                       pagesize=(595.27, 841.89))

def increment_count():
    global count
    count+=1
    return count

def set_count_to_zero():
    global count
    count=0




def create_pdf(flatmate1_name,flatmate2_name,flatmate1_bill,flatmate2_bill):


    # draw a string at x=100, y=800 points
    # point ~ standard desktop publishing (72 DPI)
    # coordinate system:
    #   y
    #   |
    #   |   page
    #   |
    #   |
    #   0-------x
    if count==0:
        now = datetime.now()
        c = canvas.Canvas("generated pdf's/" + "Flatmate_Bill" + "_" + "v" +str(now.timestamp())+str(date.today()) + ".pdf",
                      pagesize=(595.27, 841.89))


    c.setFont('Vera', 32,)
    c.drawString(200, 780, "Flatmates Bill")

    c.setFont('Vera', 20, )
    c.drawString(100,700,text="Full Name")
    c.drawString(250, y=700, text="Bill Amount to be Paid")


    increment_count()
    if count==10:
        c.drawImage(image="files/house.png", x=50, y=760, width=50, height=50)
        # finish page
        c.showPage()
        # construct and save file to .pdf
        c.save()
        set_count_to_zero()


    else:
        initial_x_for_name1 = 670
        for i in range(count):
            initial_x_for_name1-=25

            c.drawString(100, y=initial_x_for_name1, text=flatmate1_name)
            c.drawString(250, y=initial_x_for_name1, text=str(flatmate1_bill))

            c.drawString(100, y=(initial_x_for_name1 - 25), text=flatmate2_name)
            c.drawString(250, y=(initial_x_for_name1 - 25), text=str(flatmate2_bill))
        c.drawImage(image="files/house.png", x=50, y=760, width=50, height=50)
        # finish page
        c.showPage()
        # construct and save file to .pdf
        c.save()
        set_count_to_zero()





# def canvas_object(flatmate1_name,flatmate2_name):
#     c = canvas.Canvas("generated pdf's/" + "Flatmate_Bill" + "_" + "v"+str(counter)+".pdf",
#                       pagesize=(595.27, 841.89))  # A4 pagesize
#     return c

# def save_the_pdf(flatmate1_name,flatmate2_name):
#     c=canvas_object(flatmate1_name,flatmate2_name)
#     c.drawImage(image="files/house.png",x=50,y=760,width=50,height=50)
#     # finish page
#     c.showPage()
#     # construct and save file to .pdf
#     c.save()

# try:
#     create_pdf("Rain","Pain",430,333)
# # create_pdf("Rain","Pain",430,333,count=1)
# except ValueError as e:
#     print(e)
