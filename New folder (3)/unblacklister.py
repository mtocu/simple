import random
import secrets

import lxml.etree
#Updated by Bannable
#Fuck Python
file = 'PARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR.rbxlx'

doc = lxml.etree.parse(file)
def uniqueId():
    print('UniqueId Unpatched')
    for el in doc.xpath("//UniqueId[@name='UniqueId']"):
        el.text = f'ILOVEHOTDOGShjhjhjhjhhjjhjhjhjLOLlmao1O1L{secrets.token_hex(110)}'
    doc.write(file)
def referentt():
    print('Referent Unpatched')
    for el in doc.xpath("//Item[@referent]"):
        string = ''.join(random.choice('losmamis123456abcdoglolbannable') for i in range(70))
        el.attrib['referent'] = f'DASDJKADSKJKLDFLjhhjhjhjFDKJSLJAFDSKAFDKJADFSJLADFSLJKLKJDSAFLKJADF3132132123132SLKJADFSKJLADFSKJLLKJASDFLKJLFSKJADKJLAFSDJKLADFSLKJASKJLDF{string}'
    doc.write(file)
def assetId():
    print('AssetId Unpatched')
    for el in doc.xpath("//SourceAssetId[@name='SourceAssetId']"):
        el.text = f'-{secrets.token_hex(20)}'
    doc.write(file)

#0123456789ABCDEF
#unique id = 17
#referent = 33