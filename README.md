# Generalized Brocard–Ramanujan Problem: Magnitude-Curve Visualization

This repository contains the Python code to reproduce the magnitude curve visualization from the paper:

**Perfect Squares from Sums of Consecutive Factorials: Discovery of an Exceptional Solution to a Generalized Brocard-Ramanujan Problem**

### Pre-print (Zenodo) : [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17137045.svg)](https://doi.org/10.5281/zenodo.17137045)
* **DOI** - 10.5281/zenodo.17137045
* **URL** - https://doi.org/10.5281/zenodo.17137045

## Abstract
The classical Brocard-Ramanujan problem, $n!+1=k^{2}$, is a long-standing open problem in number theory. This work explores the generalized Diophantine equation $\sum_{i=0}^{a}(n+i)!+1=k^{2}$. The paper reports the discovery of a remarkable new solution, $(n,k,a)=(4,215,4)$, found through systematic computational search. This script can be used to reproduce the theoretical magnitude curve plot (Figure 1) presented in the paper, which visualizes all seven known solutions.

## Features
The code includes:
- Generation of the theoretical magnitude curve for the generalized Brocard-Ramanujan problem.
- Plotting of all seven known integer solutions, sourced from the paper's Table 1.
- Clear visual distinction between solution types: Brocard-Ramanujan (a=0), consecutive pairs (a=1), and the new discovery (a=4).
- Visualization of both the smooth theoretical approximation ($k \approx \sqrt{(n+a)!+1}$) and the discrete exact integer magnitude model ($k = \sqrt{\lfloor n+a \rfloor! + 1}$).

##Repository Contents
*`generate_magnitude_curve.py` : Core Python script for generating the plot.
*`magnitude_curve_refined.pdf` : The plot output comparing the known solutions against the theoretical curves.
*`README.md` : This documentation file.
*`requirements.txt` : List of Python dependencies required to run the code.

##Requirements
- Python 3.8+
- numpy, matplotlib

## Installation

1.  **Clone the repository:**
```
git clone https://github.com/yourusername/generalized-brocard-ramanujan-magnitude-curve.git
cd generalized-brocard-ramanujan-magnitude-curve
```

2.  **Install the required dependency:**
```
pip install -r requirements.txt
```

## Usage
Run the script from the command line to generate the plot:
```
python generate_magnitude_curve.py
```
This will save the output as magnitude_curve_refined.png and magnitude_curve_refined.pdf in the root directory.

## Citation

If you use this work, please cite the paper using the Zenodo archive.

@misc{naladiga_venkat_2025_17137045,
  author       = {Naladiga Venkat, Arvind},
  title        = {Perfect Squares from Sums of Consecutive
                   Factorials: Discovery of an Exceptional Solution
                   to a Generalized Brocard-Ramanujan Problem
                  },
  month        = sep,
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17137045},
  url          = {https://doi.org/10.5281/zenodo.17137045},
}

---

## License

The content of this repository is dual-licensed:

- **MIT License** for `generate_magnitude_curve.py` See the [LICENSE](LICENSE) file for details.
- **CC BY 4.0** (Creative Commons Attribution 4.0 International) for all other content (results.txt, README, etc.)



## Author

- **Arvind N. Venkat** - [arvind.venkat01@gmail.com](mailto:arvind.venkat01@gmail.com)
