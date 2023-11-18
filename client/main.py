import core.load_config
import core.chat_core
import gradio as gr


def greet(name):
    return "Hello " + name + "!"


with gr.Blocks() as demo:
    title = gr.Markdown("# AssistX")
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    audio_input = gr.Audio(type="filepath")
    gradio.Audio.stop_recording(fn, ···)

demo.launch()