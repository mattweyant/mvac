from PIL import Image
import glob, os

def convert():
    for infile in glob.glob("img/*.jpg"):
        # f, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im = im.resize((2047, 720), Image.ANTIALIAS)
        im.save("converted/" + infile, optimize=True, quality=95)


if __name__ == "__main__":
    convert()