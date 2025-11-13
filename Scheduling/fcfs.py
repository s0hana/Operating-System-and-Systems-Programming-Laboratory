from tabulate import tabulate
proc_number = int(input("Enter the number of processes: "))
processes = []
for i in range(proc_number):
    name = input(f"Enter the name of the process {i+1}: ")
    at = int(input(f"Enter the arrival time of {name}: "))
    bt = int(input(f"Enter the burst time of {name}: "))
    processes.append({'name': name, 'at': at, 'bt': bt})
#print(processes)
processes.sort(key=lambda x: x['at'])
result = []
current_time = 0
total_wt = 0
total_tat = 0
gc = []
for p in processes:
    if current_time<p['at']:
        current_time = p['at']
    wt = current_time - p['at']
    total_wt+=wt
    tat = p['bt'] + wt
    total_tat+=tat
    gc.append([p['name'], current_time, current_time+p['bt']])
    result.append([p['name'], p['at'], p['bt'], wt, tat])
    current_time+=p['bt']
print("Result: ")
print(tabulate(result, headers=['Name', 'Arrival Time', 'Burst Time', 'Waiting Time', 'Turnaround Time'], tablefmt="grid"))
print(f"Average Waiting Time: {total_wt/proc_number:.4f}")
print(f"Average Turnaround Time: {total_tat/proc_number:.4f}")
print(f"Throughput: {proc_number/current_time:.4f}")
names = [p[0] for p in gc]
times = [p[1] for p in gc]
times.append(gc[-1][2])
#print(times)
spaces = [len(p[0]) for p in gc]

print("Gantt Chart: ")
print(tabulate([names], tablefmt="grid"))
#print(gc)
for i in range(proc_number+1):
    if i>0 and i<=proc_number:
        for j in range(spaces[i-1]+2):
            print(" ", end='')
    print(times[i], end='')

    