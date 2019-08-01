
# create a list of my favorite numbers
nums = [1, 3, 20, 42, 60, 100]
print(nums)

# change all elements in the list
for index in range(len(nums)):
    nums[index] += 10

print(nums)

for num in nums:
    num += 10

print(nums)

# use a list of booleans to show thumbs up or down
thumbs = [True, True, False, True, False, False, False]

for thumb in thumbs:
    if thumb:
        print("Thumbs up!")
    else:
        print("Thumbs down!")