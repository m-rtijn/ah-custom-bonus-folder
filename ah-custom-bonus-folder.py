#!/usr/bin/python3
"""
    ah-custom-bonus-folder.py

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

# import json
# import smtplib

from bs4 import BeautifulSoup

with open("bonus.html") as f:
    testdata = f.read()

soup = BeautifulSoup(testdata, "html.parser")

bonus_data_json_text = ""

# Retrieve the bonus data in JSON format from the html
for script in soup.find_all("script"):
    if script.string is not None:
        script_string_stripped = script.string.strip()

        if script_string_stripped.startswith("window.__INITIAL_STATE__="):
            bonus_data_json_text = script_string_stripped.replace(
                "window.__INITIAL_STATE__= ", "")

print(bonus_data_json_text)
