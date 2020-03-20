import os

def main():
    for root,d_names,f_names in os.walk("."):
	print(root, d_names, f_names)

if __name__ == "__main__":
    main()
