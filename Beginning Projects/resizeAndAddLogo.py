#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit in a 300x300 square, and adds catlogo.png to the lower-right corner.
import os
from PIL import Image
os.makedirs('withLogo',exist_ok=True)

SQUARE_FIT_SIZE=300
LOGO_FILENAME='C:/Users/School Projects/AppData/Local/Programs/Python/Python37-32/automate_online-materials/catlogo.png'

logoIm=Image.open(LOGO_FILENAME)
logoIm=logoIm.resize((50,50))
logoWidth,logoHeight=logoIm.size

#Loop over all files in current working directory.
for filename in os.listdir('C:/Users/School Projects/AppData/Local/Programs/Python/Python37-32/automate_online-materials'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')):
        continue  #skip non-image files itself
    if filename==LOGO_FILENAME:
        continue  #skip the logo file itself
    im=Image.open(os.path.join('C:/Users/School Projects/AppData/Local/Programs/Python/Python37-32/automate_online-materials',filename))
    width,height=im.size
    


    if width>SQUARE_FIT_SIZE and height>SQUARE_FIT_SIZE:
        #Calculate the new width and height to resize to.
        if width>=height:
            height=int((SQUARE_FIT_SIZE/height)*width)
            width=SQUARE_FIT_SIZE
        else:
            width=int((SQUARE_FIT_SIZE/width)*height)
            height=SQUARE_FIT_SIZE

        #Resize image.
        print('Resizing %s ......'%(filename))
        im=im.resize((width,height))

    #Add logo.
    print('Adding logo to %s .......'%(filename))
    im.paste(logoIm,(width-logoWidth,height-logoHeight),logoIm)

    #Save changes.
    im.save(os.path.join('withLogo',filename))
    
            

        
