with open("numbers.txt", "r") as file:
    lines = file.readlines()

left_list = []
right_list = []

for line in lines:
    left, right, _ = map(int, line.split()) 
    left_list.append(left)
    right_list.append(right)

right_counts = {}
for num in right_list:
    if num in right_counts:
        right_counts[num] += 1
    else:
        right_counts[num] = 1

total_similarity_score = 0

for num in left_list:
    if num in right_counts:
        total_similarity_score += num * right_counts[num]

print("Total similarity score:", total_similarity_score)