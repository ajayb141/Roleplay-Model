from llama_cpp import Llama
from llama_cpp_agent.llm_agent import LlamaCppAgent
from llama_cpp_agent.messages_formatter import MessagesFormatterType
import gradio as gr
lama_llm = Llama(
    model_path="westlake-7b-v2.Q6_K.gguf",n_gpu_layers=-1,n_threads=8,n_ctx=3584, n_batch=521,verbose=True,chat_format="llama-2" )
llama_cpp_agent = LlamaCppAgent(lama_llm, debug_output=False,
                              system_prompt="You are a AI chatbot", predefined_messages_formatter_type=MessagesFormatterType.CHATML)
def generate_text(msg,history):
    history=[""]
    prompt=''.join(history)+msg
    outputs =llama_cpp_agent.get_chat_response(prompt,temperature=0,print_output=False,add_message_to_chat_history=False,add_response_to_chat_history=False)
    return outputs

iface = gr.ChatInterface(generate_text).launch()
