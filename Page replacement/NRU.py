from tabulate import tabulate
number_of_pages = int(input())
page_squ = list(input().split())[:number_of_pages]
number_of_frame = int(input())
page_fault = [' ']
queue = []
frames = []
count_fault = 0
lst_of_frame = ['-']*number_of_frame
bit_flag = [0]*number_of_frame
ref_bit = []
_i_ = 0
for i in page_squ:
    if '-' in lst_of_frame:
        lst_of_frame[_i_] = i
        queue.append(i)
        frames.append(lst_of_frame.copy())
        page_fault.append(' ')
        _i_+=1
    if _i_>number_of_frame:
        break


for ueor in page_squ[_i_:]:
    if ueor in lst_of_frame:
        page_fault.append(' ')
        frames.append(lst_of_frame.copy())
        ind_i = lst_of_frame.index(ueor)
        #print(f"Printing i of not fault: {i} index in lst_of_frame {ind_i}")
        #ref_bit.append(bit_flag.copy())
        #print(lst_of_frame)
    else:
        count_fault+=1
        page_fault.append("PF")
        queue.append(ueor)
        rm = []
        print("Page fault detected, input reference bit and modified bit: ")
        for __i in range(number_of_frame):
            r, m = map(int, input().split())
            if r==0 and m==0:
                rm.append(0)
            elif r==0 and m==1:
                rm.append(1)
            elif r==1 and m==0:
                rm.append(2)
            else:
                rm.append(3)
        _min = min(rm)
        ___ind = rm.index(_min)
        lst_of_frame[___ind] = ueor
        frames.append(lst_of_frame.copy())



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
for i in range(len(frames)):
    print(frames[i])
