from PIL import Image
import glob
import random
import os.path

def owatahatena():
    #print(glob.glob(os.path.dirname(os.path.abspath(__file__))+ '/data/*.jpeg'))
    im = Image.open(random.choice(glob.glob(os.path.dirname(os.path.abspath(__file__))+'/data/*.jpeg')))
    im.show()

if __name__ == '__main__':
    
    owatahatena()
    
