"""
"mp_respawnwavetime": {
    "value": 10,
    "tags": ["sv", "nf", "rep"],
    "help": "Time between respawn waves."
}
"""

with open("testcvarlist.txt","r") as f:
    print [line.split()[0] for line in f]


