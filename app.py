import gradio as gr

def study_assistant(question, personality):
    if personality == "Friendly":
        return f"😊 Let's understand this simply:\n{question}"
    else:
        return f"📘 Academic Explanation:\n{question}"

iface = gr.Interface(
    fn=study_assistant,
    inputs=[
        gr.Textbox(label="Ask a Question"),
        gr.Radio(["Friendly", "Academic"], label="Personality")
    ],
    outputs="text",
    title="AI Study Assistant"
)

iface.launch()
