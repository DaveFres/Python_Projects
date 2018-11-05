#!/usr/bin/env python3

import argparse
import os
import tempfile
import json


my_dict = dict()

parser = argparse.ArgumentParser(description='key-value storage')

parser.add_argument('--key', help='Key of key-value storage')
parser.add_argument('--value', help='Value of key-value storage')

args = parser.parse_args()


def write_in_dict(my_dict, key, val):
    if key in my_dict:
        if isinstance(my_dict[key], list):
            my_dict[key].append(val)
        else:
            my_dict[key] = [my_dict[key], val]
    else:
        my_dict[key] = val


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if os.path.isfile(storage_path):

    if args.value:
        with open(storage_path, 'r') as f:
            my_dict = json.load(f)
            write_in_dict(my_dict, args.key, args.value)

        with open(storage_path, 'w') as f:
            json.dump(my_dict, f)
    else:

        with open(storage_path, 'r') as f:
            my_dict = json.load(f)

            if my_dict[args.key] is not list and not str:
                print(', '.join(my_dict[args.key]))
            else:

                print(my_dict[args.key])


else:

    if args.value is None:

        print(None)

    else:
        my_dict = dict()

        with open(storage_path, 'w') as f:
            json.dump(my_dict, f)

        with open(storage_path, 'r') as f:
            my_dict = json.load(f)
            write_in_dict(my_dict, args.key, args.value)

        with open(storage_path, 'w') as f:
            json.dump(my_dict, f)



