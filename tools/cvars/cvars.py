def cvars(cvarlog):
    with open(cvarlog,'r') as f:
        return {a[0]: {x: y.replace('"','').split(', ')[1:] if x=='tags' else y for x,y in zip(['value','tags','desc'],a[1:])} for a in [map(str.strip, line.split(' :')) for line in f.readlines()[2:-2]]}