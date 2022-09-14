birth=int(input("Input birthday: "))
mon=input("Input month of birth (e.g. march, july etc): ")
zs=['Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius']
lst=["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
if (mon==lst[0] and birth<21) or (mon==lst[11] and birth>22):
    print(f"Your astrological sign is: {zs[0]}")
elif (mon==lst[1] and birth<20) or (mon==lst[0] and birth>20):
    print(f"Your astrological sign is: {zs[1]}")
elif (mon==lst[2] and birth<21) or (mon==lst[1] and birth>19):
    print(f"Your astrological sign is: {zs[2]}")
elif (mon==lst[3] and birth<21) or (mon==lst[2] and birth>20):
    print(f"Your astrological sign is: {zs[3]}")
elif (mon==lst[4] and birth<22) or (mon==lst[3] and birth>20):
    print(f"Your astrological sign is: {zs[4]}")
elif (mon==lst[5] and birth<22) or (mon==lst[4] and birth>21):
    print(f"Your astrological sign is: {zs[5]}")
elif (mon==lst[6] and birth<23) or (mon==lst[5] and birth>21):
    print(f"Your astrological sign is: {zs[6]}")
elif (mon==lst[7] and birth<24) or (mon==lst[6] and birth>22):
    print(f"Your astrological sign is: {zs[7]}")
elif (mon==lst[8] and birth<24) or (mon==lst[7] and birth>23):
    print(f"Your astrological sign is: {zs[8]}")
elif (mon==lst[9] and birth<24) or (mon==lst[8] and birth>23):
    print(f"Your astrological sign is: {zs[9]}")
elif (mon==lst[10] and birth<23) or (mon==lst[9] and birth>23):
    print(f"Your astrological sign is: {zs[10]}")
elif (mon==lst[11] and birth<23) or (mon==lst[10] and birth>22):
    print(f"Your astrological sign is: {zs[11]}")
else:
    print("No sign")