import cv2
import numpy as np

cv2.namedWindow('frame')
# cv2.namedWindow('foreground')
cv2.namedWindow('connectivity')
cv2.moveWindow('frame',10,200)
# cv2.moveWindow('foreground',400,200)
cv2.moveWindow('connectivity',800,200)

cap = cv2.VideoCapture(0)
GMM = cv2.createBackgroundSubtractorMOG2(history=40000,varThreshold=10)
i=0

while(1):
    contour_list=[]
    ret,frame = cap.read()
    frame = cv2.resize(frame,(700,476))
    GMM_img = GMM.apply(frame,learningRate=-1)#0不更新，1逐帧更新，-1自动更新

    img=GMM_img.copy()
    img[:,:]=0

    ret1 ,foreground = cv2.threshold(GMM_img,100,255,cv2.THRESH_BINARY)
    foreground = cv2.erode(foreground,np.ones((3,3),np.uint8))
    foreground = cv2.erode(foreground,np.ones((3,3),np.uint8))
    foreground = cv2.dilate(foreground,np.ones((8,8),np.uint8))
    foreground = cv2.morphologyEx(foreground, cv2.MORPH_OPEN, np.ones((8, 8), dtype=np.uint8))
    foreground = cv2.morphologyEx(foreground, cv2.MORPH_CLOSE, np.ones((3, 3), dtype=np.uint8))
    foreground = cv2.morphologyEx(foreground, cv2.MORPH_OPEN, np.ones((5, 5), dtype=np.uint8))
    foreground = cv2.morphologyEx(foreground, cv2.MORPH_CLOSE, np.ones((5, 5), dtype=np.uint8))
    foreground = cv2.morphologyEx(foreground, cv2.MORPH_CLOSE, np.ones((10,10),np.uint8))

    _, contours, hi = cv2.findContours(foreground, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        com = cv2.approxPolyDP(contour, 3, closed=True)
        contour_list.append(com)

    cv2.drawContours(img, contour_list, -1, (255, 255, 255), thickness=cv2.FILLED, lineType=8)

    _1, contours_1, hi_1 = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours_1:
        x,y,w,h=cv2.boundingRect(contour)
        if w*h>=500:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            if w*h>=0 and w<=frame.shape[0]/2 and h<=frame.shape[1]/2:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            else:
                w_change,h_change=np.int(w/2),np.int(h/2)
                cv2.rectangle(frame,(x,y),(x+w_change,y+h_change),(255,0,0),2)
                cv2.rectangle(frame,(x+w_change,y),(x+w_change*2,y+h_change),(255,0,0),2)
                cv2.rectangle(frame,(x,y+h_change),(x+w_change,y+h_change*2),(255,0,0),2)
                cv2.rectangle(frame,(x+w_change,y+h_change),(x+2*w_change,y+2*h_change),(255,0,0),2)

    # cv2.imwrite('E:\\myself_picture\\4\\frame\\frame%d.png'%i,frame)
    # cv2.imwrite('E:\\myself_picture\\4\\GMM\\GMM%d.png'%i,GMM_img)
    # cv2.imwrite('E:\\myself_picture\\4\\foreground\\foreground%d.png'%i,foreground)
    # cv2.imwrite('E:\\myself_picture\\4\\connect\\connect%d.png' % i, img)
    i=i+1

    cv2.imshow('frame',frame)
    cv2.imshow('foreground',foreground)
    cv2.imshow('connectivity',img)
    cv2.waitKey(10)

cap.release()
cv2.destroyAllWindows()