import streamlit as st
import pandas as pd
import joblib
import base64

# --- BACKGROUND SETUP ---
def set_background(image_file):
    try:
        with open(image_file, "rb") as file:
            encoded_string = base64.b64encode(file.read()).decode()
        
        # CSS to inject the background and add a frosted cream overlay for readability
        css = f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string});
            background-size: 400px; /* Sets a fixed scale instead of stretching */
            background-repeat: repeat; /* Tiles the image across the screen */
            background-attachment: fixed;
        }}
        .block-container {{
            background-color: rgba(241, 235, 225, 0.95);
            border-radius: 15px;
            padding: 2rem;
            margin-top: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)
    except FileNotFoundError:
        pass

# Call the background function
set_background('bg2.jpg')

# --- INITIALIZE STATE ---
if 'classified' not in st.session_state:
    st.session_state.classified = False
if 'prediction' not in st.session_state:
    st.session_state.prediction = None
if 'is_zero_nutrient' not in st.session_state:
    st.session_state.is_zero_nutrient = False

# --- LOAD MODEL ---
try:
    model = joblib.load('meal_category_model.pkl')
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'meal_category_model.pkl' is in the same folder.")
    st.stop()

st.title("Cafeteria Meal Category Classifier")
st.write("Enter the nutritional information of a meal to classify it as Light, Balanced, or High-Calorie.")

# --- INPUT LAYOUT ---
col1, col2 = st.columns(2)

with col1:
    calories = st.number_input("Calories (kcal)", min_value=0.0, step=10.0, key="cal_input")
    sugar = st.number_input("Sugar (g)", min_value=0.0, step=1.0, key="sugar_input")
    fat = st.number_input("Fat (g)", min_value=0.0, step=1.0, key="fat_input")

with col2:
    protein = st.number_input("Protein (g)", min_value=0.0, step=1.0, key="protein_input")
    sodium = st.number_input("Sodium (mg)", min_value=0.0, step=10.0, key="sodium_input")

st.write("") 


# --- CLASSIFY BUTTON & VALIDATION ---
btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])
with btn_col2:
    if st.button("Classify Meal", use_container_width=True):
        # 1. Check for invalid negative values
        if any(val < 0 for val in [calories, sugar, fat, protein, sodium]):
            st.error("Invalid input: Nutritional values cannot be negative.")
            st.session_state.classified = False
        else:
            # Set flag for zero-nutrient entry
            st.session_state.is_zero_nutrient = (
                calories == 0 and (sugar + fat + protein + sodium) == 0
            )

            input_data = pd.DataFrame({
                'CALORIES (kcal)': [calories],
                'SUGAR (g)': [sugar],
                'FAT (g)': [fat],
                'PROTEIN (g)': [protein],
                'SODIUM (mg)': [sodium]
            })
            
            st.session_state.prediction = model.predict(input_data)[0]
            st.session_state.classified = True

# --- FULL-WIDTH NOTICE ---
# Outside the columns so it stretches the full width of the container
if st.session_state.classified and st.session_state.is_zero_nutrient:
    st.write("")
    st.info("Notice: All values are 0 (e.g., plain water / zero-calorie beverage).")

# --- RESULTS DISPLAY ---
if st.session_state.classified and st.session_state.prediction is not None:
    st.markdown("---")
    pred_str = str(st.session_state.prediction).strip()
    st.subheader(f"Result: {pred_str}")
    
    # Normalized to upper case to prevent string mismatch
    pred_upper = pred_str.upper()
    if "HIGH" in pred_upper:
        st.error("Explanation: This meal contains a high density of calories and macronutrients, suitable for intensive energy recovery but should be monitored for daily intake limits.")
    elif "BALANCED" in pred_upper:
        st.success("Explanation: This meal provides a well-proportioned mix of nutrients, ideal for maintaining steady energy levels throughout the day.")
    elif "LIGHT" in pred_upper:
        st.warning("Explanation: This meal is low in calories and heavy macronutrients, making it a great option for a quick snack or a low-energy-expenditure day.")
    else:
        st.info("Explanation: Meal category successfully classified.")
        
    st.write("") 
    
    def reset_inputs():
        st.session_state.classified = False
        st.session_state.prediction = None
        st.session_state.cal_input = 0.0
        st.session_state.sugar_input = 0.0
        st.session_state.fat_input = 0.0
        st.session_state.protein_input = 0.0
        st.session_state.sodium_input = 0.0

    reset_col1, reset_col2, reset_col3 = st.columns([1, 1, 1])
    with reset_col2:
        st.button("Enter new entries", on_click=reset_inputs, use_container_width=True)
else:
    st.write("<br>" * 7, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Programmed by: Arianne Beverly Marquez & Lester Anthony Respicio</p>", unsafe_allow_html=True)