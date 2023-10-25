import pandas as pd

# Define your input data and user-provided URLs
input_file = 'input.csv'
user_provided_urls = {
    'Name': ['John Doe', 'Alice Smith'],
    'Major': ['Computer Science', 'Electrical Engineering'],
    'Year': [2021, 2020],
    'UserURL': [
        'https://www.linkedin.com/in/johndoe',
        'https://www.linkedin.com/in/alicesmith'
    ]
}

# Load the input data from the web scraper
df = pd.read_csv(input_file)

# Create a new column 'IsAccurate' to store the accuracy result
df['IsAccurate'] = df.apply(lambda row:
    row['LinkedIn'] == user_provided_urls['UserURL'][row.name], axis=1)

# Display the comparison result
print(df[['Name', 'Major', 'Year', 'LinkedIn', 'IsAccurate']])

# Save the result to a new CSV file
result_file = 'result.csv'
df.to_csv(result_file, index=False)

print(f"Comparison result saved to {result_file}")
