import cv2

class ImageController:

    def __init__(self, path):

        self.image = cv2.imread(path)

        self.scale = 1.0

    def zoom(self, value):

        self.scale += value

        if self.scale < 0.3:
            self.scale = 0.3

        if self.scale > 3:
            self.scale = 3

    def get_image(self):

        return cv2.resize(
            self.image,
            None,
            fx=self.scale,
            fy=self.scale
        )