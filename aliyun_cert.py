import os

from alibabacloud_cas20200407.client import Client as cas20200407Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_cas20200407 import models as cas_20200407_models
from alibabacloud_cas20200407.models import DescribeCertificateStateResponseBody
from alibabacloud_cas20200407.models import ListUserCertificateOrderResponseBody
from alibabacloud_cas20200407.models import GetUserCertificateDetailResponseBody
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class AliyunCertClient:
    def __init__(self):
        pass

    def certClient(self) -> cas20200407Client:
        """
        使用AK&SK初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
        )
        config.endpoint = f'cas.aliyuncs.com'
        return cas20200407Client(config)

    def create_cert(self, domain, username, phone, email, validate_type='DNS', product_code="digicert-free-1-free") -> str:
        client = self.certClient()
        create_certificate_request_request = cas_20200407_models.CreateCertificateRequestRequest(
            username=username,
            phone=phone,
            email=email,
            domain=domain,
            validate_type=validate_type,
            product_code=product_code
        )
        runtime = util_models.RuntimeOptions()
        response = client.create_certificate_request_with_options(create_certificate_request_request, runtime)
        return response.body.order_id


    def cert_state(self, order_id) -> DescribeCertificateStateResponseBody:
        client = self.certClient()
        describe_certificate_state_request = cas_20200407_models.DescribeCertificateStateRequest(order_id=order_id)
        runtime = util_models.RuntimeOptions()
        try:
            response = client.describe_certificate_state_with_options(describe_certificate_state_request, runtime)
            return response.body
        except Exception as error:
            print(error.message)
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    def cert_info(self, cert_id) -> GetUserCertificateDetailResponseBody:
        client = self.certClient()
        get_user_certificate_detail_request = cas_20200407_models.GetUserCertificateDetailRequest(
            cert_id=cert_id
        )
        runtime = util_models.RuntimeOptions()
        try:
            response = client.get_user_certificate_detail_with_options(get_user_certificate_detail_request, runtime)
            return response.body
        except Exception as error:
            print(error.message)
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)
    
    def cert_list(self, order_type='cert') -> ListUserCertificateOrderResponseBody:
        client = self.certClient()
        list_user_certificate_order_request = cas_20200407_models.ListUserCertificateOrderRequest(order_type=order_type)
        runtime = util_models.RuntimeOptions()
        try:
            response = client.list_user_certificate_order_with_options(list_user_certificate_order_request, runtime)
            return response.body
        except Exception as error:
            print(error.message)
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)