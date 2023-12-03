install:
	python3 script/runners/install.py --name MacroSelect

watch:
	python3 script/runners/watch.py --version 'Live 11.3.13'

close-set:
	pkill -x Ableton Live 11 Suite

open-set:
	open ./set/set.als

reload:
	just install && just close-set && sleep 1 && just open-set
