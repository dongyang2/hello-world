# 线程中的future
from concurrent.futures import ThreadPoolExecutor, as_completed,TimeoutError
import time

def risky_task():
    raise ValueError("模拟 API 返回异常")

def fetch_data():
    time.sleep(1)
    return {"value": 21}

def process_data(future):
    try:
        data = future.result()
        print("处理结果:", data["value"] * 2)
    except Exception as e:
        print("处理失败:", e)

def task(name, delay):
    print(f"task {name} 开始")
    time.sleep(delay)
    print(f"task {name} 完成")
    return f"task {name} 的返回值"

def chuanxing():  # 串行
    r1 = task("串行A", 2)
    r2 = task("串行B", 2)
    print(r1, r2)

def bingxing():  # 并行
    with ThreadPoolExecutor(2) as pool:
        # future这个变量现在只相当于占位符，只有在函数运行结束后，才有值
        future1 = pool.submit(task, "并行A", 2)  # submit这里第一个参数是函数名，后面是函数入参。
        future2 = pool.submit(task, "并行B", 2)
        print("线程已提交至线程池，主线程可以做别的事")
        r1 = future1.result()  # 函数运行结束。通过 .result() 拿到函数输出
        r2 = future2.result()
        print(r1, r2)

def future_stat():
    """ 常用 成员
    result(timeout=...)	阻塞 主线程 获取结果；如想未完成则等待（即限制阻塞时长），需要填写timeout=x，超时抛出 TimeoutError
    done()	是否已结束，包括成功、异常或取消
    running()	当前是否正在执行
    cancel()	尝试取消尚未开始的任务
    exception()	获取任务异常；任务尚未结束时会等待
    add_done_callback(fn)	任务结束后执行回调
    """
    with ThreadPoolExecutor() as pool:
        future1 = pool.submit(task, "-测试future状态-", 1)  # submit这里第一个参数是函数名，后面是函数入参。
        print(f"是否完成 {future1.done()}")
        print(f"正在运行 {future1.running()}")
        print(f"取消 {future1.cancelled()}")
        # Future 可以正常结束，但不代表任务成功。 如果任务内部抛出了异常，异常会在调用 result() 时重新抛出
        r1 = future1.result()
        print(r1)
        print(f"是否完成 {future1.done()}")


def use_as_completed():
    with ThreadPoolExecutor(3) as pool:
        future_to_name_dic = {
            pool.submit(task, name, delay): name
            for name, delay in [("A", 3),("B", 1),("C", 2)]
        }

        for future in as_completed(future_to_name_dic):  # as_completed 让我们可以做到谁先完成，就先处理谁的结果
            name = future_to_name_dic[future]  # future是个占位符，我们通过字典结构反向拿任务名
            try:
                print(name, future.result())
            except Exception as e:
                print(name, "失败:", e)

def use_exception():
    with ThreadPoolExecutor(2) as pool:
        future1 = pool.submit(task, "normal", 3)
        future2 = pool.submit(risky_task, )

        try:
            print(future1.result(timeout=1))
        except TimeoutError:
            print("future1 等待超时")

        ## 任务本身执行失败，result() 会在外层 抛出对应异常。
        try:
            print(future2.result())
        except TimeoutError:
            print("future1 等待超时")

def use_future_callback():
    with ThreadPoolExecutor(2) as pool:
        future1 = pool.submit(fetch_data)
        future1.add_done_callback(process_data)
        # 主线程继续做其他事情

if __name__ == '__main__':
    """-*--*--*--*--*--*- future Ⅰ -*--*--*--*--*--*-ⅥⅦⅧⅨⅩ"""
    """-*--*--*--*--*--*- 理解他是一个占位符 -*--*--*--*--*--*-"""
    # start = time.perf_counter()
    # chuanxing()
    # print(f"串行总耗时: {time.perf_counter() - start:.2f}s")
    #
    # start = time.perf_counter()
    # bingxing()
    # print(f"并行总耗时: {time.perf_counter() - start:.2f}s")

    """-*--*--*--*--*--*- future Ⅱ -*--*--*--*--*--*-"""
    """-*--*--*--*--*--*- future不光用来存结果，也维护task的执行状态 -*--*--*--*--*--*-"""
    # future_stat()

    """-*--*--*--*--*--*- future Ⅲ -*--*--*--*--*--*-"""
    """-*--*--*--*--*--*- 与 as_completed() 的配合使用 -*--*--*--*--*--*-"""
    """-*--*--*- 
        由于future是个占位符，并不知道这个任务是谁，所以我们需要用dict自己维护任务名。
        当一个future显示完成时，我们拿到了，就可以根据dict反向确定任务。
        这个方式对比future.done()有明显差别， as_completed 相当于任务自动触发回调通知用户，而 future.done() 是用户查询状态。
        as_completed() 是用户被动获知。
        future.done() 是用户主动查询。
        根据以上信息，得知几乎无人用 .done() ，绝大多数情况都是用 as_completed()。
    -*--*--*-"""
    # use_as_completed()

    """-*--*--*--*--*--*- future Ⅳ -*--*--*--*--*--*-"""
    """-*--*--*--*--*--*- 异常的抛出 -*--*--*--*--*--*-"""
    # use_exception()

    """-*--*--*--*--*--*- future Ⅴ -*--*--*--*--*--*-"""
    """-*--*--*--*--*--*- 回调（即任务的串联）。知道用法即可，性能上在多数场景，并不优于as_completed()。 -*--*--*--*--*--*-"""
    use_future_callback()
