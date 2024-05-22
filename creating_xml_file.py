import lxml.etree as et

root = et.Element('knights')
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight = et.SubElement(root, 'knight', title=title)
        k_name = et.SubElement(knight, 'name')
        k_name.text = name
        et.SubElement(knight, 'color').text = color
        et.SubElement(knight, 'quest').text = quest
        et.SubElement(knight, 'comment').text = comment

xml_bytes = et.tostring(root, pretty_print=True,
                       xml_declaration=True)

xml_text = xml_bytes.decode()
print(xml_text)
print('-' * 60)

doc = et.ElementTree(root)
doc.write('knights.xml', pretty_print=True, xml_declaration=True)
