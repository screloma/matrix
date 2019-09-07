import os
import pprint
from pathlib import Path
import json
pp = pprint.PrettyPrinter()


def path_to_dict(path, d):

    name = os.path.basename(path)

    if os.path.isdir(path):
        depth = path.count(os.sep)
        if(depth < 4):
            if name not in d:
                d[name] = {}
            for x in os.listdir(path):
                print(x)
                path_to_dict(os.path.join(path, x), d[name])
    return d


mydict = path_to_dict('.', d={})

print(json.dumps(mydict))
