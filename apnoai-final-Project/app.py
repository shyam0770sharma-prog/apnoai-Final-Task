import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="ApnoMart Executive Dashboard", page_icon="📊", layout="wide")
DATA_PATH = Path(__file__).parent / "apnomart_sales.csv"
df = pd.read_csv(DATA_PATH, parse_dates=["Order_Date"])
df["Profit_Margin_Calc"] = np.where(df["Sales"] != 0, df["Profit"] / df["Sales"] * 100, np.nan)

NAVY = "#15263D"
BLUE = "#2878B5"
GREEN = "#21865A"
RED = "#C94C4C"

st.markdown("<div style='color:#2878B5;font-weight:700;letter-spacing:1.5px'>APNOMART / BUSINESS INTELLIGENCE</div>", unsafe_allow_html=True)
st.title("ApnoMart Q2 2026 Executive Dashboard")
st.caption("Built by Shyam · ApnoAI Data Analytics Intern · October 2026")
st.warning("Scope note: the supplied 1,200-row file covers May–October 2026, not Q2 alone. All metrics reflect the selected data; request a corrected April–June dataset if Q2-only reporting is required.")

with st.sidebar:
    st.header("Interactive filters")
    regions = sorted(df["Region"].dropna().unique())
    categories = sorted(df["Category"].dropna().unique())
    selected_regions = st.multiselect("Region", regions, default=regions)
    selected_categories = st.multiselect("Category", categories, default=categories)
    date_min, date_max = df["Order_Date"].min().date(), df["Order_Date"].max().date()
    date_range = st.date_input("Order date range", value=(date_min, date_max), min_value=date_min, max_value=date_max)
    st.caption("All KPI cards and visuals respond to these filters.")

filtered = df[df["Region"].isin(selected_regions) & df["Category"].isin(selected_categories)].copy()
if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    filtered = filtered[filtered["Order_Date"].dt.date.between(date_range[0], date_range[1])]
elif isinstance(date_range, (tuple, list)) and len(date_range) == 1:
    filtered = filtered[filtered["Order_Date"].dt.date == date_range[0]]

if filtered.empty:
    st.info("No records match these filters. Select at least one region and category and a date range containing data.")
    st.stop()

sales = filtered["Sales"].sum()
profit = filtered["Profit"].sum()
orders = filtered["Order_ID"].nunique()
margin = profit / sales * 100 if sales else 0
loss_orders = int((filtered["Profit"] < 0).sum())

k1,k2,k3,k4 = st.columns(4)
k1.metric("Total Sales", f"₹{sales:,.0f}")
k2.metric("Total Profit", f"₹{profit:,.0f}", delta=f"{margin:.2f}% weighted margin")
k3.metric("Total Orders", f"{orders:,}")
k4.metric("Profit Margin %", f"{margin:.2f}%")
st.caption(f"Filtered rows: {len(filtered):,} · Loss-making orders: {loss_orders:,} · Quantity sold: {filtered['Quantity'].sum():,.0f}")

revenue_tab, profit_tab, customer_tab = st.tabs(["1 · Revenue Overview", "2 · Profitability Deep Dive", "3 · Customer Segmentation"])

