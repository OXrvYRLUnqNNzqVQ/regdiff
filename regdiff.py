import sys
from bs4 import BeautifulSoup

infile = sys.argv[1]

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
	return '/'.join(path[::-1])

for i in get_root_elements(infile):
	name_ = i.get('key') if i.get('key') is not None else "(Default)"
	type_ = i.get('type') if i.get('type') is not None else "(value not set)"
	data_ = i.get('value') if i.get('type') is not None else "(value not set)"

	print str(get_path(i)) + "\t" + str(name_) + "\t" + str(type_) + "\t" + str(data_)
