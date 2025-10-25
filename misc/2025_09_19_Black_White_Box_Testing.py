from PIL import Image

def calculate_grade(score):
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        return "Invalid score. Please enter a number between 0 and 100."

    if score >= 90:

        return "A"

    elif score >= 80:

        return "B"

    elif score >= 70:

        return "C"

    elif score >= 60:

        return "D"

    else:

        return "F"


def main():
    try:

        score = float(input("Enter your numeric score (0-100): "))

        grade = calculate_grade(score)

        print(f"Your letter grade is: {grade}")
        im = Image.open('/home/gabriel/Downloads/kill7billion.png')
        im.show()

    except ValueError:

        print("Please enter a valid number.")


if __name__ == "__main__":
    main()