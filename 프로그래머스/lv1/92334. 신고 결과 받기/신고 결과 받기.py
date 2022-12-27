def solution(id_list, report, k):
    report = set(report)
    idict = {}
    answer = {}
    report_list = []

    for i in id_list:
        idict[i] = 0
        answer[i] = 0

    for i in report:
        report_list.append(i.split(' '))

    for i in report_list:
        idict[i[1]] += 1

    ans = [i for i in id_list if idict[i] >= k]

    for i in report_list:
        if i[1] in ans:
            answer[i[0]] += 1

    return list(answer.values())  