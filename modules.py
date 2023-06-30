# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules


# Core modules
import datetime
from datetime import date
import time
from time import time

today = datetime.date.today()

today1 = date.today()

# timestamp = time.time()
timestamp1 = time()

# print(today, today1, timestamp, timestamp1)

# Pip modules
from camelcase import CamelCase

c = CamelCase()

print(c.hump("hello there world"))


# Import custom module
import validator
from validator import validate_email

email = "test#test.com"

if validate_email(email):
    print("Email is valid")
else:
    print("Email is bad")
