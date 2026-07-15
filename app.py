import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Travel Planner", page_icon="✈️")

st.title("✈️ AI Travel Planner")

# Load dataset
df = pd.read_csv("Top Indian Places to Visit-selected-columns.csv").drop(columns=["Unnamed: 0"])
# Select destination
destination = st.selectbox(
    "Select Tourist Place",
    sorted(df["Name"].dropna().unique())
)

# Travel details
days = st.number_input("Number of Days", min_value=1, value=3)

budget = st.number_input("Budget (₹)", min_value=1000, value=10000)

interest = st.selectbox(
    "Travel Interest",
    ["Adventure", "Nature", "Historical", "Shopping", "Food", "Family"]
)

if st.button("Generate Travel Plan"):

    place = df[df["Name"] == destination]

    st.success("Travel Plan Generated Successfully!")

    st.subheader("Destination Details")
    st.dataframe(place)

    st.subheader("Your Trip Summary")

    st.write(f"📍 Destination : {destination}")
    st.write(f"🗓 Duration : {days} Days")
    st.write(f"💰 Budget : ₹{budget}")
    st.write(f"❤️ Interest : {interest}")

    st.subheader("Suggested Itinerary")

    for i in range(1, days + 1):
        st.write(f"**Day {i}:** Explore {destination} and nearby attractions.")
        st.subheader("📍 Google Maps")

st.write(f"https://www.google.com/maps/search/{destination}")