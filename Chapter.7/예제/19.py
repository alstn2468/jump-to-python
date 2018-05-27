from xml.etree.ElementTree import Element, dump

# Element
note = Element('note')
to = Element('to')
to.text = 'Tove'

note.append(to)

dump(note) # <note><to>Tove</to></note>
