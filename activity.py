import cv2
import matplotlib.pyplot as plt

image=cv2.imread("peacock.jpg")
image1=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
height,width,channels=image1.shape
rect_width=300
rect_height=400
topleft=(20,20)
botright=(topleft[0]+rect_width,topleft[1]+rect_height)
cv2.rectangle(image1,topleft,botright,(149,108,147),10)

rect_width1=100
rect_height1=150
topleft1=(width-rect_width1-20,height-rect_height1-20)
botright1=(topleft1[0]+rect_width1,topleft1[1]+rect_height1)
cv2.rectangle(image1,topleft1,botright1,(149,108,147),10)

centerx=topleft[0]+rect_width//2
centery=topleft[1]+rect_height//2

cv2.circle(image1,(centerx,centery),50,(233,67,90),-1)

centerx1=topleft1[0]+rect_width1//2
centery1=topleft1[1]+rect_height1//2

cv2.circle(image1,(centerx1,centery1),50,(233,67,90),-1)

cv2.line(image1,(centerx,centery),(centerx1,centery1),(22,222,22),5)



plt.figure(figsize=(12,8))
plt.imshow(image1)
plt.title("WOW IMAGE")

plt.axis("off")
plt.show()

