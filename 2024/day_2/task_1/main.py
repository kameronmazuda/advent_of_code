import os

DIRNAME = os.path.dirname(__file__)
INPUT_DATA_NAME = "data.txt"
TEST_FILE_PATH = os.path.join(DIRNAME, INPUT_DATA_NAME)

data = []
with open(TEST_FILE_PATH, 'r') as input:
    data = [line.split() for line in input.readlines()]
    data = [[int(num) for num in num_arr] for num_arr in data]

safe_reports_count = 0
for report in data:
    safe = True
    wasIncreasing = False
    prev_level = report[0]
    first_time = True
    for level in report[1:]:
        
        difference = prev_level - level
        if first_time:
            if difference > 0:
                wasIncreasing = False
            elif difference < 0:
                wasIncreasing = True
            
            first_time = False
        
        if difference == 0:
            safe = False
            break
        elif difference < 0:
            if not wasIncreasing:
                safe = False
                break
            wasIncreasing = True
        else:
            if wasIncreasing:
                safe = False
                break
            wasIncreasing = False
        
        if 1 <= abs(difference) <= 3:
            prev_level = level
        else:
            safe = False
            break
            
    if safe:
        safe_reports_count += 1
        print(report)

print(safe_reports_count)
    
