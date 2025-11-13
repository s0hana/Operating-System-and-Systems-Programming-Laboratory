from collections import defaultdict

def add_edge(graph, u, v):
    graph[u].append(v)

def is_cyclic_util(node, visited, stack, graph, cycle_nodes):
    visited.add(node)
    stack.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if is_cyclic_util(neighbor, visited, stack, graph, cycle_nodes):
                cycle_nodes.append(neighbor)
                return True
        elif neighbor in stack:
            cycle_nodes.append(neighbor)
            return True

    stack.remove(node)
    return False

def detect_deadlock(graph):
    visited = set()
    stack = set()
    cycle_nodes = []

    for node in list(graph.keys()):
        if node not in visited:
            if is_cyclic_util(node, visited, stack, graph, cycle_nodes):
                return True, cycle_nodes[::-1]
    return False, []


graph = defaultdict(list)

n = int(input("Enter number of processes: "))

print("\nEnter information for each process:")
print("Format example: A R S,T (means A holds R and wants S,T)\n")

for _ in range(n):
    line = input("Process info: ").strip()
    if not line:
        continue
    parts = line.split()
    process = parts[0]
    holds = parts[1] if len(parts) > 1 and parts[1] != "-" else None
    wants = []
    if len(parts) > 2:
        wants = parts[2].split(",")

    if holds:
        add_edge(graph, holds, process)
    for w in wants:
        if w != "-":
            add_edge(graph, process, w)


deadlocked, cycle_nodes = detect_deadlock(graph)

if deadlocked:
    print("\nDeadlock detected!")
    print("Cycle found involving these nodes:", " -> ".join(cycle_nodes))
    processes_involved = [x for x in cycle_nodes if x[0].isalpha() and x[0].isupper()]
    print("Processes involved in deadlock:", ", ".join(processes_involved))
else:
    print("\nNo deadlock detected.")
