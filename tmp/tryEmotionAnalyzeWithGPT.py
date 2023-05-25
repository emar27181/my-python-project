# ChatGPT APIで高度な感情分析を簡単に行う方法
# https://self-development.info/chatgpt-api%E3%81%A7%E9%AB%98%E5%BA%A6%E3%81%AA%E6%84%9F%E6%83%85%E5%88%86%E6%9E%90%E3%82%92%E7%B0%A1%E5%8D%98%E3%81%AB%E8%A1%8C%E3%81%86%E6%96%B9%E6%B3%95/

from langchain.llms import OpenAIChat
from langchain import PromptTemplate, LLMChain
import os

api_key = os.environ.get('OPENAI_API_KEY')
# print("api_key: ", api_key)
os.environ["OPENAI_API_KEY"] = api_key

template = "{text}"

prompt = PromptTemplate(
    template=template,
    input_variables=["text"]
)

content = """
あなたは、世界でも有数の精神分析家です。
文章から、著者の心理状態を分析することに長けています。
次の文章をもとに心理分析してください。
返答の出力形式は、以下に従うものとします。
[result]
positive or negative
[detail]
joy:0～10
trust:0～10
fear:0～10
surprise:0～10
sadness:0～10
disgust:0～10
anger:0～10
anticipation:0～10
[review]
"""

prefix_messages = [
    {"role": "system", "content": content}
]

llm = OpenAIChat(
    temperature=0,
    prefix_messages=prefix_messages
)

llm_chain = LLMChain(
    prompt=prompt,
    llm=llm
)

text = """
ウクライナでの悲惨な状況を見ると胸が痛む。戦争反対。
"""

res = llm_chain.run(text)
print(res)
