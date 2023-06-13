from .base import BaseGraph
from .utils import human_readable_number
from .utils import calculate_ticks
from .utils import match_ticks


def stacked_bar_range(data, series_types, secondary):
    non_secondary_bars_to_use = [
        not secondary[index] and series_types[index][0] == "bar"
        for index in range(len(secondary))
    ]

    stacked_positive_data = [
        sum(
            max(value, 0)
            for i, value in enumerate(column)
            if non_secondary_bars_to_use[i]
        )
        for column in zip(*data)
    ]

    stacked_negative_data = [
        sum(
            min(value, 0)
            for i, value in enumerate(column)
            if non_secondary_bars_to_use[i]
        )
        for column in zip(*data)
    ]
    return (
        (min(stacked_negative_data), max(stacked_positive_data))
        if non_secondary_bars_to_use
        else (None, None)
    )


def non_secondary_range(data, secondary):
    non_secondary_values = [
        value
        for values, is_secondary in zip(data, secondary)
        if not is_secondary
        for value in values
    ]
    return (
        (min(non_secondary_values), max(non_secondary_values))
        if non_secondary_values
        else (None, None)
    )


class CategoricalGraph(BaseGraph):
    """
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
        show_legend=True,
        rotate_x_labels=True,
        background_color=None,
        dark_mode=None,
        title=None,
        title_font_size=None,
        element_spacing=None,
        watermark=None,
    ):
        super().__init__(
            width=width,
            height=height,
            padding=padding,
            x_padding=x_padding,
            y_padding=y_padding,
            y_top_padding=y_top_padding,
            y_bottom_padding=y_bottom_padding,
            x_left_padding=x_left_padding,
            x_right_padding=x_right_padding,
            colors=colors,
            num_y_ticks=num_y_ticks,
            x_axis_label=x_axis_label,
            primary_y_axis_label=primary_y_axis_label,
            secondary_y_axis_label=secondary_y_axis_label,
            show_legend=show_legend,
            rotate_x_labels=rotate_x_labels,
            background_color=background_color,
            dark_mode=dark_mode,
            title=title,
            title_font_size=title_font_size,
            element_spacing=element_spacing,
            watermark=watermark,
        )
        self.stacked = stacked
        self.bar_width = bar_width
        self.x_labels = []
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

    def _draw_bar(self, x, y, width, height, fill):
        if height < 0:
            y += height
            height *= -1
        return (
            f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{fill}" />'
        )

    def _draw_dot(self, x, y, fill, radius=5, stroke=None, stroke_width=1):
        if stroke is None:
            stroke_parameter = ""
        else:
            stroke_parameter = f'stroke="{stroke}" stroke-width="{stroke_width}"'
        return f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" {stroke_parameter} />'

    def _draw_line(self, x1, y1, x2, y2, stroke="black", stroke_width="1"):
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{stroke_width}" />'

    def render(self):
        self._reset_graph()
        graph_width = self.width
        has_secondary = any(self.secondary)
        max_value_secondary = None
        min_value_secondary = None
        if self.stacked:
            bar_series_indices = [
                i for i, series in enumerate(self.series_types) if series[0] == "bar"
            ]

            assert all(self.secondary[i] for i in bar_series_indices) or not any(
                self.secondary[i] for i in bar_series_indices
            ), "All stacked bar series must be either primary or secondary."

            min_value_primary, max_value_primary = stacked_bar_range(
                self.data, self.series_types, self.secondary
            )
            if has_secondary:
                min_value_secondary, max_value_secondary = stacked_bar_range(
                    self.data, self.series_types, [not sec for sec in self.secondary]
                )
        else:
            min_value_primary, max_value_primary = non_secondary_range(
                self.data, self.secondary
            )
            if has_secondary:
                min_value_secondary, max_value_secondary = non_secondary_range(
                    self.data, [not sec for sec in self.secondary]
                )

        primary_ticks = calculate_ticks(
            min_value_primary,
            max_value_primary,
            include_zero=True,
            target_tick_count=self.num_y_ticks,
        )

        if has_secondary:
            secondary_ticks = calculate_ticks(
                min_value_secondary,
                max_value_secondary,
                include_zero=True,
                target_tick_count=self.num_y_ticks,
            )

            primary_ticks, secondary_ticks = match_ticks(primary_ticks, secondary_ticks)

            adjusted_max_value_secondary = secondary_ticks[-1]
            adjusted_min_value_secondary = secondary_ticks[0]

        adjusted_max_value_primary = primary_ticks[-1]
        adjusted_min_value_primary = primary_ticks[0]

        num_bars = 0
        if not self.stacked:
            for type, _ in self.series_types:
                if type == "bar":
                    num_bars += 1
        num_bars = max(num_bars, 1)
        max_bar_width = graph_width / (num_bars * len(self.data[0]))

        bar_width = min(max_bar_width, self.bar_width)

        scale_primary = (self.height) / (
            adjusted_max_value_primary - adjusted_min_value_primary
        )
        if has_secondary:
            scale_secondary = (self.height) / (
                adjusted_max_value_secondary - adjusted_min_value_secondary
            )
        else:
            scale_secondary = None

        # Draw series
        bar_spacing = (self.width) / len(self.data[0])
        bar_series_across = (
            1
            if self.stacked
            else len(
                [
                    series_type
                    for series_type, _ in self.series_types
                    if series_type == "bar"
                ]
            )
        )
        total_bars_width = bar_series_across * bar_width

        num_categories = len(self.data[0])
        num_series = len(self.data)
        positive_bar_heights = [0] * num_categories
        negative_bar_heights = [0] * num_categories

        for sub_index in range(num_categories):
            bar_count = 0
            for index in range(num_series):
                value = self.data[index][sub_index]
                secondary_value = self.secondary[index]

                series_type, print_values = self.series_types[index]

                if series_type == "dot" or series_type == "line" or self.stacked:
                    x = sub_index * bar_spacing + (bar_spacing - bar_width) / 2
                else:
                    # Calculate the starting x-position of the bars in each category
                    start_x = (
                        sub_index * bar_spacing + (bar_spacing - total_bars_width) / 2
                    )
                    x = (
                        start_x + bar_count * bar_width - bar_width / 2
                    )  # Adjusting by half of the bar width
                    bar_count += 1
                scale = scale_secondary if secondary_value else scale_primary
                min_value = (
                    adjusted_min_value_secondary
                    if secondary_value
                    else adjusted_min_value_primary
                )
                y = self.height - (value - min_value) * scale

                if series_type == "bar" and self.stacked:
                    bar_height = value * scale
                    x -= bar_width / 2
                    if value >= 0:
                        y -= positive_bar_heights[sub_index]
                        positive_bar_heights[sub_index] += bar_height
                    else:
                        y -= negative_bar_heights[sub_index]
                        negative_bar_heights[sub_index] += bar_height
                    self.svg_elements.append(
                        self._draw_bar(x, y, bar_width, bar_height, self.colors[index])
                    )
                elif series_type == "bar":
                    self.svg_elements.append(
                        self._draw_bar(
                            x,
                            y,
                            bar_width,
                            value * scale,
                            self.colors[index],
                        )
                    )
                elif series_type == "dot":
                    center_x = (
                        sub_index * bar_spacing
                        + (bar_spacing - total_bars_width) / 2
                        + bar_width * (bar_series_across - 1) / 2
                    )
                    self.svg_elements.append(
                        self._draw_dot(
                            center_x,
                            y,
                            radius=5,
                            fill=self.colors[index],
                        )
                    )
                elif series_type == "line" and sub_index > 0:
                    prev_y = (
                        self.height
                        - (self.data[index][sub_index - 1] - min_value) * scale
                    )
                    prev_x = (sub_index - 1) * bar_spacing + (
                        bar_spacing - bar_width
                    ) / 2
                    self.svg_elements.append(
                        self._draw_line(
                            prev_x,
                            prev_y,
                            x,
                            y,
                            stroke=self.colors[index],
                        )
                    )

                if print_values:
                    if series_type == "dot":
                        value_x = center_x
                    elif series_type == "line":
                        value_x = x
                    else:
                        value_x = x + bar_width / 2

                    value_y = y - 5 if series_type == "bar" else y - 10
                    self.svg_elements.append(
                        self._generate_text(
                            value, value_x, value_y, fill=self.text_color
                        )
                    )

        # Draw axis
        self.svg_elements.append(
            f'<line x1="0" y1="0" x2="0" y2="{self.height}" stroke="{self.text_color}" stroke-width="1" />'
        )
        zero_line_y = self.height + adjusted_min_value_primary * scale_primary
        self.svg_elements.append(
            f'<line x1="0" y1="{zero_line_y}" '
            + f'x2="{self.width}" y2="{zero_line_y}" '
            + f'stroke="{self.text_color}" stroke-width="1" />'
        )

        # Draw secondary y-axis if needed
        if has_secondary:
            self.svg_elements.append(
                f'<line x1="{self.width}" y1="0" x2="{self.width}" y2="{self.height}" stroke="{self.text_color}" stroke-width="1" />'
            )
            secondary_zero_line_y = (
                self.height + adjusted_min_value_secondary * scale_secondary
            )
            assert (
                abs(secondary_zero_line_y - zero_line_y) < 1e-9
            ), f"Secondary y-axis not aligned with primary y-axis: {secondary_zero_line_y} != {zero_line_y}"

        # Draw x tick labels
        for index, label in enumerate(self.x_labels):
            x = (
                index * bar_spacing
                + (bar_spacing - total_bars_width) / 2
                + bar_width * (bar_series_across - 1) / 2
            )
            y = self.height + 5
            if label is not None and self.rotate_x_labels:
                self.svg_elements.append(
                    self._generate_text(
                        label, x, y, anchor="end", fill=self.text_color, rotation=-90
                    )
                )
            elif label is not None and not self.rotate_x_labels:
                self.svg_elements.append(
                    self._generate_text(label, x, y + 10, fill=self.text_color)
                )

        # Draw primary y-axis ticks and values
        for tick_value in primary_ticks:
            tick_y = (
                self.height - (tick_value - adjusted_min_value_primary) * scale_primary
            )
            tick_label = f"{human_readable_number(tick_value)}"

            self.svg_elements.append(
                self._generate_text(
                    tick_label,
                    -5,
                    tick_y + 3,
                    fill=self.text_color,
                    anchor="end",
                    dominant_baseline="text-bottom",
                )
            )
            self.svg_elements.append(
                f'<line x1="0" y1="{tick_y}" x2="-3" y2="{tick_y}" stroke="{self.text_color}" stroke-width="1" />'
            )

        # Draw secondary y-axis ticks and values if needed
        if has_secondary:
            for tick_value in secondary_ticks:
                tick_y = (
                    self.height
                    - (tick_value - adjusted_min_value_secondary) * scale_secondary
                )
                tick_label = f"{human_readable_number(tick_value)}"

                self.svg_elements.append(
                    self._generate_text(
                        tick_label,
                        self.width + 5,
                        tick_y + 3,
                        fill=self.text_color,
                        anchor="start",
                        dominant_baseline="text-bottom",
                    )
                )
                self.svg_elements.append(
                    f'<line x1="{self.width}" y1="{tick_y}" x2="{self.width + 3}" y2="{tick_y}" stroke="{self.text_color}" stroke-width="1" />'
                )

        # Draw axis labels
        if self.x_axis_label:
            x_label_x = (self.width) / 2
            x_label_y = (
                max(self.height, self.most_extreme_dimensions["bottom"])
                + 1.5 * self.element_spacing
            )
            self.svg_elements.append(
                self._generate_text(
                    self.x_axis_label,
                    x_label_x,
                    x_label_y,
                    font_size=12,
                    fill=self.text_color,
                )
            )

        if self.primary_y_axis_label:
            y_label_x = (
                min(0, self.most_extreme_dimensions["left"]) - self.element_spacing
            )
            y_label_y = (self.height) / 2
            self.svg_elements.append(
                self._generate_text(
                    self.primary_y_axis_label,
                    y_label_x,
                    y_label_y,
                    font_size=12,
                    fill=self.text_color,
                    rotation=-90,
                )
            )

        if any(self.secondary) and self.secondary_y_axis_label:
            sec_y_label_x = (
                max(self.width, self.most_extreme_dimensions["right"])
                + self.element_spacing
            )
            sec_y_label_y = self.height / 2
            self.svg_elements.append(
                self._generate_text(
                    self.secondary_y_axis_label,
                    sec_y_label_x,
                    sec_y_label_y,
                    font_size=12,
                    fill=self.text_color,
                    rotation=-90,
                )
            )

        # Draw legend
        if self.show_legend:
            legend_rect_size = 10
            legend_x = (
                max(self.width, self.most_extreme_dimensions["right"])
                + self.element_spacing / 2
            )
            if has_secondary:
                legend_x += 10
            legend_y = 0

            for index, label in enumerate(self.legend_labels):
                series_type, _ = self.series_types[index]
                if series_type == "dot":
                    self.svg_elements.append(
                        self._draw_dot(
                            legend_x + legend_rect_size / 2,
                            legend_y + legend_rect_size / 2,
                            radius=5,
                            fill=self.colors[index],
                        )
                    )
                elif series_type == "line":
                    self.svg_elements.append(
                        self._draw_line(
                            legend_x,
                            legend_y + legend_rect_size / 2,
                            legend_x + legend_rect_size,
                            legend_y + legend_rect_size / 2,
                            stroke=self.colors[index],
                        )
                    )
                else:  # series_type == "bar"
                    self.svg_elements.append(
                        f'<rect x="{legend_x}" y="{legend_y}" width="{legend_rect_size}" '
                        + f'height="{legend_rect_size}" fill="{self.colors[index]}" />'
                    )
                self.svg_elements.append(
                    self._generate_text(
                        label,
                        legend_x + legend_rect_size + self.element_spacing / 2,
                        legend_y + (2 / 3) * legend_rect_size,
                        fill=self.text_color,
                        anchor="start",
                    )
                )
                legend_y += self.element_spacing + legend_rect_size
                if legend_y + legend_rect_size > self.height:
                    legend_y = 0
                    legend_x = (
                        max(self.width, self.most_extreme_dimensions["right"])
                        + self.element_spacing / 2
                    )

        return self._generate_svg()
