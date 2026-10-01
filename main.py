import calculator
import messages


def main():
    messages.show_title()
    a = float(input("첫 번째 숫자: "))
    b = float(input("두 번째 숫자: "))
    print("덧셈:", calculator.add(a, b))
    print("뺄셈:", calculator.subtract(a, b))
    print("곱셈:", calculator.multiply(a, b))


if __name__ == "__main__":
    main()
