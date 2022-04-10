import streamlit as st
import numpy as np
from PIL import Image, ImageDraw
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

uploaded_file = st.file_uploader("Choose an image...")

def imgGen2(img1): 
   img = Image.open(img1)

    # Adding custom options
   custom_config = r'--oem 3 --psm 6'
   rstr = pytesseract.image_to_string(img, config=custom_config)
   dbox = pytesseract.image_to_boxes(img, config=custom_config)
   
   crd=[]
   for x in dbox.split('\n'):
     ch = x.split(' ')
     if ch[0].isdigit():
       crd.append(ch[1:5])
        
   w,h = img.size
   draw = ImageDraw.Draw(img)
   
   for c in crd:
     draw.rectangle([(int(c[0]),h-int(c[1])),(int(c[2]),h-int(c[3]))], fill='red',width=2)
  
   return img

if uploaded_file is not None:
    #src_image = load_image(uploaded_file)
    image = Image.open(uploaded_file)	
	
    st.image(uploaded_file, caption='Input Image', use_column_width=True)
    #st.write(os.listdir())
    im = imgGen2(uploaded_file)	
    st.image(im, caption='ASCII art', use_column_width=True)