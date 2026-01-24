# 🚀 AI/ML Foundations: From Logic to Libraries

Welcome to my central repository for mastering the Artificial Intelligence and Machine Learning stack. This project documents my transition from a Computer Engineering student to an AI/ML practitioner, focusing on building a deep, first-principles understanding of data tools.

---

## 🗺️ Project Roadmap

This repository is structured as a progressive learning path. Each module contains its own documentation, datasets, and Jupyter notebooks.

| Module | Focus Area | Key Concepts | Status |
| :--- | :--- | :--- | :--- |
| [🐍 Python](./python_basics) | Core Fundamentals | OOP, Logic, Data Structures | ✅ Complete |
| [🔢 NumPy](./Numpy) | Numerical Computing | Vectorization, Linear Algebra, Arrays | ✅ Complete |
| [🐼 Pandas](./Pandas) | Data Manipulation | Cleaning, Merging, Feature Extraction | ✅ Complete |
| [📊 Visualization](./viz) | Data Storytelling | Matplotlib, Seaborn | 🏗️ In Progress |

---

## 🛠️ Tech Stack & Environment

I use a **centralized virtual environment** to ensure dependency consistency across all modules.

* **Language:** Python 3.14.2
* **Libraries:** NumPy, Pandas (and growing!)
* **Editor:** VS Code / Jupyter Notebooks
* **Version Control:** Git & GitHub
* **OS:** Windows (PowerShell optimized)


---

## 📈 My Journey
I am building this in public to document my transition into the AI/ML space. My goal is to master the math and the libraries behind modern AI, focusing on creating clean, reproducible, and efficient code. 

> "The best way to learn is to build, break, and document."

---


## ⚙️ Local Setup & Installation

To run these notebooks on your local machine, follow these steps:

1. **Clone the repository:**
   ```powershell
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
2. **Create a Central Virtual Environment:**

   Instead of using per-folder environments, we use a single root environment to manage all modules efficiently:

   ```powershell
   python -m venv venv
3. **Activate the Environment:**

   ```powershell
   .\venv\Scripts\activate
4. **Install Consolidated Dependencies:**
   ```powershell
   pip install -r requirements.txt
5. **Select Interpreter in VS Code:**
   To ensure your Jupyter Notebooks use the correct environment:
   
   1. Open any `.ipynb` file in your repository.

   2. Click on "Select Kernel" in the top right corner(or press `Ctrl + Shift + P`).
   
   3. Search for and choose **"Python: Select Interpreter"**.
   
   4. Select the environment located at: `./venv/Scripts/python.exe`.
