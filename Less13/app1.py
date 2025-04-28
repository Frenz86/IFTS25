import streamlit as st
import pandas as pd


def main():
    st.title("Data Transformation")
    uploaded_file = st.file_uploader("Choose a file",type={"xlsx"})
    df = pd.read_excel(uploaded_file)
    df1 = df.copy()
    df1['prezzo'] = 3.5
    df1['tot']  = df1['prezzo'] *df1['qtà']
    st.dataframe(df1)

    st.write('il totale di magazzino è:',df1['tot'].sum())
    if st.button('convert csv'):
        df1.to_csv('test.csv',index=False)

if __name__ =='__main__':
    main()