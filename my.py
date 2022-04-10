import streamlit as st
import numpy as np
from PIL import Image, ImageDraw
import pytesseract

uploaded_file = st.file_uploader("Загрузите документ...")

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
       crd.append(list(map(int,ch[1:5])))
        
   w,h = img.size
   draw = ImageDraw.Draw(img)
   
   for c in crd:
     draw.rectangle([(c[0],h-c[1]),(c[2],h-c[3])], fill='white')
  
   return img

if uploaded_file is not None:    
    image = Image.open(uploaded_file)	
	
    st.image(uploaded_file, caption='Input Image', use_column_width=True)    
    im = imgGen2(uploaded_file)	
    st.image(im, caption='тестовая версия', use_column_width=True)