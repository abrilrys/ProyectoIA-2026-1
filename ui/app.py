import streamlit as st
from utils import load_json, extract_ingredients

RECIPIES_FILE = "all_mexican_recipes.json"

st.title("SciFitNoFat 👨🏼‍🍳👩‍🔬")

st.markdown("Hola, este sistema te ayudará a obtener las recetas perfectas :)")

data = load_json(RECIPIES_FILE)

st.header("Ingresa tus macro nutrientes 🧮")

col1, col2, col3, col4 = st.columns(4)

with col1:
    proteins = st.number_input("Proteinas")
with col2:
    fat = st.number_input("Grasa")
with col3:
    carbs = st.number_input("Carbohidratos")
with col4:
    kcal = st.number_input("kcal")

# st.header("Ingresa tu presupuesto 💸")

budget = st.number_input("Ingresa el presupuesto", icon="💸")

st.code(f"Tu budgets es de ${budget}")

option_map = {
    0: ":material/chef_hat:",
    1: ":material/kitchen:",
}

selection = st.pills(
    "Modos",
    default=1,
    options=option_map.keys(),
    format_func=lambda option: option_map[option],
    selection_mode="single",
    help="Puedes solicitar una lista de ingredientes a comprar para la semana (:material/chef_hat:) o ingresar los ingredientes que ya tienes en tu alacena/refri (:material/kitchen:)",
)

if selection is not None and selection == 1:
    ingredients = st.multiselect(
        "Selecciona tus ingredientes",
        options=extract_ingredients(data),
        format_func=lambda ingredient: ingredient.title(),
    )
    st.write(ingredients)
    st.code(data[0])
