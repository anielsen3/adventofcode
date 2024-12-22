import sys

class Node:
    def __init__(self, lhs, rhs):
        self.name = lhs
        rhs_l = rhs.split(" ")
        if (len(rhs_l) > 1):
            self.op = rhs_l[1]
            self.left = rhs_l[0]
            self.right = rhs_l[2]
            self.value = None
        else:
            self.value = int(rhs)
        
    def eval(self):
        if self.value:
            return self.value
        else:
            return eval(f"{self.lnode.eval()} {self.op} {self.rnode.eval()}")

    def part2_eval(self, target_val = None):
        if self.name == 'humn':
            return target_val
        elif self.name == 'root':
            if self.rnode.contains_humn():
                return self.rnode.part2_eval(self.lnode.eval())
            else:
                return self.lnode.part2_eval(self.rnode.eval())
        else:                    
            if self.rnode.contains_humn():
                lval = self.lnode.eval()

                if self.op == "+":
                    target_val -= lval
                elif self.op == "*":
                    target_val /= lval
                elif self.op == "/":
                    target_val = lval / target_val
                elif self.op == "-":
                    target_val = lval - target_val

                return self.rnode.part2_eval(target_val)

            else:
                rval = self.rnode.eval()

                if self.op == "+":
                    target_val -= rval
                elif self.op == "*":
                    target_val /= rval
                elif self.op == "/":
                    target_val *= rval
                elif self.op == "-":
                    target_val += rval

                return self.lnode.part2_eval(target_val)

    def contains_humn(self):
        if self.name == 'humn':
            return True
        else:
            return not self.value and (self.lnode.contains_humn() or self.rnode.contains_humn())

def root():
    nodes = [ Node(*line.strip().split(": ")) for line in open(sys.argv[1]).readlines() ]

    lookup = { node.name: node for node in nodes }
    for node in nodes:
        if not node.value:
            node.lnode = lookup[node.left]
            node.rnode = lookup[node.right]

    return lookup['root'] 

print("1:", root().eval())
print("2:", root().part2_eval())