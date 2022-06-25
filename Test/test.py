'''
fh = open('demo.txt', 'a') #r=read, r+ = read+write, w, w+, a=append, b=binary
for i in range(10):
    fh.write("this is line no %d\n" % (i+1))

fh.close()

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")  #discard=remove
print(fruits)

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model") #pop=remove
print(car)

import os
file = os.scandir('D:\\Python exe')
l=''
for i in file:
  try:
    f = open(i.name, 'r')
    text = f.read()
    l = l + text
  except:
    print('I cannot Open', i.name)
print("[",l,"]")
'''

# arr=['apple','banana','cherry']

# for i in range (len(arr)):
#   arr[i]="Eat "+arr[i]
#   print(arr[i])
# else:
#   print("Finally")
# print(arr)





######################## READ IMAGE ############################
# import cv2
# # LOAD AN IMAGE USING 'IMREAD'
# img = cv2.imread("Resources/lena.png")
# # DISPLAY
# cv2.imshow("Lena Soderberg",img)
# cv2.waitKey(0)

######################### READ VIDEO #############################
# import cv2
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture("Resources/testVideo.mp4")
# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
######################### READ WEBCAM  ############################
import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break