import httpx
from app.core.config import settings




# import os 
# import dotenv
# import requests
# import json
# from pathlib import Path
# dotenv.load_dotenv()


class TMDBClient:

    def __init__(self):
        self.api_key = settings.TMDB_API_KEY
        # self.base_url = settings.BASE_URL
        self.client = httpx.Client(timeout=15.0)
    

    def _get(self, endpoint: str, params:dict=None):
        if params is None:
            params = {}

        params['api_key'] = self.api_key
        
        response = self.client.get(f"{settings.BASE_URL}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()
    
    def get_movie(self, page:int):
        return self._get("discover/movie", params={'page':page})

    def get_movie_details(self, movie_id: int):
        return self._get(f"movie/{movie_id}")
    
    def get_credits(self, movie_id: int):
        return self._get(f"movie/{movie_id}/credits")
    
    def get_keywords(self, movie_id: int):
        return self._get(f"movie/{movie_id}/keywords")
    
    def get_similar_movies(self, movie_id: int):
        return self._get(f"movie/{movie_id}/similar")

    def close(self):
        self.client.close()

#     def init_client(self, endpoint: str):
#         url = f"{self.base_url}/{endpoint}"
#         try:
            
#             response = requests.get(url=url,
#                                     params={'api_key': self.api_key,
#                                             'page':1})
            
#             response.raise_for_status() 
#             response_data = response.json() 
            
#             return response_data

#         except Exception as e:
#             print("got execption while running init_client", e)

    
# if __name__ == "__main__":
#     import pandas as pd
#     client = TMDBClient(api_key=os.environ.get("TMDB_API_KEY"), base_url=os.environ.get("BASE_URL"))
#     resp = client.init_client(endpoint='discover/movie')
#     print(resp)
#     print(json.dump(resp, open("tmdb_response.json", "w"), indent=4))
#     pd.DataFrame(resp['results']).to_csv("tmdb_response.csv", index=False)
#     # df.to_csv("tmdb_response.csv", index=False)
