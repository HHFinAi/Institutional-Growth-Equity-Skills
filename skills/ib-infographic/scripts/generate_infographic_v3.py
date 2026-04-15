#!/usr/bin/env python3
"""
IB-Professional Infographic Generator v3.0
Enhanced with gradients, circular progress rings, dark theme, callout lines,
and modern visual styling inspired by premium infographic designs.
"""

import io
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Wedge, Circle, Arc, PathPatch
from matplotlib.path import Path
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patheffects as path_effects
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import colorsys


class IBColors:
    """Extended color palette with gradient support."""
    # Classic IB
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
    
    # Modern gradients (start, end)
    GRADIENT_PURPLE_CYAN = ('#8B5CF6', '#06B6D4')
    GRADIENT_ORANGE_PINK = ('#F97316', '#EC4899')
    GRADIENT_BLUE_PURPLE = ('#3B82F6', '#8B5CF6')
    GRADIENT_GREEN_TEAL = ('#10B981', '#14B8A6')
    GRADIENT_RED_ORANGE = ('#EF4444', '#F97316')
    GRADIENT_NAVY_BLUE = ('#1E3A5F', '#3B82F6')
    
    # Dark theme
    DARK_BG = '#0F172A'
    DARK_CARD = '#1E293B'
    DARK_BORDER = '#334155'
    DARK_TEXT = '#E2E8F0'
    DARK_MUTED = '#94A3B8'
    
    # Accent colors
    CYAN = '#06B6D4'
    PURPLE = '#8B5CF6'
    PINK = '#EC4899'
    ORANGE = '#F97316'
    TEAL = '#14B8A6'
    INDIGO = '#6366F1'
    
    @classmethod
    def hex_to_rgb(cls, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    @classmethod
    def hex_to_rgba(cls, hex_color, alpha=255):
        rgb = cls.hex_to_rgb(hex_color)
        return (*rgb, alpha)
    
    @classmethod
    def interpolate(cls, color1, color2, t):
        """Interpolate between two hex colors."""
        r1, g1, b1 = cls.hex_to_rgb(color1)
        r2, g2, b2 = cls.hex_to_rgb(color2)
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        return f'#{r:02x}{g:02x}{b:02x}'
    
    @classmethod
    def create_gradient_colors(cls, start_hex, end_hex, steps=10):
        """Create a list of gradient colors."""
        return [cls.interpolate(start_hex, end_hex, i/(steps-1)) for i in range(steps)]


class GradientDraw:
    """Helper class for drawing gradients on PIL images."""
    
    @staticmethod
    def horizontal_gradient(draw, img, x, y, w, h, color1, color2, radius=0):
        """Draw a horizontal gradient rectangle."""
        r1, g1, b1 = IBColors.hex_to_rgb(color1)
        r2, g2, b2 = IBColors.hex_to_rgb(color2)
        
        for i in range(int(w)):
            t = i / w
            r = int(r1 + (r2 - r1) * t)
            g = int(g1 + (g2 - g1) * t)
            b = int(b1 + (b2 - b1) * t)
            draw.line([(x + i, y), (x + i, y + h)], fill=(r, g, b))
    
    @staticmethod
    def vertical_gradient(draw, img, x, y, w, h, color1, color2):
        """Draw a vertical gradient rectangle."""
        r1, g1, b1 = IBColors.hex_to_rgb(color1)
        r2, g2, b2 = IBColors.hex_to_rgb(color2)
        
        for i in range(int(h)):
            t = i / h
            r = int(r1 + (r2 - r1) * t)
            g = int(g1 + (g2 - g1) * t)
            b = int(b1 + (b2 - b1) * t)
            draw.line([(x, y + i), (x + w, y + i)], fill=(r, g, b))
    
    @staticmethod
    def radial_gradient(img, center_x, center_y, radius, color1, color2):
        """Draw a radial gradient."""
        pixels = img.load()
        r1, g1, b1 = IBColors.hex_to_rgb(color1)
        r2, g2, b2 = IBColors.hex_to_rgb(color2)
        
        for y in range(max(0, int(center_y - radius)), min(img.height, int(center_y + radius))):
            for x in range(max(0, int(center_x - radius)), min(img.width, int(center_x + radius))):
                dist = math.sqrt((x - center_x)**2 + (y - center_y)**2)
                if dist <= radius:
                    t = dist / radius
                    r = int(r1 + (r2 - r1) * t)
                    g = int(g1 + (g2 - g1) * t)
                    b = int(b1 + (b2 - b1) * t)
                    if img.mode == 'RGBA':
                        pixels[x, y] = (r, g, b, 255)
                    else:
                        pixels[x, y] = (r, g, b)


class IBChartsV3:
    """Enhanced chart generators with gradients and modern styling."""
    
    @staticmethod
    def _get_gradient_cmap(color1, color2):
        """Create a matplotlib colormap from two colors."""
        c1 = np.array(IBColors.hex_to_rgb(color1)) / 255
        c2 = np.array(IBColors.hex_to_rgb(color2)) / 255
        colors = [c1, c2]
        return LinearSegmentedColormap.from_list('gradient', colors)
    
    @staticmethod
    def concentric_rings(values, labels, title=None, figsize=(4, 4), 
                         dark_theme=False, gradient_pairs=None):
        """
        Create concentric ring progress indicators.
        
        Args:
            values: List of percentages (0-100)
            labels: List of labels
            gradient_pairs: List of (start_color, end_color) tuples
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        bg_color = IBColors.DARK_BG if dark_theme else 'white'
        track_color = IBColors.DARK_CARD if dark_theme else '#E8E8E8'
        text_color = IBColors.DARK_TEXT if dark_theme else IBColors.NAVY
        
        fig.patch.set_facecolor(bg_color)
        ax.set_facecolor(bg_color)
        
        if gradient_pairs is None:
            gradient_pairs = [
                IBColors.GRADIENT_PURPLE_CYAN,
                IBColors.GRADIENT_ORANGE_PINK,
                IBColors.GRADIENT_BLUE_PURPLE,
            ]
        
        n_rings = len(values)
        ring_width = 0.15
        
        for i, (val, label) in enumerate(zip(values, labels)):
            radius = 1 - i * 0.25
            
            # Background track
            theta = np.linspace(0, 2*np.pi, 100)
            ax.plot(radius * np.cos(theta), radius * np.sin(theta),
                   color=track_color, linewidth=ring_width*100, solid_capstyle='round')
            
            # Progress arc with gradient effect
            progress_theta = np.linspace(np.pi/2, np.pi/2 - 2*np.pi*val/100, 50)
            
            # Create gradient by plotting multiple segments
            gradient = gradient_pairs[i % len(gradient_pairs)]
            colors = IBColors.create_gradient_colors(gradient[0], gradient[1], len(progress_theta))
            
            for j in range(len(progress_theta) - 1):
                ax.plot([radius * np.cos(progress_theta[j]), radius * np.cos(progress_theta[j+1])],
                       [radius * np.sin(progress_theta[j]), radius * np.sin(progress_theta[j+1])],
                       color=colors[j], linewidth=ring_width*100, solid_capstyle='round')
            
            # Percentage label
            ax.text(0, radius, f'{val:.0f}%', ha='center', va='center',
                   fontsize=10, fontweight='bold', color=text_color)
        
        # Center label
        if labels:
            ax.text(0, -0.15, labels[0] if len(labels) == 1 else 'METRICS',
                   ha='center', va='center', fontsize=8, color=text_color, alpha=0.7)
        
        ax.set_xlim(-1.3, 1.3)
        ax.set_ylim(-1.3, 1.3)
        ax.set_aspect('equal')
        ax.axis('off')
        
        if title:
            ax.set_title(title, fontsize=11, fontweight='bold', color=text_color, pad=10)
        
        plt.tight_layout()
        return fig
    
    @staticmethod
    def gradient_hbar(categories, values, title=None, figsize=(5, 3),
                      dark_theme=False, gradient=None):
        """Horizontal bar chart with gradient fills and rounded ends."""
        fig, ax = plt.subplots(figsize=figsize)
        
        bg_color = IBColors.DARK_BG if dark_theme else 'white'
        track_color = IBColors.DARK_CARD if dark_theme else '#E8E8E8'
        text_color = IBColors.DARK_TEXT if dark_theme else IBColors.NAVY
        label_color = IBColors.DARK_MUTED if dark_theme else IBColors.GRAY
        
        fig.patch.set_facecolor(bg_color)
        ax.set_facecolor(bg_color)
        
        if gradient is None:
            gradient = IBColors.GRADIENT_PURPLE_CYAN
        
        y_pos = np.arange(len(categories))
        max_val = max(values) * 1.1
        
        # Draw background tracks
        for i in range(len(categories)):
            ax.barh(i, max_val, height=0.5, color=track_color, 
                   left=0, edgecolor='none')
        
        # Draw gradient bars using multiple thin bars
        n_segments = 50
        for i, val in enumerate(values):
            segment_width = val / n_segments
            colors = IBColors.create_gradient_colors(gradient[0], gradient[1], n_segments)
            for j in range(n_segments):
                ax.barh(i, segment_width, height=0.5, left=j*segment_width,
                       color=colors[j], edgecolor='none')
        
        # Labels
        ax.set_yticks(y_pos)
        ax.set_yticklabels(categories, color=label_color, fontsize=10)
        ax.invert_yaxis()
        
        # Value labels
        for i, val in enumerate(values):
            ax.text(val + max_val*0.02, i, f'{val:.0f}%', va='center',
                   fontsize=10, fontweight='bold', color=text_color)
        
        ax.set_xlim(0, max_val)
        ax.axis('off')
        
        if title:
            ax.set_title(title, fontsize=11, fontweight='bold', color=text_color, 
                        loc='left', pad=15)
        
        plt.tight_layout()
        return fig
    
    @staticmethod
    def donut_with_callouts(labels, values, title=None, figsize=(5, 4),
                            dark_theme=False, center_text=None):
        """Donut chart with callout lines pointing to percentages."""
        fig, ax = plt.subplots(figsize=figsize)
        
        bg_color = IBColors.DARK_BG if dark_theme else 'white'
        text_color = IBColors.DARK_TEXT if dark_theme else IBColors.NAVY
        line_color = IBColors.DARK_MUTED if dark_theme else IBColors.GRAY
        
        fig.patch.set_facecolor(bg_color)
        ax.set_facecolor(bg_color)
        
        # Colors
        palette = [IBColors.PURPLE, IBColors.ORANGE, IBColors.CYAN, 
                  IBColors.PINK, IBColors.TEAL]
        colors = palette[:len(values)]
        
        # Create donut
        wedges, _ = ax.pie(values, colors=colors, startangle=90,
                          wedgeprops=dict(width=0.35, edgecolor=bg_color, linewidth=2))
        
        # Add callout lines and labels
        total = sum(values)
        cumsum = 0
        for i, (wedge, val, label) in enumerate(zip(wedges, values, labels)):
            # Calculate angle for callout
            angle = 90 - (cumsum + val/2) / total * 360
            angle_rad = math.radians(angle)
            
            # Inner and outer points
            inner_r = 0.65
            outer_r = 1.1
            text_r = 1.25
            
            x1 = inner_r * math.cos(angle_rad)
            y1 = inner_r * math.sin(angle_rad)
            x2 = outer_r * math.cos(angle_rad)
            y2 = outer_r * math.sin(angle_rad)
            x3 = text_r * math.cos(angle_rad)
            y3 = text_r * math.sin(angle_rad)
            
            # Draw callout line
            ax.plot([x1, x2], [y1, y2], color=colors[i], linewidth=1.5)
            ax.plot(x2, y2, 'o', color=colors[i], markersize=5)
            
            # Add label
            ha = 'left' if x3 > 0 else 'right'
            pct = val / total * 100
            ax.text(x3, y3, f'{pct:.0f}% {label}', ha=ha, va='center',
                   fontsize=9, color=text_color, fontweight='bold')
            
            cumsum += val
        
        # Center text
        if center_text:
            ax.text(0, 0.05, center_text.split('\n')[0] if '\n' in str(center_text) else center_text,
                   ha='center', va='center', fontsize=14, fontweight='bold', color=text_color)
            if '\n' in str(center_text):
                ax.text(0, -0.12, center_text.split('\n')[1], ha='center', va='center',
                       fontsize=9, color=line_color)
        
        ax.set_xlim(-1.6, 1.6)
        ax.set_ylim(-1.4, 1.4)
        ax.set_aspect('equal')
        ax.axis('off')
        
        if title:
            ax.set_title(title, fontsize=11, fontweight='bold', color=text_color, pad=10)
        
        plt.tight_layout()
        return fig
    
    @staticmethod
    def stacked_area(x_labels, data_dict, title=None, figsize=(6, 3),
                     dark_theme=False):
        """Smooth stacked area chart with gradient fills."""
        fig, ax = plt.subplots(figsize=figsize)
        
        bg_color = IBColors.DARK_BG if dark_theme else 'white'
        text_color = IBColors.DARK_TEXT if dark_theme else IBColors.NAVY
        grid_color = IBColors.DARK_BORDER if dark_theme else IBColors.VERY_LIGHT_GRAY
        
        fig.patch.set_facecolor(bg_color)
        ax.set_facecolor(bg_color)
        
        x = np.arange(len(x_labels))
        
        # Smooth the data with interpolation
        from scipy.interpolate import make_interp_spline
        x_smooth = np.linspace(0, len(x_labels)-1, 100)
        
        colors = [IBColors.PURPLE, IBColors.ORANGE, IBColors.CYAN]
        alphas = [0.8, 0.6, 0.4]
        
        prev_y = np.zeros(100)
        for i, (name, values) in enumerate(data_dict.items()):
            # Smooth interpolation
            try:
                spl = make_interp_spline(x, values, k=2)
                y_smooth = spl(x_smooth)
            except:
                y_smooth = np.interp(x_smooth, x, values)
            
            y_smooth = np.maximum(y_smooth, 0)
            
            ax.fill_between(x_smooth, prev_y, prev_y + y_smooth, 
                           color=colors[i % len(colors)], alpha=alphas[i % len(alphas)],
                           label=name)
            ax.plot(x_smooth, prev_y + y_smooth, color=colors[i % len(colors)], 
                   linewidth=2, alpha=0.9)
            
            prev_y = prev_y + y_smooth
        
        ax.set_xticks(x)
        ax.set_xticklabels(x_labels, color=text_color)
        ax.tick_params(colors=text_color)
        
        # Minimal styling
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(grid_color)
        ax.spines['bottom'].set_color(grid_color)
        ax.yaxis.grid(True, color=grid_color, linestyle=':', alpha=0.5)
        
        ax.legend(loc='upper left', frameon=False, fontsize=8)
        
        if title:
            ax.set_title(title, fontsize=11, fontweight='bold', color=text_color, 
                        loc='left', pad=10)
        
        plt.tight_layout()
        return fig
    
    @staticmethod
    def waterfall_gradient(categories, values, title=None, figsize=(6, 3.5),
                           dark_theme=False):
        """Waterfall chart with gradient fills."""
        fig, ax = plt.subplots(figsize=figsize)
        
        bg_color = IBColors.DARK_BG if dark_theme else 'white'
        text_color = IBColors.DARK_TEXT if dark_theme else IBColors.NAVY
        grid_color = IBColors.DARK_BORDER if dark_theme else IBColors.VERY_LIGHT_GRAY
        
        fig.patch.set_facecolor(bg_color)
        ax.set_facecolor(bg_color)
        
        n = len(values)
        cumulative = [0] * n
        
        running = 0
        bar_types = []  # 'total', 'positive', 'negative'
        
        for i, val in enumerate(values):
            if i == 0 or i == n - 1:
                cumulative[i] = 0
                bar_types.append('total')
            else:
                cumulative[i] = running
                bar_types.append('positive' if val >= 0 else 'negative')
            if i < n - 1:
                running += val if i > 0 else val
        
        # Draw bars with gradients
        for i, (val, cum, btype) in enumerate(zip(values, cumulative, bar_types)):
            if btype == 'total':
                color = IBColors.NAVY if not dark_theme else IBColors.INDIGO
            elif btype == 'positive':
                color = IBColors.GREEN if not dark_theme else IBColors.TEAL
            else:
                color = IBColors.RED if not dark_theme else IBColors.PINK
            
            ax.bar(i, val, bottom=cum, color=color, width=0.6, edgecolor='none')
            
            # Value label
            y_pos = cum + val/2
            label = f'{val:+,.0f}' if btype != 'total' else f'{val:,.0f}'
            ax.text(i, y_pos, label, ha='center', va='center', 
                   fontsize=9, fontweight='bold', color='white')
        
        # Connecting lines
        for i in range(n - 1):
            y_end = values[0] if i == 0 else cumulative[i] + values[i]
            ax.plot([i + 0.3, i + 0.7], [y_end, y_end],
                   color=grid_color, linewidth=1, linestyle='--')
        
        ax.set_xticks(range(n))
        ax.set_xticklabels(categories, color=text_color, fontsize=9)
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(grid_color)
        ax.spines['bottom'].set_color(grid_color)
        ax.tick_params(colors=text_color)
        ax.yaxis.grid(True, color=grid_color, linestyle=':', alpha=0.5)
        
        if title:
            ax.set_title(title, fontsize=11, fontweight='bold', color=text_color,
                        loc='left', pad=10)
        
        plt.tight_layout()
        return fig
    
    @staticmethod
    def grouped_bars_gradient(categories, data_dict, title=None, figsize=(6, 3.5),
                              dark_theme=False):
        """Grouped bar chart with gradient styling."""
        fig, ax = plt.subplots(figsize=figsize)
        
        bg_color = IBColors.DARK_BG if dark_theme else 'white'
        text_color = IBColors.DARK_TEXT if dark_theme else IBColors.NAVY
        grid_color = IBColors.DARK_BORDER if dark_theme else IBColors.VERY_LIGHT_GRAY
        
        fig.patch.set_facecolor(bg_color)
        ax.set_facecolor(bg_color)
        
        x = np.arange(len(categories))
        n_series = len(data_dict)
        width = 0.8 / n_series
        
        colors = [IBColors.CYAN, IBColors.PURPLE, IBColors.ORANGE, IBColors.PINK]
        
        for i, (name, values) in enumerate(data_dict.items()):
            offset = (i - n_series/2 + 0.5) * width
            bars = ax.bar(x + offset, values, width * 0.9, label=name,
                         color=colors[i % len(colors)], edgecolor='none')
        
        ax.set_xticks(x)
        ax.set_xticklabels(categories, color=text_color)
        ax.tick_params(colors=text_color)
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(grid_color)
        ax.spines['bottom'].set_color(grid_color)
        ax.yaxis.grid(True, color=grid_color, linestyle=':', alpha=0.5)
        
        ax.legend(loc='upper right', frameon=False, fontsize=8)
        
        if title:
            ax.set_title(title, fontsize=11, fontweight='bold', color=text_color,
                        loc='left', pad=10)
        
        plt.tight_layout()
        return fig


class GridLayout:
    """Grid-based layout manager."""
    
    def __init__(self, width, height, rows=12, cols=12, margin=60, gutter=20):
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.margin = margin
        self.gutter = gutter
        
        self.content_width = width - 2 * margin
        self.content_height = height - 2 * margin
        self.cell_width = (self.content_width - (cols - 1) * gutter) / cols
        self.cell_height = (self.content_height - (rows - 1) * gutter) / rows
        
        self.occupied = [[False] * cols for _ in range(rows)]
    
    def get_position(self, row, col, row_span=1, col_span=1):
        x = self.margin + col * (self.cell_width + self.gutter)
        y = self.margin + row * (self.cell_height + self.gutter)
        w = col_span * self.cell_width + (col_span - 1) * self.gutter
        h = row_span * self.cell_height + (row_span - 1) * self.gutter
        
        for r in range(row, min(row + row_span, self.rows)):
            for c in range(col, min(col + col_span, self.cols)):
                self.occupied[r][c] = True
        
        return (int(x), int(y), int(w), int(h))


class InfographicCanvasV3:
    """Enhanced infographic canvas with modern styling options."""
    
    def __init__(self, output_path, title, subtitle=None,
                 size='landscape_1080p', dark_theme=False, transparent=False):
        self.output_path = output_path
        self.title = title
        self.subtitle = subtitle
        self.dark_theme = dark_theme
        self.transparent = transparent and output_path.lower().endswith('.png') and not dark_theme
        
        sizes = {
            'landscape_1080p': (1920, 1080),
            'landscape_4k': (3840, 2160),
            'a3_landscape': (4961, 3508),
            'letter_landscape': (3300, 2550),
            'slide_16_9': (1920, 1080),
        }
        self.width, self.height = sizes.get(size, (1920, 1080))
        
        # Colors based on theme
        if dark_theme:
            self.bg_color = IBColors.hex_to_rgb(IBColors.DARK_BG)
            self.card_color = IBColors.DARK_CARD
            self.text_color = IBColors.DARK_TEXT
            self.muted_color = IBColors.DARK_MUTED
            self.border_color = IBColors.DARK_BORDER
            self.accent_color = IBColors.CYAN
        else:
            self.bg_color = (255, 255, 255)
            self.card_color = IBColors.LIGHT_FILL
            self.text_color = IBColors.NAVY
            self.muted_color = IBColors.GRAY
            self.border_color = IBColors.LIGHT_GRAY
            self.accent_color = IBColors.BLUE
        
        # Initialize image
        if self.transparent:
            self.img = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        else:
            self.img = Image.new('RGB', (self.width, self.height), self.bg_color)
        
        self.draw = ImageDraw.Draw(self.img)
        self.grid = GridLayout(self.width, self.height, rows=12, cols=12, margin=60, gutter=24)
        
        self._load_fonts()
        self._draw_header()
    
    def _load_fonts(self):
        font_paths = [
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
            '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
        ]
        
        self.fonts = {}
        try:
            self.fonts['title'] = ImageFont.truetype(font_paths[1], 42)
            self.fonts['subtitle'] = ImageFont.truetype(font_paths[0], 20)
            self.fonts['header'] = ImageFont.truetype(font_paths[1], 22)
            self.fonts['metric_value'] = ImageFont.truetype(font_paths[1], 44)
            self.fonts['metric_label'] = ImageFont.truetype(font_paths[0], 13)
            self.fonts['metric_delta'] = ImageFont.truetype(font_paths[1], 14)
            self.fonts['body'] = ImageFont.truetype(font_paths[0], 13)
            self.fonts['small'] = ImageFont.truetype(font_paths[0], 11)
            self.fonts['table_header'] = ImageFont.truetype(font_paths[1], 12)
            self.fonts['table_cell'] = ImageFont.truetype(font_paths[0], 11)
            self.fonts['badge'] = ImageFont.truetype(font_paths[1], 11)
            self.fonts['footer'] = ImageFont.truetype(font_paths[0], 10)
        except:
            for key in self.fonts:
                self.fonts[key] = ImageFont.load_default()
    
    def _draw_header(self):
        x, y, w, h = self.grid.get_position(0, 0, row_span=1, col_span=12)
        
        self.draw.text((x, y + 10), self.title,
                      font=self.fonts['title'], 
                      fill=IBColors.hex_to_rgb(self.text_color))
        
        if self.subtitle:
            self.draw.text((x, y + 58), self.subtitle,
                          font=self.fonts['subtitle'],
                          fill=IBColors.hex_to_rgb(self.muted_color))
    
    def _draw_rounded_rect(self, x, y, w, h, radius=12, fill=None, outline=None):
        if fill:
            fill_color = IBColors.hex_to_rgb(fill) if isinstance(fill, str) else fill
            self.draw.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=fill_color)
        if outline:
            outline_color = IBColors.hex_to_rgb(outline) if isinstance(outline, str) else outline
            self.draw.rounded_rectangle([x, y, x + w, y + h], radius=radius, outline=outline_color)
    
    def add_circular_metric(self, value, label, percentage, delta=None, delta_positive=True,
                            row=1, col=0, row_span=3, col_span=2, gradient=None):
        """Add a metric with circular progress ring."""
        x, y, w, h = self.grid.get_position(row, col, row_span, col_span)
        
        # Card background
        self._draw_rounded_rect(x, y, w, h, radius=12, fill=self.card_color)
        
        # Create circular progress ring
        ring_size = min(w - 40, h - 80)
        ring_img = Image.new('RGBA', (ring_size, ring_size), (0, 0, 0, 0))
        ring_draw = ImageDraw.Draw(ring_img)
        
        center = ring_size // 2
        outer_r = ring_size // 2 - 5
        inner_r = outer_r - 12
        
        # Background ring
        ring_draw.ellipse([5, 5, ring_size-5, ring_size-5], 
                         outline=IBColors.hex_to_rgb(self.border_color), width=12)
        
        # Progress arc
        if gradient is None:
            gradient = IBColors.GRADIENT_PURPLE_CYAN
        
        start_angle = -90
        end_angle = -90 + (percentage / 100) * 360
        
        # Draw progress arc
        ring_draw.arc([5, 5, ring_size-5, ring_size-5], start_angle, end_angle,
                     fill=IBColors.hex_to_rgb(gradient[0]), width=12)
        
        # Paste ring
        ring_x = x + (w - ring_size) // 2
        ring_y = y + 15
        self.img.paste(ring_img, (ring_x, ring_y), ring_img)
        
        # Value in center
        bbox = self.draw.textbbox((0, 0), value, font=self.fonts['metric_value'])
        text_w = bbox[2] - bbox[0]
        self.draw.text((x + (w - text_w) // 2, ring_y + ring_size//2 - 25), value,
                      font=self.fonts['metric_value'],
                      fill=IBColors.hex_to_rgb(self.text_color))
        
        # Label below ring
        bbox = self.draw.textbbox((0, 0), label, font=self.fonts['metric_label'])
        text_w = bbox[2] - bbox[0]
        self.draw.text((x + (w - text_w) // 2, ring_y + ring_size + 5), label,
                      font=self.fonts['metric_label'],
                      fill=IBColors.hex_to_rgb(self.muted_color))
        
        # Delta
        if delta:
            delta_color = IBColors.GREEN if delta_positive else IBColors.RED
            arrow = '▲' if delta_positive else '▼'
            delta_text = f'{arrow} {delta}'
            bbox = self.draw.textbbox((0, 0), delta_text, font=self.fonts['metric_delta'])
            text_w = bbox[2] - bbox[0]
            self.draw.text((x + (w - text_w) // 2, ring_y + ring_size + 25), delta_text,
                          font=self.fonts['metric_delta'],
                          fill=IBColors.hex_to_rgb(delta_color))
    
    def add_hero_metric(self, value, label, delta=None, delta_positive=True,
                        row=1, col=0, row_span=2, col_span=2):
        """Add a hero metric card."""
        x, y, w, h = self.grid.get_position(row, col, row_span, col_span)
        
        self._draw_rounded_rect(x, y, w, h, radius=10, fill=self.card_color)
        
        # Accent bar
        accent = IBColors.CYAN if self.dark_theme else IBColors.NAVY
        self.draw.rectangle([x, y + 10, x + 4, y + h - 10], fill=IBColors.hex_to_rgb(accent))
        
        # Value
        self.draw.text((x + 18, y + 15), value,
                      font=self.fonts['metric_value'],
                      fill=IBColors.hex_to_rgb(self.text_color))
        
        # Label
        self.draw.text((x + 18, y + 70), label,
                      font=self.fonts['metric_label'],
                      fill=IBColors.hex_to_rgb(self.muted_color))
        
        # Delta
        if delta:
            delta_color = IBColors.GREEN if delta_positive else IBColors.RED
            if self.dark_theme:
                delta_color = IBColors.TEAL if delta_positive else IBColors.PINK
            arrow = '▲' if delta_positive else '▼'
            self.draw.text((x + 18, y + h - 30), f'{arrow} {delta}',
                          font=self.fonts['metric_delta'],
                          fill=IBColors.hex_to_rgb(delta_color))
    
    def add_numbered_badge(self, number, text, row, col, col_span=3, gradient=None):
        """Add a numbered pill badge."""
        x, y, w, h = self.grid.get_position(row, col, row_span=1, col_span=col_span)
        
        if gradient is None:
            gradient = IBColors.GRADIENT_PURPLE_CYAN
        
        # Pill background with gradient
        pill_h = 36
        self._draw_rounded_rect(x, y, w, pill_h, radius=18, fill=gradient[0])
        
        # Number circle
        circle_r = 14
        self.draw.ellipse([x + 8, y + 4, x + 8 + circle_r*2, y + 4 + circle_r*2],
                         fill=(255, 255, 255))
        
        # Number
        num_text = str(number).zfill(2)
        bbox = self.draw.textbbox((0, 0), num_text, font=self.fonts['badge'])
        num_w = bbox[2] - bbox[0]
        self.draw.text((x + 8 + circle_r - num_w//2, y + 9), num_text,
                      font=self.fonts['badge'],
                      fill=IBColors.hex_to_rgb(gradient[0]))
        
        # Text
        self.draw.text((x + 45, y + 10), text,
                      font=self.fonts['body'],
                      fill=(255, 255, 255))
    
    def add_chart(self, fig, row=1, col=2, row_span=5, col_span=6):
        """Add a matplotlib figure, preserving aspect ratio."""
        x, y, w, h = self.grid.get_position(row, col, row_span, col_span)
        
        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=150, bbox_inches='tight',
                   facecolor=fig.get_facecolor(), edgecolor='none')
        buf.seek(0)
        chart_img = Image.open(buf)
        
        # Preserve aspect ratio
        orig_w, orig_h = chart_img.size
        aspect_ratio = orig_w / orig_h
        
        # Calculate new size that fits within the grid cell
        if w / h > aspect_ratio:
            # Cell is wider than image aspect ratio - fit to height
            new_h = h
            new_w = int(h * aspect_ratio)
        else:
            # Cell is taller than image aspect ratio - fit to width
            new_w = w
            new_h = int(w / aspect_ratio)
        
        chart_img = chart_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        # Center the chart in the grid cell
        paste_x = x + (w - new_w) // 2
        paste_y = y + (h - new_h) // 2
        
        if chart_img.mode == 'RGBA':
            self.img.paste(chart_img, (paste_x, paste_y), chart_img)
        else:
            self.img.paste(chart_img, (paste_x, paste_y))
        
        plt.close(fig)
    
    def add_takeaways(self, items, row=1, col=9, row_span=4, col_span=3, title="Key Takeaways"):
        """Add key takeaways box."""
        x, y, w, h = self.grid.get_position(row, col, row_span, col_span)
        
        self._draw_rounded_rect(x, y, w, h, radius=10, fill=self.card_color)
        
        self.draw.text((x + 16, y + 14), title,
                      font=self.fonts['header'],
                      fill=IBColors.hex_to_rgb(self.text_color))
        
        self.draw.line([(x + 16, y + 48), (x + w - 16, y + 48)],
                      fill=IBColors.hex_to_rgb(self.border_color), width=1)
        
        item_y = y + 60
        for i, item in enumerate(items):
            # Numbered circle
            circle_color = IBColors.CYAN if self.dark_theme else IBColors.NAVY
            self.draw.ellipse([x + 14, item_y + 2, x + 28, item_y + 16],
                             fill=IBColors.hex_to_rgb(circle_color))
            
            num_text = str(i + 1)
            self.draw.text((x + 18, item_y + 1), num_text,
                          font=self.fonts['small'], fill=(255, 255, 255))
            
            self.draw.text((x + 36, item_y), item,
                          font=self.fonts['body'],
                          fill=IBColors.hex_to_rgb(self.muted_color))
            item_y += 28
    
    def add_table(self, headers, rows, row=7, col=0, row_span=4, col_span=5,
                  col_widths=None, row_height=30, header_height=34):
        """Add a data table with proportional sizing."""
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
        
        # Header
        header_color = IBColors.INDIGO if self.dark_theme else IBColors.NAVY
        self._draw_rounded_rect(table_x, table_y, table_width, header_height, radius=6, fill=header_color)
        
        current_x = table_x
        for i, header in enumerate(headers):
            self.draw.text((current_x + 10, table_y + 8), header,
                          font=self.fonts['table_header'], fill=(255, 255, 255))
            current_x += col_widths[i]
        
        # Rows
        for row_idx, row_data in enumerate(rows):
            row_y = table_y + header_height + row_idx * row_height
            
            bg = self.card_color if row_idx % 2 == 0 else (self.bg_color if isinstance(self.bg_color, tuple) 
                                                           else IBColors.hex_to_rgb(self.bg_color))
            self.draw.rectangle([table_x, row_y, table_x + table_width, row_y + row_height],
                               fill=IBColors.hex_to_rgb(bg) if isinstance(bg, str) else bg)
            
            current_x = table_x
            for col_idx, cell in enumerate(row_data):
                text_color = self.text_color
                if isinstance(cell, str):
                    if cell.startswith('+'):
                        text_color = IBColors.TEAL if self.dark_theme else IBColors.GREEN
                    elif cell.startswith('-') and '%' in cell:
                        text_color = IBColors.PINK if self.dark_theme else IBColors.RED
                
                self.draw.text((current_x + 10, row_y + 7), str(cell),
                              font=self.fonts['table_cell'],
                              fill=IBColors.hex_to_rgb(text_color))
                current_x += col_widths[col_idx] if col_idx < len(col_widths) else col_widths[-1]
        
        total_h = header_height + n_rows * row_height
        self._draw_rounded_rect(table_x, table_y, table_width, total_h, radius=6, outline=self.border_color)
    
    def add_footer(self, source, date, confidential=False):
        """Add footer."""
        x, y, w, h = self.grid.get_position(11, 0, row_span=1, col_span=12)
        
        self.draw.line([(x, y), (x + w, y)],
                      fill=IBColors.hex_to_rgb(self.border_color), width=1)
        
        self.draw.text((x, y + 8), f'Source: {source} | Data as of {date}',
                      font=self.fonts['footer'],
                      fill=IBColors.hex_to_rgb(self.muted_color))
        
        if confidential:
            conf_color = IBColors.PINK if self.dark_theme else IBColors.RED
            bbox = self.draw.textbbox((0, 0), 'CONFIDENTIAL', font=self.fonts['footer'])
            text_w = bbox[2] - bbox[0]
            self.draw.text((x + w - text_w, y + 8), 'CONFIDENTIAL',
                          font=self.fonts['footer'],
                          fill=IBColors.hex_to_rgb(conf_color))
    
    def save(self):
        if self.output_path.lower().endswith('.png'):
            self.img.save(self.output_path, 'PNG')
        elif self.output_path.lower().endswith('.pdf'):
            rgb_img = self.img.convert('RGB') if self.img.mode == 'RGBA' else self.img
            rgb_img.save(self.output_path, 'PDF', resolution=150)
        else:
            self.img.save(self.output_path)
        
        print(f'Infographic saved to: {self.output_path}')


def create_dark_theme_sample(output_path='infographic_dark.png'):
    """Create a dark theme infographic sample."""
    
    canvas = InfographicCanvasV3(
        output_path=output_path,
        title="Q3 2024 Performance Dashboard",
        subtitle="Enterprise Division | Quarterly Business Review",
        size='landscape_1080p',
        dark_theme=True
    )
    
    # Circular metrics (top left)
    canvas.add_circular_metric('$847M', 'Revenue', 85, '+23%', True,
                               row=1, col=0, row_span=3, col_span=2,
                               gradient=IBColors.GRADIENT_PURPLE_CYAN)
    canvas.add_circular_metric('1,662', 'Customers', 72, '+34%', True,
                               row=1, col=2, row_span=3, col_span=2,
                               gradient=IBColors.GRADIENT_ORANGE_PINK)
    canvas.add_circular_metric('118%', 'NRR', 95, '+6pp', True,
                               row=1, col=4, row_span=3, col_span=2,
                               gradient=IBColors.GRADIENT_BLUE_PURPLE)
    
    # Donut with callouts (center)
    donut = IBChartsV3.donut_with_callouts(
        labels=['Comments', 'Likes', 'Shared'],
        values=[15, 50, 35],
        title='Engagement Breakdown',
        dark_theme=True,
        center_text='VISITS\nTotal Engagement'
    )
    canvas.add_chart(donut, row=1, col=6, row_span=5, col_span=4)
    
    # Takeaways (right)
    canvas.add_takeaways([
        'Enterprise logos grew 34% YoY',
        'APAC driving 40% of new ARR',
        'Net retention at all-time high',
        'Product-led growth up 25%'
    ], row=1, col=10, row_span=5, col_span=2)
    
    # Gradient bars (bottom left)
    bars = IBChartsV3.gradient_hbar(
        categories=['North America', 'EMEA', 'APAC'],
        values=[55, 30, 15],
        title='Revenue by Region (%)',
        dark_theme=True
    )
    canvas.add_chart(bars, row=4, col=0, row_span=3, col_span=4)
    
    # Stacked area (bottom center)
    try:
        area = IBChartsV3.stacked_area(
            x_labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            data_dict={
                'Visits': [100, 120, 140, 130, 160, 180],
                'Likes': [50, 60, 70, 65, 80, 90],
                'Shared': [30, 40, 45, 50, 55, 60]
            },
            title='Monthly Trends',
            dark_theme=True
        )
        canvas.add_chart(area, row=7, col=0, row_span=4, col_span=5)
    except:
        pass
    
    # Table (bottom center-right)
    canvas.add_table(
        headers=['Metric', "Q3'23", "Q3'24", 'Change'],
        rows=[
            ['Revenue', '$680M', '$847M', '+24.6%'],
            ['Customers', '1,240', '1,662', '+34.0%'],
            ['NRR', '112%', '118%', '+6pp'],
            ['ARR/Cust', '$548K', '$510K', '-7.0%'],
        ],
        row=7, col=5, row_span=4, col_span=4
    )
    
    # Grouped bars (bottom right)
    grouped = IBChartsV3.grouped_bars_gradient(
        categories=['Q1', 'Q2', 'Q3', 'Q4'],
        data_dict={
            'This Year': [720, 765, 847, 920],
            'Last Year': [580, 620, 680, 710]
        },
        title='Revenue Comparison',
        dark_theme=True
    )
    canvas.add_chart(grouped, row=7, col=9, row_span=4, col_span=3)
    
    canvas.add_footer('Internal Finance Data', 'September 30, 2024', confidential=True)
    canvas.save()


def create_light_theme_sample(output_path='infographic_light.png'):
    """Create a light theme infographic sample."""
    
    canvas = InfographicCanvasV3(
        output_path=output_path,
        title="Q3 2024 Performance Summary",
        subtitle="Enterprise Division | Quarterly Business Review",
        size='landscape_1080p',
        dark_theme=False
    )
    
    # Hero metrics
    canvas.add_hero_metric('$847M', 'Revenue', '+23% YoY', True, row=1, col=0, row_span=2, col_span=2)
    canvas.add_hero_metric('1,662', 'Customers', '+34% YoY', True, row=3, col=0, row_span=2, col_span=2)
    canvas.add_hero_metric('118%', 'Net Retention', '+6pp', True, row=5, col=0, row_span=2, col_span=2)
    
    # Waterfall (center)
    waterfall = IBChartsV3.waterfall_gradient(
        categories=["Q3'23", "New Logos", "Expansion", "Churn", "Q3'24"],
        values=[680, 120, 85, -38, 847],
        title="Revenue Bridge ($M)",
        dark_theme=False
    )
    canvas.add_chart(waterfall, row=1, col=2, row_span=5, col_span=5)
    
    # Donut with callouts
    donut = IBChartsV3.donut_with_callouts(
        labels=['North America', 'EMEA', 'APAC'],
        values=[55, 30, 15],
        title='Revenue by Region',
        dark_theme=False,
        center_text='$847M\nTotal'
    )
    canvas.add_chart(donut, row=1, col=7, row_span=5, col_span=3)
    
    # Takeaways
    canvas.add_takeaways([
        'Enterprise logos grew 34% YoY',
        'APAC driving 40% of new ARR',
        'Net retention at all-time high',
        'Product-led growth up 25%'
    ], row=1, col=10, row_span=5, col_span=2)
    
    # Gradient bars
    bars = IBChartsV3.gradient_hbar(
        categories=['Product A', 'Product B', 'Product C', 'Product D'],
        values=[45, 30, 15, 10],
        title='Revenue Mix (%)',
        dark_theme=False,
        gradient=IBColors.GRADIENT_NAVY_BLUE
    )
    canvas.add_chart(bars, row=7, col=0, row_span=4, col_span=4)
    
    # Table
    canvas.add_table(
        headers=['Metric', "Q3'23", "Q3'24", 'Change'],
        rows=[
            ['Revenue', '$680M', '$847M', '+24.6%'],
            ['Customers', '1,240', '1,662', '+34.0%'],
            ['NRR', '112%', '118%', '+6pp'],
            ['ARR/Cust', '$548K', '$510K', '-7.0%'],
        ],
        row=7, col=4, row_span=4, col_span=4
    )
    
    # Concentric rings
    rings = IBChartsV3.concentric_rings(
        values=[85, 72, 65],
        labels=['Revenue', 'Customers', 'Pipeline'],
        title='Goal Attainment',
        dark_theme=False
    )
    canvas.add_chart(rings, row=7, col=8, row_span=4, col_span=4)
    
    canvas.add_footer('Internal Finance Data', 'September 30, 2024', confidential=True)
    canvas.save()


if __name__ == '__main__':
    create_dark_theme_sample('infographic_dark_v3.png')
    create_light_theme_sample('infographic_light_v3.png')
