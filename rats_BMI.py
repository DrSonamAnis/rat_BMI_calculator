import streamlit as st

def calculate_rat_bmi(weight, length):
    """Calculate Rat BMI: weight (g) / length (cm)^2."""
    if length <= 0:
        return 0
    return weight / (length ** 2)

# Streamlit app title
st.title('Rat BMI Calculator')

# Input fields for weight and length
weight = st.number_input('Enter the weight of the rat (in grams):', min_value=0.0, format='%f')
length = st.number_input('Enter the length of the rat (excluding tail, in cm):', min_value=0.0, format='%f')

# Button to calculate BMI
if st.button('Calculate BMI'):
    # Calculate BMI
    bmi = calculate_rat_bmi(weight, length)
    # Display the result
    st.write(f'The BMI of the rat is: {bmi:.2f}')

# Note for users
st.write('Note: This calculator provides a simplified measure and is not a definitive indicator of health.')

