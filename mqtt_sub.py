__author__ = "Fairus Atoir"
__copyright__ = "Copyright 2021, Just Have Fun Project"
__license__ = "WTFPL"
__version__ = "1.0"
__email__ = "fairusatoir98@gmail.com"
__status__ = "Development when I want it"

import argparse  # https://pymotw.com/2/argparse/
import textwrap  # beautify interface
import sys

import paho.mqtt.client as mqtt  # https://pypi.org/project/paho-mqtt/

'''
    MQTT Setting
'''


def on_message(client, userdata, msg):
    '''
        Show Value of Data Sended
    '''
    value = msg.payload.decode("utf-8")
    print(value)


def on_connect(client, userdata, flags, rc):
    '''
        Check Status Connect with broker MQTT
    '''
    if rc == 0:
        sys.stdout.write("\r | Broker connect")
    else:
        sys.stdout.write("\r | Failed Connect Broker")
    print()


def mqtt_main(client):
    client.on_connect = on_connect
    if (argument.show):
        print(" | Show Message Publisher")
        client.on_message = on_message

    sys.stdout.write("\r | connecting")
    sys.stdout.flush()

    client.connect(argument.host, argument.port, 60)  # connect to broker
    client.subscribe(argument.topic)
    return client


'''
    Argparse Setting
'''


def optional_argument(parser):
    '''
        Optional Argument
    '''

    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='Show this help message and exit.')

    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 1.0', help="Show program's version number and exit.")

    parser.add_argument('-s', '--show', action='store_true',
                        dest='show',
                        help="Show data from publisher",)
    return parser


def required_argument(parser):
    '''
        Required Argument
    '''
    required_parse = parser.add_argument_group('Required')

    required_parse.add_argument('-ip', action='store', dest='host',
                                help='Set a Host Broker MQTT',
                                required=True)

    required_parse.add_argument('-p', action='store', dest='port',
                                default=1883, type=int,
                                help='Set a Port Broker MQTT (default: 1883)')

    required_parse.add_argument('-t', action='store', dest='topic',
                                help='Set a Topic MQTT',
                                required=True)
    return parser


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='mqtt_sub',
                                     description=textwrap.dedent('''
                                    Python-MQTT CLI Tools
                                    ex:
                                    - python3 mqtt_sub.py -ip broker.emqx.io -t same/topic
                                    '''),
                                     epilog=textwrap.dedent('''
                                     see  for more information.
                                    '''),
                                     add_help=False,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser = optional_argument(parser)
    parser = required_argument(parser)
    argument = parser.parse_args()

    '''
        Loop Handling
    '''
    print(" | Host Broker\t:", argument.host)
    print(" | Port Broker\t:", argument.port)
    print(" | Topic Broker\t:", argument.topic)

    try:
        client = mqtt.Client()  # create new instance
        client = mqtt_main(client)
        client.loop_forever()
    except KeyboardInterrupt:
        print("")
        print(" | See you next time!")
