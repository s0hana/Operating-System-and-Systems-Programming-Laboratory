from tabulate import tabulate
number_of_pages = int(input())
page_squ = list(map(int, input().split()))[:number_of_pages]
number_of_frame = int(input())
lst_frame = ['-', '-', '-']
page_fault_count = 0
frame = []
page_fault = [" "]
for ind, k in enumerate(page_squ):
    if str(k) in lst_frame:
        frame.append(lst_frame.copy())
        page_fault.append(" ")
        continue
    else:
        page_fault_count+=1
        if '-' in lst_frame:
            i = lst_frame.index('-')
            lst_frame[i] = str(k)
            frame.append(lst_frame.copy())
            page_fault.append("PF")
        else:
            _to_be_replaced_with = -1
            _higst_ind = -1
            temp_page_squ = page_squ[ind+1:]
            for _i, _p in enumerate(lst_frame):
                if int(_p) in temp_page_squ:
                    if temp_page_squ.index(int(_p))>_higst_ind:
                        _higst_ind = temp_page_squ.index(int(_p))
                        _to_be_replaced_with = _i
                else:
                    _to_be_replaced_with = _i
                    break
            lst_frame[_to_be_replaced_with] = str(k)
            frame.append(lst_frame.copy())
            page_fault.append("PF")
table = []
header = ["Frame/Page"] + [f"{i}" for i in page_squ]
for i in range(number_of_frame):
    row = [f"Frame{i+1}"]
    for j in range(number_of_pages):
        row.append(frame[j][i])
    table.append(row)
table.append(page_fault)
print("Sequential graphical presentation of frame: ")
print(tabulate(tabular_data=table, headers=header, tablefmt='grid'))
print(f"Number of page faults: {page_fault_count}")