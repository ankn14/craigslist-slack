# author: me
# date: today
# description: this transmits housing data from Craigslist to Slack
#
# steps:
# 1. get data from Craigslist
# 2. do stuff with the data
# 3. post data to Slack
#

from craigslist import CraigslistHousing
from slackclient import SlackClient
import json  # used to get Slack API key and Slack destination channel

# 1. get data from Craigslist
#
# documentation here
# https://github.com/juliomalegria/python-craigslist

cl_h = CraigslistHousing(site='vancouver', area='van', category='roo',
                         filters={'max_price': 1000, 'private_room': True})

housing_data = []
for result in cl_h.get_results(sort_by='newest', geotagged=True, limit=5):
    if result.get('has_map') is True:
        data = {
            'price': result.get('price'),
            'title': result.get('name'),
            'url': result.get('url'),
            'geotag': result.get('geotag')
        }
        housing_data.append(data)

# 2. do stuff with the data
#
# we want to filter our results by latitude and longitude
# define geographical coordinates here
# https://boundingbox.klokantech.com/

filtered_housing_data = []
latitudes = [49.22264, 49.247275]
longitudes = [-123.142592, -123.099952]

for house in housing_data:
    house_long = house.get('geotag')[0]
    house_lat = house.get('geotag')[1]
    if (longitudes[0] < house_long) and (house_long < longitudes[1]):
        if (latitudes[0] < house_lat) and (house_lat < latitudes[1]):
            filtered_housing_data.append(house)

# 3. post data to Slack
#
# documentation here
# https://github.com/slackapi/python-slackclient
#

with open('credentials.json') as credentials:
    credentials = json.load(credentials)


slack_token = credentials['SLACK_API_KEY']
slack_destination = credentials['SLACK_CHANNEL']

sc = SlackClient(slack_token)

results = "Your listings:\n"
for house in housing_data:
    results += house.get('title') + '\n' + house.get('price') + '\n' + \
        house.get('url') + '\n\n'

sc.api_call(
  "chat.postMessage",
  channel=slack_destination,
  text=results
)

# some sample output on Slack
#
# Your listings:
# Room for Rent
# $685
# https://vancouver.craigslist.org/van/roo/d/vancouver-room-for-rent/6800012893.html
#
# Room for lease 750$/monthly.
# $750
# https://vancouver.craigslist.org/van/roo/d/vancouver-room-for-lease-750-monthly/6797663739.html
