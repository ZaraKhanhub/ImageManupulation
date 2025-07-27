import cv2
import matplotlib.pyplot as plt
import numpy as np
image=cv2.imread("zara.jpg")
image_RGB=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image_RGB)
plt.title("My beautiful image")
plt.show()
image_GRAY=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(image_GRAY)
plt.title("My beautiful image in gray color")
plt.show()
cropped=image[0:160,0:200]
croppedRGB=cv2.cvtColor(cropped,cv2.COLOR_BGR2RGB)
plt.imshow(croppedRGB)
plt.title("My beautiful cropped image")
plt.show()
print(image.shape)
(h,w,c)=image.shape
center=(w//2,h//2)
m=cv2.getRotationMatrix2D(center,45,1)
rotated=cv2.warpAffine(image,m,(w,h))
rotatedRGB=cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB)
plt.imshow(rotatedRGB)
plt.title("My beautiful rotated image")
plt.show()
brightnessMartix=np.ones(image.shape,dtype="uint8")*50
brighter=cv2.add(image,brightnessMartix)
brighterRGB=cv2.cvtColor(brighter,cv2.COLOR_BGR2RGB)
plt.imshow(brighterRGB)
plt.title("My beautiful brighter image")
plt.show()