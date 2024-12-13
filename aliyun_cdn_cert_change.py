import os


from alibabacloud_cdn20180510.client import Client as Cdn20180510Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_cdn20180510 import models as cdn_20180510_models
from alibabacloud_cdn20180510.models import DescribeCdnSSLCertificateListResponseBodyCertificateListModel
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class AliyunCdnClient:
    def __init__(self):
        pass

    def changeCdnCertClient(self) -> Cdn20180510Client:
        """
        使用AK&SK初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
        )
        config.endpoint = f'cdn.aliyuncs.com'
        return Cdn20180510Client(config)
    
    def cert_list(self, domain_name) -> DescribeCdnSSLCertificateListResponseBodyCertificateListModel:
        client = self.changeCdnCertClient()
        describe_cdn_sslcertificate_list_request = cdn_20180510_models.DescribeCdnSSLCertificateListRequest(
            domain_name=domain_name
        )
        runtime = util_models.RuntimeOptions()
        response = client.describe_cdn_sslcertificate_list_with_options(describe_cdn_sslcertificate_list_request, runtime)
        return response.body.certificate_list_model
        

    def change_cert(self, domain_name, cert_id, cert_name, sslpub, sslpri) -> None:
        client = self.changeCdnCertClient()
        set_cdn_domain_sslcertificate_request = cdn_20180510_models.SetCdnDomainSSLCertificateRequest(
                    domain_name=domain_name,
                    sslprotocol='on',
                    cert_type='cas',
                    cert_id=cert_id,
                    cert_name=cert_name,
                    sslpub=sslpub,
                    sslpri=sslpri
                )
        runtime = util_models.RuntimeOptions()
        client.set_cdn_domain_sslcertificate_with_options(set_cdn_domain_sslcertificate_request, runtime)
