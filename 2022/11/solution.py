import sys
import re
import math

def parse_ints(s):
    return list(map(int, re.findall("\d+", s)))

class Item:
    def __init__(self, worry_level):
        self.worry_level = worry_level

class Monkey:
    def __init__(self, monkey_text):
        self.total_inspections = 0
        (_, items_text, operation_text, *test_text) = monkey_text.split("\n")
        self.items = [Item(num) for num in parse_ints(items_text)]
        self.operation = operation_text.split(" = ")[1]
        (self.divisor, self.target_true, self.target_false) = parse_ints("".join(test_text))

    def play(self, monkeys, calmdown):
        prod_divisors = math.prod([monkey.divisor for monkey in monkeys])

        for item in list(self.items):
            self.total_inspections += 1

            # evaluate operation on worry level
            item.worry_level = eval(self.operation, {"old": item.worry_level})

            # calm down (part 1) or do modulus for lcm (part 2)
            if calmdown:
                item.worry_level //= 3
            else:
                item.worry_level %= prod_divisors

            # throw to other monkey
            monkeys[(self.target_false, self.target_true)[item.worry_level % self.divisor == 0]].items.append(item)
            self.items.remove(item)
        
def monkey_business(num_rounds, calmdown):
    monkeys = [Monkey(monkey_text) for monkey_text in open(sys.argv[1]).read().split("\n\n")]

    for _ in range(num_rounds):
        for monkey in monkeys:
            monkey.play(monkeys, calmdown)

    inspections = sorted([monkey.total_inspections for monkey in monkeys])
    return inspections[-1] * inspections[-2]

print("1:", monkey_business(20, True))
print("2:", monkey_business(10000, False))