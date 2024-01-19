import designClasses
import streamlit as st
import brain

components = designClasses.WebComponents()


def main():
    st.title("SummNote")

    # Call the WebComponents functions

    # Summariser
    content_to_summarise = components.promptSummariseArea()
    print(content_to_summarise)
    if content_to_summarise is not None:
        summarised_content = brain.openAISummariser(content_to_summarise)
        components.summaryProvider(summarised_content)

    # Doubt solver
    doubt = components.doubtSolver()
    print(doubt)
    if doubt is not None:
        doubtSolution = brain.openAIDoubtSolver(doubt)
        components.doubtSolutionArea(doubtSolution)

    components.quizSection()

    # Call the note_input_form function
    notes_param: list = designClasses.note_input_form()

    # Generate notes button
    if st.button("Generate Notes"):
        print(notes_param)


if __name__ == "__main__":
    main()


