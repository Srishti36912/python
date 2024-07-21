import cv2

video = cv2.VideoCapture(r"C:\Users\Shagun\Desktop\Srishti photos\avyu\VID-20240127-WA0002.mp4")

while True:
    status, frame = video.read()
    # print(status, frame)
    if not status:
        break
    # make changes from this line
    newframe = frame * 10
    bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow("video frame", frame)
    cv2.imshow("new video frame", newframe)
    cv2.imshow("b/w", bw)
    cv2.imshow("rgb", rgb)
    if cv2.waitKey(1) == 27:
        break
video.release()
cv2.destroyAllWindows()