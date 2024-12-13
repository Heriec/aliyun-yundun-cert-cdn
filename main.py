import os
import time
from datetime import datetime, timedelta

from aliyun_cdn_cert_change import AliyunCdnClient
from aliyun_cert import AliyunCertClient
from feishuCard import FlybookRobotAlert

if __name__ == "__main__":
    feishu_webhook = os.environ.get('FEISHU_WEBHOOK')
    feishu = FlybookRobotAlert(feishu_webhook)
    try:
        domain = os.environ['DOMAIN']
        username = os.environ['USERNAME']
        phone = os.environ['PHONE']
        email = os.environ['EMAIL']  
        orderId = AliyunCertClient().create_cert(domain=domain, username=username, phone=phone, email=email)
        print(orderId)
        end_time = datetime.now() + timedelta(hours=1)

        data = None
        while datetime.now() < end_time:
            data = AliyunCertClient().cert_state(orderId)
            if data.type == 'certificate':
                break
            time.sleep(120)

        # orderId = '12921885'
        # data = AliyunCertClient().cert_state(orderId)

        if data.type == 'certificate':
            infoVo = AliyunCdnClient().cert_list(domain_name=domain)
            # find CertName 为 cert-{} 的证书
            cert = next((cert for cert in infoVo.cert_list.cert if cert.cert_name == f'cert-{orderId}'), None)
            if cert is None:
                raise Exception('cert not found')
            print(cert)
            AliyunCdnClient().change_cert(domain_name=domain, cert_name='cert-{}'.format(orderId), cert_id=cert.cert_id, sslpub=data.certificate, sslpri=data.private_key)
            # 不去删除证书，操作过于危险
        feishu.send_message(f"SSL证书更换成功，证书ID：{orderId}")
    except Exception as e:
        print(e)
        feishu.send_message(f"SSL证书更换失败，原因：{e}")
    

    
    