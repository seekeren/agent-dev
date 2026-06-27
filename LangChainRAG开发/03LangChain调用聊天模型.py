from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

model = ChatTongyi(model="qwen3-max")

# messages = [
#     SystemMessage(content="你是一个唐诗百科专家"),
#     HumanMessage(content="来一首边塞唐诗"),
#     AIMessage(content="大漠孤烟直，长河落日圆"),
#     HumanMessage(content="这首诗的作者是谁？")
# ]

messages = [
    ("system","你是一个唐诗百科专家"),
    ("human","来一首边塞唐诗"),
    ("ai","大漠孤烟直，长河落日圆"),
    ("human","这首诗的作者是谁？")
]

res = model.stream(input=messages)

for chunk in res:
    print(chunk.content, end="", flush=True)

