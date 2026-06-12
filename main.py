import cv2
import math

from hand_tracker import HandTracker
from image_controller import ImageController

cap = cv2.VideoCapture(0)

tracker = HandTracker()

controller = ImageController("image.jpg")

prev_distance = None

while True:

    success, frame = cap.read()

    frame = cv2.flip(frame, 1)

    points = tracker.get_landmarks(frame)

    if points:

        thumb = points[4]
        index = points[8]

        distance = math.hypot(
            thumb[0] - index[0],
            thumb[1] - index[1]
        )

        if prev_distance is not None:

            if distance > prev_distance + 5:
                controller.zoom(0.03)

            elif distance < prev_distance - 5:
                controller.zoom(-0.03)

        prev_distance = distance

    image = controller.get_image()

    cv2.imshow("Camera", frame)

    cv2.imshow("Image Viewer", image)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()