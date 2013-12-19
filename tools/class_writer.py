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

for i in range(len(classes)):
    with open("../" + classes[i] + ".cfg","w") as f:
        text = "@master; 1-{0}_master".format(i+1)
        f.write(text)