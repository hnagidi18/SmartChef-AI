# SmartChef AI – Recipe Preparation Agent

SmartChef AI is an AI-powered Recipe Preparation Agent developed using IBM watsonx.ai, IBM Granite Foundation Models, and Streamlit. The application helps users generate personalized recipes using ingredients available at home while reducing food waste and simplifying meal preparation.
# Features
* Ingredient-based personalized recipe generation
* AI-powered cooking instructions
* Supports Veg, Non-Veg, and Vegan preferences
* Healthy cooking tips and calorie estimation
* Ingredient substitution suggestions
* Real-time AI response generation
* Interactive and user-friendly Streamlit interface
# Technologies Used
* Python
* Streamlit
* IBM watsonx.ai
* IBM Granite Foundation Model
* Prompt Engineering
* IBM Cloud Lite Services
* 
# IBM Granite Model Used
```plaintext id="jlwm4x"
ibm/granite-4-h-small
```
# Project Workflow
User Input
   ↓
Streamlit Frontend
   ↓
IBM watsonx.ai Agent
   ↓
IBM Granite Model
   ↓
Recipe Generation
   ↓
Recipe Output

# Installation and Setup

## Step 1 – Clone Repository
```bash id="jlwm9v"
git clone https://github.com/yourusername/smartchef-ai.git
```
## Step 2 – Open Project Folder
```bash id="jlwm2x"
cd smartchef-ai
```
## Step 3 – Install Requirements
```bash id="jlwm6p"
pip install -r requirements.txt
```
## Step 4 – Add Environment Variables
Create a `.env` file and add:
```plaintext id="jlwm1v"
API_KEY=your_api_key
PROJECT_ID=your_project_id
URL=https://us-south.ml.cloud.ibm.com
```
## Step 5 – Run Application
```bash id="jlwm8p"
streamlit run app.py
```
Sample Input
rice, onion, tomato, egg

Diet Preference:

Non-Veg

# Output
The system generates:
* Recipe Name
* Ingredients Required
* Step-by-step Cooking Instructions
* Estimated Calories
* Healthy Cooking Tips
* Ingredient Substitutions

# Future Scope
* Voice-based cooking assistant
* Image-based ingredient detection
* Personalized meal planning
* Smart grocery recommendation system
* Mobile application integration

# Problem Statement
Problem Statement No.16 – Recipe Preparation Agent
The project helps users generate personalized recipes using available ingredients while reducing food waste through AI-powered cooking assistance.

# Developed Using
IBM watsonx.ai + IBM Granite Models + Streamlit
