import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Eagle Capital | Wealth Blueprint",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# HEADER SECTION
# ---------------------------------------------------------
st.title("EAGLE CAPITAL")
st.subheader("Secure Wealth Creation & Retirement Planning Desk")
st.caption("AMFI REGISTERED MUTUAL FUND DISTRIBUTOR: ARN-335909 | Distributor: Mr. Vishal Raj | Support: 9825821407")
st.write("---")

# Split Layout
left_inputs, right_calculator = st.columns([1.5, 1.2], gap="large")

# =========================================================
# LEFT COLUMN: INTERACTIVE FORM
# =========================================================
with left_inputs:
    st.header("Step 1: Investor Profile")
    
    c1, c2 = st.columns(2)
    with c1:
        full_name = st.text_input("Investor Full Name (As per PAN Card):", placeholder="E.g. Rahul Sharma")
    with c2:
        phone_number = st.text_input("WhatsApp Mobile Number:", placeholder="10-digit number")
        
    email_address = st.text_input("Email Address:", placeholder="your.email@domain.com")
    
    age_bracket = st.radio(
        "Select Your Age Group Horizon:", 
        ["20-30 Years: Wealth Accumulation", "31-45 Years: Goal Building", "46-59 Years: Pre-Retirement", "60+ Years: Capital Preservation"],
        horizontal=True
    )

    st.write("---")
    st.header("Step 2: Milestone Mapping")
    st.write("**What are your milestone goals? (Select all that apply):**")
    
    g1, g2, g3, g4 = st.columns(4)
    with g1: goal_home = st.checkbox("🏡 Dream Home")
    with g2: goal_edu = st.checkbox("🎓 Education")
    with g3: goal_retire = st.checkbox("🌴 Retirement")
    with g4: goal_wealth = st.checkbox("🚀 Wealth")
    
    if goal_home and "home_toast" not in st.session_state:
        st.toast("Great goal! Let's build that Dream Home.", icon="🏡")
        st.session_state.home_toast = True
    if goal_retire and "retire_toast" not in st.session_state:
        st.toast("Retirement planning activated.", icon="🌴")
        st.session_state.retire_toast = True
    
    # Expanded HNI Numbers (Up to 100 Crores)
    amount_mapping = {
        "5 Lakhs": 500000, "10 Lakhs": 1000000, "25 Lakhs": 2500000,
        "50 Lakhs": 5000000, "75 Lakhs": 7500000, "1 Crore": 10000000,
        "2 Crores": 20000000, "5 Crores": 50000000, "10 Crores": 100000000,
        "20 Crores": 200000000, "50 Crores": 500000000, "100 Crores": 1000000000
    }
    options_list = list(amount_mapping.keys())
    
    target_amount = 0
    selected_count = 0
    
    st.write("") 
    
    if goal_home:
        selected_count += 1
        home_val = st.select_slider("Target for 🏡 Dream Home:", options=options_list, value="1 Crore")
        target_amount += amount_mapping[home_val]
        
    if goal_edu:
        selected_count += 1
        edu_val = st.select_slider("Target for 🎓 Child's Education:", options=options_list, value="50 Lakhs")
        target_amount += amount_mapping[edu_val]
        
    if goal_retire:
        selected_count += 1
        retire_val = st.select_slider("Target for 🌴 Retirement:", options=options_list, value="5 Crores")
        target_amount += amount_mapping[retire_val]
        
    if goal_wealth:
        selected_count += 1
        wealth_val = st.select_slider("Target for 🚀 Wealth Creation:", options=options_list, value="1 Crore")
        target_amount += amount_mapping[wealth_val]
        
    if selected_count == 0:
        st.info("👈 Please select at least one milestone above to set your target.")
        target_amount = 10000000 # Failsafe default
    elif selected_count > 1:
        # Dynamic formatting for massive numbers
        display_target = f"{target_amount/10000000:,.2f} Crores" if target_amount >= 10000000 else f"{target_amount/100000:,.0f} Lakhs"
        st.success(f"**Total Combined Portfolio Target: ₹ {display_target}**")

    st.write("---")
    st.header("Step 3: Strategy & Risk")
    
    investment_type = st.radio(
        "Investment Vehicle:", 
        ["Systematic Investment Plan (SIP) Only", "Lumpsum + SIP"], 
        horizontal=True
    )
    
    lumpsum_amount = 0
    if "Lumpsum" in investment_type:
        lumpsum_mapping = {
            "₹ 1 Lakh": 100000, "₹ 5 Lakhs": 500000, "₹ 10 Lakhs": 1000000, 
            "₹ 25 Lakhs": 2500000, "₹ 50 Lakhs": 5000000, "₹ 1 Crore": 10000000, 
            "₹ 5 Crores": 50000000, "₹ 10 Crores": 100000000
        }
        lumpsum_options = list(lumpsum_mapping.keys())
        selected_lumpsum_text = st.select_slider("Initial Lumpsum Investment (One-Time Base):", options=lumpsum_options, value="₹ 5 Lakhs")
        lumpsum_amount = lumpsum_mapping[selected_lumpsum_text]
    
    sip_mapping = {
        "₹ 2,000": 2000, "₹ 5,000": 5000, "₹ 10,000": 10000, "₹ 15,000": 15000,
        "₹ 20,000": 20000, "₹ 25,000": 25000, "₹ 30,000": 30000, "₹ 40,000": 40000,
        "₹ 50,000": 50000, "₹ 75,000": 75000, "₹ 1 Lakh": 100000, "₹ 1.5 Lakhs": 150000,
        "₹ 2 Lakhs": 200000, "₹ 5 Lakhs": 500000, "₹ 10 Lakhs": 1000000
    }
    sip_options = list(sip_mapping.keys())
    
    selected_sip_text = st.select_slider("Target Monthly Savings Allocation (SIP):", options=sip_options, value="₹ 15,000")
    monthly_budget = sip_mapping[selected_sip_text]
    
    years_horizon = st.slider("Target Planning Period Horizon (Years):", min_value=3, max_value=30, value=15)

    risk_appetite = st.radio(
        "Choose Your Capital Risk Comfort Level (Determines Asset Allocation):",
        [
            "🛡️ Low Risk / Conservative: Focus heavily on capital safety and fixed-income.",
            "⚖️ Balanced Risk / Moderate: Balanced distribution across stable blue-chips.",
            "🔥 Growth Oriented / Aggressive: High-conviction equity breakout strategies."
        ],
        index=1
    )


