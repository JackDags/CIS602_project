import os
import xml.etree.ElementTree as et

class exfil:
    d = {}
    data = ""

def getValue(l, key):
    if key in l:
        return True
    else:
        return False

def createExfil(root):
    list = []
    for e in root.iter('fileobject'):
        exfilOb = exfil()
        l = {'filename': "", 'filesize': "", 'mac_daddr': [], 'src_ipn': [], 'dst_ipn': [], 'srcport': [], 'dstport': []}
        for c in e:
            if 'tcpflow' in c.tag:
                for key in c.attrib.keys():
                    if getValue(l, key):
                        tmpKey = c.attrib.get(key)
                        l[key].append(tmpKey)
            else:
                tmpKey = c.text
                l[c.tag] = tmpKey
        exfilOb.d = l
        if os.path.isfile(exfilOb.d["filename"]):
            with open(exfilOb.d["filename"], "r") as f:
                exfilOb.data = str(f.read())
            list.append(exfilOb)
    return list

def getExfil():
    if not (os.path.isdir("exfilData/day1")):
        os.system("tcpflow -r pcapFiles/filteredFTP1000.pcap -o exfilData/day1")

    treeDay1 = et.parse("exfilData/day1/report.xml")
    rootDay1 = treeDay1.getroot()
    day1 = createExfil(rootDay1)

    treeDay2 = et.parse("exfilData/day2/report.xml")
    rootDay2 = treeDay2.getroot()
    day2 = createExfil(rootDay2)

    return day1, day2