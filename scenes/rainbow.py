from scene import Scene

class RainbowScene(Scene):

    def sceneInit(self,LEDS):
        self.LEDS = LEDS
        self.frame = 0
        
        return super().sceneInit(LEDS)
    
    def draw(self, display):
        
        for i in range(self.LEDS):
            hue = float(i) / self.LEDS
            offset = float(self.frame/500.0) # lower = faster
            display.set_hsv(i, (hue + offset) % 1.0, 1.0, 0.3)
        
        self.frame = (self.frame+1) % 1000
        return display