from flask import Flask, render_template, request, jsonify, redirect, url_for
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
        goal_option = request.form['goal_option']
        goal_weight = float(request.form['goal_weight'])

        bmr = calculate_bmr(weight, height, age, gender)
        goal_calories = calculate_goal_calories(bmr, activity_level, goal_option)
        protein, fat, carbs = calculate_nutrition_goal(goal_calories)

        return jsonify(protein=protein, fat=fat, carbs=carbs, goal_calories=goal_calories)

    return render_template('index.html')

@app.route('/fridge_chef')
def fridge_chef():
    return render_template('fridge_chef.html')

@app.route('/premium_menu')
def premium_menu():
    return render_template('premium_menu.html')

if __name__ == '__main__':
    app.run(debug=True)
