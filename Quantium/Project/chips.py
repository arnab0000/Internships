from ggplot import aes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
purchase_behaviour = pd.read_csv('QVI_purchase_behaviour.csv')
pb_df = purchase_behaviour.copy()
pb_df.dropna(inplace=True)
transaction_data = pd.read_excel('QVI_transaction_data.xlsx')
td_df = transaction_data.copy()
td_df.dropna(inplace=True)
result_df = pd.merge(td_df, pb_df, on=['LYLTY_CARD_NBR'])
print(result_df)