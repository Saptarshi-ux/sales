
## 🧾 **Departmental Store Sales Dashboard (Python + Excel) — Project Report**

**Objective:**
To simulate and visualize 3-year sales data (2022–2024) for departmental stores across Kolkata using Python-generated data and Excel-based reporting, designed for Sales Supervisors and Product Managers.

---

### 1️⃣ Data Generation & Business Understanding

As an Economics graduate, I began by understanding the **consumption basket of West Bengal households** and analyzing real-world **departmental store operations**. I identified common transactional attributes: product category, item names, pricing bands, payment methods, and regional sales distinctions.

Using **Python**, I generated a **hypothetical sales dataset** covering 3,300+ daily transactions. The following Python libraries were used:

* `pandas` – data frame construction
* `numpy` – randomization and pricing logic
* `random` – simulating salespersons, categories, products
* `datetime` – date ranges
* `openpyxl` / `xlsxwriter` – Excel file export

The dataset included fields like `Date`, `Store Location`, `Sales Rep`, `Product Category`, `Unit Price`, `Quantity`, `Payment Method`, etc.

---

### 2️⃣ Dashboard Design (Excel)

Built a fully interactive, filterable dashboard in Excel using:

* **PivotTables** – core metrics (KPIs, region/category/rep/product sales)
* **Charts** – trend lines, bar graphs, donut chart (payment mix)
* **INDEX/MATCH** – to dynamically identify highest sold category, product, and top rep
* **Slicers** – for Year and Quarter filters (synchronized across visuals)
* **Conditional Formatting** – color-coded KPIs and charts for visual clarity

---

### 3️⃣ Key Performance Metrics

| Metric                       | Value                     |
| ---------------------------- | ------------------------- |
| **Total Sales**              | ₹ 102.8 Million           |
| **Total Quantity Sold**      | 18,019 units              |
| **Top Category**             | Grocery (3,906)           |
| **Top Product**              | Dal (866 units)           |
| **Top Sales Rep**            | SP013 (₹ 7,101 avg. sale) |
| **Preferred Payment Method** | Online (34%)              |
| **Best Sales Region**        | North Kolkata (₹ 27.4 M)  |

---

### 4️⃣ Challenges Faced & Business Gaps Identified

| Area                 | Challenge                                                                                                                                                                                                         |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------                                                                                         |
| **Regional Gap**     | South Kolkata lags behind (₹ 23.8 M vs. ₹ 27.4 M in North). Needs **targeted promotions and SKU realignment**.                                                                                                    |
| **Temporal Drop**    | Revenue dip observed in Q4 2024 (₹ 79.5 L). Indicates **weak festive strategies** or **clearance stock inefficiencies**.                                                                                          |
| **Sales Rep Gaps**   | Wide productivity range: SP013 (₹ 7.1k avg) vs. SP015 (₹ 4.3k). Suggests **uneven territory allocation/training gaps**.                                                                                           |
| **SKU Inefficiency** | Over 20 SKUs sold < 700 units. Calls for **SKU optimization** to avoid inventory waste.                                                                                                                           |
| **Payment Handling** | The store sees an imbalanced payment distribution: Digital payment (67%), and Cash (33%). A significant skewness has been observed toward digital payment, suggesting an opportunity to promote digital wallet    |                              incentives. **Digital wallet incentive schemes** can increase adoption.                                                                                                                                        |

---

### 5️⃣ Outcomes & Value Delivered

* Delivered an **interactive Excel dashboard** summarizing performance by category, product, region, time, and salesperson.
* Enabled **data-driven insights** for sales planning, resource deployment, and promotional strategies.
* Simulated a real-world project environment using a **Python-to-Excel pipeline**, integrating business logic and analytics.

---

### ✅ Key Tools & Skills Demonstrated

* **Python (Data Simulation):** pandas, datetime, random
* **Excel (BI Reporting):** PivotTables, dynamic formulas, slicers, dashboarding
* **Domain Understanding:** Retail Sales Analysis, Consumer Behavior (West Bengal)
* **Communication:** Insights delivery for Product & Sales Management


