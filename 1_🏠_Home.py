import streamlit as st

st.set_page_config(
    page_title="InvestWise AI",
    page_icon="💼",
    layout="wide"
)
st.title("🚀 InvestWise AI")

st.subheader("Personalized Investment Recommendation System")

st.write("""
Welcome to **InvestWise AI**, an intelligent web application that helps users choose suitable investment options using Machine Learning.

### 🌟 Key Features
- 🎯 AI-Powered Investment Recommendation
- 📈 Investment Growth Projection
- 📊 Portfolio Allocation Visualization
- 💰 Financial Health Score
- ⚡ Fast & Interactive Dashboard
""")

st.markdown("---")st.title("💼 InvestWise AI")
st.subheader("Intelligent Investment Recommendation System")

st.markdown("---")

col1, col2 = st.columns([2,1])

with col1:

    st.header("🚀 About the Project")

    st.write("""
InvestWise AI is an intelligent investment recommendation system
that uses Machine Learning to analyze a user's financial profile
and recommend the most suitable investment option.

The recommendation is based on:

- 👤 Age
- 💰 Monthly Income
- 💸 Monthly Expenses
- 🏦 Savings
- 📈 Investment Amount
- 🎯 Financial Goal
- ⚠ Risk Tolerance
- 📅 Investment Duration
""")

with col2:

    st.success("✔ Machine Learning")
    st.success("✔ AI Recommendation")
    st.success("✔ Portfolio Allocation")
    st.success("✔ Growth Prediction")
    st.success("✔ Interactive Charts")

st.markdown("---")

st.header("⚙ How It Works")

st.write("""
### Step 1
Enter your financial details.

### Step 2
Machine Learning analyzes your profile.

### Step 3
AI predicts the best investment.

### Step 4
View portfolio allocation and growth projection.
""")

st.markdown("---")

st.header("🛠 Technologies Used")

c1,c2,c3,c4 = st.columns(4)

c1.info("Python")
c2.info("Streamlit")
c3.info("Scikit-Learn")
c4.info("Plotly")

st.markdown("---")

st.header("🎯 Project Features")

st.write("""
✅ AI-based Investment Recommendation

✅ Portfolio Allocation

✅ Investment Growth Projection

✅ Risk Analysis

✅ Annual Return Estimation

✅ Interactive Dashboard

✅ Financial Learning
""")

st.markdown("---")

st.success("👈 Select 'Investment Analysis' from the sidebar to begin.")

st.caption("Developed by Anubhav Srivastava")
st.markdown("---")

st.header("🎯 Why InvestWise AI?")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🤖 AI Powered")

with col2:
    st.success("📊 Portfolio Analysis")

with col3:
    st.success("📈 Growth Projection")
