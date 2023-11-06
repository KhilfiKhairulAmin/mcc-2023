out = ''

with open('mobile game.txt', 'r') as fileIn:
  n_case = int(next(fileIn))
  while n_case != 0:
    A, B = next(fileIn).split(' ')[1:]
    A = int(A)
    B = int(B)
    P = next(fileIn).split(' ')
    P = [int(p) for p in P]

    min_kill = 0

    while A < B:
      min_diff = A
      p_i = -1
      for i in range(len(P)):
        diff = A - P[i]
        if diff > 0 and diff < min_diff:
          min_diff = diff
          p_i = i
      
      if min_diff == A:
        min_kill = -1
        break

      A += P.pop(p_i)
      min_kill += 1

    print(min_kill)
    out += f'{min_kill}\n'
    n_case -= 1
  fileIn.close()

out = out[:-1]

with open('output.txt', 'w') as fileOut:
  fileOut.write(out)
  fileOut.close()
  