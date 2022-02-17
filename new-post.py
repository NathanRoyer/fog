import json
import os

def read_json(f):
	file = open(f.replace('/', os.sep), 'r')
	obj = json.load(file)
	file.close()
	return obj

def write_json(f, content):
	file = open(f.replace('/', os.sep), 'w')
	json.dump(content, file, ensure_ascii=False)
	file.close()
	
cfg = read_json('config.json')

projects = cfg['projects']
projects.insert(0, ['[cancel]'])

for i in range(len(projects)):
	print(str(i + 1) + ' ' + projects[i][0])

i = int(input('Project [1-' + str(len(projects)) + ']: ')) - 1

if i >= 1 and i < len(projects):
	day_name = input('Day [e.g. 2021-dec-31]: ')
	project = projects[i][1]
	day_path = 'days/' + day_name + '.json'
	prj_days_path = project + '/days.json'
	day = {}
	try:
		day = read_json(day_path)
	except:
		pass
	old_day_count = 0
	if project in day:
		old_day_count = day[project]
	new_day_count = old_day_count + 1

	prj_days = read_json(prj_days_path)
	key = day_name + '/' + str(old_day_count)
	value = day_name + '/' + str(new_day_count)
	try:
		i = prj_days.index(key)
		prj_days[i] = value
	except:
		print('First post today')
		prj_days.append(value)
	
	post_path = project + '/' + day_name + '-' + str(old_day_count)
	day[project] = new_day_count

	os.mkdir(post_path)
	write_json(day_path, day)
	write_json(prj_days_path, prj_days)

	post = open(post_path + '/post.md', 'w')
	post.write('### Morning\n\n### Afternoon\n')
	post.close()

else:
	print('No such project.')