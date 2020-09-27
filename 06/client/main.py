#!/usr/bin/env python3

import argparse

from client import Client

if __name__ == "__main__":
    # Setup parser
    parser = argparse.ArgumentParser(description='Create a RMI client')

    parser.add_argument('--grade', '-g', nargs=1, type=str,
                        help='Grade service URI', required=True)
    parser.add_argument('--absences', '-a', nargs=1, type=str,
                        help='Absences service URI', required=True)
    parser.add_argument('--course', '-c', nargs=1, type=str,
                        help='Course service URI', required=True)

    args = parser.parse_args()
    client = Client(args.grade[0], args.absences[0], args.course[0])
    client.start()
