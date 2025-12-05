from scene import Scene

class LoadingScene(Scene):

    def sceneInit(self,LEDS):
        self.LEDS = LEDS
        self.position = [10,9,8,7,6,5]
        
        return super().sceneInit(LEDS)
    
    # a shooting blue line
    def draw(self, display):
        display.clear()
        #display = [(0,0,0) for i in range(len(display))] #clear entire display

        for i in range(len(self.position)):
            mod = max(120 - (15*i),40)
            #display[self.position[i]] = (0,0,mod)
            display.set_rgb(self.position[i],0,0,mod)
            self.position[i] = (self.position[i]+1) % self.LEDS
        

        return super().draw(display)