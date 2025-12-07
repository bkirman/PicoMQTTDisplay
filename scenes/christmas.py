from scene import Scene
from random import uniform, randint

class ChristmasScene(Scene):
    '''
    A simple animation with falling motes of red and green light. They go quite fast on the 2030.
    '''

    def sceneInit(self,LEDS):
        self.LEDS = LEDS
        self.MOTES = 40
        
        self.mote_positions = [float(uniform(0,LEDS)) for i in range(self.MOTES)]
        self.mote_speeds = [float(uniform(0.1,1.2)) for i in range(self.MOTES)]
        self.mote_colours = []
        for i in range(self.MOTES):
            if (uniform(0,1) > 0.5):
                self.mote_colours.append( (randint(40,160),0,0) )
            else:
                self.mote_colours.append( (0,randint(40,160),0) )

        print(self.mote_colours)
        return super().sceneInit(LEDS)
    
    def draw(self, display):
        display.clear()
        #display = [(0,0,0) for i in range(len(display))] #clear entire display

        for i in range(self.MOTES):
            self.mote_positions[i] += self.mote_speeds[i]
            if (self.mote_positions[i] >= self.LEDS or self.mote_positions[i] < 0):
                self.mote_positions[i] = 1.0
                self.mote_speeds[i] = float(uniform(0.1,1.2))
                if (uniform(0,1) > 0.5):
                    self.mote_colours.append( (randint(50,160),0,0) )
                else:
                    self.mote_colours.append( (0,randint(50,160),0) )

            display.set_rgb(int(self.mote_positions[i]), self.mote_colours[i][0], self.mote_colours[i][1], self.mote_colours[i][2])
            

        return super().draw(display)