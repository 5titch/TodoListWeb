import streamlit as st
import Functions

todos = Functions.get_t()


def add_todo():
    todo = st.session_state["IT"] + '\n'
    todos.append(todo)
    Functions.write_t(todos)

st.title("To Do list")
st.subheader("Pattern your life")
st.write("This app is created to better your life")



for i, todo in enumerate(todos):                   # for every item in toodo enumerate it and...
    checkbox = st.checkbox(todo, key=todo)      # assign the a checkbox to it then put it in checkbock give it key of toodo
    if checkbox:                        # if checkbox is true as its default is fau
        todos.pop(i)                        # this actually removes
        Functions.write_t(todos)
        del st.session_state[todo]   # this removes the session state without as without it, it just becomes true
        st.experimental_rerun()


st.text_input(label="", placeholder="Add new task", on_change=add_todo, key="IT" )  # Label is part if this function




#link
# https://5titch-letssee-web-jjduun.streamlit.app/