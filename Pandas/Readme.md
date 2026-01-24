# 🐼 Data Manipulation with Pandas

This folder contains a comprehensive guide to **Pandas**, the most powerful library for data analysis and manipulation in Python. It provides high-performance, easy-to-use data structures like Series and DataFrames, making it the "Excel of Python."

---

## 📌 Table of Contents
* [📖 What is Pandas?](#-what-is-pandas)
* [📂 Repository Structure](#-repository-structure)
    * [1. Series & DataFrame Introduction](#1-series--dataframe-introduction)
    * [2. DataFrame Essentials](#2-dataframe-essentials)
    * [3. Missing Data Management](#3-missing-data-management)
    * [4. Combining DataFrames](#4-combining-dataframes)
    * [5. GroupBy & Aggregation](#5-groupby--aggregation)
    * [6. Pivot Tables & CrossTabs](#6-pivot-tables--crosstabs)
    * [7. Basic Operations & Broadcasting](#7-basic-operations--broadcasting)
    * [8. Project: Anime Feature Extraction](#8-project-anime-feature-extraction)
    * [9. Project: Countries Dataset Analysis](#9-project-countries-dataset-analysis)

---

## 📖 What is Pandas?
**Pandas** is an open-source library built on top of NumPy. It is used for cleaning, transforming, and analyzing tabular data. 

In the AI/ML pipeline, Pandas is the primary tool used for **Data Preprocessing**—converting raw, messy data into a structured format ready for machine learning models.

---

## 📂 Repository Structure

### 1. Series & DataFrame Introduction
Understanding the two core data structures:
* **Pandas Series:** A one-dimensional labeled array (like a single column or a list).
* **DataFrames:** A two-dimensional, size-mutable, and potentially heterogeneous tabular data structure (like an Excel sheet or SQL table).

### 2. DataFrame Essentials
The basics of interacting with and modifying your tables:
* **Creation:** Building DataFrames from dictionaries, lists, or CSVs.
* **Selection:** Using `.loc` and `.iloc` for indexing.
* **Modification:** Creating and removing columns.
* **Filtering:** Performing **Conditional Selection** (e.g., `df[df['Score'] > 80]`) to extract subsets.

### 3. Missing Data Management
Real-world data is often messy. This notebook covers:
* **Detection:** Finding `null` or `NaN` values using `.isnull()`.
* **Removal:** Dropping missing values with `.dropna()`.
* **Imputation:** Filling missing slots using `.fillna()` or mean/median values.

### 4. Combining DataFrames
Mastering relational data operations:
* **Merging:** SQL-style joining based on common keys.
* **Concatenation:** Stacking DataFrames vertically or horizontally.
* **Joining:** Merging based on the index.

### 5. GroupBy & Aggregation
Summarizing data efficiently:
* **GroupBy:** Explaining the **Split-Apply-Combine** process. It returns a GroupBy object which serves as a collection of DataFrame segments.
* **Aggregation:** Using `.agg()` to compute sum, mean, or custom functions across groups.

### 6. Pivot Tables & CrossTabs
Advanced reshaping:
* **Pivot Tables:** Reorganizing a DataFrame based on index/column values to see relationships.
* **CrossTabs:** A specialized version of a pivot table specifically for computing frequency counts between categorical variables.

### 7. Basic Operations & Broadcasting
Handy tools for daily analysis:
* **Exploration:** Using `.describe()`, `.info()`, and `.shape`.
* **Applying Functions:** Using `.apply()` to run custom logic on every row/column.
* **Broadcasting:** Performing arithmetic operations across the entire table.

### 8. Project: Anime Feature Extraction
A practical project involving string manipulation on a CSV file.
* **Task:** Extracting **Title, Episodes, and Timestamps** from a single cluttered column.
* **Process:** Writing custom functions to parse strings and populating new, clean columns.

### 9. Project: Countries Dataset Analysis
A data exploration project focusing on global demographics.
* **Tasks:** Identifying the highest populated country, finding leaders from specific continents, and analyzing democracy scores.
* **Focus:** Practicing complex filtering and sorting queries.

---
