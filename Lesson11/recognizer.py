import cv2
from cv2 import Mat
from PIL import Image

class Recognizer:
    def __init__(self, path: str):
        self.Path: str = path
        self.Image: Mat = self.ReadImg(self.Path)
        self.MultiScale = list()
    def ReadImg(self, path: str):
        return cv2.imread(path)
    def ShowImg(self, wndwName: str):
        cv2.imshow(wndwName, self.Image)
        cv2.waitKey()
    def GetCoordinates(self, path: str, img: Mat):
        cascade = cv2.CascadeClassifier(path)
        return cascade.detectMultiScale(img)
    def HighLight(self, img: Mat):
        for (x, y, width, height) in self.MultiScale:
            cv2.rectangle(img, (x, y), (x+width, y+height), (215, 19, 19), 3)
    def PasteImg(self, maskPath: str, imgPath: str, newPath: str):
        try:
            fLayout = Image.open(imgPath)
            sLayout = Image.open(maskPath)
            fLayoutConverted = fLayout.convert('RGBA')
            sLayoutConverted = sLayout.convert('RGBA')
            for (x, y, width, height) in self.MultiScale:
                sLayoutConverted = sLayoutConverted.resize((width, int(height/3)))
                fLayoutConverted.paste(sLayoutConverted, (x, int(y + height/4)))
                fLayoutConverted.save(newPath)
                return cv2.imread(newPath)
        except:
            raise


