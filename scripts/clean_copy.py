#!/usr/bin/python3
import os
import re
import json
from sys import argv

dest = argv[1]
if not os.path.isdir(dest):
    print('You should provide a dir as input.')
    exit(1)

def clean(infile, outname):
    with open(infile) as fd:
        content = fd.read()
        content = re.sub(r'\n', '', content)
        obj = json.loads(content)
        for cell in obj['cells']:
            if cell['cell_type'] == 'code':
                cell['execution_count'] = None
                cell['outputs'] = []
                if (len(cell['source']) > 0 and cell['source'][0].startswith('##keep')):
                    continue
                cell['source'] = []
        with open(outname, 'w') as out:
            json.dump(obj, out)

ipynb_files = [name for name in os.listdir(dest) if name.endswith('.ipynb')]
for file in ipynb_files:
    clean(dest + '/' + file, file)

