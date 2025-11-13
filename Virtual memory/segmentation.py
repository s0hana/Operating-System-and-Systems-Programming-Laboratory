num_segments = int(input("Enter number of segments: "))
segment_table = {}
for i in range(num_segments):
    base = int(input(f"Enter base address of segment {i}: "))
    limit = int(input(f"Enter size/limit of segment {i}: "))
    segment_table[i] = (base, limit)

seg_num = int(input("Enter segment number: "))
offset = int(input("Enter offset: "))
 
if seg_num in segment_table:
    base, limit = segment_table[seg_num]
    if offset < limit:
        physical_address = base + offset
        print(f"Physical Address: {physical_address}")
    else:
        print("Invalid offset! Exceeds segment size.")
else:
    print("Invalid segment number!")
