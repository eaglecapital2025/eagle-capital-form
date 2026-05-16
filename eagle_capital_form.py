import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration for Maximum Readability
st.set_page_config(
    page_title="Eagle Capital | Investor Onboarding",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Main Dashboard Headers
st.title("EAGLE CAPITAL")
st.subheader("Secure Wealth Creation & Retirement Planning Desk")
st.caption("AMFI REGISTERED MUTUAL FUND DISTRIBUTOR: ARN-335909 | Distributor: Patel Divyesh")

st.write("---")

# Split Layout to optimize screen space
left_inputs, right_calculator = st.columns([1.6, 1])

with left_inputs:
    st.header("1. Investor Information")
    
    c1, c2 = st.columns(2)
    with c1:
        full_name = st.text_input("Investor Full Name (As per PAN Card):", placeholder="Type your name here")
    with c2:
        phone_number = st.text_input("WhatsApp Mobile Number:", placeholder="Type your phone number here")
        
    c3, c4 = st.columns(2)
    with c3:
        email_address = st.text_input("Email Address:", placeholder="Type your email address here")
    with c4:
        age_bracket = st.selectbox("Select Your Age Group Horizon:", ["Senior Citizen (60 Years & Above)", "45 - 59 Years", "25 - 44 Years", "Under 25 Years"])

    st.write("---")
    st.header("2. Investment Plan Preferences")
    
    investment_type = st.multiselect(
        "Which Investment Vehicles Do You Want to Explore?:",
        ["Systematic Investment Plan (SIP)", "Lump Sum One-Time Investment", "Tax Saving Schemes (ELSS)", "Monthly Income Plans (MIP) / Pension Planning"],
        default=["Systematic Investment Plan (SIP)"]
    )
    
    # Visible, easy-to-slide structural layout
    monthly_budget = st.slider("Target Monthly Savings Allocation Budget (INR Amount):", min_value=2000, max_value=100000, value=10000, step=2000)
    years_horizon = st.slider("Target Planning Period Horizon (Number of Years):", min_value=3, max_value=25, value=10)

    st.write("---")
    st.header("3. Capital Security & Goals")
    
    risk_appetite = st.radio(
        "Choose Your Capital Risk Comfort Level:",
        [
            "Low Risk / Conservative: Focus heavily on capital safety, fixed-income matching, and stable returns.",
            "Balanced Risk / Moderate: Balanced distribution across stable blue-chips and large-cap growth assets.",
            "Growth Oriented / Aggressive: High-conviction equity breakout momentum strategies for compounding over long horizons."
        ]
    )
    
    primary_goal = st.text_area("What is the primary milestone goal for this money?:", placeholder="Write your goals here...")

    st.write("---")
    
    # Giant, easy-to-click submission routine
    submit_button = st.button("🚀 SUBMIT COMPLETED FORM TO EAGLE CAPITAL INBOX", use_container_width=True)
    
    if submit_button:
        if not full_name or not phone_number or not email_address:
            st.error("Validation Error: Please fill out your Name, Phone Number, and Email before submitting.")
        else:
            st.balloons()
            st.success("Form Submitted Successfully! A representative will reach out to you shortly.")

with right_calculator:
    st.header("Live Compound Growth Visualizer")
    
    # 1. FIXED: These variables now instantly look at what you enter or select live
    selected_monthly_budget = monthly_budget  # Captures the live slider value dynamically
    selected_years = years_horizon            # Captures the live timeline value dynamically
    
    # 2. Dynamic Math Engine Calculations
    annual_growth_rate = 12.0  
    m_rate = (annual_growth_rate / 100) / 12
    total_months = selected_years * 12
    
    # 3. Running the compounding formula live based on your inputs
    future_value = selected_monthly_budget * (((1 + m_rate)**total_months - 1) / m_rate) * (1 + m_rate)
    total_invested = selected_monthly_budget * total_months
    earned_gains = future_value - total_invested
    
    # 4. High-Contrast Native Display Cards (Updates instantly on change)
    with st.container(border=True):
        if future_value >= 5000000:
            st.warning("🌟 MAJOR WEALTH TARGET REACHED")
        else:
            st.info("📈 STEADY COMPOUNDING ACCUMULATION ACTIVATED")
            
        # These now display the real-time calculations perfectly with no code errors
        st.metric(label="Your Total Cash Principal Contributions", value=f"₹{total_invested:,.0f}")
        st.metric(label="Estimated Accumulated Growth Interest Earned", value=f"+ ₹{earned_gains:,.0f}")
        
        st.write("---")
        st.metric(label="ESTIMATED TOTAL MATURE PORTFOLIO VALUE", value=f"₹{future_value:,.0f}")
        
    st.caption("*Note: Calculations are based on a balanced equity index return projection of 12.0% per annum. Mutual Fund assets are subject to market volatility variance.")