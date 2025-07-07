# Checking validity of email addresses in the dataframe, which adds a new column 'Email_Valid' as True or False

import re

def validate_emails(df):
    email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    def check(emailCol):
        if isinstance(emailCol, str):
            return bool(re.match(email_pattern, emailCol))
        return False
    
    df['email_valid'] = df['Company Email'].apply(check)
    
    return df