from xml.etree.ElementTree import ElementTree, Element, SubElement, dump

note = Element('note')
note.attrib['date'] = '20120104'

to = Element('to')
to.text = 'Tove'
note.append(to)

SubElement(note, 'from').text = 'Jani'
SubElement(note, 'heading').text = 'Reminder'
SubElement(note, 'body').text = "Don't forget me this weekend"

def indent(elem, level = 0) :

    i = '\n' + level * " "

    if len(elem) :

        if not elem.text or not elem.text.strip() :
            elem.text = i + " "

        if not elem.tail or not elem.tail.strip() :
            elem.tail = i

        for elem in elem :
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip() :
            elem.tail = i

    else :

        if level and (not elem.tail or not elem.tail.strip()) :
            elem.tail = i

indent(note)
dump(note)

ElementTree(note).write('note.xml')

'''
<note date="20120104">
 <to>Tove</to>
 <from>Jani</from>
 <heading>Reminder</heading>
 <body>Don't forget me this weekend</body>
</note>
'''
