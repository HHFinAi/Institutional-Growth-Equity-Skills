#!/usr/bin/env python3
"""
IB-Professional Infographic Generator v2.0
Enhanced with grid-based layout, PNG transparency, and sophisticated styling.
"""

import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Wedge, Circle
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os


class IBColors:
    """Goldman/Morgan Stanley standard color palette."""
    NAVY = '#1F3864'
    BLUE = '#2E75B6'
    GOLD = '#C5A572'
    GREEN = '#00B050'
    RED = '#C00000'
    GRAY = '#7F7F7F'
    LIGHT_GRAY = '#D0D0D0'
    VERY_LIGHT_GRAY = '#E8E8E8'
    LIGHT_FILL = '#E8F1F8'
    WHITE = '#FFFFFF'
    BLACK = '#000000'
    TRANSPARENT = (0, 0, 0, 0)
    
    # Extended palette
    TEAL = '#008080'
    ORANGE = '#ED7D31'
    PURPLE = '#7030A0'
    DARK_GREEN = '#006400'
    
    @classmethod
    def hex_to_rgb(cls, hex_color):
        """Convert hex to RGB tuple (0-255 range)."""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    @classmethod
    def hex_to_rgba(cls, hex_color, alpha=255):
        """Convert hex to RGBA tuple."""
        rgb = cls.hex_to_rgb(hex_color)
        return (*rgb, alpha)
    
    @classmethod
    def hex_to_mpl(cls, hex_color):
        """Convert hex to matplotlib (0-1 range)."""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16)/255 for i in (0, 2, 4))


