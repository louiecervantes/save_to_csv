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
    # Prompt the user to enter a filename
    filename = st.text_input('Enter a filename:', 'data.csv')
    # Create a button to save data to CSV file
    if st.button('Save data to CSV file'):
        # Save the dataframe to a CSV file
        csv = df.to_csv(filename, index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # Convert to base64
        href = f'<a href="data:file/csv;base64,{b64}" download="' + fiename + '">Download CSV file</a>'
        st.markdown(href, unsafe_allow_html=True)       
        st.success(f'Data saved to {filename}!')         
             
# run the app
if __name__ == "__main__":
    app()
