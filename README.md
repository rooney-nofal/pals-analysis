# pals-analysis
# Palworld Data Exploration Dashboard

This project is a complete exploratory data analysis (EDA) and dashboard implementation based on a rich dataset from the game **Palworld**. It includes data cleaning, statistical exploration, visual analytics, and the development of a custom **Streamlit dashboard** to visualize the most important attributes and insights related to Pals.

---

## 📁 Project Structure

- `Palworld_Data--Palu combat attribute table.csv`: Raw data file (from Google Sheets)
- `app.py`: Streamlit app source code
- `README.md`: Project documentation (you’re reading it!)
- `images/`: Screenshots or saved charts (optional)

---

## 📊 Objectives

This project answers a full set of analysis questions inspired by an academic-style case study PDF, including:

1. Cleaning and exploring Pal attributes (HP, attack, defense, etc.)
2. Visualizing combat power distribution
3. Comparing rarity and performance
4. Identifying the best Pals for combat, support, speed, and exploration
5. Highlighting work skills and nocturnal behaviors
6. Constructing the most balanced team of Pals
7. Finding the most versatile and specialized Pals

---

## 🚀 Technologies Used

- **Python 3**
- **Pandas** for data manipulation
- **Seaborn / Matplotlib** for visualization
- **Streamlit** for dashboard development
- **Scikit-learn** for normalization (MinMaxScaler)

---

## 📈 Streamlit Dashboard Features

The dashboard includes:

- 📊 **Combat Power Distribution** (histogram)
- 📐 **Volume Size vs. HP**
- ❤️ **HP and Defense Charts**
- ⚔️ **Top 10 Strongest Pals**
- 🧪 **Attribute Comparisons by Rarity**
- 🧭 **Exploration Score Analysis**
- 🧠 **Versatility Ranking**
- 🌙 **Nocturnal Behavior**
- 🛠️ **Work Skill Frequencies**

To run the dashboard:

```bash
streamlit run app.py

Analytical Highlights
Question	Summary
(a–c)	Data loaded and cleaned, including handling missing values and type conversions
(d–e)	Duplicate rows removed, columns renamed/standardized
(f–g)	Combat power calculated and visualized
(h)	Attribute distributions by rarity plotted
(i–j)	Impact of rarity analyzed and top attackers extracted
(k–l)	Size vs. performance and speed vs. efficiency relationships analyzed
(m)	Most balanced team of 5 Pals selected
(n–o)	Work skill frequencies (common and rare) discovered and charted
(p–q)	Night workers counted and profiled
(r–s)	Versatility and exploration performance scores calculated and visualized

🌟 Insights Discovered
Dark-element Pals dominate the night workforce.

Larger Pals tend to have slightly better combat stats.

Combat efficiency isn't always tied to speed, but fast Pals shine in exploration.

Top explorers are agile, enduring, and often high-support Pals.

Versatile Pals balance high stats across many categories — true all-rounders.
