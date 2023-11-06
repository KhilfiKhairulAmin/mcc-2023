class Node:
  def __init__(self) -> None:
    self.run = 1
    self.cardNeeded = 0

with open('tichu.txt', 'r') as line:
  cards_available = int(next(line).split(' ')[1])

  nums = next(line).split(' ')
  nums = [int(num) for num in nums]
  nums = sorted(list(set(nums)))
  
  runs: list[Node] = []

  node = Node()
  for i in range(0, len(nums) - 1):
    if nums[i+1] - nums[i] == 1: # Confirmed run :)
      node.run += 1
    else: # Not run :(
      node.cardNeeded = nums[i+1] - nums[i] - 1
      runs.append(node)
      node = Node()
  
  runs.append(node)

  highest_runs = 1
  for i in range(len(runs)):
    cur_run = 0
    cards = cards_available
    for j in range(i, len(runs)):
      cur_run += runs[j].run
      needed = runs[j].cardNeeded
      if cards >= needed:
        cards -= needed
        cur_run += needed
      else:
        cur_run += cards
        if cur_run > highest_runs:
          highest_runs = cur_run
        break

  print(highest_runs)
