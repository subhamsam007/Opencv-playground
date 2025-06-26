import cv2

cap = cv2.VideoCapture(0)

while True:
    sam, screen = cap.read()
    if not sam:
        break

    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(screen, (0, 0), (width, height), (255, 0, 0), 5)

    img = cv2.rectangle(img, (100, 100), (200, 200), (0, 255, 0), 3)

    # Draw a red filled circle
    img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

    # Add white text
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'OpenCV', (10, 500), font, 2, (255, 255, 255), 2, cv2.LINE_AA)


    flipped_horizontally = cv2.flip(img, 1)

    cv2.imshow('my livevideo', flipped_horizontally)

    if cv2.waitKey(1) == ord('x') or cv2.getWindowProperty('my livevideo', cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
