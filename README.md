# The Insight Board — ApnoMart Business Intelligence Dashboard

**Analyst:** SHREE KRISHAN SHARMA  
**Tool:** Python, Pandas, Matplotlib, Streamlit, Plotly  
**Source rows:** 1,200  
**Source date coverage:** 01 May 2026–28 Oct 2026

## Project summary

A three-view interactive BI dashboard with Region, Category and Date filters. Filters update KPI cards and visualizations. The project includes a 1920×1080 screenshot, executive insights, a calculated weighted profit-margin measure, and the source dataset.

## Important scope note

The assignment template calls the dashboard “Q2 2026”, but the provided dataset spans May–October 2026. Results use all supplied rows and are **not Q2-only**. If the assessment requires Q2-only figures, replace the CSV with the correct April–June data and rerun the analysis.

## Key metrics (all supplied rows)

- Total Sales: ₹16,261,998.30
- Total Profit: ₹4,419,736.17
- Unique Orders: 1,200
- Weighted Profit Margin: 27.18%
- Loss-making orders: 61; combined recorded loss: ₹82,743.74

## Files

- `app.py` — interactive Streamlit dashboard (3 views, multiple visuals, shared filters)
- `apnomart_sales.csv` — parsed source dataset (1,200 rows)
- `dashboard.png` — dashboard screenshot, 1920×1080
- `insights.md` — 3 strategic insights and 1 recommendation
- `insights.pdf` — executive insights PDF
- `ApnoMart_Executive_Report.docx` — editable executive report
- `requirements.txt` — Python dependencies
- `Mentor_Note.txt` — submission note / AI disclosure

## Run the dashboard locally

1. Install Python 3.10 or later.
2. Open a terminal in this folder.
3. Run `pip install -r requirements.txt`.
4. Run `streamlit run app.py`.
5. In the browser sidebar, change Region, Category, and Order date range to verify the dashboard is interactive.

## Main insights

1. **Revenue:** Furniture leads category sales with ₹3,518,270 (21.6% of sales); 2026-07 is the strongest sales month.
2. **Profitability:** Office Supplies contributes the highest category profit; Electronics has the lowest weighted margin (18.9%). 61 orders have negative recorded profit.
3. **Customers:** Corporate is the top sales segment; Cash leads payment-method sales.

## Strategic recommendation

Run a margin-protection pilot: investigate loss-making orders and audit price, cost, discount, product, and region patterns in the lowest-margin category. Test targeted rather than broad discounts, measure sales and profit together, and scale only after comparing against a control group.

## AI-use disclosure

ChatGPT helped structure the analysis, refine business wording, and scaffold the report/dashboard code. Metrics were calculated from the supplied dataset, and the reporting-period mismatch is explicitly disclosed.

