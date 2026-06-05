import os 
import dotenv
import requests
import json
from pathlib import Path
dotenv.load_dotenv()

# PYTHONPATH = 

class TMDBClient:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def init_client(self, endpoint: str):
        url = f"{self.base_url}/{endpoint}"
        try:
            
            response = requests.get(url=url,
                                    params={'api_key': self.api_key,
                                            'page':1})
            
            response.raise_for_status() 
            response_data = response.json() 
            
            return response_data

        except Exception as e:
            print("got execption while running init_client", e)

    
if __name__ == "__main__":
    import pandas as pd
    client = TMDBClient(api_key=os.environ.get("TMDB_API_KEY"), base_url=os.environ.get("BASE_URL"))
    resp = client.init_client(endpoint='discover/movie')
    print(resp)
    print(json.dump(resp, open("tmdb_response.json", "w"), indent=4))
    df = pd.DataFrame(resp['results']).to_csv("tmdb_response.csv", index=False)
    # df.to_csv("tmdb_response.csv", index=False)


    






        
    


