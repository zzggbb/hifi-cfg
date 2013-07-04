NOT UPDATED IN THE SLIGHTEST

/crosshairswitcher:
    Broesel's Crosshair Switcher. You should probably not edit any of the files in here. Just edit the /settings/settings_crosshairswitcher file, unless you know what you're doing.        

/general:
    /alias:
        some console aliases that can make stuff easier, like changing maps, getting ammo/health, or completely silencing the game.
    /cvars:
        a bunch of console variables that are good to have. Nearly all miscellaneous cvars have been moved to this file for ease of editing.
    /default:
        contains basic binds and options. This is executed by every single class, so changes to it will affect every class.
    /dingaling:
        contains dingaling options that can be customized for every class.        
    /function_key:
        necessary aliases for function key binds.
    /mouse:
        contains general mouse options and mouse button options that can be customized for every class.     
    /prec:
        contains prec configuration commands. If you don't have prec already, read up on it and download it from here: http://etf2l.org/faq/p-rec/    
    /protect:
        A TF2 html-motd blocker for things like pinion. I've slightly modified it to allow commands like clear and unbindall. To fully make use of this file, read the instructions in there. Or looks at this:
            Create an empty file in your tf directory named textwindow_temp.html and make it read-only (this prevents the motd from being saved & loaded)
            Add '127.0.0.1 motd.pinion.gg' to your hosts file. This prevents a well known motd advertising network to load.
    /script_switcher:
        unfinished/not thoroughly tested script for switching between different numpad, wasd, jump and network settings. might possibly be expanded later. 
    /sensitivities:
        contains mouse sensitivity options that can be customized for every class.        
    /tab:
        file for customizing what happens when tab is pressed. by default it shows the scoreboard, fps and netgraph.   
    /wait_check:
        a script to test if the wait command is disabled on a server. by itself it isn't very useful, but it can be used to run certain scripts based on whether wait is enabled or not

/graphics:
    /ares:
        /frames:
            a slightly modified version of chris's maxframes graphics config. it has some slight experimental changes. I would recomend using chris's maxframes instead of this.
        /highframes:
            a slightly modified verion of chris's highframes graphics config. it has some slight experimental changes. I would recomend using chris's highframes instead of this.
        /pyrovision:
            all of the pyrovision related cvars I could find. By default, all of the cvars are set so that the effects of pyrovision are as minimal as possible.
        /quality:
            a slightly modified version of chris's maxquality graphics config. it has some slight experimental changes. I would recomend using chris's maxquality instead of thi
        /violence_off:
            a graphics config that minimizes gibs, blood and ragdolls.
        /violence_on:
            a graphics config that maximizes gibs, blood and ragdolls.
    /chris:
        /dx9frames:
            a graphics config designed to gain performance while using dx9. for more information, go to fakkelbrigade.eu/chris/configs/
        /highframes:
            a graphics config designed to gain performance without a lot of visual loss. for more information, go to fakkelbrigade.eu/chris/configs/
        /highquality:
            a graphics config designed to make the game look good and still get good frames. for more information, go to fakkelbrigade.eu/chris/configs/
        /maxframes:
            a graphics config designed to gain the most performance possible, at the cost of visual loss. for more information, go to fakkelbrigade.eu/chris/configs/
        /maxquality:
            a graphics config designed to make the game look as good as possible, at the cost of low frames. for more information, go to fakkelbrigade.eu/chris/configs/

/movement:
    /jump:
        /cjump_jump:
            a script that makes you crouch jump instead of doing a regular jump.
        /default_jump:
            default +jump jumping. resets the crouch jump script.
    /wasd:
        /default_wasd:
            default movement. resets the null canceling movement script.
        /null_wasd:
            a script that makes the cancels out null movement. normally, when two keys that lead to opposite directions are held down together, the player stops moving. 
            with this script, this cancelation will not happen and you will move in the direction of the key that was pressed last.

