# sub_dir_search.py
import os

def search(dirname) :
	try :
		filenames = os.listdir(dirname)
		for filename in filenames :
			full_filename = os.path.join(dirname, filename)
			if os.path.isdir(full_filename) :
				search(full_filename)
			else :
				ext = os.path.splitext(full_filename)[-1]
				if ext == '.py' :
					print(full_filename)
	except PermissionError :
		pass

search('C:/Users/Beginning/Documents/python/Jump_To_Python/Chapter.6/예제')

'''
하위 디렉터리 검색을 쉽게 해주는 os.walk
import os

for (path, dir, files) in os.walk('C:/') :
	ext = os.path.splitext(filename)[-1]
	if ext == '.py' :
		print('%s/%s' % (path, filename))
'''
