process_size = int(input("Enter process size (in bytes): "))
page_size = int(input("Enter page size (in bytes): "))

num_pages = (process_size + page_size - 1) // page_size 

page_table = {} 
print("Enter frame number for each page:")
for i in range(num_pages):
    frame = int(input(f"Frame for page {i}: "))
    page_table[i] = frame

logical_address = int(input("Enter logical address: "))

page_number = logical_address // page_size
offset = logical_address % page_size

if page_number in page_table:
    frame_number = page_table[page_number]
    physical_address = frame_number * page_size + offset
    print(f"Physical Address: {physical_address}")
else:
    print("Invalid logical address! Page not present.")
