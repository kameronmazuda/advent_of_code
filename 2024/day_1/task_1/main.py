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

    data[0].sort()
    data[1].sort()

total_sum = 0
for i in range(len(data[0])):
    total_sum += abs(data[0][i] - data[1][i])
       
       
print(total_sum)