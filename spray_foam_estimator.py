import streamlit as st

st.title("Spray Foam Estimator")

# Input: Job name (optional)
job_name = st.text_input("Job Name (optional)", "")

# Foam type
foam_type = st.selectbox("Select Foam Type", ["Open Cell", "Closed Cell"])

# Area and Thickness
area = st.number_input("Enter Area (sq ft)", min_value=0.0, step=1.0)
thickness = st.number_input("Enter Thickness (inches)", min_value=0.0, step=0.5)

# Pricing settings
prices_per_board_foot = {"Open Cell": 0.44, "Closed Cell": 1.00}
price_per_bf = prices_per_board_foot.get(foam_type, 0)

# Extra cost inputs
labor_rate = st.number_input("Labor Cost ($/sq ft)", min_value=0.0, step=1.0, value=0.0)
tax_rate = st.number_input("Tax Rate (%)", min_value=0.0, step=0.5, value=0.0)

# Calculations
board_feet = (area * thickness) / 12
material_cost = board_feet * price_per_bf
labor_cost = area * labor_rate
subtotal = material_cost + labor_cost
tax = subtotal * (tax_rate / 100)
grand_total = subtotal + tax

# Output
st.subheader("Estimate Summary")
if job_name:
    st.write(f"**Job Name:** {job_name}")
st.write(f"Foam Type: **{foam_type}**")
st.write(f"Total Board Feet: **{board_feet:.2f}**")
st.write(f"Material Cost: **${material_cost:,.2f}**")
st.write(f"Labor Cost: **${labor_cost:,.2f}**")
st.write(f"Tax: **${tax:,.2f}**")
st.markdown(f"### Grand Total: **${grand_total:,.2f}**")
