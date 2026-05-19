# Audiologic Analysis
Analysis written by Oskar Gyllenör. Audiologist, Software Test Engineer and rookie AI Software Engineer.

## About the Dataset
This dataset comes from a clinical validation study of the PAHRE (*Prueba Auditiva de Habla en Ruido en Espanol*) test, a Spanish study designed to measure how well people understand speech when background babble noise is present. <br> The study also investigates the Lombard effect, comparing test results using standard speech versus Lombard speech.

## How to Run the Notebook
1. Ensure you have the raw dataset (`test_data.sav`) located in the same directory as the notebook.
2. Open `notebook.ipynb` in your preferred Jupyter Notebook environment (e.g., DataSpell, JupyterLab, VS Code).
3. Select your Python environment/kernel.
4. Run all cells from top to bottom. The notebook is designed to execute sequentially without errors.

## Required Environment & Packages
To run this analysis, you need Python 3 installed along with the following packages:

- `pandas` (for data manipulation)
- `numpy` (for numerical calculations)
- `matplotlib` (for data visualization)
- `pyreadstat` (required by pandas `read_spss()` to read `.sav` files)

You can install these dependencies using pip:

    pip install pandas numpy matplotlib pyreadstat
