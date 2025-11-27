import converters

centieters = 10
meters = 2
inches = 10
feet = 5

meters_to_centimeters = converters.cm_m(meters)
centimeters_to_meters = converters.m_cm(centieters)
cm_to_inches = converters.cm_inches(centieters)
feet_to_cm = converters.feet_cm(feet)
inches_to_cm = converters.inches_cm(inches)

print(meters_to_centimeters)
print(centimeters_to_meters)
print(cm_to_inches)
print(feet_to_cm)