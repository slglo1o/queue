import requests
import time
import threading
import queue


class run_new:
    q = queue.Queue(300)
    buy = float(2.00000)  # 买入价格
    num = float(1.0000)  # 买入数量
    num_thread = 20  # 线程数量 运行次数
    response = None
    cookie = "lang=cn; curr_fiat=CNY; _dx_uzZo5y=1e0a7ceb5aa0c9744cecf1b4d91bdc8bd0f89026e43a4337d669956912b9de8444fd1afd; finger_print=63d873b32JSFubqpy5EOFfilqUJnRtJW3LISQKl1; _ym_d=1675129781; _ym_uid=1675129781437788748; ch=null; uid=13015332; nickname=a0098aau%40163.com; is_on=1; csrftoken=5af9f0a2a5a5ba7b7ef2222d1f3dd34447d59745c14382e5; is_portfolio_margin_account_13015332=0; is_portfolio_margin_switch_status_13015332=0; c2crisktip=1; b_notify=1; pver=a50ece15864fe15647c0610ae0d7b947; defaultP2PFiat=VND; notify_close=totp; market_title=usdt; login_notice_check=%2F; lasturl=%2Ftrade%2FVGX_USDT; AWSALB=TZLSYd7b8MahS9rSZz9m25kqB5wAtbBa2PoLM8Jd746Ul1Aa3cXRMh67BXDwpErt2joNpeIlEfHROdB1cx/ZrOi7Ku3Yyqo3dwE090Av8V1/C9TQgQMant/NEDri; AWSALBCORS=TZLSYd7b8MahS9rSZz9m25kqB5wAtbBa2PoLM8Jd746Ul1Aa3cXRMh67BXDwpErt2joNpeIlEfHROdB1cx/ZrOi7Ku3Yyqo3dwE090Av8V1/C9TQgQMant/NEDri"
    headers = {
        "Host": "www.gate.io",
        "Connection": "keep-alive",
        "Content-Length": "131",
        "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="94"',
        "Accept": "application/json, text/plain, */*",
        "csrftoken": "5af9f0a2a5a5ba7b7ef2222d1f3dd34447d59745c14382e5",
        "sec-ch-ua-mobile": '?0',
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)" +
                      "Chrome/94.0.4606.71 Safari/537.36 Core/1.94.186.400 QQBrowser/11.3.5195.400",
        "sec-ch-ua-platform": '"Windows"',
        "Origin": "https://www.gate.io",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": cookie
    }
    data = {"is_margin": 0, "engine_type": "normal", "symbol": "jam_usdt", "fundpass": "", "captcha": "",
            "type": "ask", "rate": buy, "vol": num, "order_type": "", "iceberg": 0, "source": "web"}

    # 请求包
    def hick_ht(self):
        while True:
            try:
                self.response = requests.post("https://www.gate.io/json_svr/exchange/?u=1&c=782289", data=self.data,
                                              headers=self.headers)
                self.q.put(self.response.json())
                # print(self.response.json())
            except ValueError:
                print("出现异常")
            finally:
                time.sleep(0.1)

    # 生产线程
    def start(self):
        threads = []
        for x in range(self.num_thread):
            t = threading.Thread(target=self.hick_ht, daemon=True)
            threads.append(t)
            t.start()
            time.sleep(0.1)

    # 打印
    def qu(self):
        w = self.q.get()
        print(w)
        self.q.task_done()

    # 打印线程
    def start_1(self):
        for x in range(self.num_thread):
            t = threading.Thread(target=self.qu)
            t.start()
            time.sleep(0.1)

while True:
    time.sleep(0.1)
    run = run_new()
    run.start()
    run.start_1()
    time.sleep(0.3)
