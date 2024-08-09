from collections import OrderedDict
import json
import os
import pyperclip


def sort_dict_by_alphabet(a):
    d = OrderedDict()
    for k in sorted(a.keys()):
        if isinstance(a[k], dict):
            d[k] = sort_dict_by_alphabet(a[k])
        else:
            d[k] = a[k]
    return d


home_path = os.environ["HOME"]
relative_path = "Library/Application Support/Code/User/settings.json"
path = os.path.join(home_path, relative_path)
s = open(path).read()
d = json.loads(s)
d = sort_dict_by_alphabet(d)
s = json.dumps(d, ensure_ascii=False, indent=4)
pyperclip.copy(s)
