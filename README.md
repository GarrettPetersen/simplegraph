# simplegraph

This is a simple little graphing package for making graphs and exporting them as base64-encoded SVGs.

## Categorical Graph

The categorical graph is for data that comes in distinct categories. It can generate a bar chart, a stacked bar chart, dots, or lines.

Here is an example of how to make a graph:

```
from simplegraph import CategoricalGraph

graph = CategoricalGraph(
        width=600,
        height=400,
        bar_width=30,
        x_left_padding=40,
        x_right_padding=120,
        y_top_padding=10,
        y_bottom_padding=30,
        background_color="#ffffff",
    )

graph.x_labels = ["A", "B", "C", "D", "E"]
graph.x_axis_label = "X Axis"
graph.primary_y_axis_label = "Primary Y Axis"

graph.add_series([10, 20, 30, 40, 50], legend_label="Series 1")
graph.add_series([15, 25, 5, 44, 56], legend_label="Series 2")
graph.add_series([5, 35, 10, 33, 40], legend_label="Series 3", series_type="line")
graph.add_series([35, 56, 25, 5, 44], legend_label="Series 4", series_type="dot")

# Get the SVG string in base64 format
svg_base64 = graph.to_base64_src()

# Print the SVG string in an img tag so your browser can display it
print(f"\n<img src='{svg_base64}' />")
```
<img src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2MDAiIGhlaWdodD0iNDAwIj48cmVjdCB4PScwJyB5PScwJyB3aWR0aD0nNjAwJyBoZWlnaHQ9JzQwMCcgcng9JzEwJyByeT0nMTAnIGZpbGw9JyNmZmZmZmYnIC8+PHJlY3QgeD0iNDg1IiB5PSIxMCIgd2lkdGg9IjEwIiBoZWlnaHQ9IjEwIiBmaWxsPSIjMjUzYTVlIiAvPjx0ZXh0IHg9IjUwMCIgeT0iMTYuNjY2NjY2NjY2NjY2NjY0IiBmb250LXNpemU9IjEwIiBhbGlnbm1lbnQtYmFzZWxpbmU9Im1pZGRsZSIgZmlsbD0iIzAwMDAwMCI+U2VyaWVzIDE8L3RleHQ+PHJlY3QgeD0iNDg1IiB5PSIzMCIgd2lkdGg9IjEwIiBoZWlnaHQ9IjEwIiBmaWxsPSIjZThjMTcwIiAvPjx0ZXh0IHg9IjUwMCIgeT0iMzYuNjY2NjY2NjY2NjY2NjY0IiBmb250LXNpemU9IjEwIiBhbGlnbm1lbnQtYmFzZWxpbmU9Im1pZGRsZSIgZmlsbD0iIzAwMDAwMCI+U2VyaWVzIDI8L3RleHQ+PGxpbmUgeDE9IjQ4NSIgeTE9IjU1LjAiIHgyPSI0OTUiIHkyPSI1NS4wIiBzdHJva2U9IiNhNTMwMzAiIHN0cm9rZS13aWR0aD0iMSIgLz48dGV4dCB4PSI1MDAiIHk9IjU2LjY2NjY2NjY2NjY2NjY2NCIgZm9udC1zaXplPSIxMCIgYWxpZ25tZW50LWJhc2VsaW5lPSJtaWRkbGUiIGZpbGw9IiMwMDAwMDAiPlNlcmllcyAzPC90ZXh0PjxjaXJjbGUgY3g9IjQ5MC4wIiBjeT0iNzUuMCIgcj0iNSIgZmlsbD0iIzc1YTc0MyIgIC8+PHRleHQgeD0iNTAwIiB5PSI3Ni42NjY2NjY2NjY2NjY2NyIgZm9udC1zaXplPSIxMCIgYWxpZ25tZW50LWJhc2VsaW5lPSJtaWRkbGUiIGZpbGw9IiMwMDAwMDAiPlNlcmllcyA0PC90ZXh0PjxyZWN0IHg9IjQwLjAiIHk9IjMxMC4wIiB3aWR0aD0iMzAiIGhlaWdodD0iNjAuMCIgZmlsbD0iIzI1M2E1ZSIgLz48cmVjdCB4PSI3MC4wIiB5PSIyODAuMCIgd2lkdGg9IjMwIiBoZWlnaHQ9IjkwLjAiIGZpbGw9IiNlOGMxNzAiIC8+PGNpcmNsZSBjeD0iNjkuMCIgY3k9IjE2MC4wIiByPSI1IiBmaWxsPSIjNzVhNzQzIiAgLz48cmVjdCB4PSIxMjguMCIgeT0iMjUwLjAiIHdpZHRoPSIzMCIgaGVpZ2h0PSIxMjAuMCIgZmlsbD0iIzI1M2E1ZSIgLz48cmVjdCB4PSIxNTguMCIgeT0iMjIwLjAiIHdpZHRoPSIzMCIgaGVpZ2h0PSIxNTAuMCIgZmlsbD0iI2U4YzE3MCIgLz48bGluZSB4MT0iNjkuMCIgeTE9IjM0MC4wIiB4Mj0iMTU3LjAiIHkyPSIxNjAuMCIgc3Ryb2tlPSIjYTUzMDMwIiBzdHJva2Utd2lkdGg9IjEiIC8+PGNpcmNsZSBjeD0iMTU3LjAiIGN5PSIzNC4wIiByPSI1IiBmaWxsPSIjNzVhNzQzIiAgLz48cmVjdCB4PSIyMTYuMCIgeT0iMTkwLjAiIHdpZHRoPSIzMCIgaGVpZ2h0PSIxODAuMCIgZmlsbD0iIzI1M2E1ZSIgLz48cmVjdCB4PSIyNDYuMCIgeT0iMzQwLjAiIHdpZHRoPSIzMCIgaGVpZ2h0PSIzMC4wIiBmaWxsPSIjZThjMTcwIiAvPjxsaW5lIHgxPSIxNTcuMCIgeTE9IjE2MC4wIiB4Mj0iMjQ1LjAiIHkyPSIzMTAuMCIgc3Ryb2tlPSIjYTUzMDMwIiBzdHJva2Utd2lkdGg9IjEiIC8+PGNpcmNsZSBjeD0iMjQ1LjAiIGN5PSIyMjAuMCIgcj0iNSIgZmlsbD0iIzc1YTc0MyIgIC8+PHJlY3QgeD0iMzA0LjAiIHk9IjEzMC4wIiB3aWR0aD0iMzAiIGhlaWdodD0iMjQwLjAiIGZpbGw9IiMyNTNhNWUiIC8+PHJlY3QgeD0iMzM0LjAiIHk9IjEwNi4wIiB3aWR0aD0iMzAiIGhlaWdodD0iMjY0LjAiIGZpbGw9IiNlOGMxNzAiIC8+PGxpbmUgeDE9IjI0NS4wIiB5MT0iMzEwLjAiIHgyPSIzMzMuMCIgeTI9IjE3Mi4wIiBzdHJva2U9IiNhNTMwMzAiIHN0cm9rZS13aWR0aD0iMSIgLz48Y2lyY2xlIGN4PSIzMzMuMCIgY3k9IjM0MC4wIiByPSI1IiBmaWxsPSIjNzVhNzQzIiAgLz48cmVjdCB4PSIzOTIuMCIgeT0iNzAuMCIgd2lkdGg9IjMwIiBoZWlnaHQ9IjMwMC4wIiBmaWxsPSIjMjUzYTVlIiAvPjxyZWN0IHg9IjQyMi4wIiB5PSIzNC4wIiB3aWR0aD0iMzAiIGhlaWdodD0iMzM2LjAiIGZpbGw9IiNlOGMxNzAiIC8+PGxpbmUgeDE9IjMzMy4wIiB5MT0iMTcyLjAiIHgyPSI0MjEuMCIgeTI9IjEzMC4wIiBzdHJva2U9IiNhNTMwMzAiIHN0cm9rZS13aWR0aD0iMSIgLz48Y2lyY2xlIGN4PSI0MjEuMCIgY3k9IjEwNi4wIiByPSI1IiBmaWxsPSIjNzVhNzQzIiAgLz48bGluZSB4MT0iNDAiIHkxPSIxMCIgeDI9IjQwIiB5Mj0iMzcwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMSIgLz48bGluZSB4MT0iNDAiIHkxPSIzNzAiIHgyPSI0ODAiIHkyPSIzNzAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxIiAvPjx0ZXh0IHg9IjY5LjAiIHk9IjM3NSIgdGV4dC1hbmNob3I9ImVuZCIgZm9udC1zaXplPSIxMCIgdHJhbnNmb3JtPSJyb3RhdGUoLTkwIDY5LjAgMzc1KSI+QTwvdGV4dD48dGV4dCB4PSIxNTcuMCIgeT0iMzc1IiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjEwIiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMTU3LjAgMzc1KSI+QjwvdGV4dD48dGV4dCB4PSIyNDUuMCIgeT0iMzc1IiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjEwIiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMjQ1LjAgMzc1KSI+QzwvdGV4dD48dGV4dCB4PSIzMzMuMCIgeT0iMzc1IiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjEwIiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMzMzLjAgMzc1KSI+RDwvdGV4dD48dGV4dCB4PSI0MjEuMCIgeT0iMzc1IiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjEwIiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgNDIxLjAgMzc1KSI+RTwvdGV4dD48dGV4dCB4PSIzNSIgeT0iMzczLjAiIHRleHQtYW5jaG9yPSJlbmQiIGZvbnQtc2l6ZT0iMTAiIGZpbGw9IiMwMDAwMDAiPjA8L3RleHQ+PGxpbmUgeDE9IjQwIiB5MT0iMzcwLjAiIHgyPSIzNyIgeTI9IjM3MC4wIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMSIgLz48dGV4dCB4PSIzNSIgeT0iMzAxLjAiIHRleHQtYW5jaG9yPSJlbmQiIGZvbnQtc2l6ZT0iMTAiIGZpbGw9IiMwMDAwMDAiPjEyPC90ZXh0PjxsaW5lIHgxPSI0MCIgeTE9IjI5OC4wIiB4Mj0iMzciIHkyPSIyOTguMCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEiIC8+PHRleHQgeD0iMzUiIHk9IjIyOS4wIiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjEwIiBmaWxsPSIjMDAwMDAwIj4yNDwvdGV4dD48bGluZSB4MT0iNDAiIHkxPSIyMjYuMCIgeDI9IjM3IiB5Mj0iMjI2LjAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxIiAvPjx0ZXh0IHg9IjM1IiB5PSIxNTcuMCIgdGV4dC1hbmNob3I9ImVuZCIgZm9udC1zaXplPSIxMCIgZmlsbD0iIzAwMDAwMCI+MzY8L3RleHQ+PGxpbmUgeDE9IjQwIiB5MT0iMTU0LjAiIHgyPSIzNyIgeTI9IjE1NC4wIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMSIgLz48dGV4dCB4PSIzNSIgeT0iODUuMCIgdGV4dC1hbmNob3I9ImVuZCIgZm9udC1zaXplPSIxMCIgZmlsbD0iIzAwMDAwMCI+NDg8L3RleHQ+PGxpbmUgeDE9IjQwIiB5MT0iODIuMCIgeDI9IjM3IiB5Mj0iODIuMCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEiIC8+PHRleHQgeD0iMzUiIHk9IjEzLjAiIHRleHQtYW5jaG9yPSJlbmQiIGZvbnQtc2l6ZT0iMTAiIGZpbGw9IiMwMDAwMDAiPjYwPC90ZXh0PjxsaW5lIHgxPSI0MCIgeTE9IjEwLjAiIHgyPSIzNyIgeTI9IjEwLjAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxIiAvPjx0ZXh0IHg9IjI2MC4wIiB5PSIzOTIuNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwMDAwMCI+WCBBeGlzPC90ZXh0Pjx0ZXh0IHg9IjEwLjAiIHk9IjE5MC4wIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEyIiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMTAuMCAxOTAuMCkiIGZpbGw9IiMwMDAwMDAiPlByaW1hcnkgWSBBeGlzPC90ZXh0Pjwvc3ZnPg==' />