class IBCharts:
    """Pre-styled chart generators following IB conventions."""
    
    @staticmethod
    def _apply_ib_style(ax, title=None, transparent=True):
        """Apply IB styling to any matplotlib axes."""
        if transparent:
            ax.set_facecolor('none')
            ax.figure.patch.set_facecolor('none')
        
        # Remove top and right spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        # Style remaining spines
        ax.spines['bottom'].set_color(IBColors.LIGHT_GRAY)
        ax.spines['left'].set_color(IBColors.LIGHT_GRAY)
        ax.spines['bottom'].set_linewidth(0.5)
        ax.spines['left'].set_linewidth(0.5)
        
        # Style ticks
        ax.tick_params(colors=IBColors.GRAY, labelsize=9)
        
        # Grid styling
        ax.yaxis.grid(True, linestyle=':', color=IBColors.VERY_LIGHT_GRAY, linewidth=0.5, alpha=0.7)
        ax.set_axisbelow(True)
        
        # Title
        if title:
            ax.set_title(title, fontsize=11, fontweight='bold', 
                        color=IBColors.NAVY, loc='left', pad=12)
        
        return ax
    
    @staticmethod
    def waterfall(categories, values, title=None, figsize=(6, 3.5), transparent=True):
        """Create a waterfall/bridge chart."""
        colors_dict = {
            'positive': IBColors.GREEN,
            'negative': IBColors.RED,
            'total': IBColors.NAVY
        }
        
        fig, ax = plt.subplots(figsize=figsize)
        if transparent:
            fig.patch.set_alpha(0)
            ax.set_facecolor('none')
        else:
            fig.patch.set_facecolor('white')
            ax.set_facecolor('white')
        
        n = len(values)
        cumulative = [0] * n
        bar_colors = []
        
        running = 0
        for i, val in enumerate(values):
            if i == 0 or i == n - 1:
                cumulative[i] = 0
                bar_colors.append(colors_dict['total'])
            else:
                cumulative[i] = running
                bar_colors.append(colors_dict['positive'] if val >= 0 else colors_dict['negative'])
            if i < n - 1:
                running += val if i > 0 else val
        
        bars = ax.bar(categories, values, bottom=cumulative, 
                     color=bar_colors, width=0.6, edgecolor='none')
        
        # Connecting lines
        for i in range(n - 1):
            y_end = values[0] if i == 0 else cumulative[i] + values[i]
            ax.plot([i + 0.3, i + 0.7], [y_end, y_end], 
                   color=IBColors.GRAY, linewidth=0.8, linestyle='--', alpha=0.6)
        
        # Value labels
        for i, (bar, val) in enumerate(zip(bars, values)):
            height = bar.get_height()
            y_pos = bar.get_y() + height / 2
            label = f'{val:+,.0f}' if 0 < i < n - 1 else f'{val:,.0f}'
            ax.annotate(label, xy=(bar.get_x() + bar.get_width() / 2, y_pos),
                       ha='center', va='center', fontsize=9, fontweight='bold',
                       color='white')
        
        IBCharts._apply_ib_style(ax, title, transparent)
        ax.set_ylabel('')
        ax.set_xlabel('')
        
        plt.tight_layout(pad=1.5)
        return fig
    
    @staticmethod
    def hbar(categories, values, title=None, figsize=(5, 3.5), 
             highlight_index=None, color=None, transparent=True):
        """Create a horizontal bar chart."""
        if color is None:
            color = IBColors.BLUE
            
        fig, ax = plt.subplots(figsize=figsize)
        if transparent:
            fig.patch.set_alpha(0)
            ax.set_facecolor('none')
        else:
            fig.patch.set_facecolor('white')
            ax.set_facecolor('white')
        
        bar_colors = [color] * len(values)
        if highlight_index is not None:
            bar_colors[highlight_index] = IBColors.NAVY
        
        y_pos = np.arange(len(categories))
        bars = ax.barh(y_pos, values, color=bar_colors, height=0.6, edgecolor='none')
        
        ax.set_yticks(y_pos)
        ax.set_yticklabels(categories)
        ax.invert_yaxis()
        
        for bar, val in zip(bars, values):
            width = bar.get_width()
            ax.annotate(f'{val:,.1f}', xy=(width, bar.get_y() + bar.get_height() / 2),
                       xytext=(5, 0), textcoords='offset points',
                       ha='left', va='center', fontsize=9, color=IBColors.GRAY)
        
        IBCharts._apply_ib_style(ax, title, transparent)
        ax.spines['left'].set_visible(False)
        ax.tick_params(left=False)
        ax.xaxis.grid(True, linestyle=':', color=IBColors.VERY_LIGHT_GRAY, linewidth=0.5)
        ax.yaxis.grid(False)
        
        plt.tight_layout(pad=1.5)
        return fig
    
    @staticmethod
    def donut(labels, values, title=None, figsize=(4, 4), center_label=None, transparent=True):
        """Create a donut chart."""
        fig, ax = plt.subplots(figsize=figsize)
        if transparent:
            fig.patch.set_alpha(0)
            ax.set_facecolor('none')
        else:
            fig.patch.set_facecolor('white')
            ax.set_facecolor('white')
        
        palette = [IBColors.NAVY, IBColors.BLUE, IBColors.GOLD, IBColors.TEAL, IBColors.GRAY]
        chart_colors = palette[:len(values)]
        
        wedges, texts, autotexts = ax.pie(
            values, labels=None, autopct='%1.0f%%',
            colors=chart_colors, startangle=90,
            wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2),
            pctdistance=0.75
        )
        
        for autotext in autotexts:
            autotext.set_fontsize(9)
            autotext.set_fontweight('bold')
            autotext.set_color('white')
        
        if center_label:
            ax.text(0, 0, center_label, ha='center', va='center',
                   fontsize=12, fontweight='bold', color=IBColors.NAVY)
        
        ax.legend(wedges, labels, loc='center left', bbox_to_anchor=(1, 0.5),
                 fontsize=9, frameon=False)
        
        if title:
            ax.set_title(title, fontsize=11, fontweight='bold',
                        color=IBColors.NAVY, pad=15)
        
        ax.axis('equal')
        plt.tight_layout(pad=1.5)
        return fig
    
    @staticmethod
    def line_area(x_labels, y_values, title=None, figsize=(6, 3),
                  fill_alpha=0.25, color=None, transparent=True):
        """Create a line chart with area fill."""
        if color is None:
            color = IBColors.BLUE
            
        fig, ax = plt.subplots(figsize=figsize)
        if transparent:
            fig.patch.set_alpha(0)
            ax.set_facecolor('none')
        else:
            fig.patch.set_facecolor('white')
            ax.set_facecolor('white')
        
        x = np.arange(len(x_labels))
        
        ax.plot(x, y_values, color=color, linewidth=2.5, marker='o', 
               markersize=8, markerfacecolor='white', markeredgewidth=2.5)
        ax.fill_between(x, y_values, alpha=fill_alpha, color=color)
        
        ax.set_xticks(x)
        ax.set_xticklabels(x_labels)
        
        for i, val in enumerate(y_values):
            ax.annotate(f'{val:,.0f}', xy=(i, val), xytext=(0, 10),
                       textcoords='offset points', ha='center', va='bottom',
                       fontsize=9, fontweight='bold', color=IBColors.NAVY)
        
        IBCharts._apply_ib_style(ax, title, transparent)
        
        plt.tight_layout(pad=1.5)
        return fig
    
    @staticmethod
    def bullet(actual, target, ranges, title=None, figsize=(5, 1.2), transparent=True):
        """Create a bullet chart."""
        fig, ax = plt.subplots(figsize=figsize)
        if transparent:
            fig.patch.set_alpha(0)
            ax.set_facecolor('none')
        else:
            fig.patch.set_facecolor('white')
            ax.set_facecolor('white')
        
        range_colors = ['#E8E8E8', '#D0D0D0', '#B8B8B8']
        prev = 0
        for i, r in enumerate(ranges):
            ax.barh(0, r - prev, left=prev, height=0.5, color=range_colors[i], edgecolor='none')
            prev = r
        
        ax.barh(0, actual, height=0.22, color=IBColors.NAVY, edgecolor='none')
        ax.plot([target, target], [-0.3, 0.3], color=IBColors.RED, linewidth=3)
        
        ax.set_xlim(0, max(ranges) * 1.05)
        ax.set_ylim(-0.5, 0.5)
        ax.axis('off')
        
        if title:
            ax.set_title(title, fontsize=11, fontweight='bold',
                        color=IBColors.NAVY, loc='left', pad=8)
        
        plt.tight_layout(pad=1)
        return fig
    
    @staticmethod
    def heatmap(row_labels, col_labels, values, title=None, figsize=(5, 4),
                cmap='RdYlGn', show_values=True, transparent=True):
        """Create a heatmap."""
        fig, ax = plt.subplots(figsize=figsize)
        if transparent:
            fig.patch.set_alpha(0)
            ax.set_facecolor('none')
        else:
            fig.patch.set_facecolor('white')
            ax.set_facecolor('white')
        
        values = np.array(values)
        im = ax.imshow(values, cmap=cmap, aspect='auto')
        
        ax.set_xticks(np.arange(len(col_labels)))
        ax.set_yticks(np.arange(len(row_labels)))
        ax.set_xticklabels(col_labels)
        ax.set_yticklabels(row_labels)
        
        if show_values:
            thresh = np.mean(values)
            for i in range(len(row_labels)):
                for j in range(len(col_labels)):
                    val = values[i, j]
                    text_color = 'white' if val < thresh else 'black'
                    ax.text(j, i, f'{val:.0f}', ha='center', va='center',
                           fontsize=9, color=text_color, fontweight='bold')
        
        for edge in ax.spines.values():
            edge.set_visible(False)
        ax.set_xticks(np.arange(len(col_labels)+1)-.5, minor=True)
        ax.set_yticks(np.arange(len(row_labels)+1)-.5, minor=True)
        ax.grid(which="minor", color="white", linestyle='-', linewidth=2)
        ax.tick_params(which="minor", bottom=False, left=False)
        
        if title:
            ax.set_title(title, fontsize=11, fontweight='bold',
                        color=IBColors.NAVY, pad=15)
        
        plt.tight_layout(pad=1.5)
        return fig


