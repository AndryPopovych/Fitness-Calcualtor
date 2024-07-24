from flask import Flask, render_template, request, jsonify
from CaloriesCalculator import calculate_bmr, calculate_goal_calories, calculate_nutrition_goal

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        age = int(request.form['age'])
        gender = request.form['gender']
        activity_level = request.form['activity_level']
        body_fat_percentage = float(request.form['body_fat_percentage'])
        goal_option = request.form['goal_option']
        goal_weight = float(request.form['goal_weight'])

        bmr = calculate_bmr(weight, height, age, gender, body_fat_percentage)
        goal_calories = calculate_goal_calories(bmr, activity_level, goal_option)
        protein, fat, carbs = calculate_nutrition_goal(goal_calories)

        return jsonify(protein=protein, fat=fat, carbs=carbs, goal_calories=goal_calories)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)