import csv
import xml.etree.ElementTree as ET

tree = ET.parse("database.xml")

mrn_cui = set()

for record in tree.findall(".//Record"):
    mrn = record.find("./Identifier/MRN")
    items = record.findall("./Medication/Item")
    if mrn is not None and items:
        for cui in items:
            mrn_cui.add(f"{mrn.attrib['value']}|{cui.attrib['value']}")

with open("test.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(["MRN", "CUI"])
    for entry in sorted(mrn_cui):
        csvwriter.writerow(entry.split('|'))