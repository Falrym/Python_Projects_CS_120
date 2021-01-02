def main():
    x = reverse_string(str(input("Enter a random word or sentence: ")))
    reverse_string(x)
    print(x)

def reverse_string(x):
    return x[::-1]

main()
