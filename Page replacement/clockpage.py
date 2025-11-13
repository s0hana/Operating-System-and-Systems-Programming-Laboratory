num_pages = int(input("Number of pages:"))
ref_string = list(map(int, input("Reference string:").split()))
num_frames = int(input("Number of frames:"))

memo = [' '] * num_frames
reference = [0] * num_frames
pointer = 0
ref = []

table = []
total_page_fails = 0

for page in ref_string:
    pf = 0
    
    if page not in memo:
        pf = 1
        total_page_fails += 1
        
        if ' ' in memo:
            memo[memo.index(' ')] = page
        else:
            reference = list(map(int, input(f"Reference bits for inserting {page}:").split()))
            
            while True:
                if reference[pointer] == 0:
                    memo[pointer] = page
                    reference[pointer] = 1
                    pointer = (pointer + 1) % num_frames
                    break
                else:
                    reference[pointer] = 0
                    pointer = (pointer + 1) % num_frames
    else:
        page_index = memo.index(page)
        reference[page_index] = 1
    
    if pf:
        pf = "PF|"
    else:
        pf = "  |"

    table.append([str(page) + ' |'] + ["- |"] + [str(c) + " |" for c in memo] + ["- |"] + [pf])
    
    print("Frames:\t\t  ", memo)
    print("Reference Bits:   ", reference)
    print("Pointer at:\t   ", pointer)
    
    print()
    
    ref.append(reference.copy())

table.insert(0, ['|' for i in range(num_frames + 4)])

table.insert(0, ["Frame/Page"] + ["-" * 10] + [(str(i) + " " * (10 - len(str(i)))) for i in range(1, num_frames + 1)] + ["-" * 10] + ["Page Fail "])

table = [list(row) for row in zip(*table)]

print('-' * (len(''.join(table[0])) + len(table[0])))

for row in table:
    print(*row)
    
print('-' * (len(''.join(table[0])) + len(table[0])))

ref = [list(row) for row in zip(*ref)]

print("Total page fails =", total_page_fails)