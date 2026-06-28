from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate

parser = StrOutputParser()
json_parser = JsonOutputParser()

model = ChatTongyi(model="qwen3-max")
first_prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请起名，仅告知我名字无需其它内容。"
    "结果封装为JSON格式，key是name，value是姓名，严格遵循JSON格式"
)

second_prompt = PromptTemplate.from_template(
    "孩子姓名是{name}, 简要解释其含义"
)

# chain = first_prompt
chain = first_prompt | model | json_parser | second_prompt | model | parser

res = chain.invoke({"lastname": "张", "gender": "女儿"})
print(res)
print(type(res))