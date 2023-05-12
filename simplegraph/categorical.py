import base64
import math

from simplegraph.utils import DEFAULT_COLOR_PALETTE


def get_rounding_places(value_range, ticks):
    lowest_tick = value_range / ticks
    exponent = math.floor(math.log10(abs(lowest_tick)))
    return max(0, -exponent)


def get_adjusted_max(value):
    if value == 0:
        return 0
    exponent = math.floor(math.log10(abs(value)))
    base_value = 10 ** exponent
    rounding_factors = [1, 1.2, 1.5, 2, 2.5, 5]

    adjusted_value = float("inf")
    for factor in rounding_factors:
        candidate_value = math.ceil(value / (base_value * factor)) * (
            base_value * factor
        )
        if candidate_value >= value * 1.05 and candidate_value < adjusted_value:
            adjusted_value = candidate_value

    return adjusted_value


def max_stacked_bar_height(data, series_types, secondary):
    non_secondary_bars_to_use = [
        not secondary[index] and series_types[index][0] == "bar"
        for index in range(len(secondary))
    ]

    stacked_data = [
        sum(
            value
            for i, value in enumerate(column)
            if non_secondary_bars_to_use[i]
        )
        for column in zip(*data)
    ]
    return max(stacked_data) if stacked_data else 0


def max_non_secondary_value(data, secondary):
    max_values = [(max(values), index) for index, values in enumerate(data)]
    non_secondary_values = [
        value for value, index in max_values if not secondary[index]
    ]
    return max(non_secondary_values) if non_secondary_values else 0


