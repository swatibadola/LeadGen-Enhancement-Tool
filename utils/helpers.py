import pandas as pd
import streamlit as st

def read_csv(uploaded_file, sample_file='sample_data.csv'):
    ''' Will read the uploaded csv safely; fallback to sample csv if none is provided'''
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.success('✅ File uploaded successfully')
            return df
        except Exception as e:
            st.error(f'🚨 Failed to read CSV. Please check the file format. \n\nError: {e}')
            st.stop()

    else:
        df = pd.read_csv('sample_data.csv')
        st.info('Using included sample dataset (sample_data.csv)')
        return df