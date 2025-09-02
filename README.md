# US Cities (Population ≥ 20,000)

This project uses the **U.S. Census Bureau ACS 2023 API** to pull all U.S. "place" records, clean the names, and filter for cities/towns with a population of **20,000 or more**.  
The output is a clean CSV that you can explore, analyze, or use in further projects (e.g., election tracking, city comparisons, dashboards).

---

## 📂 Project Structure
```
us_cities_pop20k/
│
├── us-cities-pop20k.py       # Main Python script
├── us_cities_pop20k.csv      # Output dataset (population ≥ 20k)
└── README.md                 # Project documentation
```

---

## ⚙️ Requirements

- Python 3.8+
- Libraries:
  - `requests`
  - `pandas`

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Witchykey/us-cities-pop20k.git
   cd us-cities-pop20k
   ```

2. Run the script:
   ```bash
   python3 us-cities-pop20k.py
   ```

3. The script will:
   - Fetch all U.S. places from the Census API (ACS 2023, 5-Year Estimates).
   - Clean place names (removing “city”, “town”, “CDP”, etc.).
   - Filter out only those with **population ≥ 20,000**.
   - Save the results to **`us_cities_pop20k.csv`**.

---

## 📊 Output Example

The CSV contains columns:

| city_st        | place_name | state_name | state_abbrev | population | state_fips | place_fips | NAME                       | place_name_raw |
|----------------|------------|-------------|---------------|------------|------------|------------|---------------------------|----------------|
| San Jose, CA   | San Jose   | California  | CA            | 983489     | 06         | 68000      | San Jose city, California | San Jose city  |
| Austin, TX     | Austin     | Texas       | TX            | 979882     | 48         | 05000      | Austin city, Texas        | Austin city    |
| Miami, FL      | Miami      | Florida     | FL            | 453579     | 12         | 45000      | Miami city, Florida       | Miami city     |

---

## 📖 Data Source

- [U.S. Census Bureau](https://api.census.gov/data/2023/acs/acs5)  
  *American Community Survey, 5-Year Estimates (2023).*

---

## ✨ Future Work

- Cross-reference with election calendars to check which cities have upcoming mayor or council elections.  
- Build dashboards for population and civic data analysis.  
- Expand filtering criteria (e.g., metro areas, counties).

---

## 👤 Author
Developed by [Huichuan Li](https://github.com/Witchykey)  
Master’s in Statistics (Data Science Concentration) | Data Scientist | Automation Engineer
