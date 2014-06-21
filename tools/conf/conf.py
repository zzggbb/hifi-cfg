from __future__ import print_function
import json
import collections

with open("conf.json") as f:
    json_data = json.load(f, object_pairs_hook=collections.OrderedDict)

def construct_body(data):
    body = ""
    for item in data[:-1]:
        body += (item + "; ")
    body += data[-1]
    return body

for category in json_data:
    tf2_classes = json_data[category]["data"]
    for tf2_class in tf2_classes:
        data = tf2_classes[tf2_class]
        x = data if (type(data) == type([])) else [(("alias " if not json_data[category]["flags"]["cvars"] else "") + key + " " + str(data[key])) for key in data]
        print("alias", tf2_class + "_" + category, "\"" + construct_body(x) + "\"")
    print("\n")