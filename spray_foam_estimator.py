import streamlit as st
import io
from fpdf import FPDF
import base64
import qrcode

st.title("Spray Foam Estimator")

# Inputs
job_name = st.text_input("Job Name (optional)", "")
foam_type = st.selectbox("Select Foam Type", ["Open Cell", "Closed Cell"])
area = st.number_input("Enter Area (sq ft)", min_value=0.0, step=1.0)
thickness = st.number_input("Enter Thickness (inches)", min_value=0.0, step=0.5)
labor_rate = st.number_input("Labor Cost ($/sq ft)", min_value=0.0, step=1.0, value=0.0)
tax_rate = st.number_input("Tax Rate (%)", min_value=0.0, step=0.5, value=0.0)

# Pricing
prices_per_board_foot = {"Open Cell": 0.44, "Closed Cell": 1.00}
price_per_bf = prices_per_board_foot.get(foam_type, 0)

# Calculations
board_feet = (area * thickness) / 12
material_cost = board_feet * price_per_bf
labor_cost = area * labor_rate
subtotal = material_cost + labor_cost
tax = subtotal * (tax_rate / 100)
grand_total = subtotal + tax

# Summary Text
summary = f"""
Spray Foam Estimate

Job Name: {job_name or 'N/A'}
Foam Type: {foam_type}
Area: {area} sq ft
Thickness: {thickness} in
Board Feet: {board_feet:.2f}

Material Cost: ${material_cost:,.2f}
Labor Cost: ${labor_cost:,.2f}
Tax: ${tax:,.2f}

GRAND TOTAL: ${grand_total:,.2f}
"""

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

# Feature 1: Copyable summary
st.text_area("📋 Copyable Estimate Summary", summary, height=250)

# Feature 2: PDF download
def generate_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.strip().split('\n'):
        pdf.cell(200, 10, txt=line, ln=1)
    buffer = io.BytesIO()
    pdf.output(buffer, 'F')  # 'F' = write to file-like object
    buffer.seek(0)
    return buffer


pdf_buffer = generate_pdf(summary)
b64_pdf = base64.b64encode(pdf_buffer.getvalue()).decode()
pdf_link = f'<a href="data:application/octet-stream;base64,{b64_pdf}" download="estimate.pdf">📄 Download Estimate as PDF</a>'
st.markdown(pdf_link, unsafe_allow_html=True)

# Feature 3: QR code with link to app
st.subheader("🔗 Share This App")
app_url = st.text_input("Enter your app URL", "https://your-app-name.streamlit.app")
qr = qrcode.make(app_url)
buffer = io.BytesIO()
qr.save(buffer)
st.image(buffer.getvalue(), caption="Scan to open", width=200)
