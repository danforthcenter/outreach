# Adafruit MPL3115A2 - I2C Barometric Pressure/Altitude/Temperature Sensor

We purchased the barometric pressure sensor at [Adafruit](https://www.adafruit.com/products/1893?&main_page=product_info&products_id=1893) for $9.95.

1. 3 to 5.5 VDC logic.
2. Pressure range from 50-110 kPa (up to 10 km altitude).
3. 1.5 Pa per 0.3 m altitude resolution.
4. Communication over I2C.
5. No calibration reading and calculating required.
6. Temperature sensor with ±1°C typical accuracy (up to ±3°C max).

Adafruit provides a [GitHub](https://github.com/adafruit/Adafruit_MPL3115A2_Library) respository for this sensor for Arduino.

[Ciaduck](http://ciaduck.blogspot.com/2014/12/mpl3115a2-sensor-with-raspberry-pi.html) has a tutorial for getting the sensor to work with Raspberry Pi. Below are the steps we used from Ciaduck to work with the sensor.

The Raspberry Pi I2C communication method needs to be modified to be compatible with Arduino:

```
# Switch to the root user

sudo su

# Change the combined parameter for the i2c_bcm2708 kernel module to true

echo -n 1 > /sys/module/i2c_bcm2708/parameters/combined

# Exit the root account

exit
```

## Plug in the sensor

Plug jumper wires into the GND, 3V, SDA, and SCL pins on the sensor.

Connect the jumpers to the following Raspberry Pi pins: GND to pin 6, 3V jumper to pin 1, SDA to pin 3, and SCL to pin 5.

Check the I2C connection:

```
sudo i2cdetect -y 1
```

The barometer should appear at address 60:

```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: 60 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

Use the script modified from Ciaduck to get data from the sensor:

```
python /home/pi/outreach/raspi_teachers_2015/sensors/barometer.py

# Example output:
#Pressure (Pa)	Temperature (C)	Temperature (F)	Date-time

#99633.75	24.1875	75.5375	2015-07-15 22:16:52
```

To log barometer data over time using cron:

Create an output file for the data and note where it is (let's assume it's in the /home/pi folder for now).

```
# go home

cd ~

# Create a file with the column headers separated by tabs

echo $'Pressure (Pa)\tTemperature (C)\tTemperature (F)\tDate-time' > barometer.data.txt

# Add the script to cron

sudo echo '0 * * * * pi python /home/pi/outreach/raspi_teachers_2015/sensors/barometer.py | tail -1 >> /home/pi/barometer.data.txt' >> /etc/crontab
```