with revenue_tab:
    left,right = st.columns(2)
    by_cat = filtered.groupby("Category", as_index=False).agg(Sales=("Sales","sum"), Profit=("Profit","sum")).sort_values("Sales", ascending=True)
    fig = px.bar(by_cat, x="Sales", y="Category", orientation="h", title="Sales by Category", text_auto=".3s", color_discrete_sequence=[BLUE], hover_data={"Profit":":,.0f"})
    fig.update_layout(margin=dict(l=10,r=10,t=55,b=10),height=370,xaxis_title="Sales (₹)",yaxis_title="",plot_bgcolor="white")
    left.plotly_chart(fig,use_container_width=True)
    monthly = filtered.assign(Month=filtered["Order_Date"].dt.to_period("M").astype(str)).groupby("Month",as_index=False).agg(Sales=("Sales","sum"),Profit=("Profit","sum")).sort_values("Month")
    mlong=monthly.melt(id_vars="Month",value_vars=["Sales","Profit"],var_name="Metric",value_name="Amount")
    fig=px.line(mlong,x="Month",y="Amount",color="Metric",markers=True,title="Monthly Sales and Profit",color_discrete_map={"Sales":BLUE,"Profit":GREEN})
    fig.update_layout(margin=dict(l=10,r=10,t=55,b=10),height=370,xaxis_title="Month",yaxis_title="Amount (₹)",plot_bgcolor="white")
    right.plotly_chart(fig,use_container_width=True)
    left,right=st.columns(2)
    region=filtered.groupby("Region",as_index=False).agg(Sales=("Sales","sum"),Profit=("Profit","sum")).sort_values("Sales",ascending=False)
    fig=px.bar(region,x="Region",y="Sales",title="Sales by Region",text_auto=".2s",color_discrete_sequence=[BLUE])
    fig.update_layout(margin=dict(l=10,r=10,t=55,b=10),height=340,plot_bgcolor="white")
    left.plotly_chart(fig,use_container_width=True)
    pay=filtered.groupby("Payment_Method",as_index=False).agg(Sales=("Sales","sum"),Orders=("Order_ID","nunique"))
    fig=px.pie(pay,names="Payment_Method",values="Sales",hole=.52,title="Sales Mix by Payment Method",color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(margin=dict(l=10,r=10,t=55,b=10),height=340)
    right.plotly_chart(fig,use_container_width=True)

with profit_tab:
    left,right=st.columns(2)
    cat=filtered.groupby("Category",as_index=False).agg(Sales=("Sales","sum"),Profit=("Profit","sum"))
    cat["Weighted Margin %"]=np.where(cat["Sales"]!=0,cat["Profit"]/cat["Sales"]*100,0)
    fig=px.bar(cat.sort_values("Weighted Margin %"),x="Weighted Margin %",y="Category",orientation="h",title="Weighted Profit Margin by Category",text=cat.sort_values("Weighted Margin %")["Weighted Margin %"].map(lambda x:f"{x:.1f}%"),color_discrete_sequence=[GREEN])
    fig.update_layout(margin=dict(l=10,r=10,t=55,b=10),height=370,xaxis_title="SUM(Profit) / SUM(Sales) × 100",plot_bgcolor="white")
    left.plotly_chart(fig,use_container_width=True)
    reg=filtered.groupby("Region",as_index=False).agg(Sales=("Sales","sum"),Profit=("Profit","sum"),Discount=("Discount","mean"))
    reg["Weighted Margin %"]=np.where(reg["Sales"]!=0,reg["Profit"]/reg["Sales"]*100,0)
    fig=px.bar(reg.sort_values("Profit"),x="Profit",y="Region",orientation="h",title="Profit by Region",text_auto=".2s",color_discrete_sequence=[GREEN],hover_data={"Weighted Margin %":":.2f","Discount":":.2f"})
    fig.update_layout(margin=dict(l=10,r=10,t=55,b=10),height=370,xaxis_title="Profit (₹)",plot_bgcolor="white")
    right.plotly_chart(fig,use_container_width=True)
    fig=px.scatter(filtered,x="Discount",y="Profit",color="Profit",color_continuous_scale=[RED,"#F5F5F5",GREEN],hover_data=["Order_ID","Region","Category","Product","Sales"],title="Discount vs Profit by Order")
    fig.add_hline(y=0,line_dash="dash",line_color="#6A7C90")
    fig.update_layout(margin=dict(l=10,r=10,t=55,b=10),height=390,xaxis_title="Discount (%)",yaxis_title="Profit (₹)",plot_bgcolor="white")
    st.plotly_chart(fig,use_container_width=True)
    st.subheader("Loss-making orders to investigate")
    loss=filtered[filtered["Profit"]<0][["Order_ID","Order_Date","Region","Category","Product","Discount","Sales","Profit"]].sort_values("Profit")
    st.dataframe(loss,use_container_width=True,hide_index=True)

with customer_tab:
    left,right=st.columns(2)
    seg=filtered.groupby("Customer_Segment",as_index=False).agg(Sales=("Sales","sum"),Profit=("Profit","sum"),Orders=("Order_ID","nunique"))
    fig=px.bar(seg.sort_values("Sales"),x="Sales",y="Customer_Segment",orientation="h",title="Sales by Customer Segment",text_auto=".2s",color_discrete_sequence=[BLUE])
    fig.update_layout(margin=dict(l=10,r=10,t=55,b=10),height=370,plot_bgcolor="white")
    left.plotly_chart(fig,use_container_width=True)
    fig=px.bar(seg,x="Customer_Segment",y="Orders",title="Unique Orders by Segment",text_auto=True,color_discrete_sequence=["#609FC9"])
    fig.update_layout(margin=dict(l=10,r=10,t=55,b=10),height=370,plot_bgcolor="white",xaxis_title="",yaxis_title="Orders")
    right.plotly_chart(fig,use_container_width=True)
    pay=filtered.groupby("Payment_Method",as_index=False).agg(Sales=("Sales","sum"),Orders=("Order_ID","nunique"))
    fig=px.bar(pay.sort_values("Sales",ascending=False),x="Payment_Method",y="Sales",title="Payment Method Preferences",text_auto=".2s",color_discrete_sequence=[BLUE])
    fig.update_layout(margin=dict(l=10,r=10,t=55,b=10),height=360,plot_bgcolor="white",xaxis_title="",yaxis_title="Sales (₹)")
    st.plotly_chart(fig,use_container_width=True)
    st.subheader("Segment summary")
    st.dataframe(seg.sort_values("Sales",ascending=False).style.format({"Sales":"₹{:,.0f}","Profit":"₹{:,.0f}"}),use_container_width=True,hide_index=True)

st.divider()
st.markdown("**Strategic focus:** Protect margin in the lowest-margin category, investigate loss-making orders, and plan inventory/campaigns around observed category and monthly demand.")
st.caption("Calculated field: Weighted Profit Margin % = SUM(Profit) / SUM(Sales) × 100. Figures reflect current filters.")
