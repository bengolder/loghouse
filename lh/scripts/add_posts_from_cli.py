import os
import sys
import random
from datetime import datetime
from pprint import pprint

#import requests

def parseDate(line):
    probable_datetime = line[3:19]
    try:
        return datetime.strptime(probable_datetime, "%Y-%m-%d %H:%M")
    except ValueError:
        print("couldn't parse", probable_datetime, "from", line)

def parseTitle(line):
    if line[19:]:
        return line[19:].strip()
    else:
        return ''

def parseEntry(lines):
    date = parseDate(lines[0])
    return {
            'title': parseTitle(lines[0]),
            'date_added': date,
            'date_edited': date,
            'body': ''.join(lines[1:]).strip()
            }

def read_lines(filename):
    entries = []
    entry = None
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if i > 1000:
                print(random.choice(entries))
                return
            if line[:3] == '## ':
                if entry:
                    entries.append(parseEntry(entry))
                entry = [line]
            else:
                if entry:
                    entry.append(line)
        entries.append(parseEntry(entry))


def authenticate():
    """send username and password over https based auth
        receive a token? and use it with subsequent requests
        Server side:
            from rest_framework.authtoken.models import Token
            token = Token.objects.create(user=...)
            print token.key
        Client side (in HTTP header):
            Authorization: Token 944b09119c62bcf9418ad846dd0e4bbdfc6ee4b
        with curl test:
            curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 944b09119c62bcf9418ad846dd0e4bbdfc6ee4b'
            curl -X GET https://example.com/api/endpoint/ -H 'Authorization: Token 944b09119c62bcf9418ad846dd0e4bbdfc6ee4b'
    """
    pass

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        print('received "{}"'.format(filename))
        read_lines(filename)
    else:
        print('no filename received')