# =========================================================
# RIGHT COLUMN: THE INTELLIGENT VISUALIZER
# =========================================================
with right_calculator:
    st.header("📈 Your Wealth Creation Blueprint")
    
    # 1. Standardized 12% Math Engine
    annual_growth_rate = 12.0
    m_rate = (annual_growth_rate / 100) / 12
    total_months = years_horizon * 12
    
    # 2. Dual Compounding Calculation (SIP + Lumpsum)
    sip_future_value = monthly_budget * (((1 + m_rate)**total_months - 1) / m_rate) * (1 + m_rate)
    lumpsum_future_value = lumpsum_amount * ((1 + (annual_growth_rate / 100))**years_horizon)
    
    future_value = sip_future_value + lumpsum_future_value
    total_invested = (monthly_budget * total_months) + lumpsum_amount
    earned_gains = future_value - total_invested
    
    inflation_rate = 0.06
    real_purchasing_power = future_value / ((1 + inflation_rate)**years_horizon)
    
    goal_percentage = (future_value / target_amount) * 100 if target_amount > 0 else 0
    
    # 3. Gamified Visual Cards
    with st.container(border=True):
        st.subheader("The Accumulation Strategy")
        
        # Displaying the breakdown dynamically if lumpsum exists
        if lumpsum_amount > 0:
            st.write(f"Initial Base: ₹{lumpsum_amount:,.0f} | SIP Total: ₹{monthly_budget * total_months:,.0f}")
            
        st.metric(label="Total Cash Principal Contributions", value=f"₹{total_invested:,.0f}")
        st.metric(label=f"Estimated Growth Earned (@ 12.0%)", value=f"₹{future_value:,.0f}", delta=f"Profit: + ₹{earned_gains:,.0f}")
        
        st.write("---")
        st.subheader("The Final Outcomes")
        
        # Clean formatting for massive outcomes
        if future_value >= 10000000:
            st.metric(label="ESTIMATED TOTAL MATURE PORTFOLIO VALUE", value=f"₹ {future_value/10000000:,.2f} Crores")
        else:
            st.metric(label="ESTIMATED TOTAL MATURE PORTFOLIO VALUE", value=f"₹ {future_value/100000:,.2f} Lakhs")
        
        show_inflation = st.toggle("📉 Show Inflation-Adjusted Value (Real Purchasing Power)")
        if show_inflation:
            st.metric(
                label=f"What this money will actually buy in {years_horizon} years (6% Inflation)", 
                value=f"₹{real_purchasing_power:,.0f}", 
                delta="- Inflation Impact", 
                delta_color="inverse"
            )
            
    st.write("")
    
    # 4. Dynamic Progress Bar
    st.write("**Target Goal Achievement:**")
    capped_progress = min(int(goal_percentage), 100)
    st.progress(capped_progress)
    
    if goal_percentage >= 100:
        st.success(f"🎯 **Phenomenal!** You are strictly on track. This strategy funds **{goal_percentage:,.1f}%** of your target.")
    else:
        # Recalculating the shortfall gap purely based on SIP increase requirement
        shortfall = target_amount - future_value
        extra_monthly_needed = shortfall / ((((1 + m_rate)**total_months - 1) / m_rate) * (1 + m_rate))
        
        if extra_monthly_needed > 100000:
            extra_text = f"₹ {extra_monthly_needed/100000:,.2f} Lakhs/month"
        else:
            extra_text = f"₹ {extra_monthly_needed:,.0f}/month"
            
        st.warning(f"🎯 **Insight:** This strategy covers **{goal_percentage:,.1f}%** of your target. To reach a full 100%, consider pushing your SIP slider up by an additional **{extra_text}**.")

    st.caption("*Note: Projections use an estimated 12.0% per annum return. Mutual Fund investments are subject to market risks.")
    
    st.write("---")
    
    submit_button = st.button("🚀 START THIS PORTFOLIO STRATEGY NOW", use_container_width=True, type="primary")
    
    if submit_button:
        if not full_name or not phone_number or not email_address:
            st.error("Hold up! Please fill out your Name, Phone Number, and Email before starting.")
        else:
            st.balloons()
            st.success(f"Welcome aboard, {full_name}! Your personalized portfolio strategy has been initiated. Mr. Vishal Raj will contact you shortly.")
