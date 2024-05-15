import random


def validate(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3):
    return (a3 and
            a1 != c1 and
            a2 != b3 and
            b3 == c2 and
            b2 != d3 and
            b1 != d1 and
            c3 != d2)

while True:
    propositions = [random.choice([True, False]) for _ in range(12)]
    
    propositions[2] = True
    
    a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3 = propositions
    
    if propositions.count(True) == 6 and validate(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3):
        if not b3 and not c2: #غیر از این دو بقیه درست و غلط بودنشون اهمیت نداره
            print(f"dozd is b :)  |  (a1: {a1}, a2: {a2}, a3: {a3}, b1: {b1}, b2: {b2}, b3: {b3}, c1: {c1}, c2: {c2}, c3: {c3}, d1: {d1}, d2: {d2}, d3: {d3})")
            break

