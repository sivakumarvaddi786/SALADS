def calculate_daily_target(income_goal, margin_percentage, recipes, vegetable_prices):
    # Calculate the daily target based on the monthly goal and margin
    daily_target = (income_goal / 30) / (1 + margin_percentage / 100)
    daily_expense = 0
    
    for recipe_name, recipe_items in recipes.items():
        total_cost = calculate_total_price(vegetable_prices, recipe_items)
        selling_price = total_cost * (1 + margin_percentage / 100)
        daily_expense += total_cost
        if daily_target > 0:
            daily_target -= selling_price
    
    return daily_target, daily_expense

def main():
    margin_percentage = 100  # Margin percentage (100%)
    income_goal = 200000  # Monthly income goal in INR

    # Define vegetable prices and recipes (same as in your initial code)
    vegetable_prices = {
    'Carrot': 50,
    'Lettuce': 200,
    'Cucumber': 80,
    'Onion': 40,
    'Tomato': 50,
    'Cherry Tomato': 160,
    'Broccoli': 300,
    'Corn': 100,
    'Green Peas': 250,
    'Iceberg': 100,
    'Green Capsicum': 70,
    'Red Capsicum': 260,
    'Asparagus': 330,
    'Spinach': 360,
    'Dill': 240,
    'Kale': 300,
    'Black Beans': 200,  # Add Black Beans to the vegetable prices
    'Red Bell Pepper': 260,  # Add Red Bell Pepper to the vegetable prices
    'Red Onions': 40,  # Add Red Onions to the vegetable prices
    'American Corn Kernels': 100,  # Add American Corn Kernels to the vegetable prices
    'Sprouted Moong Beans': 200,  # Add Sprouted Moong Beans to the vegetable prices
    'Chickpeas': 150,  # Add Chickpeas to the vegetable prices
    'Bell Peppers': 200,  # Add Bell Peppers to the vegetable prices
    'Avocado': 300  # Add Avocado to the vegetable prices
}
    
    recipes = {
        'CarrotSalad': {
            'Carrot': 150,
            'Cucumber': 100,
            'Green Beans': 50,
            'Broccoli': 50
        },
        'SimpleKaleSalad': {
            'Kale': 150,
            'Carrot': 75,
            'Cherry Tomato': 50,
            'Onion': 25
        },
        'SimpleLettuceSalad': {
            'Lettuce': 150,
            'Cherry Tomato': 50,
            'Cucumber': 75,
            'Red Bell Pepper': 25
        },
        'MexicanKaleSalad': {
            'Kale': 150,
            'Black Beans': 75,
            'Corn': 50,
            'Cherry Tomato': 50,
            'Red Bell Pepper': 25,
            'Red Onions': 25
        },
        'CornSalad': {
            'American Corn Kernels': 150,
            'Tomato': 50,
            'Onion': 25,
            'Red Bell Pepper': 25
        },
        'MoongbeanSproutSalad': {
            'Sprouted Moong Beans': 150,
            'Cucumber': 50,
            'Carrot': 50,
            'Red Bell Pepper': 25,
            'Onion': 25
        },
        'ChickPeasSalad': {
            'Chickpeas': 150,
            'Tomato': 50,
            'Cucumber': 50,
            'Onion': 25,
            'Red Bell Pepper': 25
        },
        'BellPepperSalad': {
            'Bell Peppers': 150,
            'Onion': 25,
            'Cucumber': 75,
            'Dill': 50
        },
        'AvacadoSalad': {
            'Avocado': 150,
            'Cherry Tomato': 50,
            'Cucumber': 50,
            'Onion': 25,
            'Red Bell Pepper': 25
        }
    }

    daily_target, daily_expense = calculate_daily_target(income_goal, margin_percentage, recipes, vegetable_prices)

    print(f"To make {income_goal} INR per month with a {margin_percentage}% margin:")
    print(f"You need to sell {round(daily_target)} salads each day.")
    print(f"Your estimated daily expenditure on ingredients is {daily_expense:.2f} INR.")
    print(f"Your estimated monthly expenditure on ingredients is {daily_expense * 30:.2f} INR.")

if __name__ == "__main__":
    main()
