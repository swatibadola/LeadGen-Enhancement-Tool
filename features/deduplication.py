

def deduplicate_data(df):
    deduped_df =  df.drop_duplicates(subset='Company', keep='first').reset_index(drop=True)
    return deduped_df