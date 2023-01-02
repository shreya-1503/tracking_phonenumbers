import phonenumbers
from test import num1
from phonenumbers import geocoder
ab_numbers=phonenumbers.parse(num1,"CH")
print(geocoder.description_for_number(ab_numbers,"en"))

from phonenumbers import carrier
servicenumber=phonenumbers.parse(num1,"RO")
print(carrier.name_for_number(servicenumber,"en"))


