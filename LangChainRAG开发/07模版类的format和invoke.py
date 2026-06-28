from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("我的邻居是{name}")


format_ret = prompt_template.format(name="王力宏")
print(format_ret, type(format_ret))

invoke_ret = prompt_template.invoke(input={"name": "张学友"})
print(invoke_ret, type(invoke_ret))



