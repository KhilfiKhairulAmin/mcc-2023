with open(f'collatz.txt') as fileIn:
  k = int(next(fileIn).split(' ')[1])
  nums = next(fileIn).split(' ')
  
while k != 0:
  for i in range(len(nums)):
    nums[i] = int(nums[i])
    if nums[i] % 2 == 1:
      # odd number = 3a + 1
      nums[i] = 3 * nums[i] + 1
    else:
      # even number = a / 2
      nums[i] /= 2
  k -= 1

print(int(sum(nums)))
