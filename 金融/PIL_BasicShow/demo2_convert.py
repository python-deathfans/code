from PIL import Image

img = Image.open('./2.jpg')         # type: Image.Image
new_img = img.convert('L')

print(img.mode)
print(new_img.mode)

new_img.save("2_L.jpg")
new_img.show()

