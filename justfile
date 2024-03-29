install:
	python3 script/runners/install.py --name SnapSelect

watch:
	python3 script/runners/watch.py --version 'Live 11.3.13' --name SnapSelect

close-set:
	pkill -x Ableton Live 11 Suite

open-set:
	open ./set/set.als

reload:
	just install && just close-set && sleep 1 && just open-set
