



import xml.etree.ElementTree as ET
import cv2


counter = 1

for counter in range(1, 15):
    xml_path = f'D:\\indoData\\viewsall_zones\\view{counter}.xml'


    tree = ET.parse(xml_path)
    root = tree.getroot()

    redzone = []

    # find all redzone coordinates xmin, ymin, xmax, ymax
    for object in root.findall('object'):
        name = object.find('name').text
        if name == 'redzone':
            xmin = object.find('bndbox').find('xmin').text
            ymin = object.find('bndbox').find('ymin').text
            xmax = object.find('bndbox').find('xmax').text
            ymax = object.find('bndbox').find('ymin').text

            # print(xmin, ymin, xmax, ymax)
            redzone.append([xmin, ymin, xmax, ymax])
    

    fw = open('redzone.json', 'a')
    fw.write('{"'+'view' + str(counter)+'"' + ': ' +'"'+ str(redzone) +'"},'+ '\n')
    fw.close()


# view1
# [['439', '313', '765', '313'], ['1190', '33', '1411', '33'], ['1413', '128', '1741', '128'], ['1643', '148', '1752', '148'], ['1411', '663', '1719', '663'], ['1197', '713', '1319', '713'], ['642', '879', '1190', '879'], ['1313', '672', '1410', '672'], ['594', '709', '658', '709'], ['342', '688', '594', '688'], ['66', '639', '336', '639'], ['13', '91', '58', '91'], ['63', '16', '243', '16'], ['1106', '575', '1409', '575'], ['1427', '489', '1501', '489'], ['1029', '537', '1101', '537'], ['1098', '341', '1389', '341'], ['831', '589', '1006', '589'], ['1003', '621', '1039', '621'], ['1046', '645', '1071', '645'], ['1067', '664', '1098', '664'], ['1050', '739', '1086', '739'], ['970', '817', '1051', '817'], ['837', '848', '986', '848'], ['763', '807', '831', '807'], ['738', '740', '778', '740'], ['737', '672', '765', '672'], ['757', '628', '810', '628'], ['795', '620', '841', '620']] 

