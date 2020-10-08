# Author: Aniket Dinda
# Site: https://hackingivla.wordpress.com
#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import random
import time

# Random Font
data = requests.get('http://artii.herokuapp.com/fonts_list')
fontsArray = data.text.split('\n')
font = random.choice(fontsArray)
print(font)

# User Input
text = input('ASCII Art Text > ')
print('\n')
print('\n')
print('How Much ART you want to generate')
choice = int(input("Enter the number [1-418] :>>  "))

# Generate Font
for i in range(choice):
      font = random.choice(fontsArray)
      r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
      print("Font:", font)
      print(r.text)
      print()
      print()
      print()
      print()
      print(r.ok)

# Print
joker = (r.text + font)
print(joker)

# While
n = 100
while n>1:
      time.sleep(2)
