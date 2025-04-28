import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_clean_data():
    """Carica e prepara il dataset delle mance"""
    tips = sns.load_dataset('tips')
    # Rinomina le colonne in italiano per una migliore comprensione
    column_names = {
                    'total_bill': 'Conto Totale',
                    'tip': 'Mancia',
                    'sex': 'Sesso',
                    'smoker': 'Fumatore',
                    'day': 'Giorno',
                    'time': 'Orario',
                    'size': 'Dimensione Gruppo'
                    }
    
    tips = tips.rename(columns=column_names)
    return tips

def create_pairplot(data, features, hue=None):
    """Crea un pairplot con le features selezionate"""
    #fig = plt.figure(figsize=(12,12))
    fig = sns.pairplot(data[features], hue=hue, diag_kind='kde',height=1.5)
    #fig.title('Relazioni tra le Variabili Selezionate', y=1.02, size=16)
    return fig

def main():
    st.set_page_config(page_title='Analisi Dataset Mance', layout='wide')
    st.title('📊 Analisi Dataset Mance')
    
    tips = load_and_clean_data()    
    with st.sidebar:
        st.header('🎯 Opzioni di Visualizzazione')
        features = st.multiselect(
                                'Seleziona le variabili da visualizzare',
                                options=tips.columns.tolist(),
                                default=['Conto Totale', 'Mancia', 'Dimensione Gruppo'],
                                help='Seleziona almeno due variabili per creare il pairplot'
                                )        
        hue_var = st.selectbox(
                                'Seleziona la variabile per il colore',
                                options=[None] + [col for col in tips.columns if tips[col].nunique() <= 5],
                                help='Questa variabile verrà usata per colorare i punti nel pairplot'
                                )        
        show_stats = st.checkbox('Mostra statistiche descrittive', value=True)

    col1, col2 = st.columns([2, 1])
    
    with col1:
        if show_stats:
            st.subheader('📈 Statistiche Descrittive')
            st.dataframe(tips[features].describe() if features else tips.describe())
    
    with col2:
        st.subheader('🔍 Anteprima Dati')
        st.dataframe(tips[features] if features else tips,)

    if len(features) >= 2:
        st.subheader('🎨 Pairplot delle Variabili Selezionate')
        with st.spinner('Generazione del pairplot in corso...'):
            fig = create_pairplot(tips, features, hue_var)
            st.pyplot(fig,use_container_width=False)
    else:
        st.warning('⚠️ Seleziona almeno due variabili per visualizzare il pairplot.')
    
if __name__ == "__main__":
    main()