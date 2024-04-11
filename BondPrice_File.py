def getBondPrice(y, face, couponRate, m, ppy=1):
    pv = 0
    cf = face*couponRate/ppy
    for i in range(1, m*ppy + 1):
        pv += (1+y/ppy)**-i
    bondPrice = pv*cf + face*(1+y/ppy)**(-m*ppy)
    return(bondPrice)
