import cv2
import numpy as np
import time

videoCapture = cv2.VideoCapture(0)
#videoCapture.open("result.avi") 

fx = 417.849912
cx = 319.853329
fy = 419.800817
cy = 247.977768

k1, k2, p1, p2, k3 = -0.328977, 0.110309, -0.003576, -0.002456, 0.000000

R_C_U = np.array([[fx, 0.000000, cx], [0.000000, fy, cy], [0, 0, 1]])
R_U_C = np.linalg.inv(R_C_U)
k = np.array([
    [fx, 0, cx],
    [0, fy, cy],
    [0, 0, 1]
])


d = np.array([
    k1, k2, p1, p2, k3
])


mapx, mapy = cv2.initUndistortRectifyMap(k, d, None, k, (640, 480), 5)
def undistort(img):
    return cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

fps = videoCapture.get(cv2.CAP_PROP_FPS)
frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)

print("fps:",fps, "frame:",frames)
number = 0
camera = True
while camera:
  #time.sleep(1)
 
  ret, frame = videoCapture.read()
  frame = undistort(frame)
  frame = cv2.flip(frame, -1)
  frame = cv2.flip(frame, 1)
  cv2.imshow("sa", frame)
  key = cv2.waitKey(1)
  #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  if key == 99: 
    number+=1
    cv2.imwrite('./image_muti/0trainmuti_%d.jpg' % number, frame)


