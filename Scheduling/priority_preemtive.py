from tabulate import tabulate

def gantt_chart(gantt):
    print("\nGantt Chart:")

    for name, start, end in gantt:
        print("+" + "-" * (end - start) * 2, end="")
    print("+")

    for name, start, end in gantt:
        length = (end - start) * 2
        space = length - len(name)
        print("|" + name + " " * space, end="")
    print("|")

    for name, start, end in gantt:
        print("+" + "-" * (end - start) * 2, end="")
    print("+")

    for i, (name, start, end) in enumerate(gantt):
        print(str(start).ljust((end - start) * 2 + 1), end="")
    print(gantt[-1][2])

def priority_preemptive(processes):
    proc_number = len(processes)
    current_time = 0
    completed_count = 0
    total_wt = total_tat = 0
    gantt = []
    result = []
    n = proc_number

    bt_left = [p['bt'] for p in processes]
    completion_time = [0] * n

    while completed_count < proc_number:
        available = [i for i in range(n) if processes[i]['at'] <= current_time and bt_left[i] > 0]
        if not available:
            current_time += 1
            continue

        idx = min(available, key=lambda x: processes[x]['priority'])

        if not gantt or gantt[-1][0] != processes[idx]['name']:
            gantt.append([processes[idx]['name'], current_time, current_time+1])
        else:
            gantt[-1][2] += 1

        bt_left[idx] -= 1
        current_time += 1

        if bt_left[idx] == 0:
            completed_count += 1
            completion_time[idx] = current_time
            tat = completion_time[idx] - processes[idx]['at']
            wt = tat - processes[idx]['bt']
            total_tat += tat
            total_wt += wt
            result.append([processes[idx]['name'], wt, tat])

    avg_wt = total_wt / proc_number
    avg_tat = total_tat / proc_number
    throughput = proc_number / current_time

    return result, gantt, avg_wt, avg_tat, throughput


if __name__ == "__main__":
    proc_number = int(input("Enter number of processes: "))
    processes = []
    for i in range(proc_number):
        name = input(f"Process {i+1} name: ")
        at = int(input(f"Arrival time of {name}: "))
        bt = int(input(f"Burst time of {name}: "))
        pr = int(input(f"Priority of {name} (smaller = higher): "))
        processes.append({'name': name, 'at': at, 'bt': bt, 'priority': pr})

    result, gantt, avg_wt, avg_tat, throughput = priority_preemptive(processes)

    print("\nResult Table:")
    print(tabulate(result, headers=['Process','WT','TAT'], tablefmt="grid"))
    print(f"\nAverage WT: {avg_wt:.2f}")
    print(f"Average TAT: {avg_tat:.2f}")
    print(f"Throughput: {throughput:.4f}")

    gantt_chart(gantt)
