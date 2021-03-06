import numoy as np 
import cv2
cap = cv2.VideoCapture(0)
 """to give black image cmd-> np.zeroes([hieght  , width ,  3 ] , data type)"""
#cap=np.zeroes([512  , 512 , 3 ] , np.uint8)

print(cap.isOpened())
while(cap.isOpened()):
    ret , frame = cap.read()
    if ret ==True:
       # """ draw line (frame  , starting coordinates , ending coordinates , BGR color code , thickness) """
     frame  = cv2.line(frame, (0, 0), (640, 0), (0, 0, 255), 5)

    #""" draw rectangle (frame  , left most coordinates , right most  coordinates , BGR color code , thickness)"""
     frame = cv2.rectangle(frame , (10,10) , ( 630,470) , (0 , 255 , 20) ,5 )

       # if you want to fill rectangle or circle you can use -1 in place of thickness

    #""" draw arrowed-line (frame  , starting coordinates , ending coordinates , BGR color code , thickness)"""
     frame  = cv2.arrowedLine(frame , (320, 240), ( 630 , 470), (255 , 255 , 0), 5)

     #""" draw circle (frame  , center  coordinates , radius  , BGR color code , thickness)"""
     frame = cv2.circle(frame , (320,240) , (240) , (0,0,255),-1)
     font = cv2.FONT_HERSHEY_SIMPLEX # font style
	# """to out text to in image cmd-> cv2.putText(image  , ('text') , (starting cordinates),font,font size,(color),thickness,line type)""" 
	frame = cv2.putText(frame  , ('deepanshu ') , (10,150) ,font ,  3, (200,251,32), 5 , cv2.LINE_AA)
	   
        
     print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
     print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
     cv2.imshow('frame' , frame)
     if cv2.waitKey(1)& 0xFF  == ord('q'):
        break
    else:
        break
cap.release()
cv2.destroyAllWindows()
