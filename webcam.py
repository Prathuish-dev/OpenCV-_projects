import cv2

stream= cv2.VideoCapture(0)

if not stream.isOpened():
    print("No stream :(")
    exit()
fps= stream.get(cv2.CAP_PROP_FPS)
width = int(stream.get(3))
height = int(stream.get(4))

output = cv2.VideoWriter("assets/4_stream.mp4",
                         cv2.VideoWriter_fourcc('m','p','4','v'),
                         fps=fps,frameSize=(width, height))    

while(True):
    ret, frame = stream.read()
    if not ret:
        print("No more stream :(")
        break
    frame= cv2.resize(frame, (width,height))
    output.write(frame)    
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) == ord('q'):
        break

stream.release()
cv2.destroyAllWindows #!