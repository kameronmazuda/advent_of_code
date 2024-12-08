import os

DIRNAME = os.path.dirname(__file__)
INPUT_DATA_NAME = "data.txt"
TEST_FILE_PATH = os.path.join(DIRNAME, INPUT_DATA_NAME)

data = [[], []]

with open(TEST_FILE_PATH, 'r') as input:
    data_raw = [line.split() for line in input.readlines()]
    for nums_pair in data_raw:
        data[0].append(int((nums_pair[0])))
        data[1].append(int(nums_pair[1]))


id_copy_count = {}

for i in range(len(data[0])):
    current_id = data[0][i]
    current_id_in_right_list_count = 0
    
    for num in data[1]:
        if num == current_id:
            current_id_in_right_list_count += 1
    
    if data[0][i] not in id_copy_count:
        id_copy_count[data[0][i]] = current_id_in_right_list_count
    
similarity_score = 0
for (id, count) in id_copy_count.items():
    similarity_score += id * count
        
print(similarity_score)