/numpad:
    /class_team_select:
        contains binds for changing teams or class.
    /demonstration_man:
        contains binds for learning more about the game. there are 75 included, so feel free to change the binds to use your favorite ones.
    /insults:
        contains some insults. there are more insults than there are numpad keys, so feel free to change them up or add your own.
    /item_preset_select:
        contains binds for quick switching loadouts.
    /off:
        completely turns off use of the numpad.
    /spectate:
        contains binds for more easily navigating around as a spectator. by default, spectating different players is bound to the number keys and "numlock","/", and "*". 
        the "-" key toggles the scoreboard on and off. the "+" and "Enter" key spectates the next and previous players, respectively. 
        the "0" or "Ins" key toggles your view while spectating. the "." or "Del" key toggles spec_track on and off.
    /trivia:
        binds the numpad to contain trivia questions. feel free to change them.

/performance_info:
    /fps:
        binds and settings for controlling the fps display
    /netgraph:
        binds and settings for controlling the netgraph display

/plugins:
    contains all of your plugins/custom scripts.

/reference:
    /bindable_keys:
        a list of all bindable key names.
    /classes:
        a template for whenever you need every class alias.
    /every_tf2_command:
        every single command that works with tf2. most of these are source commands, so a lot of them work in all valve games. 
        stolen from the valve developer wiki: https://developer.valvesoftware.com/wiki/List_of_TF2_console_commands_and_variables
    /function_keys:
        a template for function key binds.
    /numpad.png:
        an image that can be used to reference the scripting name of each key on the numpad.
    /numpad:
        a template for numpad binds.
    /toggle:
        a template for making a toggle script.
    /voicemenu:
        aliases for voicemenu commands.

/settings:
    /settings_crosshairswitcher:
        per class settings for Broesels Crosshair Switcher. Read the ".README" file for more information. Also check out this page for more info: https://code.google.com/p/broesels-crosshair-switcher/
    /settings_function_keys:
        per class settings for function key binds.
    /settings_graphics:
        unified settings for graphical options. the options you put in here are run in autoexec every time tf2 launches.
    /settings_jump:
        per class settings for jump scripts.
    /settings_network:
        contains client rate options that can be customized for every class. 
    /settings_numpad:
        contains the settings for customizing the use of the numpad by each class. by default, all classes use insults, with the exception of engineer, who has trivia.
    /settings_plugins:
        contains the settings for customizing plugins. to install a plugin, create an alias for it which executes "plugins/<plugin name>". 
        for example, to install the plugin "my_script", place the script in the cfg/plugins folder. then place the following in settings/settings_plugins.cfg:
            alias "my_script"       "exec plugins/my_script"
        to make a class execute a script, place the script name in the class alias. for example, to make the pyro execute my_script and pyropanic , make the pyro alias in _setting.cfg look like this:
            alias "pyro"            "pyropanic; my_script
    /settings_swap:
        per class settings for the swap script. this serves the same functionality as lastinv, the only difference being that it limits you to only 2 weapons. 
        to customize the 2 weapons that are used, change next_wep and prev_wep to the corresponding weapon slot, either weapon1, weapon2 or weapon3. 
        the default bind for this script q, and it can be changed by editing the "swap_next" bind in /general/default.
    /settings_voice:
        per class settings for voice chat. by default, all classes use the push method.
    /settings_wasd:
        per class settings for the movement keys.
    /settings_weapons:
        per class settings for starting weapon and number key binds. starting weapons can be useful in a competitive setting when the soldiers, demomen and medic need to rollout or distribute buffs as quickly as possible.
        as for the number key binds, by default, keys 1-10 are bound to weapons 1-10. The only exception is medic, who has 2 bound to slot 1 and 1 bound to slot 2.

/voice:
    /push:
        the default push to talk bind.
    /toggle:
        a voice toggle script that binds v to turning voice chat on with one tap and off with a second.

/README:
    contains general information about the config

/CHANGELOG
    tracks the changes I've made to this config.