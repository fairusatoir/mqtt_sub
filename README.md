# MQTT Python Subscriber

MQTT Subscriber Command line interface Tools with Python 

## Description

This code used the [Eclipse Paho MQTT Python client library](https://pypi.org/project/paho-mqtt/), which implements versions 5.0, 3.1.1, and 3.1 of the MQTT protocol  as the base of the code.

This code provides a minimal use of Eclipse Paho MQTT Python client library with CLI only as Subscriber

## Getting Started

### Dependencies

* Python 3.8.8

### Installing

* install paho-mqtt 1.5.1

### Executing program

* Open Python command prompt
* Exce code
```bash
python3 mqtt_sub.py -ip broker.emqx.io -t same/topic
```
or
```bash
python mqtt_sub.py -ip broker.emqx.io -t same/topic
```

## Help

In Python command prompt launch:
```bash
python3 mqtt_sub.py -h
```
or
```bash
python mqtt_sub.py -h
```

## Authors

Contributors names and contact info

[@zuhairatoir](https://twitter.com/zuhairatoir)

## Version History

* Comming Soon - 
    * Various bug fixes and optimizations
    * Added option to save data to txt file
* 1.0
    * Initial Release

## License

This project is licensed under the MIT LICENSE - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [Eclipse paho](https://www.eclipse.org/paho/index.php?page=clients/python/index.php)
