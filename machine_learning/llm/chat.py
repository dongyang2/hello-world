# 摘自 try_qwen_langchain_250604.py
import time
from datetime import datetime
import requests
import os

from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI

import warnings


def basic_ask(p, url):
    print(f"请求地址 {url}")
    headers = {"Content-Type": "application/json"}
    data = {
        "prompt": p,
        # "max_new_tokens": 128,  # 控制大模型输出的token数
        "temperature": 0.3  # 值越大，灵活性和随机性越高
    }

    response = requests.post(url, headers=headers, json=data)  # 必须使用 POST 方法
    return response



def get_ans_qwen_vllm(p, template, think=False, local=False, stream=False, max_tokens=1024):
    print(f"本次请求是否开启 think 模式 {think}, 是否开启 stream 模式 {stream}, 本地模式 {local}, max_tokens={max_tokens}")
    # qw_vllm_url = f"http://localhost:{qw_port}/v1" if local else f"http://{server_ip}:{qw_port}/v1"
    qw_vllm_url = ""

    llm = ChatOpenAI(
        model_name="Qwen3-8B",
        openai_api_base=qw_vllm_url,
        api_key="0",
        temperature=0.1,
        stream=stream,
        max_tokens=max_tokens,
        model_kwargs={"extra_body": {"chat_template_kwargs": {"enable_thinking": think}}}
        # openai_api_kwargs={"extra_body": {"chat_template_kwargs": {"enable_thinking": think}}}  # 这是不支持的，是错的
    )

    prompt = ChatPromptTemplate.from_template(template)
    if stream:
        chain = prompt | llm
        # NOTICE: 虽然这儿是用的list.append（str）的形式，但是如果改用str+=str的形式，会发现怎么都拿不到输出，所以还是用list append的形式更稳定，原因未知
        response_chunks = []
        for chunk in chain.stream({"input": p}):  # langchain for stream 正确使用
            # print("DEBUG raw chunk:", chunk)  # stream 排查方式
            if hasattr(chunk, "content"):
                print(chunk.content, end="", flush=True)  # 立即刷新输出
                response_chunks.append(chunk.content)

        response = "".join(response_chunks)

        # response_chunks = ""
        # for chunk in chain.stream({"input": p}):
        #     if hasattr(chunk, "content"):
        #         response_chunks += chunk.content
        # response = response_chunks
    else:
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(p)
    return response


def get_ans_llama_vllm(p, prompt, local=False):
    # llama_url = f"http://localhost:{llama_port}/v1" if local else f"http://{server_ip}:{llama_port}/v1"
    llama_url = ""

    llm = ChatOpenAI(
        model_name="llama3d1-8B",
        openai_api_base=llama_url,
        api_key="0",
        temperature=0.1,
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run(p)

    return response


def del_think_tag(resp:str, cachexia_tag:str):
    """  返回两个结果，一个 think，一个 回答。
    cachexia tag：   prompt无法干掉的顽固tag
    """
    tag = True if resp.find("<think>") != -1 else False
    anti_tag = True if resp.find("</think>") != -1 else False
    start = resp.find("<think>") + len("<think>")
    end = resp.find("</think>")
    if tag and anti_tag:  # 有正tag和反tag
        return [resp[start: end], simple_del_tag(resp[end + len("</think>"):],cachexia_tag).strip()]
    elif not tag and not anti_tag:    # 正tag和反tag 都没有
        return ["", simple_del_tag(resp,cachexia_tag).strip()]
    elif tag and not anti_tag:
        return [resp[start:], ""]
    else:  # 只有 反tag  # 在 DeepSeekv3的qwen7b模型下，就只有反tag  # DeepSeek-v3-qwen-7b无法关闭think
        return [resp[:end], simple_del_tag(resp[end + len("</think>"):],cachexia_tag).strip()]


def simple_del_tag(s:str, tag="<solution>"):
    if tag == "":  # 此时不作处理
        return s
    anti_tag = tag[:1]+"/"+tag[1:]
    if tag in s and anti_tag in s:
        return s.replace(tag, "").replace(anti_tag, "")
    return s


def online_openai(model:str, q:str):
    from openai import OpenAI   #  v1.92.2

    key = os.environ.get("aihubkey")
    li = [
          "gpt-5.2", "gpt-5.2-pro",
          "gpt-5.1", "gpt-5"]
    li2 = ["gemini-3-flash-preview", "gemini-3-flash-preview-search", "gemini-3-pro-preview",
           "gemini-2.5-pro", ]
    client = OpenAI(base_url="https://aihubmix.com/v1",api_key=key)

    print(f"你在使用的模型是 {model}")
    if model in li:
        # 老方法
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": q}]
        )
        print(completion.choices[0].message.content)

        # # #  v1.92.2 适用方法
        # reply = client.responses.create(model=model,input=q)
        # print(reply.output[0].content[0].text)
    elif model in li2:
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": q}]
        )
        print(completion.choices[0].message.content)
    else:
        print(f"不支持该模型 {model}")


def online_gemini(model, q):
    from google import genai
    from google.genai import types

    key = os.environ.get("aihubkey")
    li2 = ["gemini-3-flash-preview","gemini-3-flash-preview-search", "gemini-3-pro-preview",
          "gemini-2.5-pro",]
    if model not in li2:
        print(f"不支持该模型 {model}")
        return
    client = genai.Client(
        api_key=key,
        http_options={"base_url": "https://aihubmix.com/gemini"},
    )
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part(text=q),
            ],
        ),
    ]
    reply = client.models.generate_content(
        model=model,
        contents=contents,
    )

    print(reply)

def main():
    template = """
    从以下情感中分类用户输入，只返回对应的单词，不要解释：
    选项: happy, sad, neutral

    用户输入: {input}
    """

    # get_emotion("I'm Happy!!", template)
    # get_emotion("The weather is really Good!!", template)
    # get_ans_qwen_vllm("I can taste the food.", template)


    model_name = "gemini-3-pro-preview"
    # model_name = "gpt-5"
    q = """ 
调研一下是否有“基于对象存储的机器学习、智能原生：直接利用对象开展模型训练”主题的相关论文，以及论证下具体可行性。我个人觉得不太可行，请给出你的论证
    """

    online_openai(model_name,q)
    # online_gemini(model_name,"你好，介绍一下你自己")




if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    print(time.ctime())
    main()
