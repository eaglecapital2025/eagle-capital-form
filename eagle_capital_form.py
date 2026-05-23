import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration for Maximum Readability
st.set_page_config(
    page_title="Eagle Capital | Wealth Blueprint",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Main Dashboard Headers
st.title("EAGLE CAPITAL")
st.subheader("Secure Wealth Creation & Retirement Planning Desk")
st.caption("AMFI REGISTERED MUTUAL FUND DISTRIBUTOR: ARN-335909 | Distributor: Mr. Vishal Raj | Support: 9825821407")

st.write("---")

# Split Layout to optimize screen space
left_inputs, right_calculator = st.columns([1.5, 1.2], gap="large")

with left_inputs:
    st.header("Step 1: Investor Profile")
    
    c1, c2 = st.columns(2)
    with c1:
        full_name = st.text_input("Investor Full Name (As per PAN Card):", placeholder="Type your name here")
    with c2:
        phone_number = st.text_input("WhatsApp Mobile Number:", placeholder="Type your phone number here")
        
    email_address = st.text_input("Email Address:", placeholder="Type your email address here")
    
    # Modern card-like selection using horizontal radio buttons
    age_bracket = st.radio(
        "Select Your Age Group Horizon:", 
        ["20-30 Years: Wealth Accumulation", "31-45 Years: Goal Building", "46-59 Years: Pre-Retirement", "60+ Years: Capital Preservation"],
        horizontal=True
    )

    st.write("---")
    st.header("Step 2: Milestone Mapping")
    
    primary_goal = st.radio(
        "What is the primary milestone goal for this money?",
        ["🏡 Dream Home", "🎓 Child's Education", "🌴 Peaceful Retirement", "🚀 General Wealth Creation"],
        horizontal=True
    )
    
    target_amount = st.slider(
        "Estimated Target Amount Needed for Goal (INR):", 
        min_value=500000, max_value=100000000, value=10000000, step=500000, format="₹%d"
    )

    st.write("---")
    st.header("Step 3: Strategy & Risk")
    
    investment_type = st.radio(
        "Investment Vehicle:", 
        ["Systematic Investment Plan (SIP)", "Lumpsum + SIP"], 
        horizontal=True
    )
    
    monthly_budget = st.slider("Target Monthly Savings Allocation (INR):", min_value=2000, max_value=100000, value=15000, step=1000, format="₹%d")
    years_horizon = st.slider("Target Planning Period Horizon (Years):", min_value=3, max_value=30, value=15)

    risk_appetite = st.radio(
        "Choose Your Capital Risk Comfort Level:",
        [
            "🛡️ Low Risk / Conservative (Est. 8%): Focus on capital safety.",
            "⚖️ Balanced Risk / Moderate (Est. 12%): Distribution across blue-chips.",
            "🔥 Growth Oriented / Aggressive (Est. 15%): High-conviction equity breakout."
        ]
    )

# Right Column - The Intelligent Visualizer
with right_calculator:
    st.header("📈 Your Wealth Creation Blueprint")
    
    # 1. Dynamic Math Engine Calculations based on Risk Selection
    if "Low Risk" in risk_appetite:
        annual_growth_rate = 8.0
    elif "Balanced Risk" in risk_appetite:
        annual_growth_rate = 12.0
    else:
        annual_growth_rate = 15.0
        
    m_rate = (annual_growth_rate / 100) / 12
    total_months = years_horizon * 12
    
    # Running the compounding formula live
    future_value = monthly_budget * (((1 + m_rate)**total_months - 1) / m_rate) * (1 + m_rate)
    total_invested = monthly_budget * total_months
    earned_gains = future_value - total_invested
    
    # Inflation Mathematics (Assuming 6% average inflation)
    inflation_rate = 0.06
    real_purchasing_power = future_value / ((1 + inflation_rate)**years_horizon)
    
    # Goal Tracking Mathematics
    goal_percentage = (future_value / target_amount) * 100
    
    # 2. High-Contrast Native Display Cards
    with st.container(border=True):
        st.subheader("The Accumulation Strategy")
        st.metric(label="Total Cash Principal Contributions", value=f"₹{total_invested:,.0f}")
        st.metric(label=f"Estimated Growth Earned (@ {annual_growth_rate}%)", value=f"+ ₹{earned_gains:,.0f}")
        
        st.write("---")
        st.subheader("The Final Outcomes")
        st.metric(label="ESTIMATED TOTAL MATURE PORTFOLIO VALUE", value=f"₹{future_value:,.0f}")
        
        # Interactive Inflation Toggle
        show_inflation = st.toggle("📉 Show Inflation-Adjusted Value (Real Purchasing Power)")
        if show_inflation:
            st.metric(
                label=f"What this money will actually buy in {years_horizon} years (6% Inflation)", 
                value=f"₹{real_purchasing_power:,.0f}", 
                delta="- Inflation Impact", 
                delta_color="inverse"
            )
            
    st.write("")
    
    # 3. Dynamic Goal Insight Engine
    if goal_percentage >= 100:
        st.success(f"🎯 **Goal Insight:** You are perfectly on track! This SIP will fund **{goal_percentage:,.1f}%** of your {target_amount:,.0f} target.")
    else:
        shortfall = target_amount - future_value
        extra_monthly_needed = shortfall / ((((1 + m_rate)**total_months - 1) / m_rate) * (1 + m_rate))
        st.warning(f"🎯 **Goal Insight:** This SIP covers **{goal_percentage:,.1f}%** of your target. To reach 100%, consider increasing your SIP by an estimated **₹{extra_monthly_needed:,.0f}/month**.")

    st.caption(f"*Note: Projections use an estimated {annual_growth_rate}% per annum return based on your risk profile. Mutual Fund investments are subject to market risks.")
    
    st.write("---")
    
    # Giant, easy-to-click submission routine
    submit_button = st.button("🚀 START THIS SIP PORTFOLIO NOW", use_container_width=True, type="primary")
    
    if submit_button:
        if not full_name or not phone_number or not email_address:
            st.error("Validation Error: Please fill out your Name, Phone Number, and Email before starting.")
        else:
            st.balloons()
            st.success(f"Welcome aboard, {full_name}! Your personalized portfolio strategy has been initiated. Mr. Vishal Raj will contact you shortly.")
