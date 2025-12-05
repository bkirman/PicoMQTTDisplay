from pimoroni import RGBLED, Button
import plasma
import time
from scenes.loading import LoadingScene
from scenes.teatime import TeatimeScene
from scenes.rainbow import RainbowScene
from scenes.snow import SnowScene
from scene import Scene
import wifi
import mqtt_settings
from lib.umqtt import simple
from lib.uhome import uhome

FPS = 60 
NUM_LEDS = 300
BRIGHTNESS = 0.3

# set up the Pico W's onboard LED
#pico_led = Pin('LED', Pin.OUT)
led = RGBLED("LED_R", "LED_G", "LED_B")
led.set_rgb(0, 0, 0)
button_a = Button("BUTTON_A", repeat_time=0)

# set up the WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(NUM_LEDS, color_order=plasma.COLOR_ORDER_GRB)
led_strip.clear()

# start updating the LED strip
led_strip.start()

# Set animation scene
scene = LoadingScene()
scene.sceneInit(NUM_LEDS)

def changeMode(data):
    global scene
    global led_strip
    print("CHANGING MODE! to " + str(data))
    if(int(data) == 0):
        print("Off")
        scene = Scene()
        led_strip.clear()
        return
    if(int(data) == 1):
        print("Loading Scene")
        scene = LoadingScene()
        scene.sceneInit(NUM_LEDS)
        return
    if(int(data) == 2):
        print("Teatime Scene")
        scene = TeatimeScene()
        scene.sceneInit(NUM_LEDS)
        return
    if(int(data)==3):
        print("Rainbow Scene")
        scene = RainbowScene()
        scene.sceneInit(NUM_LEDS)
        return
    if(int(data)==4):
        print("Snow Scene")
        scene = SnowScene()
        scene.sceneInit(NUM_LEDS)
        return


# Listen for MQTT messages
wifi.connect()
print("wifi connected")
device = uhome.Device('pico_300')
mqttc = simple.MQTTClient(device.id, mqtt_settings.broker,user=mqtt_settings.user,password=mqtt_settings.password,keepalive=7600)
device.connect(mqttc)
print("mqtt connected")

# Set up functions
remote_change = uhome.Number(device, 'Change Mode', entity_category="config")
remote_change.set_action(changeMode)

device.discover_all()

while True:
    scene.draw(led_strip)
    #new_pixels = scene.draw(pixels)
    #for i in range(len(new_pixels)): #only change updated pixels - you might instead do some smoothing or animated shenanigans here
    #    print(str(new_pixels[i]) + " : "+ str(pixels[i]))
    #    if new_pixels[i] != pixels[i]:
    #        
    #        led_strip.set_rgb(i, new_pixels[i][0],new_pixels[i][1],new_pixels[i][2])
    #pixels = new_pixels
    
    device.loop()
    time.sleep(1.0 / FPS)
