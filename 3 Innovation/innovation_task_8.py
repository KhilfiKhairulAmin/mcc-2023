with open('innovation.txt', 'r') as fileIn:
  total = 0
  n, m = next(fileIn).split(' ')
  n = int(n)
  m = int(m)

  pairs = []
  while n != 0:
    nth_cards = next(fileIn).split(' ')
    nth_cards = [int(card) for card in nth_cards]
    ab = nth_cards[0] + nth_cards[1]
    abcd = ab + nth_cards[2] + nth_cards[3]
    # (a + b, sum(a, b, c, d))
    pairs.append((ab, abcd))
    n -= 1
  
  desc_abcd = sorted(pairs, key=lambda x: (x[1], x[0]), reverse=True)
  desc_ab = sorted(pairs, key=lambda x: (x[0], x[1]), reverse=True)


  max_outside_ab_range = max(desc_ab[m-1:], key=lambda x: x[1])[1]  

  # Has to resolve based on profit
  while len(desc_abcd) != 0:
    high_abcd = desc_abcd.pop(0)
    index = desc_ab.index(high_abcd)

    if index >= m - 1:
      total += high_abcd[1]
      break

    profit = (desc_ab[m-1][0] - high_abcd[0]) + (high_abcd[1] - max_outside_ab_range)

    if profit > 24: 
      print("Here", index, high_abcd, profit, pairs.index(high_abcd))
      total += high_abcd[1]
      desc_ab.pop(index)
      break
    
  m -= 1

  for i in range(m):
    total += desc_ab.pop(0)[0]
    m -= 1
  
  print(m)
  print(total)
