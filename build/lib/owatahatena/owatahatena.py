from PIL import Image
import glob
import random
import os.path

def owatahatena():
    im = Image.open(random.choice(glob.glob(os.path.dirname(__file__)+'/*.jpeg')))
    im.show()

if __name__ == '__main__':
    
    owatahatena()
    
