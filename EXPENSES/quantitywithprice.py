# Vegetable prices per kilogram in INR
vegetable_prices_inr = {
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
    'Black Beans': 200,
    'Red Bell Pepper': 260,
    'Red Onions': 40,
    'American Corn Kernels': 100,
    'Sprouted Moong Beans': 200,
    'Chickpeas': 150,
    'Bell Peppers': 200,
    'Avocado': 300
}

def calculate_total_price_inr(vegetable_dict, items):
    total_price = 0
    for veg, grams in items.items():
        if veg in vegetable_dict:
            price_per_kg = vegetable_dict[veg]
            price_per_gram = price_per_kg / 1000  # Convert price per kg to price per gram
            total_price += price_per_gram * grams
    return total_price

def calculate_quantity_required(vegetable_prices, recipes):
    total_quantity_required = {}
    total_price_for_vegetable_inr = {}
    
    for recipe_items in recipes.values():
        for veg, grams in recipe_items.items():
            if veg in vegetable_prices:
                if veg not in total_quantity_required:
                    total_quantity_required[veg] = 0
                    total_price_for_vegetable_inr[veg] = 0
                price_per_kg = vegetable_prices[veg]
                price_per_gram = price_per_kg / 1000  # Convert price per kg to price per gram
                total_quantity_required[veg] += grams
                total_price_for_vegetable_inr[veg] += (price_per_gram * grams)
    
    return total_quantity_required, total_price_for_vegetable_inr

def main():
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

    total_quantity_required, total_price_for_vegetable_inr = calculate_quantity_required(vegetable_prices_inr, recipes)

    print("Total quantities required for each vegetable across all recipes:")
    for veg, quantity in total_quantity_required.items():
        print(f'{veg}: {quantity:.2f} grams')

    print("\nTotal price for each vegetable across all recipes (in INR):")
    grand_total_inr = 0
    for veg, price in total_price_for_vegetable_inr.items():
        print(f'{veg}: ₹{price:.2f}')
        grand_total_inr += price
    
    print("\nGrand Total for all vegetables (in INR):")
    print(f'₹{grand_total_inr:.2f}')

if __name__ == "__main__":
    main()
