"""
Script to pull the daily trend from PyTrends
"""

import pandas as pd
from pytrends.request import TrendReq
import json

# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq(tz=360) 

# We want to get the top searched terms the last day
df = pytrend.trending_searches(pn='denmark')
# get top trending search term
top_search = df.iloc[0,0]
print("Top search term: " + top_search)
# get related queries
pytrend.build_payload(kw_list=[top_search])
related_queries = pytrend.related_queries()[top_search]["top"]
print("Related queries: " + str(related_queries))

# save to json
json_format = {top_search: related_queries.to_dict(orient='records')}
with open('daily_trend.json', 'w') as outfile:
    json.dump(json_format, outfile)