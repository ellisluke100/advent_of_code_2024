import copy

########################### REPORT STUFF ############################ 

def perform_check(report: str) -> bool:
    # Check order
    ascending = all(report[i] < report[i+1] for i in range(len(report)-1))
    descending = all(report[i] > report[i+1] for i in range(len(report)-1))
    
    if not ascending and not descending:
        return False

    valid_diffs = all(1 <= abs(int(report[i]) - int(report[i+1])) <= 3 for i in range(len(report)-1))
    
    if not valid_diffs:
        return False
    
    return True

def is_safe(report: str) -> bool:
    if perform_check(report):
        return True
    else:
        for index, _ in enumerate(report):
            new_report = copy.copy(report)
            del(new_report[index])
            if perform_check(new_report):
                return True

    return False

def analyse_reports(reports: list[str]) -> tuple[int, int]:
    safe_total = 0
    unsafe_total = 0

    for report in reports:
        if is_safe(report):
            safe_total += 1
        else:
            unsafe_total += 1

    return safe_total, unsafe_total

############################ LOAD DATA ##############################

# Read reports
g_reports = []

with open("input.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        report = line.split(' ')
        report[-1] = report[-1].rstrip('\n')
        
        g_reports.append(list(map(int, report)))

safe, unsafe = analyse_reports(g_reports)

print("Total:", len(g_reports))
print("Safe:", safe)
print("Unsafe:", unsafe)