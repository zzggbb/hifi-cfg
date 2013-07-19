import datetime
import os

path = "C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf/custom/custom_configs/cfg/extra/extended/updater.cfg"
garbage = "C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf/garbage.log"
if os.path.isfile(garbage):
        os.remove(garbage)

f = open(path,'w')
now = datetime.datetime.now()

f.write(now.strftime("alias \"set_current\" \"con_logfile cvar_list_%m-%d-%y_%I-%M\"\n"))
f.write("alias \"set_empty\" \"con_logfile garbage\"\n")
f.write("alias \"updater\" \"clear; set_current; clear; cvarlist; set_empty; quit\"\n")
f.close()