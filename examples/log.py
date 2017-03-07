import time
from envirophat import light, motion, weather, leds

out = open('enviro.log', 'w')
out.write('light\trgb\tmotion\theading\ttemp\tpress\n')

# def write(line):
#     sys.stdout.write(line)
#     sys.stdout.flush()

try:
    while True:
        lux = light.light()
        leds.on()
        rgb = str(light.rgb())[1:-1].replace(' ', '')
        time.sleep(1)
        leds.off()
        acc = str(motion.accelerometer())[1:-1].replace(' ', '')
        heading = motion.heading()
        temp = weather.temperature()
        press = weather.pressure()
        out.write('%f\t%s\t%s\t%f\t%f\t%f\n' % (lux, rgb, acc, heading, temp, press))
        time.sleep(1)
# write("--- Enviro pHAT Monitoring ---")
#         rgb = light.rgb()
#         analog_values = analog.read_all()

#         output = """
# Temp: {t}c
# Pressure: {p}Pa
# Light: {c}
# RGB: {r}, {g}, {b}
# Heading: {h}
# Analog: 0: {a0}, 1: {a1}, 2: {a2}, 3: {a3}
# """.format(
#         t = round(weather.temperature(),2),
#         p = round(weather.pressure(),2),
#         c = light.light(),
#         r = rgb[0],
#         g = rgb[1],
#         b = rgb[2],
#         h = motion.heading(),
#         a0 = analog_values[0],
#         a1 = analog_values[1],
#         a2 = analog_values[2],
#         a3 = analog_values[3]
#     )
#         output = output.replace("\n","\n\033[K")
#         write(output)
#         lines = len(output.split("\n"))
#         write("\033[{}A".format(lines - 1))

#         time.sleep(1)

except KeyboardInterrupt:
    leds.off()
    out.close()
