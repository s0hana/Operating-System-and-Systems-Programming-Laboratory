from tabulate import tabulate
number_of_pages = int(input("Enter number of pages in reference string: "))
page_seq = input("Enter reference string (space-separated): ").split()[:number_of_pages]
number_of_frames = int(input("Enter number of frames: "))

frames = []
page_faults = []
frame_history = []

for page in page_seq:
    if page in frames:
        frames.remove(page)
        frames.append(page)
        page_faults.append(' ')
    else:
        page_faults.append("PF")
        if len(frames) < number_of_frames:
            frames.append(page)
        else:
            frames.pop(0)
            frames.append(page)
    snapshot = frames.copy()
    while len(snapshot) < number_of_frames:
        snapshot.append('-')
    frame_history.append(snapshot)
table = []
header = ["Frame/Page"] + [f"{p}" for p in page_seq]
for i in range(number_of_frames):
    row = [f"Frame{i+1}"]
    for f in frame_history:
        row.append(f[i])
    table.append(row)
table.append(page_faults)
print("\nSequential graphical presentation of frames (LRU):")
print(tabulate(table, headers=header, tablefmt='grid'))
print(f"\nNumber of page faults: {page_faults.count('PF')}")
