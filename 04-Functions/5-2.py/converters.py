def m_cm(cm):
    m = cm / 100
    return m
    
def cm_m(m):
    cm = m * 100
    return cm

def cm_inches(cm):
    inches = cm / 2.54
    return inches

def feet_inches_cm(feet, inches):
    cm_feet = feet*30.48
    cm_inches = inches * 2.54
    return cm_feet + cm_inches

