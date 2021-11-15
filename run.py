#!/usr/bin/env python

import ipaddress
import sys

from duckduckgoose import DuckDuckGoose

def main(argv):
    if len(argv) < 1:
        print('usage: ./run.py [host IP] [seed IP]')
        sys.exit()

    seed = None

    try:
        myip = format(ipaddress.ip_address(argv[0]))
    except ValueError as e:
        print(e)
        sys.exit()
    try:
        seed = format(ipaddress.ip_address(argv[1]))
    except ValueError as e:
        print(e)
        sys.exit()
    except IndexError:
        pass

    duckDuckGoose = DuckDuckGoose(myip, seed)

if __name__ == "__main__":
    main(sys.argv[1:])
