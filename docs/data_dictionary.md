# 📘 Data Dictionary

This document describes all tables and fields used in the Sales Analytics project.

---

# 1. Fact Table — `Sales_Data`

| Column | Description | Type |
|--------|-------------|------|
| order_number | Unique order identifier | Text |
| order_date | Date the order was placed | Date |
| ship_date | Date the order was shipped | Date |
| customer_name_index | Foreign key → Customer dimension | Integer |
| channel | Sales channel (Wholesale, Distributor, Export) | Category |
| currency_code | Currency used (NZD) | Text |
| warehouse_code | Warehouse identifier | Text |
| delivery_region_index | Foreign key → Region dimension | Integer |
| product_description_index | Foreign key → Product dimension | Integer |
| order_quantity | Units ordered | Numeric |
| unit_selling_price | Selling price per unit | Numeric |
| unit_cost | Cost per unit | Numeric |
| sales | Total sales amount | Numeric |
| total_cost | Total cost amount | Numeric |
| profit | Profit amount | Numeric |

---

# 2. Dimension Table — `Products_Data`

| Column | Description |
|--------|-------------|
| Index | Product ID (PK) |
| Product Name | Name of the product |

---

# 3. Dimension Table — `Customer_Data`

| Column | Description |
|--------|-------------|
| Customer Index | Customer ID (PK) |
| Customer Names | Customer name |

---

# 4. Dimension Table — `Regions_Table`

| Column | Description |
|--------|-------------|
| Index | Region ID (PK) |
| Suburb | Suburb name |
| City | City name |
| postcode | Postal code |
| Longitude | Geo coordinate |
| Latitude | Geo coordinate |
| Full Address | Full address string |

---

# 5. Dimension Table — `DateTable`

| Column | Description |
|--------|-------------|
| Date | Calendar date |
| Year | Year number |
| Quarter | Quarter label |
| Month No | Month number |
| Month Name | Full month name |
| Month Short Name | Abbreviated month |
| Month Short Name Plus Year | e.g., "Jan,17" |
| Day Name | Day of week |
| Day Number | Day of month |
| Month Sort | YYYYMM format |

---

This dictionary ensures clarity and consistency across the entire BI project.