class GridLayout:
    """Grid-based layout manager to prevent overlapping."""
    
    def __init__(self, width, height, rows=12, cols=12, margin=60, gutter=20):
        """
        Initialize grid layout.
        
        Args:
            width, height: Canvas dimensions in pixels
            rows, cols: Grid divisions
            margin: Page margin in pixels
            gutter: Space between grid cells
        """
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.margin = margin
        self.gutter = gutter
        
        # Calculate cell dimensions
        self.content_width = width - 2 * margin
        self.content_height = height - 2 * margin
        self.cell_width = (self.content_width - (cols - 1) * gutter) / cols
        self.cell_height = (self.content_height - (rows - 1) * gutter) / rows
        
        # Track occupied cells
        self.occupied = [[False] * cols for _ in range(rows)]
    
    def get_position(self, row, col, row_span=1, col_span=1):
        """
        Get pixel position for a grid cell.
        
        Args:
            row, col: Starting cell (0-indexed, top-left origin)
            row_span, col_span: Number of cells to span
            
        Returns:
            (x, y, width, height) in pixels
        """
        x = self.margin + col * (self.cell_width + self.gutter)
        y = self.margin + row * (self.cell_height + self.gutter)
        w = col_span * self.cell_width + (col_span - 1) * self.gutter
        h = row_span * self.cell_height + (row_span - 1) * self.gutter
        
        # Mark cells as occupied
        for r in range(row, min(row + row_span, self.rows)):
            for c in range(col, min(col + col_span, self.cols)):
                self.occupied[r][c] = True
        
        return (int(x), int(y), int(w), int(h))
    
    def is_available(self, row, col, row_span=1, col_span=1):
        """Check if cells are available."""
        for r in range(row, min(row + row_span, self.rows)):
            for c in range(col, min(col + col_span, self.cols)):
                if self.occupied[r][c]:
                    return False
        return True


