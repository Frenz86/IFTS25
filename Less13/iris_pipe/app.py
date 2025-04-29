import streamlit as st
import pandas as pd
import seaborn as sns
import joblib
import io

class_mapping = {'setosa': 0,
                'versicolor': 1,
                'virginica': 2
                }

@st.cache_data
def load_data():
    #df = pd.read_csv('iris.csv')
    df = sns.load_dataset('iris')
    df['species']= df['species'].map(class_mapping)
    loaded_model = joblib.load('iris_pipe.pkl')

    return df,loaded_model

def convert_to_excel(df):
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine="xlsxwriter")
    df.to_excel(writer, sheet_name="data",index=False)
    # see: https://xlsxwriter.readthedocs.io/working_with_pandas.html
    writer.close()
    return output.getvalue()

def main():
    st.title('Iris Dataset')
    df,loaded_model = load_data()
    st.dataframe(df)
    tab1, tab2,tab3 = st.tabs(["EDA", "Pred", "Batch"])
    with tab1:
        st.header("EDA")
        fig = sns.pairplot(df,hue='species')
        st.pyplot(fig)

    with tab2:
        st.header("Pred")

        sepal_lenght = st.slider('sepal lenght',0.0,6.5,2.5)
        sepal_width = st.slider('sepal width',0.0,6.5,2.5)
        petal_lenght = st.slider('petal lenght',0.0,6.5,0.5)
        petal_width = st.slider('petal width',0.0,6.5,0.5)

        data = {
                "sepal_length": [sepal_lenght],
                "sepal_width": [sepal_width],
                "petal_length": [petal_lenght],
                "petal_width": [petal_width],
                }

        input_df = pd.DataFrame(data)

        if st.button('prediction'):
            res = loaded_model.predict(input_df).astype(int)[0]
            classes = {0:'setosa',
                        1:'versicolor',
                        2:'virginica',
                            }
            y_pred = classes[res]
            st.success(y_pred)
    with tab3:
        st.header("Batch")  

        uploaded_file = st.file_uploader("Choose a file",type={"xlsx"})
        if uploaded_file is not None:
            ###### transformation #####################################
            df = pd.read_excel(uploaded_file)
            st.dataframe(df)


            if st.button('prediction_batch'):
                classes = {0:'setosa',
                            1:'versicolor',
                            2:'virginica',
                                }
                df['predicted_class'] = loaded_model.predict(df).astype(int)
                df['predicted_class'] = df['predicted_class'].map(classes)
                st.dataframe(df)
                
                st.balloons()
                st.download_button(
                                    label="download as Excel-file",
                                    data=convert_to_excel(df),
                                    file_name="classified.xlsx",
                                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                    key="excel_download",
                                    )



##############################################################

if __name__ == "__main__":
    main()




