from color import Color
from box import Box
class ColorBox(Box, Color):
    def __init__(self, height:float, width:float, colorValue:str):
        super().__init__(height, width)
        Color.__init__(self, colorValue)
    def __str__(self):
        return (f"Width: {self.Width}\n"
                f"Height: {self.Height}\n"
                f"Color: {self.ColorValue}")