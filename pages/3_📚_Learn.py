import streamlit as st

st.title("📚 Investment Learning")

topics = {
    "📈 Stocks":
    "Stocks represent ownership in a company. They offer high returns but involve higher risk.",

    "💰 Mutual Funds":
    "Mutual funds pool money from many investors and are managed by professionals.",

    "🏦 Fixed Deposits":
    "FDs are safe investments with guaranteed returns but lower growth.",

    "🏛 Government Bonds":
    "Government-backed securities with low risk and stable returns.",

    "🥇 Gold ETF":
    "Gold ETFs allow investment in gold without physically buying it."
}

for title, desc in topics.items():
    with st.expander(title):
        st.write(desc)