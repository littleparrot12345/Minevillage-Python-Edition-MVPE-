from PIL import Image, ImageDraw

# 打开图片
image = Image.open("path_to_image.png")

# 创建一个同样大小的全透明的颜色图片
color_image = Image.new("RGB", image.size, (0, 0, 0, 0))
image=image.convert('RGB') 

# 创建一个上色的颜色
color = (85, 255, 0)  # #55FF00

# 获取图片的宽度和高度
width, height = image.size

# 循环每个像素，并按照指定颜色给黑色像素上色
for x in range(width):
    for y in range(height):
        # 获取像素的RGB值
        r, g, b = image.getpixel((x, y))
        # 如果是黑色像素，则上色
        color_image.putpixel((x, y), (int((r+85)/2), int((g+255)/2), int((b+0)/2)))
        #color_image.paste(((r+85)/2, (g+255)/2, (b+0)/2),(x,y,x,y))

# 保存上色后的图片
color_image.save("path_to_save_image.png")
