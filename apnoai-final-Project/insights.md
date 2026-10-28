# ApnoMart — Executive Insights & Strategic Recommendation

**Project:** The Insight Board — Business Intelligence Dashboard  
**Dashboard title:** ApnoMart Q2 2026 Executive Dashboard  
**Analyst:** Shyam  
**Tool:** Python (Pandas, Matplotlib) for analysis and screenshot; Streamlit + Plotly for the interactive dashboard  
**Dataset:** 1,200 orders, 01 May 2026 to 28 Oct 2026

> **Data-scope limitation:** The task template requests Q2 2026, but the supplied source data spans May–October 2026. The analysis below uses all 1,200 supplied rows and must not be interpreted as Q2-only results. Request a corrected April–June dataset if Q2-only reporting is mandatory.

## Executive snapshot

| KPI | Result |
|---|---:|
| Total sales | ₹16,261,998.30 |
| Total profit | ₹4,419,736.17 |
| Unique orders | 1,200 |
| Quantity sold | 6,736 |
| Weighted profit margin (SUM(Profit) / SUM(Sales)) | 27.18% |
| Loss-making orders | 61 (5.08%) |
| Profit lost on loss-making rows | ₹82,743.74 |

## Insight 1 — Revenue pattern

**Pattern:** Furniture is the largest sales category, generating **₹3,518,270.00 (21.63% of total sales)**. The strongest month by sales is **2026-07**, with **₹2,957,618.40**.

**So what:** Revenue is spread across several categories rather than dominated by one. Protect the leading category's availability, and use monthly sales patterns to plan stock and campaign timing rather than applying the same budget every month.

## Insight 2 — Profitability pattern

**Pattern:** Office Supplies generates the highest total category profit at **₹1,176,657.32**, with a weighted margin of **34.80%**. Electronics has the lowest weighted category margin at **18.88%**. There are **61 loss-making orders**, with a combined recorded loss of **₹82,743.74**.

**So what:** Sales alone is not a sufficient performance measure. Review the low-margin category's pricing, product costs and discounting, and investigate the loss-making order lines before expanding discounts. The dataset does not prove that discounts caused every loss, so this should be tested at order/product level.

## Insight 3 — Customer behavior pattern

**Pattern:** The **Corporate** segment is the largest segment by sales, contributing **₹4,311,027.50 (26.51%)**. **Cash** is the leading payment method by sales at **₹3,574,076.95 (21.98%)**.

**So what:** Maintain a strong experience for the largest segment while testing targeted offers and repeat-purchase campaigns across the other segments. Keep all major payment methods reliable; the leading method is not so dominant that other methods should be neglected.

## Strategic recommendation

**Run a margin-protection pilot before increasing broad discount spend.** Start with the lowest weighted-margin category (Electronics, 18.88% weighted margin): audit the 61 loss-making orders by product, discount, region and payment method; test more selective discounts and monitor sales, profit and conversion together. In parallel, use the leading category and strongest month as inputs for inventory and campaign planning. Compare results against an unexposed control group before scaling.

## Dashboard and interactivity

The project includes a 1920×1080 dashboard screenshot plus a Streamlit app with **Region, Category and date-range filters** that update KPI cards and charts. The app has three views: Revenue Overview, Profitability Deep Dive and Customer Segmentation. Visuals include category sales, monthly trend, regional profit, customer-segment sales, profit-margin comparison, discount-versus-profit scatter, and payment-method mix.

## Metric definition

**Calculated field — Weighted Profit Margin % = SUM(Profit) / SUM(Sales) × 100.** This is used for the overall KPI and weighted category/region margin comparisons. The source also contains a `Profit_Margin` column; it is retained, while this calculated measure is recomputed from the row-level sales and profit to match the task specification.

## AI use disclosure

ChatGPT was used to help organize the analysis, refine the business wording, and scaffold the dashboard/report code. Figures were calculated from the supplied dataset; the scope mismatch is disclosed rather than silently treating May–October as Q2 .
