import streamlit as st
from dotenv import load_dotenv
import os

from ibm_watsonx_ai.foundation_models import Model

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
URL = os.getenv("URL")

# IBM Granite Model Setup
model = Model(
    model_id="ibm/granite-4-h-small",
    params={
        "decoding_method": "greedy",
        "max_new_tokens": 500
    },
    credentials={
        "apikey": API_KEY,
        "url": URL
    },
    project_id=PROJECT_ID
)

# Streamlit UI
st.set_page_config(page_title="SmartChef AI", page_icon="🍳")

st.markdown(
    "<h1 style='text-align:center; color:orange;'>🍳 SmartChef AI</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align:center;'>AI Recipe Preparation Agent</h3>",
    unsafe_allow_html=True
)

st.write("---")

ingredients = st.text_area(
    "Enter ingredients separated by commas"
)

diet = st.selectbox(
    "Select Diet Preference",
    ["Veg", "Non-Veg", "Vegan"]
)

if st.button("Generate Recipe"):

    if ingredients.strip() == "":
        st.warning("Please enter ingredients.")
    else:

        prompt = f"""
You are an AI cooking assistant.

Generate ONLY a food recipe.

Ingredients:
{ingredients}

Diet Preference:
{diet}

Provide the response in this format:

1. Recipe Name
2. Ingredients Required
3. Step-by-step Cooking Instructions
4. Estimated Calories
5. Healthy Cooking Tips
6. Ingredient Substitutions

Do not generate unrelated topics.
Only generate cooking-related content.
"""

        with st.spinner("Generating recipe..."):

            response = model.generate_text(prompt=prompt)

            response = str(response)

            st.success("Recipe Generated!")

            st.markdown(response)