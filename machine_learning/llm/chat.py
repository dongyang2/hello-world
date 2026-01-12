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
    q = """ 帮我润色论文，符合acl标准。
修改 Limitations，在保持专业性的基础上，帮我去除一些内容，大概20~30个单词左右。

Despite its demonstrated effectiveness, the proposed framework has several limitations that warrant discussion.

First, while the audit-driven design improves reasoning stability and output correctness, it introduces additional inference overhead due to iterative validation. Although this overhead is moderate in our current implementation and remains practical for local deployment, the latency may become non-negligible in time-critical applications or when deeper audit loops are required. Future work may explore early-exit strategies or adaptive auditing policies to balance efficiency and verification rigor.

Second, the effectiveness of the Audit Pipeline depends on the evaluative capability of the underlying language model. When the Judge model exhibits limited reasoning or discrimination ability, the quality of validation may degrade, potentially allowing subtle errors to pass or rejecting correct but unconventional reasoning paths. While our experiments show that this issue can be mitigated by allocating stronger models to the Judge role, systematic strategies for judge calibration and robustness remain an open problem.

% 我的RAG检索方法是相关性检索，而非维持概念的全局一致性。同时，我的记忆机制并不是跨任务记忆，虽然在 Question1 回答过程中会用到历史记忆，且会通过 搜索引擎或本地api 获取短期记忆，但是拼接之后就丢弃了，在 Question2 中若有和 Question1 子问题的相关内容，需要重新检索，这就是面向单任务而非多任务的设计。信息并没有进行显式的跨任务整合，只会在需要时进行相关性检索。
Third, the proposed memory design is optimized for supporting coherent reasoning within individual tasks and does not aim to enforce global consistency across multiple tasks or long-term sessions. While relevance-based retrieval is effective for contextual grounding, extending the framework toward explicit cross-task memory consolidation remains an open direction.

Finally, our evaluation primarily focuses on question answering and reasoning-centric benchmarks. While these tasks are representative of many agent-based applications, further validation on interactive, embodied, or continuously evolving environments would be necessary to fully assess the generality of the framework.
    """

    online_openai(model_name,q)
    # online_gemini(model_name,"你好，介绍一下你自己")




if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    print(time.ctime())
    main()
