# From Template
# pip install pandas hvplot==0.7.1 holoviews==1.14.3 bokeh panel==0.11.3
# panel serve holoviz_linked_brushing.py --auto --show
import hvplot.pandas
import holoviews as hv
import panel as pn
from bokeh.sampledata.iris import flowers

pn.extension(sizing_mode="stretch_width")
hv.extension("bokeh")

accent_color = "#00286e"

# InterestRate
from ltfqia import InterestRate
params = {
    'real_risk_free_interest_rate': 0.01,
    'inflation_premium': 0.01,
    'default_risk_premium': 0.01,
    'liquidity_premium': 0.01,
    'maturity_premium': 0.01,
}
rate = InterestRate(**params)
rate_view = pn.Column(rate, "Interest Rate:", rate.interest_rate)

from ltfqia import ContinuousCompoundingCashFlow
# ContinuousCompoundingCashFlow
params = {
    'present_value': 100,
    'N': 1,
}

continuous_compounding_cashflow = ContinuousCompoundingCashFlow(rate, **params)
continous_compounding_cashflow_view = pn.Column(
    continuous_compounding_cashflow, 
    continuous_compounding_cashflow.view)

pn.template.FastListTemplate(
    site="Quantitative Investment Analysis",
    title="Investement and Cash Flow Modelling",
    header_background=accent_color,
    main=[
        rate_view, 
        continous_compounding_cashflow_view,
    ],
).servable()
