from PIL import Image, ImageFilter
import os
image1 = Image.open('1.png')
# image1.rotate(90).save('1_90.png')

# convert to gray
# image1.convert(mode='L').save('mode_l.png')

image1.filter(ImageFilter.GaussianBlur(15)).save('blur.png')

# image1.show()
# image1.save('1.jpg')

# size_300 = (300, 300)
# size_700 = (700, 700)


# for f in os.listdir('.'):
# 	if f.endswith('.jpg'):
# 		# print(f)
# 		i = Image.open(f)
# 		fn, fext = os.path.splitext(f)
# 		# print(fn)
# 		# print(fext)
# 		i.thumbnail(size_300)
# 		i.save('pngs/{}_300.png'.formate(fn))

# 		i.thumbnail(size_700)
# 		i.save('pngs/{}_700.png'.formate(fn))