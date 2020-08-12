imporsut cv2
import math
import numpy as np
from matplotlib import pyplot as plt


#Function to detect the orientation of the object by the ellipse method
#img is a binarized image (stored as a numpy array)
def detect_orientation(img):

  m00 = 0
  m01 = 0
  m10 = 0
  m11 = 0
  m02 = 0
  m20 = 0

  for i in range(img.shape[0]):
    for j in range(img.shape[1]):
      if (img[i][j] == 255):
        m00 += 1
        m01 += j
        m10 += i 
        m11 += (i) * (j)
        m02 += (j)**2
        m20 += (i)**2

  x_bar = m10 / m00
  y_bar = m01 / m00

  print("m00 : {}, m01 : {}, m10 : {}, m11 : {}, m02 : {}, m20 : {}".format(m00, m01, m10, m11, m02, m20))

  print("Barycenter is ({}, {})".format(x_bar, y_bar))

  cov = np.zeros((2,2))
  cov[0][0] = (m20 / m00) - x_bar**2
  cov[0][1] = (m11 / m00) - x_bar * y_bar
  cov[1][0] = cov[0][1]
  cov[1][1] = (m02 / m00) - y_bar**2

  theta = 0.5 * math.atan((2 * cov[0][1]) / (cov[0][0] - cov[1][1]))
  l = math.sqrt(8 * (cov[0][0] + cov[1][1] + math.sqrt(4 * (cov[0][1])**2 + (cov[0][0] - cov[1][1])**2)))
  w = math.sqrt(8 * (cov[0][0] + cov[1][1] - math.sqrt(4 * (cov[0][1])**2 + (cov[0][0] - cov[1][1])**2)))

  print("Orientation : {}, Length of major axis : {}, Length of minor axis: {}".format(math.degrees(theta), l, w))

  ellipse_float = ((x_bar, y_bar), (l, w), math.degrees(theta))
  cv2.ellipse(img, ellipse_float, (255, 255, 255), 1)
  cv2.imshow(img)
  #img = cv2.ellipse(img, (x_bar, y_bar), (l, w), theta, 0, 360, (255, 0, 0), 2.5)
  #img_plot = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  #plt.imshow(img)
  #plt.title('output')
  #plt.show()
       
img = cv2.imread('./Images/Image2.png', 0)

#Image preprocessing
#img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#plt.imshow(img1)
#plt.title('input')
#plt.xticks([]),plt.yticks([])
#plt.show()

#img_binary = np.uint8((img < 127) * 255)
_, img_binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
#print(img_binary)

#img2 = cv2.cvtColor(img_binary, cv2.COLOR_BGR2RGB)
#plt.imshow(img2)
#plt.title('Processed')
#plt.xticks([]), plt.yticks([])
#plt.show()

#Plotting the ellipse
detect_orientation(img_binary)

