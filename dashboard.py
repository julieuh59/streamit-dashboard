import streamlit as st
import pandas as pd

st.title("Work Order Dashboard (Excel)")

# Load Excel file
file_path = "Dashboard.xlsx"  # Change this to GitHub raw URL when deploying online
df = pd.read_excel(file_path, engine='openpyxl')

# Drop completely empty columns
df = df.dropna(axis=1, how='all')

# Show raw data
st.subheader("Raw Work Order Data")
st.dataframe(df)

# Work Orders by Type
if 'WO Type' in df.columns:
    st.subheader("Work Orders by Type")
    wo_type_counts = df['WO Type'].value_counts()
    st.bar_chart(wo_type_counts)

# Work Orders by Building
if 'Building' in df.columns:
    st.subheader("Work Orders by Building")
    building_counts = df['Building'].value_counts()
    st.bar_chart(building_counts)

# Status Counts (Open vs. Historical)
if 'Status' in df.columns:
    st.subheader("Work Order Status")
    status_counts = df['Status'].value_counts()
    st.bar_chart(status_counts)

# Cost Summary
if 'Extcost' in df.columns:
    st.subheader("Cost Summary")
    st.write("Total Cost: $", round(df['Extcost'].sum(), 2))