class InfographicCanvas:
    """
    Main class for creating IB-professional infographics.
    Now with PNG transparency support and grid-based layout.
    """
    
    def __init__(self, output_path, title, subtitle=None, 
                 size='landscape_1080p', transparent=True, bg_color=None):
        """
        Initialize the infographic canvas.
        
        Args:
            output_path: Path for output (PNG or PDF)
            title: Main headline
            subtitle: Optional subtitle
            size: 'landscape_1080p', 'landscape_4k', 'a3_landscape', 'letter_landscape'
            transparent: Whether background is transparent (PNG only)
            bg_color: Background color (overrides transparent)
        """
        self.output_path = output_path
        self.title = title
        self.subtitle = subtitle
        self.transparent = transparent and output_path.lower().endswith('.png')
        
        # Size presets (width, height in pixels)
        sizes = {
            'landscape_1080p': (1920, 1080),
            'landscape_4k': (3840, 2160),
            'a3_landscape': (4961, 3508),  # 300 DPI
            'letter_landscape': (3300, 2550),  # 300 DPI
            'slide_16_9': (1920, 1080),
            'slide_4_3': (1600, 1200),
        }
        self.width, self.height = sizes.get(size, (1920, 1080))
        
        # Initialize image
        if self.transparent:
            self.img = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        else:
            bg = IBColors.hex_to_rgb(bg_color) if bg_color else (255, 255, 255)
            self.img = Image.new('RGB', (self.width, self.height), bg)
        
        self.draw = ImageDraw.Draw(self.img)
        
        # Grid layout
        self.grid = GridLayout(self.width, self.height, rows=12, cols=12, margin=60, gutter=24)
        
        # Try to load fonts
        self._load_fonts()
        
        # Draw header
        self._draw_header()
    
    def _load_fonts(self):
        """Load system fonts with fallbacks."""
        font_paths = [
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
            '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
            '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
            '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
        ]
        
        self.fonts = {}
        try:
            self.fonts['title'] = ImageFont.truetype(font_paths[1], 42)
            self.fonts['subtitle'] = ImageFont.truetype(font_paths[0], 20)
            self.fonts['header'] = ImageFont.truetype(font_paths[1], 24)
            self.fonts['metric_value'] = ImageFont.truetype(font_paths[1], 48)
            self.fonts['metric_label'] = ImageFont.truetype(font_paths[0], 14)
            self.fonts['metric_delta'] = ImageFont.truetype(font_paths[1], 16)
            self.fonts['body'] = ImageFont.truetype(font_paths[0], 14)
            self.fonts['small'] = ImageFont.truetype(font_paths[0], 12)
            self.fonts['table_header'] = ImageFont.truetype(font_paths[1], 13)
            self.fonts['table_cell'] = ImageFont.truetype(font_paths[0], 12)
            self.fonts['takeaway'] = ImageFont.truetype(font_paths[0], 13)
            self.fonts['footer'] = ImageFont.truetype(font_paths[0], 11)
        except:
            # Fallback to default
            for key in ['title', 'subtitle', 'header', 'metric_value', 'metric_label',
                       'metric_delta', 'body', 'small', 'table_header', 'table_cell',
                       'takeaway', 'footer']:
                self.fonts[key] = ImageFont.load_default()
    
    def _draw_header(self):
        """Draw the headline and subtitle in row 0."""
        x, y, w, h = self.grid.get_position(0, 0, row_span=1, col_span=12)
        
        # Title
        self.draw.text((x, y + 10), self.title, 
                      font=self.fonts['title'], fill=IBColors.hex_to_rgb(IBColors.NAVY))
        
        # Subtitle
        if self.subtitle:
            self.draw.text((x, y + 60), self.subtitle,
                          font=self.fonts['subtitle'], fill=IBColors.hex_to_rgb(IBColors.GRAY))
    
    def _draw_rounded_rect(self, x, y, w, h, radius=12, fill=None, outline=None, outline_width=1):
        """Draw a rounded rectangle."""
        if fill:
            fill_color = IBColors.hex_to_rgba(fill) if isinstance(fill, str) else fill
            # Draw rounded rectangle using multiple shapes
            self.draw.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=fill_color)
        if outline:
            outline_color = IBColors.hex_to_rgb(outline) if isinstance(outline, str) else outline
            self.draw.rounded_rectangle([x, y, x + w, y + h], radius=radius, 
                                        outline=outline_color, width=outline_width)
    
    def add_hero_metric(self, value, label, delta=None, delta_positive=True,
                        row=1, col=0, row_span=2, col_span=2):
        """
        Add a hero metric card.
        
        Args:
            value: The main metric value (string)
            label: Label describing the metric
            delta: Optional change indicator
            delta_positive: Whether delta is positive
            row, col: Grid position
            row_span, col_span: Grid span
        """
        x, y, w, h = self.grid.get_position(row, col, row_span, col_span)
        
        # Card background
        self._draw_rounded_rect(x, y, w, h, radius=10, fill=IBColors.LIGHT_FILL)
        
        # Left accent bar
        accent_color = IBColors.NAVY
        self.draw.rectangle([x, y + 10, x + 4, y + h - 10], fill=IBColors.hex_to_rgb(accent_color))
        
        # Value
        self.draw.text((x + 20, y + 20), value,
                      font=self.fonts['metric_value'], fill=IBColors.hex_to_rgb(IBColors.NAVY))
        
        # Label
        self.draw.text((x + 20, y + 80), label,
                      font=self.fonts['metric_label'], fill=IBColors.hex_to_rgb(IBColors.GRAY))
        
        # Delta
        if delta:
            delta_color = IBColors.GREEN if delta_positive else IBColors.RED
            arrow = '▲' if delta_positive else '▼'
            self.draw.text((x + 20, y + h - 35), f'{arrow} {delta}',
                          font=self.fonts['metric_delta'], fill=IBColors.hex_to_rgb(delta_color))
    
    def add_chart(self, fig, row=1, col=2, row_span=5, col_span=6):
        """
        Add a matplotlib figure to the canvas, preserving aspect ratio.
        
        Args:
            fig: matplotlib Figure object
            row, col: Grid position
            row_span, col_span: Grid span
        """
        x, y, w, h = self.grid.get_position(row, col, row_span, col_span)
        
        # Convert figure to image
        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=150, bbox_inches='tight',
                   facecolor='none' if self.transparent else 'white', 
                   edgecolor='none', transparent=self.transparent)
        buf.seek(0)
        chart_img = Image.open(buf)
        
        # Preserve aspect ratio
        orig_w, orig_h = chart_img.size
        aspect_ratio = orig_w / orig_h
        
        # Calculate new size that fits within the grid cell
        if w / h > aspect_ratio:
            # Cell is wider than image - fit to height
            new_h = h
            new_w = int(h * aspect_ratio)
        else:
            # Cell is taller than image - fit to width
            new_w = w
            new_h = int(w / aspect_ratio)
        
        chart_img = chart_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        # Center the chart in the grid cell
        paste_x = x + (w - new_w) // 2
        paste_y = y + (h - new_h) // 2
        
        # Paste onto canvas
        if chart_img.mode == 'RGBA':
            self.img.paste(chart_img, (paste_x, paste_y), chart_img)
        else:
            self.img.paste(chart_img, (paste_x, paste_y))
        
        plt.close(fig)
    
    def add_takeaways(self, items, row=1, col=9, row_span=4, col_span=3, title="Key Takeaways"):
        """
        Add a key takeaways box.
        
        Args:
            items: List of takeaway strings
            row, col: Grid position
            row_span, col_span: Grid span
            title: Box title
        """
        x, y, w, h = self.grid.get_position(row, col, row_span, col_span)
        
        # Background
        self._draw_rounded_rect(x, y, w, h, radius=10, fill=IBColors.LIGHT_FILL)
        
        # Title
        self.draw.text((x + 16, y + 16), title,
                      font=self.fonts['header'], fill=IBColors.hex_to_rgb(IBColors.NAVY))
        
        # Divider line
        self.draw.line([(x + 16, y + 50), (x + w - 16, y + 50)], 
                      fill=IBColors.hex_to_rgb(IBColors.LIGHT_GRAY), width=1)
        
        # Items
        item_y = y + 65
        line_height = 28
        for item in items:
            # Bullet
            self.draw.ellipse([x + 16, item_y + 4, x + 24, item_y + 12],
                             fill=IBColors.hex_to_rgb(IBColors.NAVY))
            # Text
            self.draw.text((x + 32, item_y), item,
                          font=self.fonts['takeaway'], fill=IBColors.hex_to_rgb(IBColors.GRAY))
            item_y += line_height
    
    def add_table(self, headers, rows, row=7, col=0, row_span=4, col_span=5,
                  col_widths=None, row_height=32, header_height=36):
        """
        Add a compact data table with proportional sizing.
        
        Args:
            headers: List of header strings
            rows: List of row data (list of lists)
            row, col: Grid position
            row_span, col_span: Grid span
            col_widths: Optional list of column widths
            row_height: Height of each data row
            header_height: Height of header row
        """
        x, y, w, h = self.grid.get_position(row, col, row_span, col_span)
        
        n_cols = len(headers)
        n_rows = len(rows)
        
        # Calculate column widths based on content if not provided
        if col_widths is None:
            col_widths = []
            for col_idx in range(n_cols):
                max_width = self.draw.textbbox((0, 0), headers[col_idx], font=self.fonts['table_header'])[2]
                for row_data in rows:
                    if col_idx < len(row_data):
                        text_width = self.draw.textbbox((0, 0), str(row_data[col_idx]), font=self.fonts['table_cell'])[2]
                        max_width = max(max_width, text_width)
                col_widths.append(max_width + 24)
        
        # Calculate actual table dimensions
        table_width = sum(col_widths)
        table_height = header_height + n_rows * row_height
        
        # Center table in grid cell
        table_x = x + (w - table_width) // 2 if table_width < w else x
        table_y = y + (h - table_height) // 2 if table_height < h else y
        
        # Scale down if needed
        if table_width > w:
            scale = w / table_width
            col_widths = [int(cw * scale) for cw in col_widths]
            table_width = sum(col_widths)
            table_x = x
        
        # Header background
        self._draw_rounded_rect(table_x, table_y, table_width, header_height, radius=6, fill=IBColors.NAVY)
        
        # Header text
        current_x = table_x
        for i, header in enumerate(headers):
            self.draw.text((current_x + 12, table_y + 10), header,
                          font=self.fonts['table_header'], fill=(255, 255, 255))
            current_x += col_widths[i]
        
        # Data rows
        for row_idx, row_data in enumerate(rows):
            row_y = table_y + header_height + row_idx * row_height
            
            # Alternating background
            bg_color = IBColors.LIGHT_FILL if row_idx % 2 == 0 else IBColors.WHITE
            self.draw.rectangle([table_x, row_y, table_x + table_width, row_y + row_height],
                               fill=IBColors.hex_to_rgb(bg_color))
            
            # Row text
            current_x = table_x
            for col_idx, cell in enumerate(row_data):
                # Color for positive/negative
                if isinstance(cell, str):
                    if cell.startswith('+'):
                        text_color = IBColors.GREEN
                    elif cell.startswith('-') and not cell.startswith('-$'):
                        text_color = IBColors.RED
                    else:
                        text_color = IBColors.BLACK
                else:
                    text_color = IBColors.BLACK
                
                self.draw.text((current_x + 12, row_y + 8), str(cell),
                              font=self.fonts['table_cell'], fill=IBColors.hex_to_rgb(text_color))
                current_x += col_widths[col_idx] if col_idx < len(col_widths) else col_widths[-1]
        
        # Border
        total_height = header_height + n_rows * row_height
        self._draw_rounded_rect(table_x, table_y, table_width, total_height, radius=6, outline=IBColors.LIGHT_GRAY)
    
    def add_section_title(self, title, row, col, col_span=4):
        """Add a section title."""
        x, y, w, h = self.grid.get_position(row, col, row_span=1, col_span=col_span)
        self.draw.text((x, y), title,
                      font=self.fonts['header'], fill=IBColors.hex_to_rgb(IBColors.NAVY))
    
    def add_footer(self, source, date, confidential=False):
        """Add footer with source and date."""
        x, y, w, h = self.grid.get_position(11, 0, row_span=1, col_span=12)
        
        # Divider line
        self.draw.line([(x, y), (x + w, y)], 
                      fill=IBColors.hex_to_rgb(IBColors.LIGHT_GRAY), width=1)
        
        # Source text
        self.draw.text((x, y + 10), f'Source: {source} | Data as of {date}',
                      font=self.fonts['footer'], fill=IBColors.hex_to_rgb(IBColors.GRAY))
        
        # Confidential
        if confidential:
            conf_text = 'CONFIDENTIAL'
            bbox = self.draw.textbbox((0, 0), conf_text, font=self.fonts['footer'])
            text_width = bbox[2] - bbox[0]
            self.draw.text((x + w - text_width, y + 10), conf_text,
                          font=self.fonts['footer'], fill=IBColors.hex_to_rgb(IBColors.RED))
    
    def add_kpi_row(self, kpis, row=1, col=0, col_span=12):
        """
        Add a row of mini KPI cards.
        
        Args:
            kpis: List of dicts with 'value', 'label', 'delta', 'positive' keys
            row, col: Grid position
            col_span: Total span for all KPIs
        """
        n_kpis = len(kpis)
        kpi_col_span = col_span // n_kpis
        
        for i, kpi in enumerate(kpis):
            self.add_hero_metric(
                value=kpi['value'],
                label=kpi['label'],
                delta=kpi.get('delta'),
                delta_positive=kpi.get('positive', True),
                row=row,
                col=col + i * kpi_col_span,
                row_span=2,
                col_span=kpi_col_span
            )
    
    def save(self):
        """Save the infographic."""
        if self.output_path.lower().endswith('.png'):
            self.img.save(self.output_path, 'PNG')
        elif self.output_path.lower().endswith('.pdf'):
            # Convert to PDF
            rgb_img = self.img.convert('RGB') if self.img.mode == 'RGBA' else self.img
            rgb_img.save(self.output_path, 'PDF', resolution=150)
        else:
            self.img.save(self.output_path)
        
        print(f'Infographic saved to: {self.output_path}')


