import cv2

video = cv2.VideoCapture(r"C:\Users\Shagun\Desktop\Srishti photos\avyu\VID-20240127-WA0002.mp4")
while True:
    status, frame = video.read()
    # print(status, frame)
    if not status:
        break
    cv2.imshow("video frame", frame)
    if cv2.waitKey(1) == 27:
        break
video.release()
cv2.destroyAllWindows()