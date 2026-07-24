import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Investment Analysis",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load ML Model
# -----------------------------
@st.cache_resource
def load_models():
    model = joblib.load("model/model.pkl")
    goal_encoder = joblib.load("model/goal_encoder.pkl")
    risk_encoder = joblib.load("model/risk_encoder.pkl")
    recommendation_encoder = joblib.load("model/recommendation_encoder.pkl")

    return (
        model,
        goal_encoder,
        risk_encoder,
        recommendation_encoder,
    )


model, goal_encoder, risk_encoder, recommendation_encoder = load_models()

# -----------------------------
# Heading
# -----------------------------
st.title("📊 Investment Analysis")

st.write(
    "Fill in your financial details below and let our AI recommend the best investment option."
)

st.markdown("---")

# -----------------------------
# Input Form
# -----------------------------

left, right = st.columns(2)

with left:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=80,
        value=25,
    )

    income = st.number_input(
        "Monthly Income (₹)",
        min_value=10000,
        max_value=500000,
        value=50000,
        step=1000,
    )

    expenses = st.number_input(
        "Monthly Expenses (₹)",
        min_value=5000,
        max_value=500000,
        value=25000,
        step=1000,
    )

    savings = st.number_input(
        "Monthly Savings (₹)",
        min_value=0,
        max_value=500000,
        value=10000,
        step=500,
    )

with right:

    investment = st.number_input(
        "Monthly Investment (₹)",
        min_value=500,
        max_value=100000,
        value=5000,
        step=500,
    )

    goal = st.selectbox(
        "Investment Goal",
        [
            "Wealth Creation",
            "Retirement",
            "Child Education",
            "Emergency Fund",
            "House Purchase",
        ],
    )

    duration = st.slider(
        "Investment Duration (Years)",
        min_value=1,
        max_value=30,
        value=10,
    )

    risk = st.selectbox(
        "Risk Tolerance",
        [
            "Low",
            "Medium",
            "High",
        ],
    )

st.markdown("---")

# -----------------------------
# Prediction
# -----------------------------

