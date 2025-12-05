from scene import Scene

class TeatimeScene(Scene):

    def sceneInit(self,LEDS):
        self.LEDS = LEDS
        self.position = [10,9,8,7,6,5]
        
        return super().sceneInit(LEDS)
    
    # a shooting red line
    def draw(self, display):
        display.clear()
        #display = [(0,0,0) for i in range(len(display))] #clear entire display

        for i in range(len(self.position)):
            mod = max(120 - (15*i),40)
            display.set_rgb(self.position[i],mod,0,0)
            self.position[i] = (self.position[i]+1) % self.LEDS
        

        return super().draw(display)