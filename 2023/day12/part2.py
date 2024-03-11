cache = {}

with open('./input.txt', 'r')as file:
    lines = file.read().split('\n')

def count(hot_spring, nums):
    if hot_spring == "":
        return 1 if nums == () else 0
    
    if nums == ():
        return 0 if "#" in hot_spring else 1
    
    key = (hot_spring, nums)

    if key in cache:
        return cache[key]

    result = 0

    if hot_spring[0] in '.?':
        result += count(hot_spring[1:], nums)

    if hot_spring[0] in "#?":
        if nums[0] <= len(hot_spring) and '.' not in hot_spring[:nums[0]] and (nums[0] == len(hot_spring) or hot_spring[nums[0]] != "#"):
            result += count(hot_spring[nums[0] + 1:], nums[1:])

    cache[key] = result

    return result

total = 0

for line in lines:
    hot_spring, nums = line.split()
    nums = tuple(map(int, nums.split(',')))

    hot_spring = "?".join([hot_spring] * 5)
    nums *= 5

    total += count(hot_spring, nums)

print(total)
