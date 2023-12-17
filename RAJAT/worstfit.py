def worstfit(block, process):
    block.sort(reverse=True)
    process.sort()
    d = {}
    for i in process:
        for j in block:
            if i <= j and j not in d.values():
                d[i] = j
                break
    print(d)
block = [100, 500, 200, 300, 600]
process = [212, 417, 112, 426]
worstfit(block, process)
