from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Diet dictionary
diets = {
    "bulking": [
        "Breakfast: 6 egg whites + 2 whole eggs + oats + banana",
        "Lunch: Chicken breast + brown rice + broccoli",
        "Snack: Protein shake + almonds",
        "Dinner: Salmon + sweet potato + spinach"
    ],
    "lean-bulking": [
        "Breakfast: 4 eggs + oats with honey",
        "Lunch: Grilled chicken + quinoa + veggies",
        "Snack: Low-fat Greek yogurt + whey protein",
        "Dinner: Lean beef + brown rice + salad"
    ],
    "cutting": [
        "Breakfast: 3 egg whites + 1 whole egg + spinach",
        "Lunch: Tuna + mixed greens + olive oil",
        "Snack: Protein shake + cucumber sticks",
        "Dinner: Grilled fish + steamed broccoli"
    ]
}

# 🔹 Rule for choosing diet based on weight
def get_diet_by_weight(weight: int) -> str:
    if weight <= 55:
        return "bulking"
    elif 56 <= weight <= 75:
        return "lean-bulking"
    else:
        return "cutting"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            weight = int(request.form.get("weight", 0))
            diet_type = get_diet_by_weight(weight)
            meals = diets[diet_type]
            return render_template(f"{diet_type}.html", meals=meals, weight=weight)
        except (ValueError, KeyError):
            return render_template("index.html", error="⚠️ Please enter a valid number")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
