from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_community.llms.tongyi import Tongyi

promptTempla = PromptTemplate.from_template("单词: {word}, 反义词:{antonym}")

examples_data = [
    {"word": "上", "antonym": "下"},
    {"word": "前", "antonym": "后"},
]

fewShotTemplate = FewShotPromptTemplate(example_prompt=promptTempla,
                                        examples=examples_data,
                                        prefix="我提供如下示例，告诉我单词的反义词",
                                        suffix="基于前面的实例，{input_word}的反义词是什么",
                                        input_variables=['input_word'])

fewShotStr = fewShotTemplate.invoke(input={"input_word": "左"}).to_string()

model = Tongyi(model="qwen-max")

res = model.invoke(input=fewShotStr)

print(res)

