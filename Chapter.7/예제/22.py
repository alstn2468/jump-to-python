from xml.etree.ElementTree import parse

tree = parse('note.xml')
note = tree.getroot()

print(note.get('date')) # 20120104
print(note.get('foo', 'default')) # default
print(note.keys()) # ['date']
print(note.items()) # [('date', '20120104')]

from_tag = note.find('from')
from_tags = note.findall('from')
from_text = note.findtext('from')

child = note.getiterator()
childs = note.getchildren()

note.getiterator('from')
