from scene import Scene
from random import uniform
# How much snow? [bigger number = more snowflakes]
SNOW_INTENSITY = 0.0002

# Change RGB colours here (RGB colour picker: https://g.co/kgs/k2Egjk )
BACKGROUND_COLOUR = [20, 22, 22]  # dim blue
SNOW_COLOUR = [200, 200, 200]  # bluish white

# how quickly current colour changes to target colour [1 - 255]
FADE_UP_SPEED = 255  # abrupt change for a snowflake
FADE_DOWN_SPEED = 1

class SnowScene(Scene):
    def move_to_target(self,n):
        # nudge our current colours closer to the target colours
        for i in range(n):
            for c in range(3):  # 3 times, for R, G & B channels
                if self.current_leds[i][c] < self.target_leds[i][c]:
                    self.current_leds[i][c] = min(self.current_leds[i][c] + FADE_UP_SPEED, self.target_leds[i][c])  # increase current, up to a maximum of target
                elif self.current_leds[i][c] > self.target_leds[i][c]:
                    self.current_leds[i][c] = max(self.current_leds[i][c] - FADE_DOWN_SPEED, self.target_leds[i][c])  # reduce current, down to a minimum of target


    def sceneInit(self,LEDS):
        self.LEDS = LEDS
        self.current_leds = [[0] * 3 for i in range(LEDS)]
        # Create a list of [r, g, b] values that will hold target LED colours, to move towards
        self.target_leds = [[0] * 3 for i in range(LEDS)]
        return super().sceneInit(LEDS)
    
    def draw(self, display):

        for i in range(self.LEDS):
            # randomly add snow
            if SNOW_INTENSITY > uniform(0, 1):
                # set a target to start a snowflake
                self.target_leds[i] = SNOW_COLOUR
            # slowly reset snowflake to background
            if self.current_leds[i] == self.target_leds[i]:
                self.target_leds[i] = BACKGROUND_COLOUR
        self.move_to_target(self.LEDS)   # nudge our current colours closer to the target colours

        for i in range(self.LEDS):
            display.set_rgb(i, self.current_leds[i][0], self.current_leds[i][1], self.current_leds[i][2])

        
        return display