from PIL import Image

img = Image.open("2.jpg")   # type: Image.Image

print(img.size)

img.show()

"""
三个属性:
    format
        格式信息，不一定是文件的后缀
    size
        尺寸
    mode
        模式
    常见mode
        L 黑白
        P
            使用调色板映射到任何其他模式
        RGB
        RGBA
        CMYK
"""