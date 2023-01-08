import cv2
# instance of video capture

cap=cv2.VideoCapture(0)
opened=cap.isOpened()

width =cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps=cap.get(cv2.CAP_PROP_FPS)
print("height:{},width :{},fps:{}".format(int(height),int(width),fps))
# four cc

fourcc=cv2.VideoWriter_fourcc(*'MJPG')
# video writer


out=cv2.VideoWriter('video.avi',fourcc,fps,(int(width),int(height)))
if opened:
    while cap.isOpened():
        ret,frame=cap.read()
        if(ret == True):
            cv2.imshow('winname',frame)
            out.write(frame)
            if cv2.waitKey(2)==27:
                break
out.release()
cap.release()
cv2.destroyAllWindows()




