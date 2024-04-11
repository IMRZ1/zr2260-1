##getBondPrice_Z
def getBondPrice_Z(face, couponRate, times, yc):
    pv_coupon = 0
    cf = face*couponRate
    for t,y in zip(times,yc):
        pv_coupon += (1+y)**-t
        pv_face = (1+yc[-1])**-times[-1]
    bondPrice = pv_coupon*cf + pv_face*face
    return(bondPrice)