import sys
import os
from PIL import Image

input_file= sys.argv[1]
output_file= sys.argv[2]

if not os.path.exists(output_file):
    print("Input file does not exist")
    print("Dont worry we will create it for you")
    os.makedirs(output_file)

for file in os.listdir(input_file):
    img= Image.open(f"{input_file}{file}")
    clean_name= os.path.splitext(file)[0]
    img.save(f"{output_file}{clean_name}.png","png")
    print(f"All Done! converted {file} to PNG")    
   












