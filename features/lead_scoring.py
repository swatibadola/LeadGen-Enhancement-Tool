
def lead_scores(df):
    def calculate_score(row):
        try:
            revenue_num = int(row['Revenue'].replace('$', '').replace('M', ''))
        except:
            revenue_num = 0


        # Employees heuristic
        employees_score = min(row['Employees count']/100, 10)

        # BBB rating heuristic
        bbb_map = {'A+':10, 'A':8, 'B':5, 'C':2, 'NR':1}
        bbb_score = bbb_map.get(row['BBB Rating'], 1)


        # Industry heuristic
        industry_score = 5 if 'Information Technology' in row['Industry'] or 'Finance' in row['Industry'] else 0

        # Combine Scores
        total_score = revenue_num/100 + employees_score + bbb_score + industry_score
        return round(total_score, 2)
    
    df['lead_score'] = df.apply(calculate_score, axis=1)
    return df