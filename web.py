import streamlit as st
import modules.functions as fns

st.title("Todos")
st.subheader("Declan's Todos")
st.write("Check the box of the todo you wish to delete")

todos = fns.read_todos_file()
def add_todo():
    to_do = st.session_state["new_todo"]
    todos.append(to_do+'\n')
    fns.write_todos_file(todos)
    st.session_state["new_todo"] = ''

todos = fns.read_todos_file()
# how to delete a todo by selecting its checkbox
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    # this will return true if the checkbox is checked, otherwise it will return false. If true then enter the
    # condition which deletes the todo
    if checkbox:
        todos.pop(index)
        fns.write_todos_file(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a Todo: ", placeholder="Add a new todo", on_change=add_todo, key="new_todo")
# Before you enter anything in this Enter a ToDo box, here is what st.session_state will look like
# {
#     "new_todo": ""
# }
# After you enter 'I'm a new todo' and click Add, here is what st.session_state will look like
# {
#     "new_todo": "I'm a new todo"
# }
st.session_state  #include this statement so that the dictionaries in use in memory will be displayed on the web page


