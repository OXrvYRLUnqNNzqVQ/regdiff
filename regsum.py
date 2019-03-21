import argparse
import sh
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()

parser.add_argument('-k', action='store_true')
parser.add_argument('-n', action='store_true')
parser.add_argument('-d', action='store_true')
parser.add_argument('-t', action='store_true')
parser.add_argument('file')
args = parser.parse_args()
infile = args.file

xml = str(sh.hivexml(infile))


reg_a = []

def get_root_elements(path_to_file):
    soup = BeautifulSoup(path_to_file, 'lxml')
    all_elements = soup.find_all('value')
    return all_elements

def get_path(element):
	path = []
	for parent in element.parents:
		if parent.name == "node":
			if parent['name'] is not "None":
				path.append(parent['name'])
	return '/'.join(path[::-1][1:])

for i in get_root_elements(xml):
	name_ = i.get('key') if i.get('key') is not None else "(Default)"
	type_ = i.get('type') if i.get('type') is not None else "(value not set)"
	data_ = i.get('value') if i.get('type') is not None else "(value not set)"
	reg_a.append((get_path(i), name_, type_, data_))
	line = ""
	if args.k: line = line + str(get_path(i)) + "\t" 
	if args.n: line = line + str(name_) + "\t" 
	if args.t: line = line + str(type_) + "\t" 
	if args.d: line = line + str(data_) + "\t" 
	print line
