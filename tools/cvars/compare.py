import sys
import json
import cvars

args = sys.argv[1:]

if len(args) < 3:
    print "useage: compare.py <old> <new> <output> [-v]"
else:
    v = (args[-1] == '-v')
    with open(args[2],"w") as output:
        logs = map(cvars.make_dict, args[0:2])
        diff = map(list, [set(x)-set(y) for x,y in [logs[::-1],logs]])
        g = (('+',1,diff[0]),('-',0,diff[1]))
        x = {d: {x:logs[e][x] for x in f} if v else f for d,e,f in g}
        res = json.dumps(x,indent=4,separators=(',', ': '))
        print res
        output.write(res)
