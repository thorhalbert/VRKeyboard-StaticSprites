#!/usr/bin/env python3

import sys


def procLine(line, count):
    global defCols, keys

    line = line.strip()
    # print("Line="+line)

    key = {}

    columns = line.split('\t')
    if defCols is None:
        defCols = columns
        for i in range(0, len(columns)):
            defCols[i] = defCols[i].strip()
        return
    else:
        for i in range(0, len(columns)):
            key[defCols[i]] = columns[i]

    keys.append(key)


def quot(c):
    if c == "'":
        return "\"'\""
    return "'" + c + "'"


defCols = None
keys = []

count = 0
for line in sys.stdin:
    try:
        count += 1
        procLine(line, count)
    except Exception as e:
        print("Error processing line: " + line + ", err="+str(e))
        # traceback.print_exc(file=sys.stdout)

# print(keys)

# {'Group': 'L', 'Main': 'BT', 'Temlate ': 'Template_Cmd2', 'Chord': 'S', 'Cell': '19', 'Keyboard': 'American1', 'Glyph': '*BackTab', 'S1': 'TAB'}]

templates = {}

for key in keys:
    if 'Main' not in key:
        key['Main'] = ''
    if 'S1' not in key:
        key['S1'] = ''
    if 'S2' not in key:
        key['S2'] = ''

    template = key['Temlate']

    keyName = key['Keyboard']+'_'+key['Group'] + \
        '_'+key['Chord']+'-'+key['Cell'].zfill(3)
    print("generateKey "+keyName
          + ' ' + key['Temlate']
          + ' ' + quot(key['Main'])
          + ' ' + quot(key['S1'])
          + ' ' + quot(key['S2']))

    key['Name'] = keyName

    if template not in templates:
        templates[template] = 0

    templates[template] += 1

print(templates)