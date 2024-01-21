import designClasses
import streamlit as st
import brain

components = designClasses.WebComponents()


def main():
    st.title("SummNote")

    # Call the WebComponents functions

    # Summariser
    components.promptSummariseArea()

    # Doubt solver
    components.doubtSolver()

    # Quiz section
    components.quizSection()

    # Call the note_input_form function
    components.generateNotes()

if __name__ == "__main__":
    main()


