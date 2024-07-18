import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils import qa_agent

api_key = "sk-l4dQc5Ncyvst0Krr06B6EaE6Ba7d4753A1Fb1a5a535cC5Cf"
st.title("AI智能PDF问答工具")
if "memory" not in st.session_state:
    st.session_state["memory"]=ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history" ,
        output_key="answer"
    )
uploaded_file=st.file_uploader("上传你的Pdf文件",type="pdf")
question=st.text_input("请输入问题",disabled=not uploaded_file)

if uploaded_file and question:
    with st.spinner("请稍等"):
        response=qa_agent(api_key,st.session_state["memory"],uploaded_file,question)
    st.write("### 答案")
    st.write(response["answer"])
    st.session_state["chat_history"]=response["chat_history"]
if "chat_history" in st.session_state:
    with st.expander("历史消息"):
        for i in range(0, len(st.session_state["chat_history"]), 2):
            human_message=st.session_state["chat_history"][i]
            ai_message = st.session_state["chat_history"][i+1]
            st.write(human_message)
            st.write(ai_message)
            if i<len(st.session_state["chat_history"])-2:
                st.divider()