## Ribbon Graph

The ribbon graph is for comparing two numbers on the same scale and a third number on a different scale (represented through color).

The three series must be added in order, with the first representing the back of the ribbon, the second representing the point, and the (optional) third representing the color.

Here's an example:

```
from simplegraph import RibbonGraph

graph = RibbonGraph(
    width=600,
    height=400,
    bar_width=30,
    x_left_padding=30,
    x_right_padding=60,
    y_top_padding=40,
    y_bottom_padding=30,
    background_color="#ffffff",
)

graph.x_labels = ["A", "B", "C", "D", "E"]
graph.x_axis_label = "X Axis"
graph.primary_y_axis_label = "Primary Y Axis"

graph.add_series([10, 20, 30, 40, 50], legend_label="Series 1", print_values=True)
graph.add_series([20, 30, 40, 30, 20], legend_label="Series 2", print_values=True)
graph.add_series(
    [-10, -20, 30, 20, 10], legend_label="Color Series", print_values=True
)

# Get the SVG string in base64 format
svg_base64 = graph.to_base64_src()

# Print the SVG string in an img tag so your browser can display it
print(f"\n<img src='{svg_base64}' />")
```


<img src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2MDAiIGhlaWdodD0iNDAwIj4KPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImxlZ2VuZF9ncmFkIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjAlIiB5Mj0iMTAwJSI+CiAgICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3R5bGU9InN0b3AtY29sb3I6I2U4YzE3MCIgLz4KICAgICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0eWxlPSJzdG9wLWNvbG9yOiMyNTNhNWUiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50Pgo8L2RlZnM+PHJlY3QgeD0nMCcgeT0nMCcgd2lkdGg9JzYwMCcgaGVpZ2h0PSc0MDAnIHJ4PScxMCcgcnk9JzEwJyBmaWxsPScjZmZmZmZmJyAvPjxwYXRoIGQ9Ik0yMDAuMCA1LjAgaDE3MC4wIGwxNS4wIDE1LjAgbC0xNS4wIDE1LjAgaC0xNzAuMCBsMTUuMCAtMTUuMCIgZmlsbD0iIzI1M2E1ZSIgLz48dGV4dCB4PSIyMDAuMCIgeT0iMjAuMCIgZHk9IjAuMzVlbSIgZm9udC1zaXplPSIxMCIgdGV4dC1hbmNob3I9ImVuZCIgZmlsbD0iIzAwMDAwMCI+U2VyaWVzIDE8L3RleHQ+PHRleHQgeD0iMzkwLjAiIHk9IjIwLjAiIGR5PSIwLjM1ZW0iIGZvbnQtc2l6ZT0iMTAiIHRleHQtYW5jaG9yPSJzdGFydCIgZmlsbD0iIzAwMDAwMCI+U2VyaWVzIDI8L3RleHQ+PHJlY3QgeD0iNTU1LjAiIHk9IjQwIiB3aWR0aD0iMzAiIGhlaWdodD0iMzMwIiBmaWxsPSJ1cmwoI2xlZ2VuZF9ncmFkKSIgLz48dGV4dCB4PSI1NTAuMCIgeT0iMjA1LjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIHRyYW5zZm9ybT0icm90YXRlKC05MCA1NTAuMCAyMDUuMCkiIGZpbGw9IiMwMDAwMDAiPkNvbG9yIFNlcmllczwvdGV4dD48dGV4dCB4PSI1OTAuMCIgeT0iNDAiIGR5PSIwLjM1ZW0iIHRleHQtYW5jaG9yPSJzdGFydCIgZm9udC1zaXplPSIxMCIgZmlsbD0iIzAwMDAwMCI+MzY8L3RleHQ+PHRleHQgeD0iNTkwLjAiIHk9IjM3MCIgZHk9IjAuMzVlbSIgdGV4dC1hbmNob3I9InN0YXJ0IiBmb250LXNpemU9IjEwIiBmaWxsPSIjMDAwMDAwIj4tMjQ8L3RleHQ+PHBhdGggZD0iTTc2LjM2MzYzNjM2MzYzNjM3IDI2MC4wIHY1NS4wIGwxNS4wIC0xNS4wIGwxNS4wIDE1LjAgdi01NS4wIGwtMTUuMCAtMTUuMCIgZmlsbD0iIzUyNWE2MiIgLz48dGV4dCB4PSI5MS4zNjM2MzYzNjM2MzYzNyIgeT0iMzE1LjAiIGR5PSIwLjM1ZW0iIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZpbGw9IiMwMDAwMDAiPjEwPC90ZXh0Pjx0ZXh0IHg9IjkxLjM2MzYzNjM2MzYzNjM3IiB5PSIyNDAuMCIgZHk9IjAuMzVlbSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZmlsbD0iIzAwMDAwMCI+MjA8L3RleHQ+PHRleHQgeD0iOTEuMzYzNjM2MzYzNjM2MzciIHk9IjI4MC4wIiBkeT0iMC4zNWVtIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmaWxsPSJ3aGl0ZSI+LTEwPC90ZXh0PjxwYXRoIGQ9Ik0xNjkuMDkwOTA5MDkwOTA5MSAyMDUuMCB2NTUuMCBsMTUuMCAtMTUuMCBsMTUuMCAxNS4wIHYtNTUuMCBsLTE1LjAgLTE1LjAiIGZpbGw9IiMzMjQzNWYiIC8+PHRleHQgeD0iMTg0LjA5MDkwOTA5MDkwOTEiIHk9IjI2MC4wIiBkeT0iMC4zNWVtIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmaWxsPSIjMDAwMDAwIj4yMDwvdGV4dD48dGV4dCB4PSIxODQuMDkwOTA5MDkwOTA5MSIgeT0iMTg1LjAiIGR5PSIwLjM1ZW0iIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZpbGw9IiMwMDAwMDAiPjMwPC90ZXh0Pjx0ZXh0IHg9IjE4NC4wOTA5MDkwOTA5MDkxIiB5PSIyMjUuMCIgZHk9IjAuMzVlbSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZmlsbD0id2hpdGUiPi0yMDwvdGV4dD48cGF0aCBkPSJNMjYxLjgxODE4MTgxODE4MTg3IDE1MC4wIHY1NS4wIGwxNS4wIC0xNS4wIGwxNS4wIDE1LjAgdi01NS4wIGwtMTUuMCAtMTUuMCIgZmlsbD0iI2Q0YjQ2ZSIgLz48dGV4dCB4PSIyNzYuODE4MTgxODE4MTgxODciIHk9IjIwNS4wIiBkeT0iMC4zNWVtIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmaWxsPSIjMDAwMDAwIj4zMDwvdGV4dD48dGV4dCB4PSIyNzYuODE4MTgxODE4MTgxODciIHk9IjEzMC4wIiBkeT0iMC4zNWVtIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmaWxsPSIjMDAwMDAwIj40MDwvdGV4dD48dGV4dCB4PSIyNzYuODE4MTgxODE4MTgxODciIHk9IjE3MC4wIiBkeT0iMC4zNWVtIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiA+MzA8L3RleHQ+PHBhdGggZD0iTTM1NC41NDU0NTQ1NDU0NTQ1NiAxNTAuMCB2NTUuMCBsMTUuMCAxNS4wIGwxNS4wIC0xNS4wIHYtNTUuMCBsLTE1LjAgMTUuMCIgZmlsbD0iI2I0OWQ2YiIgLz48dGV4dCB4PSIzNjkuNTQ1NDU0NTQ1NDU0NTYiIHk9IjE1MC4wIiBkeT0iMC4zNWVtIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmaWxsPSIjMDAwMDAwIj40MDwvdGV4dD48dGV4dCB4PSIzNjkuNTQ1NDU0NTQ1NDU0NTYiIHk9IjIyNS4wIiBkeT0iMC4zNWVtIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmaWxsPSIjMDAwMDAwIj4zMDwvdGV4dD48dGV4dCB4PSIzNjkuNTQ1NDU0NTQ1NDU0NTYiIHk9IjE4NS4wIiBkeT0iMC4zNWVtIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiA+MjA8L3RleHQ+PHBhdGggZD0iTTQ0Ny4yNzI3MjcyNzI3MjczIDk1LjAgdjE2NS4wIGwxNS4wIDE1LjAgbDE1LjAgLTE1LjAgdi0xNjUuMCBsLTE1LjAgMTUuMCIgZmlsbD0iIzkzODY2OCIgLz48dGV4dCB4PSI0NjIuMjcyNzI3MjcyNzI3MyIgeT0iOTUuMCIgZHk9IjAuMzVlbSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZmlsbD0iIzAwMDAwMCI+NTA8L3RleHQ+PHRleHQgeD0iNDYyLjI3MjcyNzI3MjcyNzMiIHk9IjI4MC4wIiBkeT0iMC4zNWVtIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmaWxsPSIjMDAwMDAwIj4yMDwvdGV4dD48dGV4dCB4PSI0NjIuMjcyNzI3MjcyNzI3MyIgeT0iMTg1LjAiIGR5PSIwLjM1ZW0iIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiID4xMDwvdGV4dD48bGluZSB4MT0iMzAiIHkxPSI0MCIgeDI9IjMwIiB5Mj0iMzcwIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMSIgLz48bGluZSB4MT0iMzAiIHkxPSIzNzAiIHgyPSI1NDAiIHkyPSIzNzAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxIiAvPjx0ZXh0IHg9IjkxLjM2MzYzNjM2MzYzNjM3IiB5PSIzNzUiIHRleHQtYW5jaG9yPSJlbmQiIGZvbnQtc2l6ZT0iMTAiIHRyYW5zZm9ybT0icm90YXRlKC05MCA5MS4zNjM2MzYzNjM2MzYzNyAzNzUpIiBmaWxsPSIjMDAwMDAwIj5BPC90ZXh0Pjx0ZXh0IHg9IjE4NC4wOTA5MDkwOTA5MDkxIiB5PSIzNzUiIHRleHQtYW5jaG9yPSJlbmQiIGZvbnQtc2l6ZT0iMTAiIHRyYW5zZm9ybT0icm90YXRlKC05MCAxODQuMDkwOTA5MDkwOTA5MSAzNzUpIiBmaWxsPSIjMDAwMDAwIj5CPC90ZXh0Pjx0ZXh0IHg9IjI3Ni44MTgxODE4MTgxODE4NyIgeT0iMzc1IiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjEwIiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMjc2LjgxODE4MTgxODE4MTg3IDM3NSkiIGZpbGw9IiMwMDAwMDAiPkM8L3RleHQ+PHRleHQgeD0iMzY5LjU0NTQ1NDU0NTQ1NDU2IiB5PSIzNzUiIHRleHQtYW5jaG9yPSJlbmQiIGZvbnQtc2l6ZT0iMTAiIHRyYW5zZm9ybT0icm90YXRlKC05MCAzNjkuNTQ1NDU0NTQ1NDU0NTYgMzc1KSIgZmlsbD0iIzAwMDAwMCI+RDwvdGV4dD48dGV4dCB4PSI0NjIuMjcyNzI3MjcyNzI3MyIgeT0iMzc1IiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjEwIiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgNDYyLjI3MjcyNzI3MjcyNzMgMzc1KSIgZmlsbD0iIzAwMDAwMCI+RTwvdGV4dD48dGV4dCB4PSIyNSIgeT0iMzczLjAiIHRleHQtYW5jaG9yPSJlbmQiIGZvbnQtc2l6ZT0iMTAiIGZpbGw9IiMwMDAwMDAiPjA8L3RleHQ+PGxpbmUgeDE9IjMwIiB5MT0iMzcwLjAiIHgyPSIyNyIgeTI9IjM3MC4wIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMSIgLz48dGV4dCB4PSIyNSIgeT0iMzA3LjAiIHRleHQtYW5jaG9yPSJlbmQiIGZvbnQtc2l6ZT0iMTAiIGZpbGw9IiMwMDAwMDAiPjEyPC90ZXh0PjxsaW5lIHgxPSIzMCIgeTE9IjMwNC4wIiB4Mj0iMjciIHkyPSIzMDQuMCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEiIC8+PHRleHQgeD0iMjUiIHk9IjI0MS4wIiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjEwIiBmaWxsPSIjMDAwMDAwIj4yNDwvdGV4dD48bGluZSB4MT0iMzAiIHkxPSIyMzguMCIgeDI9IjI3IiB5Mj0iMjM4LjAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxIiAvPjx0ZXh0IHg9IjI1IiB5PSIxNzUuMCIgdGV4dC1hbmNob3I9ImVuZCIgZm9udC1zaXplPSIxMCIgZmlsbD0iIzAwMDAwMCI+MzY8L3RleHQ+PGxpbmUgeDE9IjMwIiB5MT0iMTcyLjAiIHgyPSIyNyIgeTI9IjE3Mi4wIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMSIgLz48dGV4dCB4PSIyNSIgeT0iMTA5LjAiIHRleHQtYW5jaG9yPSJlbmQiIGZvbnQtc2l6ZT0iMTAiIGZpbGw9IiMwMDAwMDAiPjQ4PC90ZXh0PjxsaW5lIHgxPSIzMCIgeTE9IjEwNi4wIiB4Mj0iMjciIHkyPSIxMDYuMCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjEiIC8+PHRleHQgeD0iMjUiIHk9IjQzLjAiIHRleHQtYW5jaG9yPSJlbmQiIGZvbnQtc2l6ZT0iMTAiIGZpbGw9IiMwMDAwMDAiPjYwPC90ZXh0PjxsaW5lIHgxPSIzMCIgeTE9IjQwLjAiIHgyPSIyNyIgeTI9IjQwLjAiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIxIiAvPjx0ZXh0IHg9IjI4NS4wIiB5PSIzOTIuNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwMDAwMCI+WCBBeGlzPC90ZXh0Pjx0ZXh0IHg9IjcuNSIgeT0iMjA1LjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTIiIHRyYW5zZm9ybT0icm90YXRlKC05MCA3LjUgMjA1LjApIiBmaWxsPSIjMDAwMDAwIj5QcmltYXJ5IFkgQXhpczwvdGV4dD48L3N2Zz4=' />

