import json
import os

cfg_file = open('config.json', 'r')
cfg = json.load(cfg_file)
cfg_file.close()

print('Please enter the project\'s name and directory name.')
print('Leave any field empty to cancel project creation.')
prj_name = input('Name: ')
if len(prj_name):
	prj_dir = input('Directory: ')
	if len(prj_dir):
		cfg['projects'].append([prj_name, prj_dir])
		cfg_file = open('config.json', 'w')
		os.mkdir(prj_dir)
		json.dump(cfg, cfg_file, ensure_ascii=False)
		cfg_file.close()
		days_file = open(prj_dir + os.sep + 'days.json', 'w')
		days_file.write('{}')
		days_file.close()