import streamlit as st
import pandas as pd
import io

def convert_to_excel(df):
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine="xlsxwriter")
    df.to_excel(writer, sheet_name="data",index=False)
    # see: https://xlsxwriter.readthedocs.io/working_with_pandas.html
    writer.close()
    return output.getvalue()

def main():
    st.title("Data Transformation")
    uploaded_file = st.file_uploader("Choose a file",type={"xlsx"})
    if uploaded_file is not None:
        ###### transformation #####################################
        df = pd.read_excel(uploaded_file)
        st.dataframe(df)


        if st.button('Start Processing', help="Process Dataframe"):
            st.header('Addes Column')
            df['new_col'] = 1
            st.dataframe(df)
            st.balloons()
            st.download_button(
                                label="download as Excel-file",
                                data=convert_to_excel(df),
                                file_name="data.xlsx",
                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                key="excel_download",
                                )
                
if __name__ == "__main__":
    main()