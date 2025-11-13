from tabulate import tabulate
number_of_pages = int(input())
page_squ = list(input().split())[:number_of_pages]
number_of_frame = int(input())
page_fault = [' ']
queue = []
frames = []
count_fault = 0
lst_of_frame = ['-']*number_of_frame
for i in page_squ:
    if i in lst_of_frame:
        page_fault.append(' ')
        frames.append(lst_of_frame.copy())
        #print(lst_of_frame)
    else:
        count_fault+=1
        page_fault.append("PF")
        queue.append(i)
        if '-' in lst_of_frame:
            ind = lst_of_frame.index('-')
            lst_of_frame[ind] = i
            frames.append(lst_of_frame.copy())
           # print(lst_of_frame)
        else:
            poped = queue.pop(0)
            ind_key_with_highest = lst_of_frame.index(poped)
            lst_of_frame[ind_key_with_highest] = i
            frames.append(lst_of_frame.copy())
           # print(lst_of_frame)
table = []
header = ["Frame/Page"] + [f"{i}" for i in page_squ]
for i in range(number_of_frame):
    row = [f"Frame{i+1}"]
    for j in range(len(frames)):
        #print(f"i: {i} j: {j}")
        row.append(frames[j][i])
    table.append(row)
table.append(page_fault)
print("Sequential graphical presentation of frame: ")
print(tabulate(tabular_data=table, headers=header, tablefmt='grid'))
print(f"Number of page faults: {count_fault}")