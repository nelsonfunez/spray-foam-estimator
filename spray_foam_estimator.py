import streamlit as st

st.title("Spray Foam Estimator")

# Input: Foam type
foam_type = st.selectbox("Select Foam Type", ["Open Cell", "Closed Cell"])

# Input: Area and Thickness
area = st.number_input("Enter Area (sq ft)", min_value=0.0, step=1.0)
thickness = st.number_input("Enter Thickness (inches)", min_value=0.0, step=0.5)

# Foam type pricing
prices_per_board_foot = {
    "Open Cell": 0.44,
    "Closed Cell": 1.00
}

# Calculation logic
board_feet = (area * thickness) / 12
price_per_bf = prices_per_board_foot.get(foam_type, 0)
estimated_cost = board_feet * price_per_bf

# Output
st.subheader("Estimate Summary")
st.write(f"Foam Type: **{foam_type}**")
st.write(f"Total Board Feet: **{board_feet:.2f}**")
st.write(f"Estimated Cost: **${estimated_cost:,.2f}**")
