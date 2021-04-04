
import xml.etree.ElementTree as ET
tree = ET.parse('/home/manju/Downloads/batch_23_5.xml')
root = tree.getroot()
for object in root.findall('object'):
	name = object.find('name').text
	
	if name == 'Shot_Shot_Presence':
		root.remove(object)	

tree.write('/home/manju/Downloads/output.xml')

