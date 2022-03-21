import pandas as pd
from IPython.display import display
pd.set_option("display.max_columns", None)
import warnings
warnings.filterwarnings("ignore")

def proportional_sightings(birds:pd.DataFrame, scope_constraints:dict, search_params:dict):
	all_sightings = birds
	for constraint in scope_constraints:
		all_sightings = all_sightings.loc[all_sightings[constraint] == scope_constraints[constraint]]
	all_sum = all_sightings["individualCount"].sum()
	search_sightings = all_sightings
	for constraint in search_params:
		search_sightings = search_sightings.loc[search_sightings[constraint] == search_params[constraint]]
	search_sum = search_sightings['individualCount'].sum()
	proportion = search_sum / all_sum
	return proportion

birds = pd.read_csv("birds.csv", index_col=False)
display(birds.head())
print("Number of rows:", birds.shape[0])
scope_constraints = {"year": 2018, "month": 6}
search_params = {"verbatimScientificName": "Turdus iliacus"}
prop = proportional_sightings(birds, scope_constraints, search_params)
print(prop)
