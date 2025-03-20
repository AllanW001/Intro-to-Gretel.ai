from gretel_client import Gretel

gretel = Gretel(api_key="your_api_key_here")

tabular = gretel.factories.initialize_navigator_api("tabular", backend_model="gretelai/auto")

prompt = """\
Generate a table with simulated movie streaming ratings. The table should contain the following columns:
- user_id (integer, randomly assigned from 1 to 100)
- movie_id (string, format: movie+title+year, e.g., 'the+cove+2009')
- timestamp (datetime, between 2025-03-09 and 2025-03-15, format: YYYY-MM-DD HH:MM:SS)
- rating (integer, range: 1 to 5)
"""

df = tabular.generate(prompt, num_records=100)
# print(df)

# saved as csv file
df.to_csv("gretel_movie_ratings.csv", index=False)
print("Synthetic dataset saved as gretel_movie_ratings.csv")

