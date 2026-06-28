from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_prompt_template = ChatPromptTemplate.from_messages(
    [("system", "你是一个唐诗百科全书"), MessagesPlaceholder("history"), ("human", "再来一首李白的唐诗")])

history_data = [
    ("human","来一首李白的唐诗"),
    ("ai", "好的。床前明月光，疑是地上霜。举头望明月，低头思故乡。")
]

chatModel = ChatTongyi(model="qwen3-max", streaming=True)

chain = chat_prompt_template | chatModel
# print(type(chain))

# res = chain.invoke({"history": history_data})
# print(res.content)

for chunk in chain.stream({"history": history_data}):
    print(chunk.content, end="", flush=True)