## Bubble and Arrow Graph
The bubble and arrow graph is for displaying relationships between nodes in a network.

The user adds bubbles, which are displayed in clockwise order around a larger circle. Then the user can add arrows that exit from one bubble and enter another. Arrow width is scaled to show more important connections.

Here's an example:
```
from simplegraph import BubbleAndArrowGraph

graph = BubbleAndArrowGraph(
    width=600,
    height=600,
    background_color="#ffffff",
)

# Optional str label param can be referred to later when defining arrows
graph.add_bubble(100, None, "Bubble 0", label="big_bubble")

# Otherwise bubbles must be referred to by their index number
graph.add_bubble(50, 25, "Bubble 1")
graph.add_bubble(25, 12.5, "Bubble 2")

graph.add_arrow(
    origin="big_bubble",
    destination=1,
    size=60,
)
graph.add_arrow(
    origin="big_bubble",
    destination=2,
    size=40,
)
graph.add_arrow(
    origin=1,
    destination=2,
    size=30,
)

# Arrows pointing to their origin will loop around
graph.add_arrow(
    origin=2,
    destination=2,
    size=20,
)

# Get the SVG string in base64 format
svg_base64 = graph.to_base64_src()

# Print the SVG string in an img tag so your browser can display it
print(f"\n<img src='{svg_base64}' />")
```
<img src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0NDguMTI1MDU3MjA1MzkwOCIgaGVpZ2h0PSI1MjIuNjY5NDc0MDg1NzY4MyIgdmlld0JveD0iNzUuNTA0OTkyNzEwMzAzMiA5NS4yMDQ2NzM1NzA0NzM3MyA0MjguMTI1MDU3MjA1MzkwOCA1MDIuNjY5NDc0MDg1NzY4MyI+PHJlY3QgeD0nNzUuNTA0OTkyNzEwMzAzMicgeT0nOTUuMjA0NjczNTcwNDczNzMnIHdpZHRoPSc0MjguMTI1MDU3MjA1MzkwOCcgaGVpZ2h0PSc1MDIuNjY5NDc0MDg1NzY4Mycgcng9JzEwJyByeT0nMTAnIGZpbGw9JyNmZmZmZmYnIC8+PHBhdGggZD0iTSAzNDcuNzE0NDMxOTg4NzEzMDUsNDg0LjE3MDA0ODg4MzUwNjYgUTM1Mi45NTI4MDU4MzA2Nzc5NiwyNzAuODQ4MDczNzEzNDQzIDI2OC40NzU4Mzc3Nzk2OSwxOTIuOTg2ODIxNzA3NjQ1OSBMMjgwLjMxOTU5OTc4NDkyLDE3OS4yNTQ3Mjc4MzIyMTIzMiBMMjEwLjY4NzE3MjU5NTAxMTg0LDIyMi45Njg3ODUyODU0NTExNiBMMTc3LjY3MzY2MjQwNjI1OTksMjk4LjI2NjIwODA4NTk3IEwxODkuNTE3NDI0NDExNDg5OSwyODQuNTM0MTE0MjEwNTM2NFEyNDcuMDQ3MTk0MTY5MzIyLDMyOS4xNTE5MjYyODY1NTcgMjI4LjEzMTQyMTAyODIwODUsNDU2LjE0NTczNTc1NTcxNDY3IHoiIGZpbGw9InJnYmEoMzcsIDU4LCA5NCwgMC41KSIgLz48cGF0aCBkPSJNIDQyNy40MzY0MzkyOTU3MTYwNyw0NzIuMzMzMzU4MzU3Nzk3MDcgUTMzNy43NzMzMzU3Mzk2NDcxLDMxNC4wMzkyODUyMzg3NDA0IDQxOS4yMjYwNDcwOTExODM2NiwyNTAuMzg0OTg1NTM1MjcwNyBMNDI3LjEyMTg4ODQyODAwMzcsMjU5LjUzOTcxNDc4NTU1OTc0IEw0MDUuMTEyODgxNjM1NTAyMzMsMjA5LjM0MTQzMjkxODU0NzE4IEwzNTguNjkxMjYzNTA4ODk2OSwxODAuMTk4NzI3OTQ5NzIxMzMgTDM2Ni41ODcxMDQ4NDU3MTY5LDE4OS4zNTM0NTcyMDAwMTAzOFEyNjIuMjI2NjY0MjYwMzUyOSwyODUuOTYwNzE0NzYxMjU5NiAzNDcuNzE0NDMxOTg4NzEzMSw1NTIuODM5MDcyMjU4MDQxIHoiIGZpbGw9InJnYmEoMzcsIDU4LCA5NCwgMC41KSIgLz48cGF0aCBkPSJNIDEyOC44MjYzOTgzOTI3Njc1NCwyMDguODA4OTQ5Njc5MTYxNjMgUTMwMC4wLDM0Mi43NDI0NTIyNjY3OTQxIDQyMC4wODIxNTQxMzIwODIzNCwyNTIuODc0Njk0NDg3NDU1MjYgTDQyOC40NTY5NTg1NjA3NCwyNjIuNTg0NzUxMTg2NjY0NiBMNDA1LjExMjg4MTYzNTUwMjMzLDIwOS4zNDE0MzI5MTg1NDcxOCBMMzU1Ljg3NTMyMDE3OTAzOTc2LDE3OC40MzA5MjY0NjAxODM2OCBMMzY0LjI1MDEyNDYwNzY5NzQ0LDE4OC4xNDA5ODMxNTkzOTMwNFEzMDAuMCwyNTcuMjU3NTQ3NzMzMjA1OSAxODQuNjU4NDI3OTE3MTUyMzgsMTQ0LjA3NTIzODM1MTA5OTM2IHoiIGZpbGw9InJnYmEoMjMyLCAxOTMsIDExMiwgMC41KSIgLz48cGF0aCBkPSJNIDQ4My40NDYxNjcxMjkxODksMTc5LjQwOTMyMTI4MzAyMjkzIEM0MjkuMzI3ODA4OTIxNjAyNjQsMzY1LjEwOTEzODMyMDc5MDIgMjU0LjU5MDU0MjUzOTM4MDMsMTYyLjUxMjMxNjA5MTY5MzEgMzc5LjkxMzY1NjY0NDA4NjYsMTMxLjM1NzU4ODczODk1ODg3IEwzODAuODAzODI0ODI0NDU0MzUsMTE5LjMwMTAxNDY1MzcxNDE2IEwzOTMuMDIxODYxNDg5ODUzNzMsMTcyLjczMzA1OTkzMDI2NDkgTDM3My4wODkwMzM5Mjc5MzM5NCwyMjMuNzkxMzIzMzkyNTAxNjIgTDM3My45NzkyMDIxMDgzMDE3LDIxMS43MzQ3NDkzMDcyNTY5MiBDNDE1LjM0NDg2MzY3NTk3NjQsMTc0LjM4MTIyNTE2MzI2Mjk3IDQ0MS4xOTY3MTc5OTMxNzI1LDIwNC4zNTQ4MTcxODQxOTQwOCA0MDMuMDY5MDA2NTYwODkxLDE3My40NzQ4NjY3NDcyMzggeiIgZmlsbD0icmdiYSgxNjUsIDQ4LCA0OCwgMC41KSIgLz48Y2lyY2xlIGN4PSIzMjcuNzgzOTMwMTYxOTYyMyIgY3k9IjQ4Ny4xMjkyMjE1MTQ5MzQiIHI9IjEwMC43NDQ5MjYxNDEzMDc5OSIgZmlsbD0iIzI1M2E1ZSIgLz48Y2lyY2xlIGN4PSIxNTYuNzQyNDEzMTU0OTU5OTYiIGN5PSIxNzYuNDQyMDk0MDE1MTMwNSIgcj0iNzEuMjM3NDIwNDQ0NjU2NzYiIGZpbGw9IiNlOGMxNzAiIC8+PGNpcmNsZSBjeD0iMTU2Ljc0MjQxMzE1NDk1OTk2IiBjeT0iMTc2LjQ0MjA5NDAxNTEzMDUiIHI9IjUwLjM3MjQ2MzA3MDY1Mzk5IiBmaWxsPSIjZmZmZmZmIiAvPjxjaXJjbGUgY3g9IjQ0My4yNTc1ODY4NDUwNCIgY3k9IjE3Ni40NDIwOTQwMTUxMzA0NiIgcj0iNTAuMzcyNDYzMDcwNjUzOTkiIGZpbGw9IiNhNTMwMzAiIC8+PGNpcmNsZSBjeD0iNDQzLjI1NzU4Njg0NTA0IiBjeT0iMTc2LjQ0MjA5NDAxNTEzMDQ2IiByPSIzNS42MTg3MTAyMjIzMjgzOCIgZmlsbD0iI2ZmZmZmZiIgLz48dGV4dCB4PSIzMjcuNzgzOTMwMTYxOTYyMyIgeT0iNDg3LjEyOTIyMTUxNDkzNCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZG9taW5hbnQtYmFzZWxpbmU9Im1pZGRsZSIgZmlsbD0id2hpdGUiIGZvbnQtc2l6ZT0iMTAiPkJ1YmJsZSAwPC90ZXh0Pjx0ZXh0IHg9IjE1Ni43NDI0MTMxNTQ5NTk5NiIgeT0iMTc2LjQ0MjA5NDAxNTEzMDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGRvbWluYW50LWJhc2VsaW5lPSJtaWRkbGUiIGZpbGw9ImJsYWNrIiBmb250LXNpemU9IjEwIj5CdWJibGUgMTwvdGV4dD48dGV4dCB4PSI0NDMuMjU3NTg2ODQ1MDQiIHk9IjE3Ni40NDIwOTQwMTUxMzA0NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZG9taW5hbnQtYmFzZWxpbmU9Im1pZGRsZSIgZmlsbD0iYmxhY2siIGZvbnQtc2l6ZT0iMTAiPkJ1YmJsZSAyPC90ZXh0Pjwvc3ZnPg==' />