report = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

percentage = {}
for state in report:
    percentage[state] = (report[state]/sum(report.values()))*100

print(percentage)