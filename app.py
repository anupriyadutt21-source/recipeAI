import pandas as pd
import streamlit as st

st.title("🍳 RecipeAI")

recipes = pd.read_csv("recipes.csv")

# Show CSV data
st.write("Your CSV columns:")
st.write(recipes.columns)

ingredient = st.text_input("Enter an ingredient:")

if ingredient:
    # Search in the whole CSV
    result = recipes[
        recipes.astype(str)
        .apply(lambda x: x.str.contains(ingredient, case=False, na=False))
        .any(axis=1)
    ]

    if not result.empty:
        st.subheader("Recipes Found:")
        st.dataframe(result)
    else:
        st.write("No recipe found 😔")
        