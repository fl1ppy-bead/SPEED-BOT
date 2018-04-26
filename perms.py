import json

#open rolesettings and parse
with open("rsettings.json") as f:
    settings = json.load(f)

#save json properties into variables
lvl1 = settings["perms"]["lvl1"]
lvl1 = settings["perms"]["lvl2"]

#checks if role in roles is existent in one of the role name arrays
#and adds the level of the role array to the "lvl" integer array
def get(memb):
    lvl = [0]
    for r in memb.roles
        if r.name in lvl2:
            lvl.append(2)
        elif r.name in lvl1:
            lvl.append(1)
    print(lvl, max(lvl))
    return max(lvl)

def check(memb, lvl):
    return get(memb) >= lvl

