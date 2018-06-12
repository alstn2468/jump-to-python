'''
ElementTree를 이용하여 다음 XML 문서를 작성하고 파일에 저장해 보자.
<blog date="20151231">
    <subject>Why Python?</subject>
    <author>Eric</author>
    <content>Life is too short, You need Python!</content>
</blog>
'''

from xml.etree.ElementTree import Element, SubElement, ElementTree

blog = Element('blog')
blog.attrib['date'] = '20151231'

SubElement(blog, 'subject').text = 'Why Python?'
SubElement(blog, 'author').text = 'Eric'
SubElement(blog, 'content').text = 'Life is too short, You need Python!'

ElementTree(blog).write('blog.xml')
