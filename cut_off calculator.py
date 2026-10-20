
print("_________________________")
print("Find your cut off")
print("__________________________")

try:
    maths = int(input("Enter your maths mark: "))
    phy = int(input("Enter your physics mark: "))
    che = int(input("Enter your chemistry mark: "))

except ValueError:
    print("Invalid input! Please enter numbers only.")

else:
    marks = [maths, phy, che]
    subject = ["maths", "physics", "chemistry"]

    valid = True

    for k in range(len(marks)):
        if marks[k] < 0 or marks[k] > 100:
            print(f"Invalid mark for {subject[k]}")
            print(f"And the mark is {marks[k]}")
            valid = False

    def cut_off(maths, phy, che):
        a = phy / 2
        b = che / 2
        c = a + b
        d = maths + c
        return d

    if valid:
        if maths >= 35 and phy >= 35 and che >= 35:
            print(f"Your mark in maths: {maths}")
            print(f"Your mark in physics: {phy}")
            print(f"Your mark in chemistry: {che}")
            print("Your cut off:", cut_off(maths, phy, che))

        else:
            count = 0
            passed = 0

            print("__________FAILED__________")

            for i in range(3):
                if marks[i] < 35:
                    print(f"Your failed subject is {subject[i]}")
                    print(f"Your mark is {marks[i]}")
                    count += 1

            print("__________PASSED__________")

            for j in range(3):
                if marks[j] >= 35:
                    print(f"Your passed subject is {subject[j]}")
                    print(f"Your mark is {marks[j]}")
                    passed += 1

            print("_________________________")
            print("Total subjects passed:", passed)
            print("Total subjects failed:", count)