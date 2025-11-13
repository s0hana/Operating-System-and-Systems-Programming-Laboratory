from tabulate import tabulate
proc_number = int(input("Enter the number of processes: "))
processes = []
for i in range(proc_number):
    name = input(f"Enter the name of the process {i+1}: ")
    at = int(input(f"Enter the arrival time of {name}: "))
    bt = int(input(f"Enter the burst time of {name}: "))
    processes.append({'name': name, 'at': at, 'bt': bt, 'rt': bt})
current_time = 0
completed_count = 0
total_wt = total_tat = 0
gantt = []
result = []
last_proc = None

while completed_count<proc_number:
    available = [p for p in processes if p['at']<=current_time and p['rt']>0]
    if not available:
        current_time+=1
        continue
    next_proc = min(available, key=lambda x : x['rt'])
    if last_proc!=next_proc['name']:
        gantt.append([next_proc['name'], current_time, current_time+1])
    else:
        gantt[-1] = [next_proc['name'], gantt[-1][1], current_time+1]
    next_proc['rt'] -= 1
    current_time+=1
    last_proc = next_proc['name']
    if next_proc['rt']==0:
        tat = current_time - next_proc['at']
        total_tat+=tat
        wt = tat - next_proc['bt']
        total_wt+=wt
        completed_count+=1
        result.append([next_proc['name'], next_proc['at'], next_proc['bt'], wt, tat])
print("Result: ")
print(tabulate(result, headers=['Name', 'Arrival Time', 'Burst Time', 'Waiting Time', 'Turnaround Time'], tablefmt="grid"))
print(f"Average Waiting Time: {total_wt/proc_number:.4f}")
print(f"Average Turnaround Time: {total_tat/proc_number:.4f}")
print(f"Throughput: {proc_number/current_time:.4f}")
names = [p[0] for p in gantt]
times = [p[1] for p in gantt]
times.append(gantt[-1][2])
spaces = [len(p[0]) for p in gantt]
print()
print()
print("Gantt Chart: ")
print(tabulate([names], tablefmt="grid"))
for i in range(len(times)):
    if i>0 and i<=len(times):
        for j in range(spaces[i-1]+2):
            print(" ", end='')
    print(times[i], end='')