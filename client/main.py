import core.load_config
import core.chat_core
import gradio as gr


# def speechr(msg, audio_input):

def chat(msg,chatbot):
    res
    return [(msg,'1')]
with gr.Blocks() as demo:
    title = gr.Markdown("# AssistX")
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    audio_input = gr.Audio(type="filepath")
    # audio_input.stop_recording(fn, inputs = [msg, audio_input], output = [msg])
    msg.submit(chat, inputs = [msg,chatbot], outputs = [chatbot])

demo.launch()