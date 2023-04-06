# Converts Roman numerals to integers

def romanToInt(s):
        romanNum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and romanNum[s[i]] < romanNum[s[i + 1]]:
                result -= romanNum[s[i]]
            else:
                result += romanNum[s[i]]
        return result

def main():
    try:
        prompt = input("Give me a valid Roman numeral. ").upper() # It doesn't matter if the user types in lowercase
        print(romanToInt(prompt))
    except:
        print("Not a valid Roman numeral. ") # If the user's input is not valid, give an error message and try again.
        main()

main()