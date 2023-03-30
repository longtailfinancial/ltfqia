import holoviews as hv
import panel as pn

pn.extension(sizing_mode="stretch_width")
hv.extension("bokeh")

accent_color = "#00286e"

from ltfqia.bonding_curve import PureCurve

pure_curve = PureCurve()

app = pn.Column(
    pure_curve, 
    pn.Row(pure_curve.view_curve_over_supply, pure_curve.info)
)

pn.template.FastListTemplate(
    site="Quantitative Investment Analysis",
    title="Bonding Curve",
    header_background=accent_color,
    main=[
        app, 
    ],
).servable()
