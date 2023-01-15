
from PIL import Image,ImageFilter

img= Image.open("./pokedex/pickachu.png")
 
filter_img= img.filter(ImageFilter.BLUR)
filter_img.save("Blur.png","png")
img.show()