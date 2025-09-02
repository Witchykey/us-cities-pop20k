import requests, pandas as pd

# 1) Pull all places with population
URL = "https://api.census.gov/data/2023/acs/acs5"
params = {
    "get": "NAME,B01003_001E",  # NAME + total population
    "for": "place:*",
    "in": "state:*"
}
resp = requests.get(URL, params=params)
resp.raise_for_status()
rows = resp.json()

df = pd.DataFrame(rows[1:], columns=rows[0])

# 2) Clean + split fields
# NAME is usually like "San Jose city, California" or "Town of X, State"
df["population"] = pd.to_numeric(df["B01003_001E"], errors="coerce")
df["state_fips"] = df["state"]
df["place_fips"] = df["place"]

# Extract city/town name and state via the comma
name_split = df["NAME"].str.split(",", n=1, expand=True)
df["place_name_raw"] = name_split[0].str.strip()
df["state_name"] = name_split[1].str.strip()

# Normalize place_name (strip endings like "city", "town", "village" but keep originals too)
df["place_name"] = (df["place_name_raw"]
                    .str.replace(r"\b(city|town|village|borough|CDP)\b", "", case=False, regex=True)
                    .str.replace(r"\s+", " ", regex=True)
                    .str.strip())

# 3) Filter population > 20,000
df20k = df[df["population"] >= 20000].copy()

# 4) Add a canonical key for searching, e.g., "City, ST"
# (We'll create state abbreviations quickly; a small static map is fine.)
state_abbrev_map = {
    "Alabama":"AL","Alaska":"AK","Arizona":"AZ","Arkansas":"AR","California":"CA","Colorado":"CO","Connecticut":"CT",
    "Delaware":"DE","District of Columbia":"DC","Florida":"FL","Georgia":"GA","Hawaii":"HI","Idaho":"ID","Illinois":"IL",
    "Indiana":"IN","Iowa":"IA","Kansas":"KS","Kentucky":"KY","Louisiana":"LA","Maine":"ME","Maryland":"MD","Massachusetts":"MA",
    "Michigan":"MI","Minnesota":"MN","Mississippi":"MS","Missouri":"MO","Montana":"MT","Nebraska":"NE","Nevada":"NV",
    "New Hampshire":"NH","New Jersey":"NJ","New Mexico":"NM","New York":"NY","North Carolina":"NC","North Dakota":"ND",
    "Ohio":"OH","Oklahoma":"OK","Oregon":"OR","Pennsylvania":"PA","Rhode Island":"RI","South Carolina":"SC","South Dakota":"SD",
    "Tennessee":"TN","Texas":"TX","Utah":"UT","Vermont":"VT","Virginia":"VA","Washington":"WA","West Virginia":"WV",
    "Wisconsin":"WI","Wyoming":"WY","Puerto Rico":"PR"
}
df20k["state_abbrev"] = df20k["state_name"].map(state_abbrev_map).fillna(df20k["state_name"])
df20k["city_st"] = df20k["place_name"] + ", " + df20k["state_abbrev"]

# Save for the next step
df20k = df20k[["city_st","place_name","state_name","state_abbrev","population","state_fips","place_fips","NAME","place_name_raw"]].drop_duplicates()
print(f"{len(df20k):,} places with population >= 20,000")
df20k.head(10)
df20k.to_csv("us_cities_pop20k.csv", index=False)

