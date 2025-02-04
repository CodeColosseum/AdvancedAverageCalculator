import streamlit as st
from calculator import Calculator

st.set_page_config(page_title="Advanced Average Calculator")

def update():
    if 'result' not in st.session_state and 'calculat' not in st.session_state:
        st.session_state["result"] = "### result"
        st.session_state["calculat"] = "calculat"
        return
    
    new_text = ""
    for data in model.data:
        new_text += F"({data['score']} * {data["coefficient"]}) + "
    new_text = new_text[:-2] + "= "
    st.session_state['calculat'] = new_text

    st.session_state['result'] = model.calculate()
    

def AdvancedAverageCalculator():
    with st.container(border=True):
        update()
        st.write(st.session_state['result'])
        st.divider()
        st.write(st.session_state['calculat'])
        
        with st.form("add"):
            _, col1, col2, col3, _ = st.columns(5)
            with col1:
                score = st.number_input(label="Enter score: ", placeholder="123", step=1, min_value=1)
            with col3:
                coefficient = st.number_input(label="Enter coefficient:", placeholder="123", step=1, min_value=1)
            with col2:
                submit = st.form_submit_button()
            if submit:
                data = {
                    'name': None,
                    'score': score,
                    'coefficient': coefficient
                }
                model.add(data)
                update()
                submit = None
        
def main():
    AdvancedAverageCalculator()
    
model = Calculator()
main()