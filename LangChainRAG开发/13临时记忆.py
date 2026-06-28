from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

prompt_template = ChatPromptTemplate(
    [
        ("system", "根据对话历史回答问题"),
        MessagesPlaceholder("chat_history"),
        ("human", "回答以下问题：{input}")
    ])

model = ChatTongyi(model="qwen3-max")


def print_prompt(promptValue):
    print('=' * 10, promptValue.to_string(), '=' * 10)
    return promptValue


str_parser = StrOutputParser()

base_chain = prompt_template | print_prompt | model | str_parser

history_store = {}


def get_history(session_id):
    if session_id not in history_store:
        history_store[session_id] = InMemoryChatMessageHistory()
    return history_store[session_id]


strong_chain = RunnableWithMessageHistory(
    base_chain,
    get_history,
    input_messages_key="input",
    history_messages_key="chat_history")

if __name__ == '__main__':
    # 固定格式，添加LangChain的配置，为当前程序配置所属的session_id
    session_config = {
        "configurable": {
            "session_id": "user_001"
        }
    }

    res = strong_chain.invoke({"input": "小明有2个猫"}, session_config)
    print("第1次执行：", res)

    res = strong_chain.invoke({"input": "小刚有1只狗"}, session_config)
    print("第2次执行：", res)

    res = strong_chain.invoke({"input": "总共有几个宠物"}, session_config)
    print("第3次执行：", res)
