import cv2
import numpy as np

stream= cv2.VideoCapture("assets/face.mp4")

if not stream.isOpened():
    print("No stream :(")
    exit()

num_frames = stream.get(cv2.CAP_PROP_FRAME_COUNT)
frame_ids=np.random.uniform(size=20)*num_frames

frames=[]
for fid in frame_ids:
    stream.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = stream.read()
    if not ret:
        print("some thing went wrong :(")
        exit()
    frames.append(frame)

median = np.median(frames,axis=0).astype(np.uint8) 
median = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)


fps= stream.get(cv2.CAP_PROP_FPS)
width = int(stream.get(3))
height = int(stream.get(4)) 

output = cv2.VideoWriter("assets/no_back_ground.mp4",
                         cv2.VideoWriter_fourcc('m','p','4','v'),
                         fps=fps,frameSize=(width, height))    

stream.set(cv2.CAP_PROP_POS_FRAMES,0)
while(True):
    ret, frame = stream.read()
    if not ret:
        print("No more stream :(")
        break

    frame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    dif_frame= cv2.absdiff(median, frame)
    threshold, diff = cv2.threshold(dif_frame, 30,255,
                                    cv2.THRESH_BINARY)
    frame= cv2.resize(frame, (width,height))
    output.write(frame)    
    cv2.imshow("Video!", dif_frame)
    cv2.waitKey(20)
    if cv2.waitKey(1) == ord('q'):
        break

stream.release()
cv2.destroyAllWindows 