# Tool: ordered.py  v1.0.0
# Author: Road Labo (https://roadlabo.com)
# Terms: 本スクリプトは「roadlabo.com」表記を条件に無償利用可。再配布は禁止。
# See: LICENSE.txt

import xml.etree.ElementTree as ET

input_file_path = 'export.osm'
output_file_path = 'export_ordered.osm'

tree = ET.parse(input_file_path)
root = tree.getroot()

nodes, ways, relations = [], [], []

for elem in list(root):
    if elem.tag == 'node':
        nodes.append(elem)
    elif elem.tag == 'way':
        ways.append(elem)
    elif elem.tag == 'relation':
        relations.append(elem)

root.clear()
for node in nodes:
    root.append(node)
for way in ways:
    root.append(way)
for relation in relations:
    root.append(relation)

tree.write(output_file_path, encoding='UTF-8', xml_declaration=True)
print(f"整形済みファイルを保存しました: {output_file_path}")
