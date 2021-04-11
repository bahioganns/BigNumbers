def addition(num1, num2):
    result = []
    num1.reverse()
    num2.reverse()

    if len(num1) < len(num2):
        temp = num1
        num1 = num2
        num2 = temp

    balance = 0
    for i in range(0, len(num1)):
        temp = 0
        if i < len(num2):
            temp = int(num1[i]) + int(num2[i]) + balance
        else:
            temp = int(num1[i]) + balance

        if temp >= 10:
            balance = 1
            result.append(temp % 10)
        else:
            balance = 0
            result.append(temp)

    if balance == 1:
        result.append(1)
    return list(reversed(result))


def creation(filein, fileout):
    fin = open(filein)
    fout = open(fileout)

    quantity_of_numbers = int(fin.readline())

    for i in range(quantity_of_numbers):
        line1, line2 = fin.readline().split()
        num1 = [c for c in line1]
        num2 = [c for c in line2]

        result = addition(num1, num2)

        res_line = ""
        for i in range(len(result)):
            res_line += str(result[i])

        compare_line = fout.readline()
        if res_line + "\n" != compare_line:
            print("error in file ", filein)
            return False

    print("Success in file ", filein)
    return True


if __name__ == '__main__':

    creation("sources/in1.txt", "sources/out1.txt")
    creation("sources/in2.txt", "sources/out2.txt")
