import streamlit as st

st.set_page_config(
    page_title="InvestWise AI",
    page_icon="💼",
    layout="wide"
)

st.title("💼 InvestWise AI")
st.caption("AI-Powered Personal Investment Advisor")

st.markdown("---")

col1, col2 = st.columns([2,1])

with col1:
    st.header("Welcome!")

    st.write("""
InvestWise AI helps beginners make smarter investment decisions
using Artificial Intelligence and Machine Learning.

Instead of guessing where to invest,
the system analyzes your financial profile
and recommends the most suitable investment option.
""")

    st.success("✔ Personalized Recommendations")
    st.success("✔ AI Risk Analysis")
    st.success("✔ Investment Readiness Score")
    st.success("✔ Beginner Friendly Guidance")

with col2:
    st.metric("AI Accuracy", "92%")
    st.metric("Investment Types", "5")
    st.metric("Risk Levels", "3")

st.markdown("---")

st.subheader("How It Works")

st.write("""
1️⃣ Enter your financial details.

2️⃣ AI analyzes your profile.

3️⃣ Get personalized investment recommendations.

4️⃣ Learn why the recommendation was made.

5️⃣ Start investing confidently.
""")

st.info("👈 Use the sidebar to navigate to the Investment Analysis page.")