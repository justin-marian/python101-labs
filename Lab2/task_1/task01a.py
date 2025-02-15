def task1a(nums):
    '''
    nums -> vector int
    return -> vector int

    Dublati elementele care se divid cu 6, iar pe cele 
    care nu se divid, triplati-le folosind functionale
    '''
    return [x * 2 if x % 6 == 0 else x * 3 for x in nums]
