# 📊 Data Visualization: Matplotlib & Seaborn

This folder covers the art of data storytelling. We move beyond raw numbers to create visual representations of data using the two most powerful plotting libraries in Python: **Matplotlib** and **Seaborn**.

## 📖 Key Libraries
* **Matplotlib:** The "grandfather" of Python visualization. It provides low-level control over every element of a figure (axes, labels, colors) and is highly customizable.
* **Seaborn:** A high-level library built on top of Matplotlib. It integrates closely with Pandas DataFrames and provides beautiful default styles and complex statistical plots with very little code.

---

## 📂 Folder Structure

### 1. Matplotlib Fundamentals
Understanding the core mechanics of plotting.
* **Array Plotting:** Basic X-Y plotting using NumPy arrays.
* **Subplots:** Creating multiple plots within a single figure.
* **Object-Oriented (OO) API:** The professional way to plot—creating a `figure` object and manually adding `axes` to it for maximum control and resizing.
* **Plot Types:** Working with **Scatter** (correlation), **Histograms** (distribution), and **Boxplots** (outliers).
* **Image Processing:** Loading images and using coordinate-based cropping.
* **Exporting:** Saving high-quality figures using `savefig()`.

### 2. Distribution Plots (Quantitative Data)
Used to visualize how a single variable or a pair of variables are distributed.
* **Histplot/Distplot:** Shows the frequency distribution of a continuous variable.
* **Jointplot:** Combines two different plots (usually a scatter and a histogram) to show the relationship between two variables.
* **Pairplot:** Creates a matrix of plots for every numerical column in a DataFrame—ideal for instant Exploratory Data Analysis (EDA).
* **Rugplot:** Draws a small vertical tick for every data point along an axis; a simple way to see data density.



### 3. Categorical Data Plots
Used when one of your variables is a category (e.g., "Day of the week", "Gender").
* **Barplot:** General plot that aggregates data based on some function (default is the mean).
* **Countplot:** A specialized barplot that simply counts the number of occurrences in a category.
* **Boxplot:** Visualizes the "Five Number Summary" (Min, Q1, Median, Q3, Max) and highlights outliers.
* **Violinplot:** Combines a boxplot with a Kernel Density Estimate (KDE) to show the actual density of the data.
* **Stripplot:** Draws a scatterplot where one variable is categorical.
* **Swarmplot:** Similar to a stripplot, but the points are adjusted so they don't overlap, giving a better view of the distribution.

### 4. Matrix Plots (Heat Maps & Cluster Maps)
Visualizing data where variables are located on both the rows and columns.
* **Correlation (`.corr()`):** A mathematical method to find the relationship strength between numerical variables (-1 to 1).
* **Heat Map:** Uses color-coding to represent the values in a matrix (excellent for visualizing correlations).
* **Cluster Map:** Uses hierarchical clustering to group similar rows and columns together, revealing hidden patterns in the data.

### 5. Regression Plots
* **lmplot():** A powerful tool that allows you to display linear regression models between variables, helping you visualize trends and predictions.

### 6. Interactive Visualizations
* **Plotly & Cufflinks:** Moving beyond static images to create interactive, zoomable, and hoverable charts directly in the browser or notebook.

### 7. Capstone Project: IPL 2022 Analysis
A real-world application of all visualization skills using the **IPL 2022 dataset**.
* **Match Trends:** Analyzing 'Match Winners', 'Toss Decisions', and 'Toss Winner vs. Match Winner'.
* **Performance Analysis:** Identifying 'Top 10 Players', 'Best Bowling Figures', and 'Highest Individual Scores'.
* **Venue Insights:** Analyzing which stadiums favor high-run margins or specific bowling styles.

---

## 🛠️ Requirements
To run these notebooks, install the following:
```bash
pip install matplotlib seaborn plotly cufflinks