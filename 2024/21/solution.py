import itertools
import functools

num_keypad = { '7': (0, 0), '8': (1, 0), '9': (2, 0), '4': (0, 1), '5': (1, 1), '6': (2, 1), '1': (0, 2), '2': (1, 2), '3': (2, 2), '0': (1, 3), 'A': (2, 3), 'GAP': (0, 3) }
dir_keypad = { '^': (1, 0), 'A': (2, 0), '<': (0, 1), 'v': (1, 1), '>': (2, 1), 'GAP': (0, 0) }

def get_keypad(name):
    if name == 'num':
        return num_keypad
    else:
        return dir_keypad

def all_paths(f, t, keypad_name):
    keypad = get_keypad(keypad_name)
    (fx, fy) = keypad[f]
    (tx, ty) = keypad[t]
    dx = tx - fx
    dy = ty - fy

    path = ""
    if dx < 0:
        path += "<" * abs(dx)
    else:
        path += ">" * abs(dx)

    if dy < 0:
        path += "^" * abs(dy)
    else:
        path += "v" * abs(dy)

    return set(map(lambda l: "".join(l), itertools.permutations(path, len(path))))

def shortest(sequences):
    min_len = None
    result = list()
    for s in sequences:
        if not min_len or len(s) < min_len:
            result = [s]
            min_len = len(s)
        elif len(s) == min_len:
            result.append(s)

    return result

@functools.cache
def legal_paths(f, t, keypad_name):
    result = set()
    paths = all_paths(f, t, keypad_name)
    paths_to_gap = all_paths(f, 'GAP', keypad_name)
    for p in paths:
        if not any(p.startswith(ptg) for ptg in paths_to_gap):
            result.add(p + 'A')
    return shortest(result)

@functools.cache
def type(f, t, depth):
    if depth == 0:
        return legal_paths(f, t, 'num')
    else:
        results = set()
        xs = type(f, t, depth - 1)
        for x in xs:
            cur = 'A'
            tmp_res = []
            for p in x:
                sub_paths = legal_paths(cur, p, 'dir')
                if sub_paths:
                    tmp_res.append(sub_paths)
                cur = p
            results |= set(map(lambda l: "".join(l), itertools.product(*tmp_res)))

        return shortest(results)

def type_code(code, depth):
    code = f"A{code}"
    return "".join([type(code[i], code[i+1], depth)[0] for i in range(len(code)-1)])

def complexity(code, depth=2):
    return len(type_code(code, depth)) * int(code.replace('A', ''))

#codes = "029A,980A,179A,456A,379A"
codes = "169A,279A,540A,869A,789A"
print("1:", sum(complexity(code, 2) for code in codes.split(",")))
print("2:", sum(complexity(code, 3) for code in codes.split(",")))
# print("2:", sum(complexity(code, 24) for code in codes.split(",")))


