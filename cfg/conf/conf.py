from __future__ import print_function
import json
import collections

with open("conf.json") as f:
    json_data = json.load(f, object_pairs_hook=collections.OrderedDict)

for category in json_data:
    tf2_classes = json_data[category]["data"]
    for tf2_class in tf2_classes:
        data = tf2_classes[tf2_class]
        if type(data) == type([]):

            alias_body = ""
            #avoid pesky extra semicolons
            for alias in data[:-1]:
                alias_body += (alias + "; ")
            alias_body += data[-1]
            print ("alias", tf2_class + "_" + category, "\"" + alias_body + "\"")

        if type(data) == type(collections.OrderedDict()):

            alias_body = ""
            sub_aliases = []
            if (not json_data[category]["flags"]["cvars"]):
                opt_string = "alias "
            else:
                opt_string = ""
            for key in data:
                sub_aliases.append(opt_string + key + " " + str(data[key]))
            #avoid pesky extra semicolons
            for item in sub_aliases[:-1]:
                alias_body += (item + "; ")
            alias_body += sub_aliases[-1]
            print ("alias", tf2_class + "_" + category, "\"" + alias_body + "\"")

    print("\n")
