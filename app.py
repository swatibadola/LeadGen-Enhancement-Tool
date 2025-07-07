# STREAMLIT APP FILE

import streamlit as st
import pandas as pd

from features.deduplication import deduplicate_data
from features.email_validation import validate_emails
from features.lead_scoring import lead_scores
from features.crm_export import generate_crm_csv

from utils.helpers import read_csv


# SIDEBAR
st.sidebar.title('LeadGen Prototype Tool')
st.sidebar.info(
    "This tool helps you clean, score, and export leads for CRM integration. "
    "Upload a dataset or use the sample data included."
)

# TITLE
st.markdown("<h1 style='color: #6C63FF;'>🚀 Lead Generation Prototype Tool</h1>", unsafe_allow_html=True)
st.markdown("<p>Use this tool to process, clean, and prepare your leads for CRM integration.</p>", unsafe_allow_html=True)


# DATA UPLOAD
st.markdown("---")
st.markdown("<h2>📤 Upload & Preview Leads</h2>", unsafe_allow_html=True)

uploaded_file = st.file_uploader('Upload your leads CSV', type=['csv'])
df = read_csv(uploaded_file)

with st.expander('Preview Leads data'):
    st.dataframe(df)

# FEATURES - DATA PROCESSING
st.markdown("---")
st.markdown("<h2>🧹 Data Processing Features</h2>", unsafe_allow_html=True)

selected_steps = st.multiselect(
    "Choose processing steps to apply:",
    ['Remove Duplicates', 'Validate emails', 'Calculate lead scores']
)

# LEAD SCORING THRESHOLD SECTION
if 'Calculate lead scores' in selected_steps:
    st.markdown("<h3>🎯 Lead Scoring Options</h3>", unsafe_allow_html=True)
    apply_score_filter = st.checkbox('Filter by minimum lead score')

    if apply_score_filter:
        score_threshold = st.number_input(
                "Enter your desired minimum lead score (0-100):",
                min_value = 0,
                max_value = 100,
                value = 40,
                step = 1,
                help = 'Type the minimum score you consider as a high-quality lead',
                key = 'score_threshold_input'
            )

# PROCESSING SELECTED STEPS
if st.button('Process Selected Steps'):
    processed_df = df.copy()

    # REMOVE DEDUPLICATES
    try:
        if 'Remove Duplicates' in selected_steps:
            processed_df = deduplicate_data(processed_df)
            st.success('✅ Deduplication completed!')

    except KeyError:
        st.error(f"🚨 Missing required column for deduplication. Please ensure your dataset has a 'Company' column or adjust your processing steps.")
        st.stop()

    # EMAIL VALIDATION
    REQUIRED_COLUMNS = ['Company', 'Company Email']
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing_cols:
        st.error(f"🚨 Uploaded dataset is missing required columns: {', '.join(missing_cols)}. Please upload a valid leads file.")
        st.stop()

    if 'Validate emails' in selected_steps:
        processed_df = validate_emails(processed_df)
        st.success("✅ Email validation completed!")
        processed_df = processed_df[processed_df['email_valid'] == True]
        st.subheader("📧 Leads with Valid Emails")
    
    if "Calculate lead scores" in selected_steps:
        processed_df = lead_scores(processed_df)
        st.success('✅ Lead scoring completed!')

# and 'apply_score_filter' in locals() and apply_score_filter
        # APPLYING FILTERING IF CHECKBOX WAS CHECKED
        if 'Calculate lead scores' in selected_steps:
            processed_df = processed_df[processed_df['lead_score'] >= score_threshold]
            st.success(f'✅ Filtered leads with lead_score >= {score_threshold}')

    # storing processed_df in session state so it is accessible later
    st.session_state['processed_df'] = processed_df

    with st.expander(' Preview Processed Leads'):
        st.dataframe(processed_df)

    st.download_button(
        label="💾 Download Processed CSV",
        data=processed_df.to_csv(index=False).encode("utf-8"),
        file_name="processed_leads.csv",
    )

    st.toast("🎉 Leads processing complete! Ready for CRM export.", icon="✅")

    # CRM EXPORT SECTION
    st.markdown("---")
    st.markdown("<h2>📤 CRM Export</h2>", unsafe_allow_html=True)

    if 'processed_df' in st.session_state:
        if st.button("🏁 Generate CRM-ready CSV", key="generate_crm_btn"):
            df_to_use = st.session_state["processed_df"]
            # st.write(f"✅ Processed DataFrame shape: {df_to_use.shape}")

            try:
                crm_ready_df = generate_crm_csv(df_to_use)
                st.success("✅ CRM-compatible CSV generated successfully!")
                st.dataframe(crm_ready_df)

                st.download_button(
                    label="💾 Download CRM-ready CSV",
                    data=crm_ready_df.to_csv(index=False).encode("utf-8"),
                    file_name="crm_ready_leads.csv"
                )
                st.toast("🎉 CRM-ready file is ready to download!", icon="✅")
            except Exception as e:
                st.error("🚨 Something went wrong while generating the CRM CSV. Please check your data and try again.")
                st.write(f"🔎 Debug info: {e}")
    else:
        st.info("ℹ️ Process your leads first by clicking 'Process Selected Steps' before generating a CRM-ready file.")