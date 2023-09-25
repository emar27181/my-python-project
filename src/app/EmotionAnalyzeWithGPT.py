# ChatGPT APIで高度な感情分析を簡単に行う方法
# https://self-development.info/chatgpt-api%E3%81%A7%E9%AB%98%E5%BA%A6%E3%81%AA%E6%84%9F%E6%83%85%E5%88%86%E6%9E%90%E3%82%92%E7%B0%A1%E5%8D%98%E3%81%AB%E8%A1%8C%E3%81%86%E6%96%B9%E6%B3%95/

from langchain.llms import OpenAIChat
from langchain import PromptTemplate, LLMChain
import os

# def analyse_emotion():などで関数宣言をしないと、他ファイルでインポートが出来ない

api_key = os.environ.get('OPENAI_API_KEY')
# print("api_key: ", api_key)
os.environ["OPENAI_API_KEY"] = api_key

template = "{text}"

def analyze_emotion():
    prompt = PromptTemplate(
        template=template,
        input_variables=["text"]
    )

    content = """
    あなたは、世界でも有数の精神分析家です。
    文章から、著者の心理状態を分析することに長けています。
    次の文章をもとに心理分析してください。
    返答の出力形式は、以下に従うものとします。ただし、hueの値は以下の値をそのまま出力してください。
    [
    {"name": "anger", "hue": "344", "intense": 0～10},
    {"name": "anticipation", "hue": "19", "intense":0～10},
    {"name": "joy", "hue": "53", "intense": 0～10},
    {"name": "trust", "hue": "66", "intense": 0～10},
    {"name": "fear", "hue": "153", "intense" :0～10},
    {"name": "surprise", "hue": "201", "intense": 0～10},
    {"name": "sadness", "hue": "209", "intense": 0～10},
    {"name": "disgust", "hue": "300", "intense": 0～10}
    ]
    """

    content_test ="""
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
        # {"role": "system", "content": content_test} # 感情分析がより詳細に行われる prefix message
    ]

    llm = OpenAIChat(
        temperature=0,
        prefix_messages=prefix_messages
    )

    llm_chain = LLMChain(
        prompt=prompt,
        llm=llm
    )

    with open('data/input/InputData.txt', 'r') as input_file:
        input_data = input_file.read()

    res = llm_chain.run(input_data)

    with open('data/output/OutputData.json', 'w') as output_file:
        output_file.write(res)
        print("出力結果が保存されました.\n")

    print("入力文章: ", input_data)
    print("出力結果: \n", res)

analyze_emotion()