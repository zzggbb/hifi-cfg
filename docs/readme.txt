Using this config:
	Any and all settings are in the 'conf' folder. If the setting is a
	class-specific one, it is probably inside 'conf/class'. Any other settings
	are inside of 'conf/game'.

	Changing Class-Specific Settings:
		There are 14 class-specific settings files. EVERY settings file follows
		the same format of 9 aliases, one for each class.
		For example, to edit scout settings, edit the '1-1_<setting>' alias in
		the appropriate setting file.

			dingaling:
				customize dingaling and hitsound related cvars.
			function_keys:
				customize what the function keys are bound to. Stick to editing
				the alias AFTER the 'fn_<number>' alias.
			jump:
				customize what type of jumping is done when (by default) the
				spacebar is pressed.
				Possible values for the class aliases:
					jump_default
					jump_cjump
					jump_ctap
			masking:
				customize the voicemenu voice used in voicemasking.
				The voice_mask alias will cycle through each of the three
				aliases when used.
			mouse:
				customize how the game reacts to different mouse buttons.
			network:
				customize network related cvars.
			numpad:
				customize numpad binds.
				Possible values for the class aliases:
					numpad_change
					numpad_demon
					numpad_insult
					numpad_item
					numpad_off
					numpad_spect
					numpad_trivia
			plugins:
				customize which plugins are used by which class.
				Possible values for the class aliases:
					path.p_auto_detonate
					path.p_auto_medic
					path.p_demoknight
					path.p_equalizer_call
					path.p_guillotine
					path.p_idle
					path.p_intel_timepath
					path.p_medic_chris
					path.p_pyropanic
					path.p_radar
					path.p_regen
					path.p_reverse_heal
					path.p_sentry_jump
					path.p_stabbyscript
					path.p_winger_jump
			sensitivity:
				customize sensitivity
				Possible values for the class aliases:
					sensitivity <0...INFINITY>
			swap:
				customize how the (by default) q key behaves.
				The next_wep and prev_wep aliases can be any of the following
				aliases:
					weapon1
					weapon2
					weapon3
				next_wep and prev_wep specify which TWO weapons to cycle between
				when using quickswitch.
			voice:
				customize what the (by default) v key does.
				Possible values for the class aliases:
					voice_setting_push
					voice_setting_toggle
			wasd:
				customize movement type.
				Possible values for the class aliases:
					wasd_null
					wasd_default
			weapons:
				customize your starting weapon and 1-5 keys.
				Possible values for starting weapon, <1-5>_key:
					weapon1
					weapon2
					weapon3
			xhair:
				customize your crosshair for each slot, for each class.
				DO NOT touch those '1-<1...9>_xhair' aliases.
				Possible size values:
					smallest
					smaller
					small
					medium
					big
					bigger
					biggest
					invisible
				Possible color values:
					red
					green
					blue
					yellow
					cyan
					pink
					orange
					purple
					mint
					lime
					skyblue
					black
					grey
					white
				Possible crosshair type values:
					cross_dot
					half_cross_dot
					ring
					ex
					dot
					open_cross
					cross
					default
				Possible viewmodel values:
					off
					any number (inclusive) between 60 and 130

	Changing Game Settings:
		There are 7 game-setting real

	Other info:

		If you don't know what an alias does (trust me, the time will come),
		check 'core/meta/lib'.
		A very large majority of VERY USEFUL aliases are inside that file.