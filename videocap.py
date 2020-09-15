import cv2,time

video= cv2.VideoCapture("C://Users//Adwit//Desktop//Test2.mp4")

'''a=1
while True:

    a=a+1    #this is a counter for how many frames are captured/shown
    check,frame=video.read()        #this reads the cideo capture and returns check= true and a numpyarray to frame of every frame(image): many images make a video
    print(check)
    cv2.imshow("capturing",frame)  #makes a window to show the capture
    key= cv2.waitKey(0)            #every 1 milliseconf it switches to a new frame , waitKey(0)is used to close the current frame at the moment user presses a key
    if  key==ord('q') :
        break


print(a)
cv2.destroyWindow()'''

first_frame=None
a=0
while True:
    a=a+1
    check,frame=video.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)       #to make the frame captured gray
    gray=cv2.GaussianBlur(gray,(21,21),0)   #to make the motion detection  more efficient

    if first_frame is None :               #to capture the first frame
        first_frame= gray
        continue



    delta_frame=cv2.absdiff(first_frame,gray)         #to find the difference between the first frame captured by first_frame and its subsequent frames

    thresh_delta= cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]     #this line and the next provides a threshold, it will convert the difference value of less than 30 to black, if more the it is white
    thresh_delta=cv2.dilate(thresh_delta,None,iterations=0)

    ( cnts, _)=cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)    #this is to create a contour around areas of same intensity such as white areas, it returns a list of the contours of the area.
    for contour in cnts:
        if cv2.contourArea(contour) < 20000:
            continue

        #cv2.drawContours(frame,contour,-1,(255,0,0),3)
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

    cv2.imshow('frame',frame)

    key = cv2.waitKey(1)  # every 1 millisecond it switches to a new frame , waitKey(0)is used to close the current frame at the moment user presses a key
    if key == ord('q') :
        break
print(a)
cv2.destroyWindow()
