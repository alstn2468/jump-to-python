from xml.etree.ElementTree import Element, SubElement, dump

# SubElement
note = Element('note')
to = Element('to')
to.text = 'Tove'

note.append(to)
SubElement(note, 'from').text = 'Jani'

dump(note) # <note><to>Tove</to><from>Jani</from></note>

# Attribute

note.attrib['date'] = '20120104'

dump(note) # <note date="20120104"><to>Tove</to><from>Jani</from></note>
