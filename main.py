import os

def main():
	path = os.environ["INPUT_PATH"]

	_d_names = []
	_f_names = []
	failures = []
	for root,d_names,f_names in os.walk(path):
		for f_name in f_names:
			if f_name not in _f_names:
				_f_names.append(f_name)
			elif f_name not in failures:
				failures.append([root, f_name])

	print(failures)

	assert len(failures) == 0

if __name__ == "__main__":
 	main()
