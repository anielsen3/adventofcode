import sys

input = str(open(sys.argv[1]).readline())

def expand(input):
    fs = []

    file_count = 0
    is_space = False
    for c in input:
        if is_space:
            for i in range(int(c)):
                fs.append(None)
            is_space = False
        else:
            for i in range(int(c)):
                fs.append(str(file_count))
            file_count += 1
            is_space = True

    return fs

def defrag(fs):

    def find_next_space(start, fs):
        for i in range(start, len(fs)):
            if not fs[i]:
                return i

    lp = find_next_space(0, fs)
    rp = len(fs) - 1

    while(lp < rp):
        if not fs[rp]:
            rp -= 1
        else:
            fs[lp] = fs[rp]
            fs[rp] = None
            lp = find_next_space(lp, fs)
            rp -= 1

    return fs

def read_files_spaces(input):
    files = []  # tuple(start, end, fileno)
    spaces = [] # tuple(start, end)

    file_count = 0
    is_space = False
    start = 0
    for c in input:
        if is_space:
            spaces.append((start, start+int(c)))
            start += int(c)
            is_space = False
        else:
            files.append((start, start+int(c), file_count))
            start += int(c)
            file_count += 1
            is_space = True

    return files, spaces

def defrag2(files, spaces):
    result = []

    for file in reversed(files):
        moved_file = False
        f_start, f_end, fileno = file
        for i, (s_start, s_end) in enumerate(spaces):
            if (s_start < f_start) and (f_end - f_start) <= (s_end - s_start): # file fits
                # move file
                spaces[i] = (s_start+(f_end-f_start), s_end)
                result.append((s_start, s_start+(f_end-f_start), fileno))
                moved_file = True
                break

        if not moved_file:
            result.append(file)

    return result

def expand2(files):
    fs = [None for _ in range(99999)]

    for (f_start, f_end, f_no) in sorted(files):
        for i in range(f_start, f_end):
            fs[i] = f_no

    return fs

def checksum(fs):
    return sum(i * int(c) for i, c in enumerate(fs) if c)

print("1:", checksum(defrag(expand(input)))) # 6154342787400
print("2:", checksum(expand2(defrag2(*read_files_spaces(input))))) # 6183632723350
