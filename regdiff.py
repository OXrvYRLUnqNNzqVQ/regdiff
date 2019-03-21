import sys
from bs4 import BeautifulSoup

infile_a = sys.argv[1]
infile_b = sys.argv[2]

reg_a = []
reg_b = []

def get_root_elements(path_to_file):
    soup = BeautifulSoup(open(path_to_file), 'lxml')
    all_elements = soup.find_all('value')

    #count_element_indices = [len(list(a.parents)) for a in all_elements]

    #absolute_roots_index = min(
     #   (index for index, element in enumerate(count_element_indices)
      #      if element == max(count_element_indices)
       # )
    #)
    return all_elements
    #return all_elements[absolute_roots_index:]

def get_path(element):
	path = []
	for parent in element.parents:
		if parent.name == "node":
			if parent['name'] is not "None":
				path.append(parent['name'])
	#return(path)
	#return [i for j in element.parent.parents] 
    #to_remove = ['[document]', 'body', 'html']
    #path = [element.name] + [e.attrs for e in element.parents if e.name not in to_remove]
	return '/'.join(path[::-1][1:])

for i in get_root_elements(infile_a):
	name_ = i.get('key') if i.get('key') is not None else "(Default)"
	type_ = i.get('type') if i.get('type') is not None else "(value not set)"
	data_ = i.get('value') if i.get('type') is not None else "(value not set)"
	reg_a.append((get_path(i), name_, type_, data_))
	#print str(get_path(i)) + "|" + str(name_) + "|" + str(type_) + "|" + str(data_)
	print str(get_path(i)) + "|" + str(name_) + "|" + str(data_)

for i in get_root_elements(infile_b):
	name_ = i.get('key') if i.get('key') is not None else "(Default)"
	type_ = i.get('type') if i.get('type') is not None else "(value not set)"
	data_ = i.get('value') if i.get('type') is not None else "(value not set)"
	reg_b.append((get_path(i), name_, type_, data_))
	
set_a = set(reg_a)
set_b = set(reg_b)

changes = set_a^set_b

#for c in changes:
#	print(c)
#	print("\n\n")


