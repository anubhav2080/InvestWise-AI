import streamlit as st
import joblib

# -------------------------
# Load Model and Encoders
# -------------------------

model = joblib.load("model/model.pkl")
goal_encoder = joblib.load("model/goal_encoder.pkl")
risk_encoder = joblib.load("model/risk_encoder.pkl")
recommendation_encoder = joblib.load("model/recommendation_encoder.pkl")

# -------------------------
# Page Title
# -------------------------

st.title("📊 Investment Analysis")
st.write("Fill in your details to get an AI-powered investment recommendation.")
st.markdown("---")

# -------------------------
# Input Fields
# -------------------------

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=80,
        value=25
    )

    income = st.number_input(
        "Monthly Income (₹)",
        min_value=10000,
        max_value=500000,
        value=50000,
        step=1000
    )

    expenses = st.number_input(
        "Monthly Expenses (₹)",
        min_value=5000,
        max_value=500000,
        value=25000,
        step=1000
    )

    savings = st.number_input(
        "Monthly Savings (₹)",
        min_value=0,
        max_value=500000,
        value=10000,
        step=500
    )

with col2:

    investment = st.number_input(
        "Monthly Investment (₹)",
        min_value=500,
        max_value=100000,
        value=5000,
        step=500
    )

    goal = st.selectbox(
        "Investment Goal",
        [
            "Wealth Creation",
            "Retirement",
            "Child Education",
            "Emergency Fund",
            "House Purchase"
        ]
    )

    duration = st.slider(
        "Investment Duration (Years)",
        1,
        30,
        10
    )

    risk = st.selectbox(
        "Risk Tolerance",
        ["Low", "Medium", "High"]
    )

st.markdown("---")

# -------------------------
# Prediction
# -------------------------

if st.button("🚀 Analyze Investment"):

    goal_value = goal_encoder.transform([goal])[0]
    risk_value = risk_encoder.transform([risk])[0]

    prediction = model.predict([[
        age,
        income,
        expenses,
        savings,
        investment,
        goal_value,
        duration,
        risk_value
    ]])

    recommendation = recommendation_encoder.inverse_transform(prediction)[0]

    prediction_proba = model.predict_proba([[
        age,
        income,
        expenses,
        savings,
        investment,
        goal_value,
        duration,
        risk_value
    ]])

    confidence = prediction_proba.max() * 100

    st.success("✅ Analysis Completed Successfully!")

    st.subheader("🎯 AI Recommendation")

    st.success(f"Recommended Investment: **{recommendation}**")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "AI Confidence",
            f"{confidence:.1f}%"
        )

    with col2:
        st.metric(
            "Risk Level",
            risk
        )

    with col3:
        st.metric(
            "Monthly Investment",
            f"₹{investment:,}"
        )

    st.markdown("---")

    st.subheader("📈 Estimated Annual Return")

    returns = {
        "Stocks": "12% - 18%",
        "Mutual Fund": "10% - 14%",
        "Government Bonds": "7% - 9%",
        "Fixed Deposit": "6% - 7%",
        "Balanced Fund": "8% - 11%"
    }

    st.info(
        f"Expected Annual Return: **{returns.get(recommendation,'8%')}**"
    )

    st.subheader("💰 Total Planned Investment")

    future_value = investment * 12 * duration

    st.metric(
        "Total Investment",
        f"₹{future_value:,}"
    )

    st.markdown("---")

    st.subheader("📂 Suggested Portfolio")

    if recommendation == "Stocks":

        st.write("""
📈 Stocks — 70%

💰 Mutual Funds — 20%

🥇 Gold ETF — 10%
""")

    elif recommendation == "Mutual Fund":

        st.write("""
💰 Mutual Funds — 60%

🥇 Gold ETF — 20%

🏦 Fixed Deposit — 20%
""")

    elif recommendation == "Government Bonds":

        st.write("""
🏛 Government Bonds — 60%

🏦 Fixed Deposit — 30%

🥇 Gold ETF — 10%
""")

    elif recommendation == "Fixed Deposit":

        st.write("""
🏦 Fixed Deposit — 70%

🥇 Gold ETF — 20%

💰 Mutual Funds — 10%
""")

    else:

        st.write("""
⚖️ Balanced Fund — 60%

🥇 Gold ETF — 20%

🏦 Fixed Deposit — 20%
""")

    st.markdown("---")

    st.subheader("💡 Why this recommendation?")

    st.write("✔ Based on your age")

    st.write("✔ Based on your income")

    st.write("✔ Based on your monthly savings")

    st.write("✔ Based on your investment goal")

    st.write("✔ Based on your risk tolerance")

    st.markdown("---")

    st.subheader("🚀 How to Start")

    st.write("""
1. Complete your KYC.

2. Open a Demat/Investment account.

3. Start investing every month.

4. Review your portfolio every year.

5. Stay invested for the long term.
""")

    st.info("This recommendation is for educational purposes only.")