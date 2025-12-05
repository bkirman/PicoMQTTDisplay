from scene import Scene
from math import sin

class TeatimeScene(Scene):

    REVERSE = False
    FACTOR = 0.5 # how long the trails are - lower = longer

    def sceneInit(self,LEDS):
        self.LEDS = LEDS
        self.position = [10,9,8,7,6,5]
        self.frame = 0
        return super().sceneInit(LEDS)
    
    # a shooting red line
    def draw(self, display):
        self.frame = (self.frame + (1 if self.REVERSE else -1)) % self.LEDS
        for i in range(self.LEDS):
            v = max([(sin((i+self.frame)*self.FACTOR) * 127 + 128) / 255,0])

            display.set_rgb(i, int(v * 100), 0,0)

        return super().draw(display)