def calculate_bmr(weight, height, age, gender, body_fat_percentage):
    if gender.lower() == "чоловік":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender.lower() == "жінка":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Стать повинна бути 'чоловік' або 'жінка'")

    bmr *= 1.0 - (body_fat_percentage / 100)

    return bmr


def calculate_goal_calories(bmr, activity_level, goal_option):
    goal_multiplier = {
        "хороша форма": 1.0,
        "схуднути": 0.8,
        "набрати масу": 1.2
    }

    if activity_level.lower() == "низька":
        activity_multiplier = 1.2
    elif activity_level.lower() == "помірна":
        activity_multiplier = 1.35
    elif activity_level.lower() == "середня":
        activity_multiplier = 1.55
    elif activity_level.lower() == "висока":
        activity_multiplier = 1.725
    else:
        raise ValueError("Неправильний рівень активності. Виберіть між 'низька', 'помірна', 'середня' або 'висока'")
    return round(bmr * activity_multiplier * goal_multiplier[goal_option])


def calculate_nutrition_goal(calories_per_day):
    protein_percentage = 25
    fat_percentage = 30
    carb_percentage = 45

    protein_grams = (protein_percentage / 100) * calories_per_day / 4  # 1г білка = 4ккал
    fat_grams = (fat_percentage / 100) * calories_per_day / 9  # 1г жиру = 9ккал
    carb_grams = (carb_percentage / 100) * calories_per_day / 4  # 1г вуглеводів = 4ккал

    return round(protein_grams, 2), round(fat_grams, 2), round(carb_grams, 2)


def main():
    def validate_age(age):
        if age <= 10 or age > 100:
            raise ValueError("Введіть вірне число")
        return age

    def validate_weight(weight):
        if weight <= 0 or weight > 595:
            raise ValueError("Вага не може бути від'ємною")
        return weight

    def validate_height(height):
        if height <= 0:
            raise ValueError("Зріст не може бути від'ємним")
        return height

    def validate_gender(gender):
        if gender.lower() not in ['чоловік', 'жінка']:
            raise ValueError("Введіть вірну стать")
        return gender

    def validate_activity_level(activity_level):
        if activity_level.lower() not in ['мала', 'помірна', 'середня', 'висока']:
            raise ValueError("Введіть вірний рівень активності")
        return activity_level

    def validate_body_fat_percentage(body_fat_percentage):
        if body_fat_percentage <= 0 or body_fat_percentage > 100:
            raise ValueError("Індекс жиру в тілі має бути від 0 до 100%")
        return body_fat_percentage

    def validate_goal_option(goal_option):
        if goal_option.lower() not in ['хороша форма', 'схуднути', 'набрати масу']:
            raise ValueError("Введіть вірну мету")
        return goal_option

    def validate_goal_weight(goal_weight):
        if goal_weight <= 30:
            raise ValueError("Цільова вага не є вірною")
        return goal_weight

    try:
        age = validate_age(int(input("Введіть вік: ")))
        weight = validate_weight(float(input("Введіть вагу: ")))
        height = validate_height(float(input("Введіть зріст: ")))
        gender = validate_gender(input("Введіть стать (чоловік/жінка): "))
        activity_level = validate_activity_level(input("Введіть рівень активності (мала/помірна/середня/висока): "))
        body_fat_percentage = validate_body_fat_percentage(float(input("Введіть індекс жиру в тілі (%): ")))
        goal_option = validate_goal_option(input("Введіть вашу мету (хороша форма/схуднути/набрати масу): "))
        goal_weight = validate_goal_weight(float(input("Введіть цільову вагу: (кг:)")))
    except ValueError as e:
        print(e)

    bmr = calculate_bmr(weight, height, age, gender, body_fat_percentage)
    goal_calories = calculate_goal_calories(bmr, activity_level, goal_option)
    protein, fat, carbs = calculate_nutrition_goal(goal_calories)
    print("\n Рекомендації раціону харчування: ")
    print(f"Кількість калорій на день: {goal_calories} ккал ")
    print(f"Білки: {protein} грам")
    print(f"Жири: {fat} грам")
    print(f"Вуглеводи: {carbs} грам")


if __name__ == "__main__":
    main()