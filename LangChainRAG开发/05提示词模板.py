from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate

# promptStr = PromptTemplate.from_template("我姓{lastname}, 刚生了{gender},你帮我取个名字")
# str_format = promptStr.format(lastname="王", gender="男孩")
# model = Tongyi(model="qwen-max")
# res = model.invoke(input=str_format)
# print(res)

promptTemplate = PromptTemplate.from_template("我姓{lastname}, 刚生了{gender},你帮我取个名字")
model = Tongyi(model="qwen-max")
chain = promptTemplate | model
res = chain.invoke(input={"lastname": "王", "gender": "男孩"})
print(res)