def create_sample_infographic(output_path='sample_infographic.png', transparent=True):
    """Create a sample infographic demonstrating all features."""
    
    # Initialize with transparent background
    canvas = InfographicCanvas(
        output_path=output_path,
        title="Q3 2024 Performance Summary: Revenue Growth Accelerating",
        subtitle="Enterprise Division | Quarterly Business Review",
        size='landscape_1080p',
        transparent=transparent
    )
    
    # Hero metrics (left column)
    canvas.add_hero_metric('$847M', 'Revenue', '+23% YoY', True, row=1, col=0, row_span=2, col_span=2)
    canvas.add_hero_metric('1,662', 'Customers', '+34% YoY', True, row=3, col=0, row_span=2, col_span=2)
    canvas.add_hero_metric('118%', 'Net Retention', '+6pp', True, row=5, col=0, row_span=2, col_span=2)
    
    # Waterfall chart (center)
    waterfall = IBCharts.waterfall(
        categories=["Q3'23", "New Logos", "Expansion", "Churn", "Q3'24"],
        values=[680, 120, 85, -38, 847],
        title="Revenue Bridge ($M)",
        transparent=transparent
    )
    canvas.add_chart(waterfall, row=1, col=2, row_span=5, col_span=5)
    
    # Donut chart (right of waterfall)
    donut = IBCharts.donut(
        labels=['North America', 'EMEA', 'APAC'],
        values=[55, 30, 15],
        title='Revenue by Region',
        center_label='$847M\nTotal',
        transparent=transparent
    )
    canvas.add_chart(donut, row=1, col=7, row_span=5, col_span=3)
    
    # Key takeaways (far right)
    canvas.add_takeaways([
        'Enterprise logos grew 34% YoY',
        'APAC expansion driving 40% of new ARR',
        'Net revenue retention at all-time high',
        'Product-led growth up 25%'
    ], row=1, col=10, row_span=5, col_span=2)
    
    # Line chart (bottom left)
    line = IBCharts.line_area(
        x_labels=['Q1', 'Q2', 'Q3', 'Q4 Est'],
        y_values=[720, 765, 847, 920],
        title='Quarterly Revenue Trend ($M)',
        transparent=transparent
    )
    canvas.add_chart(line, row=7, col=0, row_span=4, col_span=5)
    
    # Table (bottom center)
    canvas.add_table(
        headers=['Metric', "Q3'23", "Q3'24", 'Change'],
        rows=[
            ['Revenue', '$680M', '$847M', '+24.6%'],
            ['Customers', '1,240', '1,662', '+34.0%'],
            ['NRR', '112%', '118%', '+6pp'],
            ['ARR/Customer', '$548K', '$510K', '-7.0%'],
        ],
        row=7, col=5, row_span=4, col_span=4
    )
    
    # Heatmap (bottom right)
    heatmap = IBCharts.heatmap(
        row_labels=['Q1', 'Q2', 'Q3', 'Q4'],
        col_labels=['NA', 'EMEA', 'APAC'],
        values=[[80, 60, 40], [85, 65, 50], [90, 70, 55], [95, 75, 60]],
        title='Regional Performance Index',
        transparent=transparent
    )
    canvas.add_chart(heatmap, row=7, col=9, row_span=4, col_span=3)
    
    # Footer
    canvas.add_footer('Internal Finance Data', 'September 30, 2024', confidential=True)
    
    # Save
    canvas.save()
    return canvas


if __name__ == '__main__':
    # Create both transparent PNG and white background versions
    create_sample_infographic('sample_infographic_transparent.png', transparent=True)
    create_sample_infographic('sample_infographic_white.png', transparent=False)
