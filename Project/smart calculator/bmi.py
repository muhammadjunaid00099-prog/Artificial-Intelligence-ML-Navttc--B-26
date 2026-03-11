def calculate_bmi(weight, feet, inches):
    height = (feet * 12 + inches) * 0.0254
    bmi_value = weight / (height ** 2)
    return bmi_value


def bmi_category(bmi_value):
    if bmi_value <= 18.5:
        print("You are underweight")
        category = "underweight"
    elif bmi_value <= 25:
        print("You are normal weight")
    elif bmi_value <= 30:
        print("You are overweight")
    else:
        print("You are obese")
    return category
       

