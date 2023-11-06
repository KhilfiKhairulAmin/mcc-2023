'''
**NOTE
The solution isn't correct.
For this problem, I completed Task 1 to Task 4 using simple logic and some simple calculations.
For Task 5, this is my best take yet to solve it. But it is not completed.
'''

with open('rectangles.txt', 'r') as file:
  N, K = next(file).split(' ')
  N = int(N)
  K = int(K)

  rects = []
  for line in file:
    h, w = [int(num) for num in line.split(' ')]
    rects.append((h, w))
  
  # Start with assumption K = N
  minimum_blue_area = sum(rect[0] * rect[1] for rect in rects)

  for _ in range(0, N-K):
    if len(rects) == 2:
      # print(rects)
      rects[0] = (max(rects[0][0], rects[1][0]), sum([rects[0][1], rects[1][1]]))
      rects.pop(1)
      minimum_blue_area = rects[0][0] * rects[0][1]
      break

    targets = []
    
    for j in range(len(rects)):

      cur = rects[j]
      right_h = float('inf')
      left_h = float('inf')
      right = j + 1
      if right != len(rects): 
        if rects[right][0] >= rects[j][0]:
          right_h = rects[right][0]
      left = j - 1
      if j != -1:
        if rects[left][0] >= rects[j][0]:
          left_h = rects[left][0]

      minimum = min([right_h, left_h])

      if minimum == float('inf'):
        continue
      elif minimum == right_h:
        targets.append((j, right))
      else:
        targets.append((j, left))

    # print(targets)
    # print(rects)

    smallest_area = float('inf')

    target_j = 0
    for i in range(len(targets)):
      excess_area = abs(rects[targets[i][0]][0] - rects[targets[i][1]][0]) * (rects[targets[i][0]][1] + rects[targets[i][1]][1])
      if excess_area < smallest_area:
        smallest_area = excess_area
        target_j = i
    
    # if len(targets) == 0:
    #   continue

    rects[targets[target_j][0]] = (max(rects[targets[target_j][0]][0], rects[targets[target_j][1]][0]), sum([rects[targets[target_j][0]][1], rects[targets[target_j][1]][1]]))
    rects.pop(targets[target_j][1])
    # print(smallest_area)
    minimum_blue_area += smallest_area
    # print(rects)

  print(minimum_blue_area)





      


# from collections import Counter

# with open('rectangle.txt', 'r') as file:
#   K = int(next(file).split(' ')[1])

#   rects = []
#   for line in file: 
#     h, w = [int(num) for num in line.split(' ')]
#     rects.append((h, w))
  
#   h_arr = sorted(rects, key=lambda x: x[0], reverse=True)
#   stack_h = []

#   # print(Counter([h[0] for h in rects]))

#   copy = [h[0] for h in rects]

#   h_vals = set()

#   while K != 0:

#     h_val = h_arr.pop(0)
#     index_max_h = rects.index(h_val)
#     h_val = h_val[0]

#     if h_val in h_vals:
#       h_val = h_arr.pop(0)
#       index_max_h = rects.index(h_val)
#       h_val = h_val[0]

#     stack_h.insert(0, index_max_h)
#     h_vals.add(h_val)
#     K -= 1

#   total_blue_area = 0
#   hasVisited = set()
#   print(len(stack_h))
  
#   for _ in range(len(stack_h)):
#     index = stack_h.pop(0)

#     # print(index)
#     cur_rect = rects[index]

#     total_width = cur_rect[1]
#     hasVisited.add(index)
#     right = index + 1

#     while (right != len(rects)) and (right not in hasVisited) and (rects[right][0] <= cur_rect[0]):
#       total_width += rects[right][1]
#       hasVisited.add(right)
#       right += 1
#     left = index - 1
#     while (left not in hasVisited) and (rects[left][0] <= cur_rect[0]):
#       total_width += rects[left][1]
#       hasVisited.add(left)
#       left -= 1
#       if left == -1:
#         break
#     total_blue_area += total_width * rects[index][0]
#     # print(total_blue_area, total_width, rects[index][0])

#   print(hasVisited)
#   print(total_blue_area)



  
  
  # total_area = 0
  # if w_before < w_after:
  #   total_area = heights[highest] * (w_before + widths[highest])
  # else:
  #   total_area = heights[highest] * (w_after + widths[highest])

  # heights.pop(highest)
  # widths.pop(highest)


  # print(heights[highest])
  
  # if w_before < w_after:
  #   total_area += heights[highest] * w_after
  # else:
  #   total_area += heights[highest] * w_before

  # print(total_area)
  