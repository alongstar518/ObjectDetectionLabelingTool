import os
from PIL import Image
import glob

imglist = glob.glob('d:\data\*.*')

for im in imglist:
    try:
        img = Image.open(im)
        img = img.resize((1280,1280), Image.ANTIALIAS)
        img.save(im.replace('data', 'data3').replace('.png','.jpg'))
        print 'saved image:',im
    except Exception:
        print 'error image', im
        try:
            os.remove(im)
        except Exception:
            pass
    finally:
        pass


