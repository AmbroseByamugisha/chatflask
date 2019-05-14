from PIL import Image
try:
    img = Image.open("/home/ambrose/Pictures/3500.jpg")
except IOError:
    print("The image cannot be found")
    
image_1 = img.save("/home/ambrose/Pictures/3500.jpg")
