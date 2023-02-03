import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from open_jobs import open_jobs

role = st.text_input("Role", help="e.g Python Developer")
location = st.text_input("Location", help="e.g new york")
limit = st.slider("Limit", 20, 200, step=20)

if st.button("Search Jobs"):
    st.write("loading...")
    jobs = open_jobs(role, location, limit)
    print(jobs)
    df = pd.DataFrame(jobs)
    print(df)
    st.table(df)
    # AgGrid(df)
    st.write("Done")
