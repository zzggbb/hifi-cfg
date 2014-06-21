classes = [
        "scout",
        "soldier",
        "pyro",
        "demoman",
        "heavyweapons",
        "engineer",
        "medic",
        "sniper",
        "spy"
    ]

for i,v in enumerate(classes):
    with open("../" + v + ".cfg","w") as f:
        text = "@master; c{0}_master".format(i+1)
        f.write(text)
