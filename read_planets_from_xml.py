import lxml.etree as et

doc = et.parse('DATA/solar.xml')  # read file

root = doc.getroot()

print(f"{root = }")

for planet in root.findall('.//planet'):
    print(planet.get('planetname'))
    for moon in planet.findall('moon'):
        print(f"   {moon.text}")

