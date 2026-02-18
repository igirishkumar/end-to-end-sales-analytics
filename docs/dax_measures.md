```markdown
# 📘 DAX Measures Documentation

This document lists all DAX measures used in the Sales Performance Dashboard.

---

## 🧮 Sales Measures

### **Total Sales**
```DAX
Total Sales = SUM(Sales_Data[Sales])

Sales CY

Sales CY =
CALCULATE(
    [Total Sales],
    YEAR(DateTable[Date]) = YEAR(TODAY())
)

Sales PY

Sales PY =
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR(DateTable[Date])
)

Sales Growth %

Sales Growth % =
DIVIDE([Sales CY] - [Sales PY], [Sales PY])

💰 Profit Measures

Total Profit = SUM(Sales_Data[Profit])

Profit Margin

Profit Margin =
DIVIDE([Total Profit], [Total Sales])

Profit CY

Profit CY =
CALCULATE(
    [Total Profit],
    YEAR(DateTable[Date]) = YEAR(TODAY())
)

Profit PY

Profit PY =
CALCULATE(
    [Total Profit],
    SAMEPERIODLASTYEAR(DateTable[Date])
)

Profit Growth %

Profit Growth % =
DIVIDE([Profit CY] - [Profit PY], [Profit PY])


📦 Units Sold

Units Sold = SUM(Sales_Data[Order Quantity])
```
