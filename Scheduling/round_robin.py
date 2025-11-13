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
    

def round_robin(processes, quantum):
    proc_number = len(processes)
    bt_left = [p['bt'] for p in processes]
    current_time = 0
    completed_count = 0
    total_wt = total_tat = 0
    gantt = []
    result = []
    completion_time = [0] * proc_number

    ready_queue = []
    visited = [False] * proc_number

    while completed_count < proc_number:
        for i in range(proc_number):
            if processes[i]['at'] <= current_time and not visited[i]:
                ready_queue.append(i)
                visited[i] = True

        if not ready_queue:
            current_time += 1
            continue

        idx = ready_queue.pop(0)
        exec_time = min(quantum, bt_left[idx])

        gantt.append([processes[idx]['name'], current_time, current_time+exec_time])
        bt_left[idx] -= exec_time
        current_time += exec_time

        for i in range(proc_number):
            if processes[i]['at'] <= current_time and not visited[i]:
                ready_queue.append(i)
                visited[i] = True

        if bt_left[idx] > 0:
            ready_queue.append(idx)
        else:
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
        processes.append({'name': name, 'at': at, 'bt': bt})

    q = int(input("Enter Time Quantum: "))
    result, gantt, avg_wt, avg_tat, throughput = round_robin(processes, q)

    print("\nResult Table:")
    print(tabulate(result, headers=['Process','WT','TAT'], tablefmt="grid"))
    print(f"\nAverage WT: {avg_wt:.2f}")
    print(f"Average TAT: {avg_tat:.2f}")
    print(f"Throughput: {throughput:.4f}")

    gantt_chart(gantt)