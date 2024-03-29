#Input the relevant libraries
import streamlit as st
import altair as alt
import nltk
import numpy as np
import pandas as pd
import base64

# Define the Streamlit app
def app():
    
    # Create a sample dataframe
    data = {
        'Name': ['John', 'Mary', 'Mike', 'Linda'],
        'Age': [30, 25, 40, 35],
        'City': ['New York', 'London', 'Paris', 'Tokyo']
    }
    df = pd.DataFrame(data)

    # Create a button to save data to CSV file
    if st.button('Save data to CSV file'):
        # Save the dataframe to a CSV file
        csv = df.to_csv(index=False)
        if csv:
            b64 = base64.b64encode(csv.encode()).decode()  # Convert to base64
            href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV file</a>'
            st.markdown(href, unsafe_allow_html=True)
        else:
            st.write("Error: Unable to generate CSV file.")
      
             
# run the app
if __name__ == "__main__":
    app()
