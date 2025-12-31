import streamlit as st
import math

st.set_page_config(
    page_title="Lot Calculator",
    layout="centered"
)

LOT_SIZES = {
    "NIFTY": 65,
    "SENSEX": 20
}


st.title("Lot Calc")

st.markdown("Fast quantity calculation")

capital = st.number_input(
    "💰 Capital (₹)",
    min_value=0,
    value=100000,
    step=5000
)

premium = st.number_input(
    "📈 Option Premium (₹)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

instrument = st.radio(
    "📊 Instrument",
    ["NIFTY", "SENSEX"],
    horizontal=True
)

# CALCULATION
lot_size = LOT_SIZES[instrument]

if capital > 0 and premium > 0:
    capital_per_lot = premium * lot_size
    max_lots = math.floor(capital / capital_per_lot)
    quantity = max_lots * lot_size
    capital_used = quantity * premium
    capital_left = capital - capital_used

    st.divider()

    st.subheader("Order Details (Upstox)")

    st.metric("Quantity to Enter", quantity)
    st.metric("Lots", max_lots)
    st.metric("Capital Used (₹)", f"{capital_used:,.0f}")
    st.metric("Capital Left (₹)", f"{capital_left:,.0f}")

    if max_lots == 0:
        st.warning("⚠️ Capital too low for even 1 lot")
else:
    st.info("Enter capital and premium to calculate")

