# Webscrappin with Foursquare

These scripts are used to retrieve a list of venues, music pubs, concert halls and all kind of places that may offer a music experience as a core element of its business. With just little modifications you can retrieve whatever you want.

Documentation is very clear in the [Foursquare page](https://location.foursquare.com/developer/) but here is a quick summary:
1. Register in [Foursquare](https://location.foursquare.com/developer/) and create a project. When you do so, you will get an API key that you must write in the `01_retrieveData.py` file.
2. Modify the [categories](https://location.foursquare.com/places/docs/categories) you want to search for. You will get the 50 most relevant results for each category so it's better to add many subcategories instead of just one big category.
3. The url of the query contains a lot of info about what you will get. You can easily understand and modify it with the [Places API](https://location.foursquare.com/developer/reference/place-search).

Now, you should have `.json` file with your results. If you want to process this file, do it in a different script for the following reasons:
- You have 200$ worth of credits per month to make queries; these are renewed the first of every month but of course, you can pay to obtain more in an instant.
- To give an approximation, I have spent around 10$ when retrieving 1000 places.
- The data you want to obtain may come in a slightly different format for different countries so you should take a look when looking in a different location.
- If you don't want to spend credits in vain, store the raw `.json` response and process it in
