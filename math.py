def binary_search(x, a):
    i = 0                   # i is the left endpoint (Python uses 0-based indexing)
    j = len(a)              # j is the right endpoint (exclusive in Python)
    
    while i < j:
        m = (i + j) // 2    # floor division to get middle index
        if x > a[m]:
            i = m + 1
        else:
            j = m

    if i < len(a) and a[i] == x:
        location = i + 1    # +1 to match the image's 1-based indexing
    else:
        location = 0        # not found

    return location         # location is the position or 0 if not found
