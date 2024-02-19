# Goal

- general information/thoughts relating to the project

### Notes

- it looks like WorldBank altered their API or is having issues with it now, API endpoints are redirecting to their "boost-portal"

### Helpful links

- info on Worldbank API calls: <https://datahelpdesk.worldbank.org/knowledgebase/articles/898581>

### Pandas info

- iterating over rows of a DF
  - <https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas?rq=1>
    - in order of speed: vectorize using `vec_numpy` or `vec`, list comprehension, `.apply()`, `.iterrows()`
