import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/cleaned_gold_price_data.csv")

# Define a simulated Elasticsearch query (mimic the query structure)
query = {
    "query": {
        "match": {
            "Date": "2008-01-02"
        }
    }
}

# Simulate the 'match' query on the DataFrame (this would be equivalent to an Elasticsearch match query)
def elasticsearch_query(df, query):
    # Extract the search term (date) from the query
    search_date = query["query"]["match"]["Date"]
    
    # Perform the filtering (equivalent to an Elasticsearch query)
    result = df[df["Date"] == search_date]
    
    return result

# Perform the simulated search
result = elasticsearch_query(df, query)

# Print the results (simulating Elasticsearch response)
print("Search results from simulated Elasticsearch query:")
print(result)