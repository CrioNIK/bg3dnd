import pathlib, xml.etree.ElementTree as ET
W=pathlib.Path(__file__).resolve().parent
L=W/'bg3dnd/Mods/DnD2024_897914ef-5c96-053c-44af-0be823f895fe/Localization'
E=list(ET.parse(L/'English/english.xml').getroot()); P={x.attrib['contentuid']:x.text for x in ET.parse(L/'Polish/polish.xml').getroot()}
terms=['Chromatic Orb','Command','Darkvision',"Dragon’s Breath","Dragon's Breath",'Fly','Protection from Energy','Banishment','Charm Monster','Dominate Person','Synaptic Static','Arcane Eye','Artificer','Cleric','Wizard','Sorcerer','Warlock','Channel Divinity','Charmed','Frightened','Incapacitated','Draconic Presence','Short Rest','Conjurer','Enchanter']
for t in terms:
    print(t+':')
    for x in E:
        if x.text==t and x.attrib['contentuid'] in P: print(' ',x.attrib['contentuid'],P[x.attrib['contentuid']])
print('\nSCROLL/DRAGON CONTEXT')
for x in E:
    if x.attrib['contentuid'] not in P: continue
    if (x.text.startswith('Usable Classes:') and ('Artificer' in x.text or len(x.text)>60)) or ('Domain Spells table' in x.text) or ('Emanation' in x.text and 'Channel Divinity' in x.text):
        print(x.text,'\nPL:',P[x.attrib['contentuid']],'\n')
