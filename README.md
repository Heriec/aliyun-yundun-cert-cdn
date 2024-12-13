# aliyun-yundun-cert-cdn
每两个月的第20天自动获取阿里云免费证书并部署到cdn上



## 如何使用

fork该项目，并填写对应参数，再push一次代码即可（随便改点啥，workflow需要push才能触发）

 GitHub 仓库的 "Settings" -> "Secrets and variables" -> "Actions" 中添加以下 secrets：

- `ALIYUN_ACCESS_KEY_ID`：阿里云账户AK
- `ALIYUN_ACCESS_KEY_SECRET`：阿里云账户SK
- `DOMAIN`: 要设置的域名
- `USERNAME`: 姓名
- `PHONE`: 手机号
- `EMIAL`: 邮箱
- `FEISHU_WEBHOOK`: 飞书机器人webhook
