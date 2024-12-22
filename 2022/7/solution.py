import re
import sys

def read_input():
    filesystem = set("/")
    pwd = "/"

    for line in open(sys.argv[1]).readlines():
        if m := re.match("^\$ cd (.+)$", line):
            dir = m.group(1)
            if dir == "/": # "cd /"
                pwd = "/"
            elif dir == "..": # "cd .."
                pwd = re.sub("[^/]+/$", "", pwd)
            else: # "cd <directory>""            
                pwd = f"{pwd}{dir}/"
                filesystem.add(f"{pwd}") # store "<full-path>"
        elif m := re.match("^(\d+) (.+)$", line): # file
            size, name = m.groups()
            filesystem.add(f"{pwd}{name} {size}") # store "<full-path> <size>"

    return filesystem

def is_dir(f):
    return not re.match("\d+$", f)

def is_file_in_dir(f, dir):
    return re.match(f"^{dir}.* \d+$", f)

def file_size(f):
    return int(f.split(" ")[1])

def dir_size(dir, fs):
    return sum(file_size(f) for f in fs if is_file_in_dir(f, dir))

fs = read_input()
root_size = dir_size("/", fs)
dir_sizes = [dir_size(d, fs) for d in fs if is_dir(d)]

print("1:", sum(s for s in dir_sizes if s <= 100000))
print("2:", min(s for s in dir_sizes if s >= (root_size - 40000000)))