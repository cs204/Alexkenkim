def main ():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter (v):
    res = 0.0
    v = v.split(sep = '.')
    for i in range(len(v[0])):
        res = res + (float(v[0][i])*(10**(len(v[0])-(i+1))))

    for i in range(len(v[1])):
        if (v[1][i].isdigit()):
            res = res + ((float(v[1][i]))/10**(i+1))

    res = res * 0.3048
    return res


main()
