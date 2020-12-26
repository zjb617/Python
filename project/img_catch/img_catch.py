from PIL import ImageGrab, Image
def screen():
    im = ImageGrab.grab()
    im = im.resize((2560,1600), Image.ANTIALIAS)
    im.save("screen.jpg")
    im.show()
screen()