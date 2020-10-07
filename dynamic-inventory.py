#!/usr/bin/python3
import sys
import os 
import argparse
import json
paser = argparse.Argumentparse()
parser.addargument('--list',action='store_true',help='creates dynamic inventory of all vars')
parser.addagrument('--host',action='store',help='returnshostvariables')
cli_args = parser.parse_args()

def get_inventory():
    return {
    "RHCE": {
        "children": [
            "db",
            "web"
        ]
    },
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "RHCE",
            "ungrouped"
        ]
    },
    "db": {
        "hosts": [
            "ansible2.example.com"
        ]
    },
    "web": {
        "hosts": [
            "ansible1.example.com"
        ]
    }
}
def main(): 
  if cli_args.list()
  inventory = get_inventory()

