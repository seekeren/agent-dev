import json
import os
from msilib.schema import Property
from typing import Sequence

from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory

class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id, storage_path):
        self.session_id = session_id
        self.storage_path = storage_path
        self.full_file_path = os.path.join(self.storage_path, self.session_id)
        # 确保文件夹是存在的
        os.makedirs(os.path.dirname(self.full_file_path), exist_ok=True)


    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        all_messages = list(self.messages)
        all_messages.extend(messages)

        new_messages = []
        for message in all_messages:
            d = message_to_dict(message)
            new_messages.append(d)
        # 以上的写法等同于以下
        # new_messages = [message_to_dict(msg) for msg in new_messages]

        with open(self.full_file_path, "w", encoding="utf-8") as f:
            json.dump(new_messages, f)

    @property
    def messages(self) -> list[BaseMessage]:
        # 当前文件中是list[多个字典]
        try:
            with open(self.full_file_path, "r", encoding="utf-8") as f:
                messages_data = json.load(f)
                return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []

    def clear(self) -> None:
        with open(self.full_file_path, "w", encoding="utf-8") as f:
            json.dump([], f)

prompt_template = ChatPromptTemplate(
    [
        ("system", "根据对话历史回答问题"),
        MessagesPlaceholder("chat_history"),
        ("human", "回答以下问题：{input}")
    ])

model = ChatTongyi(model="qwen3-max", api_key="sk-90a5a5552b30402fa2375d69a7548306")


def print_prompt(promptValue):
    print('=' * 10, promptValue.to_string(), '=' * 10)
    return promptValue


str_parser = StrOutputParser()

base_chain = prompt_template | print_prompt | model | str_parser

history_store = {}


def get_history(session_id):
    return FileChatMessageHistory(session_id, "./chat_history")


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

    # res = strong_chain.invoke({"input": "小明有2个猫"}, session_config)
    # print("第1次执行：", res)
    #
    # res = strong_chain.invoke({"input": "小刚有1只狗"}, session_config)
    # print("第2次执行：", res)

    res = strong_chain.invoke({"input": "总共有几个宠物"}, session_config)
    print("第3次执行：", res)
