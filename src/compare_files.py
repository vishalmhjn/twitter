import os
import json
from shutil import copyfile
import sys
#FILE_OLD = os.environ.get("CITY")

from twisted.internet import reactor
from twisted.internet import task as task_twisted
CITY = sys.argv[1]
FILE_NEW = "../data/16aug copy.json"
FILE_OLD = "../data/16aug.json"

timeout = 10*60

def get_numlines(PATH):
	num_lines = sum(1 for line in open(PATH))
	return num_lines

def save_new(FILE_OLD, FILE_NEW):
	copyfile(FILE_NEW, FILE_OLD)


def main():
	num_lines_new = get_numlines(FILE_NEW)
	num_lines_old = get_numlines(FILE_OLD)
	if num_lines_new > num_lines_old:
		save_new(FILE_OLD, FILE_NEW)
		print("FILE Saved")
	else:
		os.system("python get_tweets.py "+CITY)
		print("Calling tweets")


if __name__=="__main__":
	l = task_twisted.LoopingCall(main)
	l.start(timeout)
	reactor.run()