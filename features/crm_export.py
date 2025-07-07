import pandas as pd

def generate_crm_csv(df):
    try:
        crm_df = df.copy()

        # RENAMING EXPECTED COLUMNS
        rename_map = {}
        if 'Company' in crm_df.columns:
            rename_map['Company'] = 'Company Name'
        if 'Company Email' in crm_df.columns:
            rename_map['Company Email'] = 'Email'
        if 'lead_score' in crm_df.columns:
            rename_map['lead_score'] = 'Lead Score'

        crm_df = crm_df.rename(columns=rename_map)

        # Checking required columns
        required_cols = ['Company Name', 'Email', 'Lead Score']
        missing_cols = [col for col in required_cols if col not in crm_df.columns]
        if missing_cols:
            raise ValueError(f"🚨 Cannot generate CRM CSV. Missing required columns: {', '.join(missing_cols)}")

        return crm_df[required_cols]
    except Exception as e:
        raise e