##getBondPrice_E
def getBondPrice_E(face, couponRate, m, yc):
    pv_coupon = 0
    cf = face*couponRate
    for t,y in enumerate(yc,1):
        pv_coupon += (1+y)**-t
        pv_face = (1+yc[-1])**-m
    BondPrice = pv_coupon*cf + pv_face*face
    return(BondPrice)