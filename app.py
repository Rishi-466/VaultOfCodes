import random
import streamlit as st

# Richer and diverse recipe templates
RECIPE_TEMPLATES = {
    "salad": [
        "{ingredient1} & {ingredient2} Mediterranean Salad",
        "Fresh Garden Salad with {ingredient1} and {ingredient2}"
    ],
    "stir_fry": [
        "Spicy {ingredient1} and {ingredient2} Stir-Fry",
        "Wok-Tossed {ingredient1} with {ingredient2} & Soy Glaze"
    ],
    "soup": [
        "Warm {ingredient1} and {ingredient2} Velvety Soup",
        "Savory {ingredient1}-{ingredient2} Infusion Soup"
    ]
}

def select_recipe_template(ingredients):
    """Choose a random recipe type and template."""
    recipe_type = random.choice(list(RECIPE_TEMPLATES.keys()))
    template = random.choice(RECIPE_TEMPLATES[recipe_type])
    recipe_name = template.format(
        ingredient1=ingredients[0].capitalize(),
        ingredient2=ingredients[1].capitalize()
    )
    return recipe_type, recipe_name

def create_instructions(ingredients, recipe_type):
    """Build detailed cooking instructions."""
    common_steps = [
        f"1. Rinse and prep all ingredients: {', '.join(ingredients)}.",
        f"2. Dice {ingredients[0]} and finely slice {ingredients[1]}.",
        f"3. Place them in a {'preheated pan with oil' if recipe_type == 'stir_fry' else 'large bowl or pot'}."
    ]

    if recipe_type == "salad":
        steps = [
            "4. Add olive oil, a splash of lemon juice, and herbs like mint or basil.",
            "5. Toss everything gently to coat evenly.",
            "6. Chill for 10 minutes before serving."
        ]
    elif recipe_type == "stir_fry":
        steps = [
            "4. Stir-fry on medium-high heat for 6-8 minutes until lightly browned.",
            "5. Add soy sauce, garlic, or chili flakes for extra flavor.",
            "6. Serve hot with a sprinkle of sesame seeds or green onions."
        ]
    else:  # soup
        steps = [
            "4. Add 2 cups of vegetable broth and bring to a boil.",
            "5. Simmer for 15 minutes, then blend until smooth (optional).",
            "6. Garnish with cream or croutons before serving."
        ]
    
    final_steps = [
        "7. Taste and adjust seasoning with salt and pepper.",
        "8. Serve fresh and enjoy your delicious homemade dish!"
    ]
    
    return common_steps + steps + final_steps

def generate_simple_recipe(ingredients):
    """Master function to generate recipe text."""
    if len(ingredients) < 2:
        return "Please provide at least 2 ingredients"
    
    recipe_type, recipe_name = select_recipe_template(ingredients)
    instructions = create_instructions(ingredients, recipe_type)
    
    recipe_text = (
        f"Recipe Name: {recipe_name}\n\n"
        f"Preparation Time: 10 minutes\n"
        f"Cooking Time: {'10-15 minutes' if recipe_type == 'stir_fry' or recipe_type == 'soup' else 'None'}\n"
        f"Serves: 2\n\n"
        "Instructions:\n" + "\n".join(instructions)
    )
    return recipe_text

def main():
    st.title("👨‍🍳 Pro-Level Recipe Generator")
    ingredients_input = st.text_input("Enter ingredients (comma separated):", "spinach, mushrooms")

    if st.button("Generate Recipe"):
        if ingredients_input.strip():
            ingredients = [item.strip() for item in ingredients_input.split(",") if item.strip()]
            if len(ingredients) >= 2:
                recipe = generate_simple_recipe(ingredients)
                st.subheader("Your Chef-Style Recipe")
                st.text(recipe)
            else:
                st.warning("Please enter at least two valid ingredients.")
        else:
            st.warning("Please enter some ingredients to get started.")

if __name__ == "__main__":
    main()
