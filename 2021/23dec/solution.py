move_cost = { 'A': 1, 'B': 10, 'C': 100, 'D': 1000 }

def is_end(state):
    sz = len(state) // 4
    result = True
    for y in range(1, sz+1):
        result &= state.get((2, y)) == 'A' 
        result &= state.get((4, y)) == 'B' 
        result &= state.get((6, y)) == 'C' 
        result &= state.get((8, y)) == 'D' 
    return result

assert is_end({(2,1): 'A', (4, 1): 'B', (6,1): 'C', (8,1): 'D'})
assert not is_end({ (2, 1): 'B', (2, 2): 'A', (4, 1): 'C', (4, 2): 'D', (6, 1): 'D', (6, 2): 'A' })

init_state = { (2, 1): 'B', (2, 2): 'A', (4, 1): 'C', (4, 2): 'D', (6, 1): 'B', (6, 2): 'C', (8, 1): 'D', (8, 2): 'A' }

def manh_dist(from_, to):
    (fx, fy) = from_
    (tx, ty) = to
    return abs(fx-tx) + abs(fy-ty)

def cost(from_, to, letter):
    return move_cost.get(letter) * manh_dist(from_, to) 

slot_left = [(1, 0), (0, 0)]
slot_right = [(9, 0), (10, 0)]
slotA = [(2, 1), (2, 2), (2, 3), (2, 4)]
slotB = [(4, 1), (4, 2), (4, 3), (4, 4)]
slotC = [(6, 1), (6, 2), (6, 3), (6, 4)]
slotD = [(8, 1), (8, 2), (8, 3), (8, 4)]
spaceAB = (3,0)
spaceBC = (5,0)
spaceCD = (7,0)
home_slots = {'A': slotA, 'B': slotB, 'C': slotC, 'D':slotD}
all_slots = [slotA, slotB, slotC, slotD]
hallway = [(x, 0) for x in range(0, 11)]

def can_go_home(letter, state):
    home_slot = home_slots.get(letter)
    return all(state.get(xy, letter) == letter for xy in home_slot)

def first_am_in_slot(slot, state):
    for xy in slot:
        if xy in state:
            return xy

def first_free_in_slot(slot, state):
    for xy in slot:
        if xy not in state:
            return xy

#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########

def possible_moves(state):
    moves = []

    if fromxy := state.get(first_am_in_slot(slot_left)):
        if toxy := first_free_in_slot(slotA):
            moves.append((fromxy, toxy))

        if spaceAB not in state:
            if toxy := first_am_in_slot(slotB):
                moves.append((fromxy, toxy))

            if spaceBC not in state:
                if toxy := first_am_in_slot(slotC):
                    moves.append((fromxy, toxy))

                if spaceBC not in state:
                    if toxy := first_am_in_slot(slotC):
                        moves.append((fromxy, toxy))

    return moves

def solve(state, path):
    if is_end(state):
        return [path]

    for cost_move in sorted(possible_moves(state)):
        if (new_path := solve(do_move(state, cost_move), path + [cost_move])):
            return new_path 

def do_move(state, cost_move):
    _, from_, to_ = cost_move
    new_state = state.copy()
    new_state[to_] = state[from_]
    del new_state[from_]
    return new_state

solve(init_state, [])