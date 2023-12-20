from xml.etree import ElementTree


class XML:
    def __init__(self, file_name):
        self.tree = ElementTree.parse(file_name)
        self.collection = self.tree.getroot()

    def xml_to_string(self):
        return ElementTree.tostring(self.collection)

    def decode_string(self):
        return ElementTree.tostring(self.collection).decode()

    def get_items(self, item):
        get_item = self.collection
        item_list = []
        for element in get_item.iter(item):
            item_list.append(element.items())
        return item_list

    def get_attributes(self, attribute):
        get_attribute = self.collection
        attribute_list = []
        for element in get_attribute.iter(attribute):
            attribute_list.append(element.attrib)
        return attribute_list

    def get_child_elements(self, root_element):
        get_child_el = self.collection
        el_list = []
        for el in get_child_el.iter(root_element):
            for child in el.findall('*'):
                el_list.append({child.tag: child.text})
        return el_list


file1 = XML('example.xml')

to_string = file1.xml_to_string()
print(to_string)

decoding = file1.decode_string()
print(decoding)

items = file1.get_items('movie')
for el in items:
    print(el)

attributes = file1.get_attributes('genre')
for el in attributes:
    print(el)

child_elements = file1.get_child_elements('movie')
for el in child_elements:
    print(el)