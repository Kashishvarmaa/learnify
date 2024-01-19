import designClasses
import streamlit as st
import brain

components = designClasses.WebComponents()


def main():
    st.title("SummNote")

    # Call the WebComponents functions
    content_to_summarise = components.promptSummariseArea()
    summarised_content = brain.openAISummariser(content_to_summarise)
    components.summaryProvider(summarised_content)
    components.doubtSolver()
    components.quizSection()

    # Call the note_input_form function
    notes_param: list = designClasses.note_input_form()

    # Generate notes button
    if st.button("Generate Notes"):
        print(notes_param)


if __name__ == "__main__":
    main()


