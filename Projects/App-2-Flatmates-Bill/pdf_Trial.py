# import the canvas object
from reportlab.pdfgen import canvas
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0


from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))

# create a Canvas object with a filename
def create_pdf(flatmate1_name,flatmate2_name,flatmate1_bill,flatmate2_bill):


    c = canvas.Canvas("Flatmate_Bill.pdf", pagesize=(595.27, 841.89))  # A4 pagesize
    # draw a string at x=100, y=800 points
    # point ~ standard desktop publishing (72 DPI)
    # coordinate system:
    #   y
    #   |
    #   |   page
    #   |
    #   |
    #   0-------x


    c.setFont('Vera', 32,)
    c.drawString(200, 780, "Flatmates Bill")

    c.setFont('Vera', 20, )
    c.drawString(100,700,text="Full Name")
    c.drawString(250, y=700, text="BIll Amount to be Paid")

    c.drawString(100, 670, text=flatmate1_name)
    c.drawString(250, 670, text=str(flatmate1_bill))

    c.drawString(100, 650, text=flatmate2_name)
    c.drawString(250, 650, text=str(flatmate2_bill))

    c.drawImage(image="files/house.png",x=50,y=760,width=50,height=50)
    # finish page
    c.showPage()
    # construct and save file to .pdf
    c.save()


#create_pdf("Rain","Pain",430,333)