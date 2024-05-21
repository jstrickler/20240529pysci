airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

print(f"{airports['MCO'] = }")
print(f"{airports['RDU'] = }")
print(f"{airports.get('OAK') = }")
print(f"{airports.get('MXP') = }")
print(f"{airports.get('MXP', 'not found') = }")

print(f"{airports.setdefault('MXP', 'Milan') = }")
print(f"{airports = }\n")

# DICT.items()  iterator of key/value pairs

for code, city in airports.items():
    print(code, city)
print()
print(airports.items())




