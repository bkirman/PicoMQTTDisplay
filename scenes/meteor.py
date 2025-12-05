from scene import Scene
from random import uniform
from math import sin

class MeteorScene(Scene):
    # inspired by https://www.tweaking4all.com/hardware/arduino/adruino-led-strip-effects/

    DECAY = 10 # how quickly the meteor trails fade - lower = longer trails
    SIZE = 10  # how big the meteor is
    REPEAT = True  # whether the meteor restarts when it reaches the end


    def sceneInit(self,LEDS):
        self.LEDS = LEDS
        self.frame = 0
        self.last_leds = [[0] * 3 for i in range(LEDS)]
        self.meteor_colour = [160, 50, 160]  # white meteor
        self.meteor_colour_variation = 30  # how much to vary each RGB channel randomly
        self.meteor_position = 0
        
        return super().sceneInit(LEDS)
    
    
    def draw(self, display):
        self.frame = (self.frame + 1) % self.LEDS
        
        for i in range(self.LEDS):
            if(uniform(0,1) < 0.3):
                # fade all LEDs a bit
                self.last_leds[i][0] = max(self.last_leds[i][0] - self.DECAY, 0)
                self.last_leds[i][1] = max(self.last_leds[i][1] - self.DECAY, 0)
                self.last_leds[i][2] = max(self.last_leds[i][2] - self.DECAY, 0)

            display.set_rgb(i, self.last_leds[i][0], self.last_leds[i][1], self.last_leds[i][2])

        if (self.meteor_position >= 0) and (self.meteor_position < self.LEDS):
            # draw meteor
            for j in range(self.SIZE):
                if (self.meteor_position - j >= 0) and (self.meteor_position - j < self.LEDS):
                    varied_colour = [
                        max(min(self.meteor_colour[0] + int(uniform(-self.meteor_colour_variation, self.meteor_colour_variation)), 200), 0),
                        max(min(self.meteor_colour[1] + int(uniform(-self.meteor_colour_variation, self.meteor_colour_variation)), 200), 0),
                        max(min(self.meteor_colour[2] + int(uniform(-self.meteor_colour_variation, self.meteor_colour_variation)), 200), 0)
                    ]


                    display.set_rgb(self.meteor_position - j,
                                    varied_colour[0],
                                    varied_colour[1],
                                    varied_colour[2])
                    self.last_leds[self.meteor_position - j][0] = varied_colour[0]
                    self.last_leds[self.meteor_position - j][1] = varied_colour[1]
                    self.last_leds[self.meteor_position - j][2] = varied_colour[2]
            self.meteor_position += 1

        if self.meteor_position >= self.LEDS:
            if self.REPEAT:
                self.meteor_position = 0

        return super().draw(display)