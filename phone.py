def phone_formats():
    phone = "5556665555"
    area_code = phone[0:3]
    middle = phone[3:6]
    last_four = phone[6:]
    return "({}){}-{}".format(area_code, middle, last_four)

print(phone_formats())
