# Streamer Home Invader

This is a small personnal project aimed at animating LEDs strips according to my Twitch channel events and viewers interactions. It is made of:
- the code in here ;
- short AWS Lambda python function as an API entrypoint for event subscriptions ;
- subscription script (not included yet) ;
- simple electronic circuit (3 NPN transistors and 3 capacitors and the led strips) ;
- a Raspberry Pi ;

# Features

- the three colors are independant, each in its own thread ;
- barely efficient resource-wise (10-15% CPU at 1 MHz base clock on RasPi for 3 colors, which way ) ;
- rather simple animation runs made of atomic effects (fade in/out, blinking, breathing, wait, etc.) ;
- possibility to manage multiple strips (up to three strips on RasPi 3 with 9 GPIO pins and 620Ohms base resistor to stay within the 50mA max output of the Pi) ;

# Disclaimer

As it is a personnal project, I do not intend to work on abstracting the code to fit various usages (I would rather rewrite it in Elixir). If you bump into this and may need it, simply send a request and I'll check on it.
