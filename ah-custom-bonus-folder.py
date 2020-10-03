#!/usr/bin/python3
"""
    ah-custom-bonus-folder.py

    This script reads the weekly discounts of the Albert Heijn super market
    in The Netherlands, checks them against a pre-configured list and mails
    an overview to a recipient.

    https://github.com/m-rtijn/ah-custom-bonus-folder

    Copyright (c) 2020 Martijn

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import json
# import smtplib

from bs4 import BeautifulSoup

with open("bonus.html") as f:
    testdata = f.read()


def retrieve_json_from_bonus_html_page(html_text):
    """Extract the json from the bonus html page

    html_text -- a string with the html text
    returns the parsed data from the json
    """
    soup = BeautifulSoup(testdata, "html.parser")

    bonus_data_json_text = ""

    # Retrieve the bonus data in JSON format from the html
    for script in soup.find_all("script"):
        if script.string is not None:
            script_string_stripped = script.string.strip()

            # Check if we found the script tag with the json with discount
            # information
            if script_string_stripped.startswith("window.__INITIAL_STATE__="):
                bonus_data_json_text = script_string_stripped.replace(
                    "window.__INITIAL_STATE__= ", "")
                bonus_data_json_text = bonus_data_json_text.replace(
                        ":undefined}", ":\"undefined\"}")
                bonus_data_json_text = bonus_data_json_text.replace(
                        ":undefined,", ":\"undefined\",")

    return json.loads(bonus_data_json_text)


def check_collection(b_json, collection, keywords):
    """Check for a list of items in a specified collection.

    b_json -- the parsed json with bonus data (parsed json)
    collection -- the number of the collection to search in (int)
    keywords -- the keywords to look for (list of uncapitalized strings)

    Returns a list of json items that matched

    Valid collection number table
    0 header
    1 personal bonus segments
    2 personal bonus box
    3 personal bonus products
    4 spotlight
    5 free delivery
    6 bezorg-bundel
    7 landelijke bonus
    8 ahonline
    9 gall
    10 gallcard
    11 etos
    12 ads
    13 total bonus products
    """

    if collection < 0 or collection > 13:
        raise IndexError("Invalid collection number")

    return_list = []

    for item in b_json["collections"][collection]["items"]:
        for keyword in keywords:
            if keyword in item['title'].lower():
                print(keyword + "\t" + item['title'].lower())
                print("Match!")
                return_list.append(item)

    return return_list


def format_item(item_json):
    """Format json items into a human-readable format."""

    # Temp
    return item_json['title']
