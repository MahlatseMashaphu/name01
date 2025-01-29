# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# My Plot of data

import streamlit as st
import pandas as pd

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Dr. Mahlatse Mashaphu"
field = "Conservation Genetics"
institution = "University of KwaZulu-Natal"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Add research background
st.header("Research background")
st.write("I am a Postdoctoral Researcher at the University of KwaZulu-Natal, specializing in conservation genetics. My work combines population genetics and eDNA metabarcoding to study freshwater fish in South Africa. I focus on conserving native species like Oreochromis mossambicus and tackling the impacts of invasive species. My research aims to protect biodiversity, promote sustainable resource use, and support better management of freshwater ecosystems.")

# Add Research interest
st.header("Research interest")
st.write("1. Conservation genetics of freshwater fish")
st.write("2. Population genetics and evolutionary biology")
st.write("3. eDNA metabarcoding for species monitoring")
st.write("4. Invasive species detection and management")
st.write("5. Population genetics and evolutionary biology")

# Add Current Research
st.header("Current research")
st.write("1. Assessing genetic diversity and population structure of Oreochromis mossambicus")
st.write("2. Developing species-specific primers for distinguishing O. mossambicus and O. niloticus")
st.write("3. Using eDNA metabarcoding to monitor invasive freshwater fish in South African river systems")

# Add Collaborations and Opportunities
st.header("Collabroations and opprtunities")
st.write("I am open to collaborations in conservation genetics, fisheries management, and molecular ecology. If you're interested in working together, feel free to reach out.")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "fortunate.mashaphu@gmail.com"
st.write(f"You can reach {name} at {email}.")
















