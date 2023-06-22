import time

import streamlit as st

import utils.globals as globals
from extractor import Extractor
from basic_search import basic
from advanced_search import advanced
from utils.unify_dfs import unify


def main():
    st.title("Systematic Review")
    mode = st.radio('Mode:', options=("Basic", "Advanced"))

    # BASIC INPUT
    if mode == "Basic":
        request = basic()
    
    # ADVANCED INPUT
    if mode == "Advanced":
        request = advanced()

    @st.cache_data
    def convert_df(df):
        return df.to_csv().encode("utf-8")

# RESULTADOS
    if 'boolean_error' in st.session_state: # Avoid submitting with error
        st.error("Boolean operators might not work within these fields")
    
    if st.button("Submit"):
        st.sidebar.write("""## Extracting...""")
        st.session_state.dataframes = {}
        st.session_state.unify_parameters = {}

        globals.stop_extraction = False
        if st.button("Stop Extraction"):
            globals.stop_extraction = True

        # BUSCA PARA O PUBMED
        if request['pm_check']:
            with st.spinner(f'Searching articles with keyword "{request["pm_keyword"]}" in PubMed ({request["pm_num"]} articles) wait...'):
                data_tmp = Extractor(request["pm_keyword"], request["pm_num"]).pubmed()
                
                if not globals.stop_extraction:
                    st.session_state.dataframes["pubmed_df"] = data_tmp
                    st.session_state.unify_parameters['pm'] = data_tmp
                    st.success("PubMed Done!")
                else:
                    st.error('Stopped')

        # BUSCA PARA O Scopus
        if request["sc_check"]:
            with st.spinner(f'Searching articles with keyword "{request["sc_keyword"]}" in Scopus ({request["sc_num"]}) wait...'):
                data_tmp = Extractor(request["sc_keyword"], request["sc_num"]).scopus()

                if not globals.stop_extraction:
                    st.session_state.dataframes["scopus_df"] = data_tmp
                    st.session_state.unify_parameters['sc'] = data_tmp
                    st.success("Scopus Done!")
                else:
                    st.error('Stopped')
        
        # BUSCA PARA O Science Direct
        if request["sd_check"]:
            with st.spinner(f'Searching articles with keyword "{request["sd_keyword"]}" in ScienceDirect ({request["sd_num"]}) wait...'):
                data_tmp = Extractor(request["sd_keyword"], request["sd_num"]).scidir()

                if not globals.stop_extraction:
                    st.session_state.dataframes["scidir_df"] = data_tmp
                    st.session_state.unify_parameters['sd'] = data_tmp
                    st.success("ScienceDirect Done!")
                else:
                    st.error('Stopped')


        # UNIFICA AS TABELAS
        st.session_state.dataframes["unified_df"] = unify(st.session_state.unify_parameters)

                
        
    
    # Renderiza os downloads
    if not globals.stop_extraction:
        if hasattr(st.session_state, 'dataframes'): 
            st.sidebar.success("Extraction complete!")

            for df in st.session_state.dataframes:
                st.sidebar.download_button(
                    label=f"Download {df} as CSV",
                    data=convert_df(st.session_state.dataframes[df]),
                    file_name=f"{df}.csv",
                    mime="text/csv",
                    )
            
            st.sidebar.write('Unified results')
            st.sidebar.download_button(
                label='Download results in unified dataframe',
                data=convert_df(st.session_state.dataframes["unified_df"]),
                file_name='results.csv',
                mime='text/csv'
                )
            
            # Show unified dataframes
            st.dataframe(st.session_state.dataframes["unified_df"])

    else:
        st.sidebar.error('Extraction stopped by the user') 



if __name__ == "__main__":
    main()
