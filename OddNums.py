def unpaired_val(a):
    no_pair = []
    pairs = []
    passes = []
    for i in range(len(a)):
        if i in passes:
            continue
        else:
            try:
                if a[i] == a[i + 2]:
                    pairs.append((a[i], a[i + 2]))
                    passes.append(i + 2)
                else:
                    no_pair.append(a[i])
            except IndexError:
                no_pair.append(a[i])

    if len(no_pair) <= 1:
        unpaired = no_pair[0]
    else:
        unpaired = no_pair

    return unpaired


print(unpaired_val([9, 3, 9, 3, 6, 7, 9]))
