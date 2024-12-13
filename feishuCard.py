"""
飞书群机器人发送通知
"""
import json
from logging import Logger
import requests


class FlybookRobotAlert():
    def __init__(self, webhook_url, logger=Logger("飞书通知")):
        self.webhook = webhook_url
        self.logger = logger

        self.headers = {'Content-Type': 'application/json; charset=UTF-8'}

    def post_to_robot(self, post_data):
        '''
        给飞书机器人发送请求
        :param data:
        :return:
        '''
        try:
            resp = requests.request(
                method="POST", url=self.webhook, data=post_data, headers=self.headers).json()
            if resp.get("StatusCode") == 0 and resp.get("msg") == "success":
                self.logger.info(f"飞书通知发送成功，msg={resp}")
            else:
                self.logger.warning(f"飞书通知发送失败,{resp}")
        except Exception as e:
            self.logger.warning("飞书通知发送异常")
            self.logger.warning(e)
            pass

    def send_message(self, text):
        # 飞书通知标题
        robot_headers = 'SSL证书更换通知'

        elements = [
            {
                "tag": "div",
                "text": {
                    "content": text,
                    "tag": "lark_md"
                }
            }
        ]

        card = json.dumps({
            "config": {
                "wide_screen_mode": True
            },
            "elements": elements,
            "header": {
                "template": "green",
                "title": {
                    "content": robot_headers,
                    "tag": "plain_text"
                }
            }
        })

        msg_body = json.dumps({"msg_type": "interactive", "card": card})
        self.post_to_robot(msg_body)
        return
