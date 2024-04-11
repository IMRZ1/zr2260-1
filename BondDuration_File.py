##getBondDuration
def getBondDuration(y, face, couponRate, m, ppy=1):
    pv = 0
    cf = face*couponRate/ppy
    pvcf_coupon = 0
    for i in range(1, m*ppy + 1):
        pv += (1+y/ppy)**-i
        pvcf_coupon += ((1+y/ppy)**-i)*cf*(i)
    bondPrice = pv*cf + face*(1+y/ppy)**(-m*ppy)
    pvcf_face = ((1+y/ppy)**(-m*ppy))*face*(m*ppy)
    w = pvcf_coupon + pvcf_face
    bondDuration = w/bondPrice
    return(bondDuration)
