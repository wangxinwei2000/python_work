# =================
from PIL import Image,ImageFilter
import cv2
import matplotlib.pyplot as plt
im = Image.open('longge.jpg')
r,g,b = im.split()
plt.figure("longlong")
om = Image.merge("RGB",(b,r,g))
om2 = im.filter(ImageFilter.CONTOUR)
plt.imshow(om2)
# ===================
plt.show()

# ========================

# im2 = Image.open('unstopPicture.gif')
# plt.figure('unstop_picture')
# try:
#     plt.imshow(im2)
#     plt.show()
#     while True:
#         im2.seek(im2.tell()+1)
#         plt.imshow(im2)
#         plt.show()
# except:
#     print("处理结束")
#



