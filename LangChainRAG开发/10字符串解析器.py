from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_community.llms.tongyi import Tongyi

parser = StrOutputParser()
model_llm = Tongyi(model="qwen-max")
model = ChatTongyi(model="qwen3-max")
prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请起名，仅告知我名字无需其它内容。"
)

chain = prompt | model | parser | model
# chain = prompt | model_llm | model_llm

res: str = chain.invoke({"lastname": "张", "gender": "女儿"})
print(res)
print(type(res))