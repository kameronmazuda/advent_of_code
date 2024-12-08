import os

DIRNAME = os.path.dirname(__file__)
INPUT_DATA_NAME = "data.txt"
TEST_FILE_PATH = os.path.join(DIRNAME, INPUT_DATA_NAME)

data = []
with open(TEST_FILE_PATH, 'r') as input:
    data = [line.split() for line in input.readlines()]
    data = [[int(num) for num in num_arr] for num_arr in data]


def report_is_safe(report, isRemoving):
    is_safe = True
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
            is_safe = False
            break
        elif difference < 0:
            if not wasIncreasing:
                if isRemoving:
                    try:
                        i = report.index(level)
                        modified_report = report[:i] + report[i+1:]
                        is_safe = report_is_safe(modified_report, False)
                        if not is_safe:
                            i = report.index(prev_level)
                            modified_report = report[:i] + report[i+1:]
                            is_safe = report_is_safe(modified_report, False)
                    except Exception as e:
                        print(report)
                        print(e)
                else:
                    is_safe = False
                    break
            wasIncreasing = True
        else:
            if wasIncreasing:
                if isRemoving:
                    try:
                        i = report.index(level)
                        modified_report = report[:i] + report[i+1:]
                        is_safe = report_is_safe(modified_report, False)
                        if not is_safe:
                            i = report.index(prev_level)
                            modified_report = report[:i] + report[i+1:]
                            is_safe = report_is_safe(modified_report, False)
                    except Exception as e:
                        print(report)
                        print(e)
                else:
                    is_safe = False
                    break
            wasIncreasing = False
        
        if 1 <= abs(difference) <= 3:
            prev_level = level
        else:
            is_safe = False
            break
    
    return is_safe


safe_reports_count = 0
for report in data:
    if report_is_safe(report, isRemoving=True):
        safe_reports_count += 1

print(safe_reports_count)
    
