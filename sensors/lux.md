# Adafruit TSL2561 Digital Luminosity/Lux/Light Sensor Breakout

We purchased the LUX light sensor at [Adafruit](https://www.adafruit.com/products/439?&main_page=product_info&products_id=439) for $5.95.

1. 3 to 5 VDC logic.
2. Communication over I2C.
3. Low power: 0.5mA active and 15uA in sleep mode.
4. Dynamic range (Lux): 0.1 to 40,000 Lux.
5. Both visible and infrared photodiode sensors.

Adafruit provides a [GitHub](https://github.com/adafruit/Adafruit_TSL2561) respository for this sensor for Arduino.

## Plug in the sensor

Plug jumper wires into the GND, 3V, SDA, and SCL pins on the sensor.

Connect the jumpers to the following Raspberry Pi pins: GND to pin 6, 3V jumper to pin 1, SDA to pin 3, and SCL to pin 5.

Check the I2C connection:

```
sudo i2cdetect -y 1
```

The barometer should appear at address 39:

```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- 39 -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

To control the LUX sensor we need a Python code library from Adafruit:

```
sudo pip install Adafruit_BBIO
```

Tom Callaway has developed a Python script for controlling the TSL2561 LUX sensor on GitHub. First clone his rpihacks respository:

```
# Go home

cd ~

# Clone the repository

git clone https://github.com/spotrh/rpihacks.git

```

Running the tsl2561.py script will return the luminosity with three gain settings:

```
python /home/pi/rpihacks/tsl2561-lux.py

# Example:
# LUX HIGH GAIN  0
# LUX LOW GAIN  16.7808
# LUX AUTO GAIN  139.811
```

To log LUX data over time using cron:

Create an output file for the data and note where it is (let's assume it's in the /home/pi folder for now).

```
# go home

cd ~

# Create a file with the column headers separated by tabs

echo $'Lux\tDate-time' > lux.data.txt
```

Use your favorite text editor to add the following to /etc/crontab:

```
0 * * * * pi python /home/pi/rpihacks/tsl2561-lux.py | grep AUTO | awk -v date=$(date +"\%Y-\%m-\%d_\%H:\%M:\%S") '{print $4"\t"date}' >> /home/pi/lux.data.txt
```