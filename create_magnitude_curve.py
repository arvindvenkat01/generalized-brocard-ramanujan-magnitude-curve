"""
This script generates the theoretical magnitude curve plot from the paper:
"Perfect Squares from Sums of Consecutive Factorials: Discovery of an
Exceptional Solution to a Generalized Brocard-Ramanujan Problem" by
Arvind N. Venkat (2025).

The script visualizes the seven known integer solutions to the generalized
Brocard-Ramanujan Diophantine equation sum_{i=0 to a}(n+i)! + 1 = k^2
against two theoretical curves:
1. A smooth approximation based on the largest factorial term.
2. A discrete step-wise curve representing the exact integer magnitude model.

The final plot is saved as 'magnitude_curve_refined.png' and
'magnitude_curve_refined.pdf'.
"""

# MIT License
#
# Copyright (c) 2025 Arvind N. Venkat
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import matplotlib.pyplot as plt
import numpy as np
import math
from math import lgamma

def create_publication_figure_final():
    """
    Generate the final, publication-quality figure with refined aesthetics
    based on user feedback.
    """

    # Data for the seven known solutions from the paper's Table 1
    solutions = [(4, 5, 0), (5, 11, 0), (7, 71, 0),
                 (1, 2, 1), (2, 3, 1), (5, 29, 1),
                 (4, 215, 4)]

    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(10, 6.5))

    # --- Theoretical Curves ---
    x_range_continuous = np.linspace(0.9, 9.1, 1000)
    factorials = {i: math.factorial(i) for i in range(11)}

    # 1. Dashed Step Curve (Exact Integer Magnitude)
    # MODIFICATION: Linewidth reduced from 1.2 to 1.0 for a more subtle look.
    y_step = [np.log10(np.sqrt(factorials.get(int(x), 0) + 1)) for x in x_range_continuous]
    ax.plot(x_range_continuous, y_step, 'k--', linewidth=1.0, dashes=(4, 2),
            label=r'Exact Integer Magnitude: $k = \sqrt{\lfloor n+a \rfloor! + 1}$')

    # 2. Dotted Smooth Curve (Theoretical Approximation)
    # MODIFICATION: Changed linestyle to be finer dots, similar to the old figure.
    def get_log10_k_smooth(x_val):
        log_factorial = lgamma(x_val + 1)
        log_factorial_plus_1 = np.logaddexp(log_factorial, 0)
        log10_k = 0.5 * log_factorial_plus_1 / np.log(10)
        return log10_k
    y_smooth = [get_log10_k_smooth(x) for x in x_range_continuous]
    ax.plot(x_range_continuous, y_smooth, color='gray', linestyle=(0, (1, 1.5)),
            linewidth=1.5, label=r'Theoretical Approximation: $k \approx \sqrt{(n+a)!+1}$')

    # --- Plot the Actual Solutions ---
    markers = {0: 'o', 1: 's', 4: '^'}
    colors = {0: '#3498db', 1: '#2ecc71', 4: '#e74c3c'}
    sizes = {0: 90, 1: 90, 4: 130}
    labels = {0: 'Brocard-Ramanujan (a=0)', 1: 'Consecutive pairs (a=1)', 4: 'New discovery (a=4)'}

    plotted_labels = set()
    for n, k, a in solutions:
        x = n + a
        label_key = labels[a]
        label = label_key if label_key not in plotted_labels else None
        plotted_labels.add(label_key)

        ax.scatter(x, np.log10(k), marker=markers[a], c=colors[a],
                   s=sizes[a], edgecolors='black', linewidth=1.0,
                   zorder=5, label=label)

        # 3. Annotate k-values for each point
        # MODIFICATION: Using a single, consistent offset for all labels for symmetry.
        offset = (0, 8) # Places all labels directly above the point.
        ax.annotate(f'k={k}', (x, np.log10(k)),
                    xytext=offset, textcoords='offset points',
                    fontsize=9, ha='center', fontweight='bold')

    # --- Final Touches ---
    ax.set_xlabel(r'$x = n + a$ (index of largest factorial term)', fontsize=12)
    ax.set_ylabel(r'$\log_{10}(k)$', fontsize=12)
    ax.set_title('All Known Solutions Lie on the Theoretical Magnitude Curve',
                 fontsize=14, fontweight='bold')
    
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.legend(loc='upper left', frameon=True, fancybox=True,
              shadow=True, framealpha=1.0, title_fontsize='10')

    ax.set_xlim(0.5, 9.5)
    ax.set_ylim(-0.1, 2.6)
    ax.set_xticks(range(1, 10))

    ax.text(0.97, 0.03, 'Note: Curve shows necessary but not sufficient condition',
            transform=ax.transAxes, fontsize=8, ha='right',
            style='italic', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.6))

    plt.tight_layout()
    plt.savefig('magnitude_curve_refined.pdf', format='pdf', dpi=300)
    plt.savefig('magnitude_curve_refined.png', format='png', dpi=150)
    plt.show()

    print("Refined figure saved as 'magnitude_curve_refined.pdf' and 'magnitude_curve_refined.png'")

if __name__ == '__main__':
    create_publication_figure_final()