if st.button("🚀 Get AI Recommendation"):

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
        risk_value,
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
        risk_value,
    ]])

    confidence = prediction_proba.max() * 100

    st.success("✅ Analysis Completed Successfully!")

    st.subheader("🎯 AI Recommendation")

    st.success(
    f"Our AI recommends **{recommendation}** based on your age, income, savings, investment goal and risk tolerance."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "AI Confidence",
            f"{confidence:.1f}%"
        )

        st.progress(min(confidence / 100, 1.0))

    with c2:
        st.metric(
            "Risk Level",
            risk,
        )
        st.subheader("⚠ Risk Assessment")

        risk_score = {
        "Low": 30,
        "Medium": 60,
        "High": 90
        }

        st.progress(risk_score[risk] / 100)

        st.write(f"Risk Profile: **{risk}**")

    with c3:
        st.metric(
            "Monthly Investment",
            f"₹{investment:,}",
        )

    st.markdown("---")
        # -----------------------------
    # Estimated Annual Return
    # -----------------------------

    st.subheader("📈 Estimated Annual Return")

    returns = {
        "Stocks": "12% - 18%",
        "Mutual Fund": "10% - 14%",
        "Government Bonds": "7% - 9%",
        "Fixed Deposit": "6% - 7%",
        "Balanced Fund": "8% - 11%"
    }

    st.info(
        f"Expected Annual Return: **{returns.get(recommendation, '8%')}**"
    )

    # -----------------------------
    # Total Investment
    # -----------------------------

    st.subheader("💰 Total Planned Investment")

    total_investment = investment * 12 * duration

    st.metric(
        "Total Investment",
        f"₹{total_investment:,}"
    )

    st.markdown("---")

    # -----------------------------
    # Investment Growth Projection
    # -----------------------------

    st.subheader("📈 Investment Growth Projection")

    growth_rate = {
        "Stocks": 0.15,
        "Mutual Fund": 0.12,
        "Government Bonds": 0.08,
        "Fixed Deposit": 0.07,
        "Balanced Fund": 0.10
    }

    rate = growth_rate.get(recommendation, 0.10)

    years = list(range(1, duration + 1))

    invested = []
    estimated = []

    amount = 0

    for year in years:
        invested_amount = investment * 12 * year
        invested.append(invested_amount)

        amount = (amount + investment * 12) * (1 + rate)
        estimated.append(round(amount))

    chart = pd.DataFrame({
        "Year": years,
        "Amount Invested": invested,
        "Estimated Value": estimated
    })

    fig = px.line(
        chart,
        x="Year",
        y=["Amount Invested", "Estimated Value"],
        markers=True,
        title="Investment Growth Over Time"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # -----------------------------
    # Suggested Portfolio
    # -----------------------------

    st.subheader("📂 Suggested Portfolio")
        # -----------------------------
    # Portfolio Allocation
    # -----------------------------

    if recommendation == "Stocks":

        portfolio = {
            "Stocks": 70,
            "Mutual Fund": 20,
            "Gold ETF": 10
        }

    elif recommendation == "Mutual Fund":

        portfolio = {
            "Mutual Fund": 60,
            "Gold ETF": 20,
            "Fixed Deposit": 20
        }

    elif recommendation == "Government Bonds":

        portfolio = {
            "Government Bonds": 60,
            "Fixed Deposit": 30,
            "Gold ETF": 10
        }

    elif recommendation == "Fixed Deposit":

        portfolio = {
            "Fixed Deposit": 70,
            "Gold ETF": 20,
            "Mutual Fund": 10
        }

    else:

        portfolio = {
            "Balanced Fund": 60,
            "Gold ETF": 20,
            "Fixed Deposit": 20
        }

    for investment_name, allocation in portfolio.items():
        st.write(f"**{investment_name}** : {allocation}%")

    st.markdown("---")

    # -----------------------------
    # Portfolio Pie Chart
    # -----------------------------

    st.subheader("🥧 Portfolio Allocation Chart")

    portfolio_df = pd.DataFrame({
        "Investment": list(portfolio.keys()),
        "Allocation": list(portfolio.values())
    })

    fig = px.pie(
        portfolio_df,
        names="Investment",
        values="Allocation",
        hole=0.45,
        title="Recommended Portfolio Distribution"
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # -----------------------------
    # Portfolio Summary
    # -----------------------------

    st.success(
        "This portfolio is generated according to your age, investment goal, financial condition and risk tolerance."
    )

    st.markdown("---")
        # -----------------------------
    # Why this Recommendation
    # -----------------------------

    st.subheader("💡 Why this Recommendation?")

    st.write("Our Machine Learning model analyzed the following factors before making this recommendation:")

    reasons = [
        "👤 Your Age",
        "💰 Monthly Income",
        "💸 Monthly Expenses",
        "🏦 Monthly Savings",
        "📈 Investment Amount",
        "🎯 Investment Goal",
        "⚠ Risk Tolerance",
        "📅 Investment Duration"
    ]

    for reason in reasons:
        st.write(f"✅ {reason}")

    st.markdown("---")

    # -----------------------------
    # Financial Summary
    # -----------------------------

    st.subheader("📋 Financial Summary")

    summary = pd.DataFrame({
        "Parameter": [
            "Age",
            "Monthly Income",
            "Monthly Expenses",
            "Monthly Savings",
            "Monthly Investment",
            "Investment Goal",
            "Risk Level",
            "Duration"
        ],
        "Value": [
            age,
            f"₹{income:,}",
            f"₹{expenses:,}",
            f"₹{savings:,}",
            f"₹{investment:,}",
            goal,
            risk,
            f"{duration} Years"
        ]
    })

    st.dataframe(summary, use_container_width=True)

    st.markdown("---")

    # -----------------------------
    # How to Start Investing
    # -----------------------------

    st.subheader("🚀 How to Start")

    st.info("""
1️⃣ Complete your KYC.

2️⃣ Open a Demat / Investment Account.

3️⃣ Invest every month (SIP).

4️⃣ Diversify your portfolio.

5️⃣ Review investments annually.

6️⃣ Stay invested for the long term.
""")

    st.markdown("---")

    # -----------------------------
    # Disclaimer
    # -----------------------------

    st.warning(
        "This recommendation is generated by a Machine Learning model for educational purposes only and should not be considered professional financial advice."
    )

    st.markdown("---")

    # -----------------------------
    # Footer
    # -----------------------------

    st.caption(
        "© 2026 InvestWise AI | Developed by Anubhav Srivastava | Built using Python, Streamlit, Scikit-Learn and Plotly."
    )