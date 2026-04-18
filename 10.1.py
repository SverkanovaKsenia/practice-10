from PIL import Image

image = Image.open('zaika.jpg')

cropped = image.crop((100, 100, 300, 200))

cropped.save('zaikacropp.jpg')