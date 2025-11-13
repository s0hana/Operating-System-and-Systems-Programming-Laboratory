def deadlock_detection(E, A, C, R):
    num_processes = len(C)
    num_resources = len(E)
    
    marked = [False] * num_processes
    changed = True
    while changed:
        changed = False
        for i in range(num_processes):
            if not marked[i]:
                can_proceed = all(R[i][j] <= A[j] for j in range(num_resources))
                if can_proceed:
                    for j in range(num_resources):
                        A[j] += C[i][j]
                    marked[i] = True
                    changed = True
    
    deadlocked_processes = [i for i, m in enumerate(marked) if not m]
    
    if deadlocked_processes:
        print("Deadlocked Processes:", deadlocked_processes)
    else:
        print("\nNo deadlock detected.")

num_processes = int(input("Enter number of processes: "))
num_resources = int(input("Enter number of resource types: "))
E = list(map(int, input(f"Enter total instances of each resource ({num_resources} values): ").split()))
A = list(map(int, input(f"Enter available instances of each resource ({num_resources} values): ").split()))
C = []
print("Enter Current Allocation Matrix (one row per process):")
for i in range(num_processes):
    row = list(map(int, input(f"P{i} allocation: ").split()))
    C.append(row)
R = []
print("Enter Request Matrix (one row per process):")
for i in range(num_processes):
    row = list(map(int, input(f"P{i} request: ").split()))
    R.append(row)
deadlock_detection(E, A, C, R)