class CategoricalGraph:
    """
    This class is used to generate SVG graphs and compile them to base64
    strings. This allows us to embed SVG graphs into forum posts by inserting
    them into the src attribute of an <img> tag.
    The graphs generated by this class should have a categorical x-axis (e.g.
    user accounts). They can have a primary and secondary y-axis with different
    scales. Each series can display as bars (stacked or side by side), a line,
    or dots.
    """

    def __init__(
        self,
        width=300,
        height=200,
        bar_width=30,
        padding=20,
        x_padding=None,
        y_padding=None,
        y_top_padding=None,
        y_bottom_padding=None,
        x_left_padding=None,
        x_right_padding=None,
        colors=None,
        stacked=False,
        num_y_ticks=5,
        x_axis_label=None,
        primary_y_axis_label=None,
        secondary_y_axis_label=None,
    ):
        self.width = width
        self.height = height
        self.bar_width = bar_width
        self.y_top_padding = y_top_padding or y_padding or padding
        self.y_bottom_padding = y_bottom_padding or y_padding or padding
        self.x_left_padding = x_left_padding or x_padding or padding
        self.x_right_padding = x_right_padding or x_padding or padding
        self.colors = colors or DEFAULT_COLOR_PALETTE
        self.stacked = stacked
        self.num_y_ticks = num_y_ticks
        self.x_axis_label = x_axis_label
        self.primary_y_axis_label = primary_y_axis_label
        self.secondary_y_axis_label = secondary_y_axis_label
        self.data = []
        self.x_labels = []
        self.legend_labels = []
        self.series_types = []
        self.secondary = []

    def add_series(
        self,
        series,
        legend_label=None,
        series_type="bar",
        print_values=False,
        secondary=False,
    ):
        self.data.append(series)
        self.legend_labels.append(legend_label or "")
        self.series_types.append((series_type, print_values))
        self.secondary.append(secondary)

    def _draw_bar(
        self, x, y, width, height, fill, stroke="black", stroke_width="2"
    ):
        return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" />'

    def _draw_dot(self, x, y, fill, radius=5, stroke="black", stroke_width="1"):
        return f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" />'

    def _draw_line(self, x1, y1, x2, y2, stroke="black", stroke_width="1"):
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{stroke_width}" />'

    def render(self):
        if self.stacked:
            max_value_primary = max(
                max_stacked_bar_height(
                    self.data, self.series_types, self.secondary
                ),
                max_non_secondary_value(self.data, self.secondary),
            )

            max_value_secondary = max(
                max_stacked_bar_height(
                    self.data,
                    self.series_types,
                    [not sec for sec in self.secondary],
                ),
                max_non_secondary_value(
                    self.data,
                    [not sec for sec in self.secondary],
                ),
            )
        else:
            max_value_primary = max_non_secondary_value(
                self.data, self.secondary
            )
            max_value_secondary = max_non_secondary_value(
                self.data, [not sec for sec in self.secondary]
            )

        adjusted_max_value_primary = get_adjusted_max(max_value_primary)
        adjusted_max_value_secondary = get_adjusted_max(max_value_secondary)

        scale_primary = (
            self.height - self.y_top_padding - self.y_bottom_padding
        ) / adjusted_max_value_primary
        scale_secondary = (
            self.height - self.y_top_padding - self.y_bottom_padding
        ) / adjusted_max_value_secondary

        svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}">'

        # Draw legend
        legend_x = self.x_left_padding
        legend_y = self.y_top_padding / 2
        legend_spacing = 5
        legend_rect_size = 10

        for index, label in enumerate(self.legend_labels):
            series_type, _ = self.series_types[index]
            if series_type == "dot":
                svg += self._draw_dot(
                    legend_x + legend_rect_size / 2,
                    legend_y + legend_rect_size / 2,
                    radius=5,
                    fill=self.colors[index],
                )
            elif series_type == "line":
                svg += self._draw_line(
                    legend_x,
                    legend_y + legend_rect_size / 2,
                    legend_x + legend_rect_size,
                    legend_y + legend_rect_size / 2,
                    stroke=self.colors[index],
                )
            else:  # series_type == "bar"
                svg += f'<rect x="{legend_x}" y="{legend_y}" width="{legend_rect_size}" height="{legend_rect_size}" fill="{self.colors[index]}" />'
            svg += f'<text x="{legend_x + legend_rect_size + legend_spacing}" y="{legend_y + legend_rect_size}" font-size="10" alignment-baseline="central">{label}</text>'
            legend_x += (2 * legend_spacing) + legend_rect_size + len(label) * 6

        # Draw series
        bar_spacing = (
            self.width - self.x_left_padding - self.x_right_padding
        ) / len(self.data[0])
        num_bar_series = len(
            [
                series_type
                for series_type, _ in self.series_types
                if series_type == "bar"
            ]
        )
        total_bars_width = (
            self.bar_width if self.stacked else num_bar_series * self.bar_width
        )

        num_categories = len(self.data[0])
        num_series = len(self.data)
        bar_heights = [0] * num_categories

        for sub_index in range(num_categories):
            for index in range(num_series):
                value = self.data[index][sub_index]
                secondary_value = self.secondary[index]

                series_type, print_values = self.series_types[index]

                if (
                    series_type == "dot"
                    or series_type == "line"
                    or self.stacked
                ):
                    x = (
                        self.x_left_padding
                        + sub_index * bar_spacing
                        + (bar_spacing - self.bar_width) / 2
                    )
                else:
                    x = (
                        self.x_left_padding
                        + sub_index * bar_spacing
                        + index * self.bar_width
                    )
                scale = scale_secondary if secondary_value else scale_primary
                y = self.height - self.y_bottom_padding - value * scale

                if series_type == "bar" and self.stacked:
                    bar_height = value * scale
                    y -= bar_heights[sub_index]
                    svg += self._draw_bar(
                        x, y, self.bar_width, bar_height, self.colors[index]
                    )
                    bar_heights[sub_index] += bar_height
                elif series_type == "bar":
                    svg += self._draw_bar(
                        x,
                        y,
                        self.bar_width,
                        value * scale,
                        self.colors[index],
                    )
                elif series_type == "dot":
                    center_x = (
                        self.x_left_padding
                        + sub_index * bar_spacing
                        + (bar_spacing - total_bars_width) / 2
                        + self.bar_width * (num_bar_series - 1) / 2
                    )
                    svg += self._draw_dot(
                        center_x,
                        y,
                        radius=5,
                        fill=self.colors[index],
                    )
                elif series_type == "line" and sub_index > 0:
                    prev_y = (
                        self.height
                        - self.y_bottom_padding
                        - self.data[index][sub_index - 1] * scale
                    )
                    prev_x = (
                        self.x_left_padding
                        + (sub_index - 1) * bar_spacing
                        + (bar_spacing - self.bar_width) / 2
                    )
                    svg += self._draw_line(
                        prev_x,
                        prev_y,
                        x,
                        y,
                        stroke=self.colors[index],
                    )

                if print_values:
                    if series_type == "dot":
                        value_x = center_x
                    elif series_type == "line":
                        value_x = x
                    else:
                        value_x = x + self.bar_width / 2

                    value_y = y - 5 if series_type == "bar" else y - 10
                    svg += f'<text x="{value_x}" y="{value_y}" text-anchor="middle" font-size="10">{value}</text>'

        # Draw axis
        svg += f'<line x1="{self.x_left_padding}" y1="{self.y_top_padding}" x2="{self.x_left_padding}" y2="{self.height - self.y_bottom_padding}" stroke="black" stroke-width="1" />'
        svg += f'<line x1="{self.x_left_padding}" y1="{self.height - self.y_bottom_padding}" x2="{self.width - self.x_right_padding}" y2="{self.height - self.y_bottom_padding}" stroke="black" stroke-width="1" />'

        # Draw secondary y-axis if needed
        if any(self.secondary):
            svg += f'<line x1="{self.width - self.x_right_padding}" y1="{self.y_top_padding}" x2="{self.width - self.x_right_padding}" y2="{self.height - self.y_bottom_padding}" stroke="black" stroke-width="1" />'

        # Draw x tick labels
        for index, label in enumerate(self.x_labels):
            x = (
                self.x_left_padding
                + index * bar_spacing
                + (bar_spacing - total_bars_width) / 2
                + self.bar_width * (num_bar_series - 1) / 2
            )
            y = self.height - self.y_bottom_padding + 5
            svg += f'<text x="{x}" y="{y}" text-anchor="end" font-size="10" transform="rotate(-90 {x} {y})">{label}</text>'

        # Determine the appropriate number of decimal places for rounding based on the range
        rounding_places_primary = get_rounding_places(
            max_value_primary, self.num_y_ticks
        )
        rounding_places_secondary = get_rounding_places(
            max_value_secondary, self.num_y_ticks
        )

        # Draw primary y-axis ticks and values
        for i in range(self.num_y_ticks + 1):
            tick_value = adjusted_max_value_primary * i / self.num_y_ticks
            tick_y = (
                self.height - self.y_bottom_padding - tick_value * scale_primary
            )
            tick_label = f"{round(tick_value, rounding_places_primary)}"

            svg += f'<text x="{self.x_left_padding - 5}" y="{tick_y + 3}" text-anchor="end" font-size="10">{tick_label}</text>'
            svg += f'<line x1="{self.x_left_padding}" y1="{tick_y}" x2="{self.x_left_padding - 3}" y2="{tick_y}" stroke="black" stroke-width="1" />'

        # Draw secondary y-axis ticks and values if needed
        if any(self.secondary):
            for i in range(self.num_y_ticks + 1):
                tick_value = adjusted_max_value_secondary * i / self.num_y_ticks
                tick_y = (
                    self.height
                    - self.y_bottom_padding
                    - tick_value * scale_secondary
                )
                tick_label = f"{round(tick_value, rounding_places_secondary)}"

                svg += f'<text x="{self.width - self.x_right_padding + 5}" y="{tick_y + 3}" text-anchor="start" font-size="10">{tick_label}</text>'
                svg += f'<line x1="{self.width - self.x_right_padding}" y1="{tick_y}" x2="{self.width - self.x_right_padding + 3}" y2="{tick_y}" stroke="black" stroke-width="1" />'

        # Draw axis labels
        if self.x_axis_label:
            x_label_x = self.width / 2
            x_label_y = self.height - self.y_bottom_padding / 4
            svg += f'<text x="{x_label_x}" y="{x_label_y}" text-anchor="middle" font-size="12">{self.x_axis_label}</text>'

        if self.primary_y_axis_label:
            y_label_x = self.x_left_padding / 4
            y_label_y = self.height / 2
            svg += f'<text x="{y_label_x}" y="{y_label_y}" text-anchor="middle" font-size="12" transform="rotate(-90 {y_label_x} {y_label_y})">{self.primary_y_axis_label}</text>'

        if any(self.secondary) and self.secondary_y_axis_label:
            sec_y_label_x = self.width - self.x_right_padding / 4
            sec_y_label_y = self.height / 2
            svg += f'<text x="{sec_y_label_x}" y="{sec_y_label_y}" text-anchor="middle" font-size="12" transform="rotate(-90 {sec_y_label_x} {sec_y_label_y})">{self.secondary_y_axis_label}</text>'

        svg += "</svg>"
        return svg

    def to_base64_src(self):
        svg_str = self.render()
        svg_bytes = svg_str.encode("utf-8")
        encoded_svg = base64.b64encode(svg_bytes).decode("utf-8")
        return "data:image/svg+xml;base64," + encoded_svg


