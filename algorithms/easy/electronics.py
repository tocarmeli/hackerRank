def getMoneySpent(keyboards, drives, b):
    totals = []
    for keyboard in keyboards:
        for drive in drives:
            if keyboard + drive <= b:
                totals.append(keyboard + drive)
    if not totals:
        return -1
    else:
        return max(totals)