README
======

What's Pi-Stop?
---------------
Pi-Stop is an educational pistop traffic light add-on for Raspberry Pi. The Pi-Stop was designed in partnership between [4Tronix.co.uk](http://4Tronix.co.uk) and [PiHardware.com](http://pihardware.com).

What do those scripts do?
-------------------------
They use Pi-Stop as a CPU load indicator:

+ Green light: CPU load bellow 33%
+ Orange light: CPU load between 33% and 66%
+ Red light: CPU load over 66%

Where should I plug the Pi-Stop in my Raspberry Pi?
---------------------------------------------------
Pi-Stop has 4 posible placements in the GPIO port. Those scripts use the 14, 15 and 18 GPIO. This means Pi-Stop should be placed in pins 6, 8, 10 and 12 with the lights facing the same direction as the composite RCA connector.

If you want to use another position just change the values of the G, A and R variables.

What's the difference between ``piStopCpuLoad.py`` and ``piStopCpuLoadPwm.py``?
-------------------------------------------------------------------------------
+ piStopCpuLoad.py uses RPi.GPIO to interface with the GPIO port.
+ piStopCpuLoadPwm.py uses RPIO library and a PWM approach to dim the LEDs. You'll have to install RPIO to use this script.

How do I install RPIO?
----------------------
There are several ways to do this as you can see in it's [official site](http://pythonhosted.org/RPIO/). This is how I did it:

    $ sudo apt-get -y install python-setuptools
    $ sudo easy_install -U RPIO

How do I run the scripts?
-------------------------
Just as any Python script but you'll have do it as root (or use sudo) because they interface the GPIO port directly:

    $ sudo python piStopCpuLoad.py
    $ sudo python piStopCpuLoadPwm.py

Troubleshooting
---------------
Q: I get this error when running both scripts:

    RuntimeError: No access to /dev/mem. Try running as root!

A: You have to run python as root because it directly interfaces the GPIO port.

Q: How do I stop the scripts?

A: Just press CONTROL+C