if __name__ == "__main__":
    graph = CategoricalGraph(
        width=600,
        height=600,
        bar_width=40,
        x_padding=40,
        y_top_padding=30,
        y_bottom_padding=60,
    )

    graph.x_labels = ["A long label", "B", "C", "D", "E"]
    graph.x_axis_label = "X Axis"
    graph.primary_y_axis_label = "Primary Y Axis"
    graph.secondary_y_axis_label = "Secondary Y Axis"

    graph.add_series([10, 20, 30, 40, 50], legend_label="Series 1")
    graph.add_series(
        [25, 35, 45, 55, 65], legend_label="Series 2", print_values=True
    )
    graph.add_series(
        [1.1, 1.6, 2.2, 0.99, 1.37],
        legend_label="Series 3",
        series_type="dot",
        print_values=True,
        secondary=True,
    )
    graph.add_series(
        [2.5, 1.1, 1.6, 2.2, 0.99],
        legend_label="Series 4",
        series_type="line",
        print_values=True,
        secondary=True,
    )

    encoded_svg = graph.to_base64_src()

    graph.stacked = True
    encoded_svg_stacked = graph.to_base64_src()

    print(
        f"<img src='{encoded_svg}' alt='test graph 1'>\n"
        + f"<img src='{encoded_svg_stacked}' alt='test graph 2 (stacked)'>\n"
    )