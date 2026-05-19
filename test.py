import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Testing SPSS file loading...")
try:
    # Läser in SPSS-filen
    df = pd.read_spss('data/test_data.sav')
    
    print(f"Rader och kolumner: {df.shape}")
    print("\n--- DataFrame Head ---")
    print(df.head())
    
    print("\n--- DataFrame Info ---")
    df.info()
    
    print("\nFungerar!")
except Exception as e:
    print(f"\nError occurred...WHAT THE: {e}")
