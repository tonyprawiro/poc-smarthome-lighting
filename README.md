# poc-smarthome-lighting

Proof of concept of synchronizing smart LED Bulb color with screen average color

# Problem

I want to be able to synchronize the color of my smart LED bulb to what my monitor is showing. E.g if my monitor is displaying a majority blue-colored picture, I want my LED bulb color to turn blue-ish.

# Assets

Use Pillow (Python Image Library) to get average color of the picture currently displayed in my monitor

```
$ pip install pillow
```

Use TP-Link's local network API to manipulate the color and brightness of the LED bulb (hue, saturation, & brightness)

Loop the script and refresh the color in intervals

Usage:

```
$ python main.py <refresh_rate_in_second> <monitor_number> <IP_address_of_smart_led_bulb>
```

example:

```
$ python main.py 1 2 192.168.1.111
```

