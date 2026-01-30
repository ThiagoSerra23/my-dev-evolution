from PIL import Image

def resize(path, size):
    img = Image.open(path)
    img.resize(size).save('resized.png')