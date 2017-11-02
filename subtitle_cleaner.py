#code to clean up srt files, and give you raw text. WARNING: makes heavy use of regex!!!
def change_str(inp):
	'''Given an srt file text, extracts just the raw text.'''
	#input: str. Output: str
	changes = [('[0-9]+\n[0-9:,]+ --> [0-9:,]+\n', ''),
		   ('\n\n', ' '),
		   ('<font color="#[A-Z0-9a-z]*">', ''),
		   ('<[ ]*/font>', ' '),
		   ('[ ]+', ' ')]
	output = inp
	for change in changes:
		output = re.sub(change[0], change[1], output)
	return output
  
def clean_name_shiffman(name):
  '''Cleans up janky filenames in Daniel Shiffman's video subs'''
	if '#' in name:
		return name.split('#')[1]
	else:
		return name.replace('[DownSub.com] ', '')



def read_and_output_srt(dir_entry):
  '''takes a directory name full of srts, cleans up srts, and puts them in a new folder
  without touching the old files
  '''
	fnames = os.listdir(dir_entry)
	target_dir = dir_entry+'cleaned_srts\\'
	os.mkdir(target_dir)
	for fname in fnames:
		if fname.endswith('.srt'):
			f_loc = dir_entry+fname
			with open(f_loc, 'r') as fd:
				txt = fd.read()
				cleaned = change_str(txt)
				new_name = target_dir+clean_name_shiffman(fname)
				with open(new_name, 'w') as fdw:
					fdw.write(cleaned)
