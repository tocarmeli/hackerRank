def getMoneySpent(keyboards, drives, b):
    total = 0
    for purchase_keyboard in keyboards:
        for purchase_drive in drives:
            if purchase_keyboard + purchase_drive > total:
                total += purchase_keyboard + purchase_drive
            
    print(total)


keyboard = [40, 50, 60]
drive = [5, 8, 12]

print(getMoneySpent(keyboard, drive, 60))