#!/usr/bin/env python

import json
import urllib
import urllib.parse
import urllib.request
import os


def main():
    city = "Brussels"
    api_key = "880c7514a75c6d1ede955f1874790893"

    try:
        data = urllib.parse.urlencode({'q': city, 'appid': api_key, 'units': 'metric'})
        weather = json.loads(urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?' + data)
            .read())
        desc = weather['weather'][0]['description'].capitalize()
        temp = int(float(weather['main']['temp']))
        #return '{}, {}°F'.format(desc, temp)
        return '{}°C'.format(temp)
    except:
        return ''


if __name__ == "__main__":
	print(main())
