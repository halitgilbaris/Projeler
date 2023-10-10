from PIL import Image
img = Image.open("download.png")
img = img.convert("RGB")
img.save("download.jpg")
