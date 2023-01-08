import cv2

# video capture instance
cap=cv2.VideoCapture('video.avi')

# video properties

frames=cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps=cap.get(cv2.CAP_PROP_FPS)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)

fourcc=cv2.VideoWriter_fourcc(*'MJPG')
out=cv2.VideoWriter('reversed.avi',fourcc,fps,(int(width),int(height)))

# reversal process
frame_index=frames-1

# checking if instance is ready

if cap.isOpened():
    # reading till end
    while frame_index!= 0:
        # set current frame to the last frame
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame_index)
        ret,frame = cap.read()

        # write reverse video
        out.write(frame)
        frame_index = frame_index - 1
        if frame_index % 100 == 0:
            print(frame_index)


out.release()
cap.release()
cv2.destroyAllWindows()