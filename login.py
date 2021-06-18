import json
import requests

domain_url = r"http://"+ "IP" +"/k3cloud/Kingdee.BOS.WebApi."
login_url = domain_url + r"ServicesStub.AuthService.ValidateUser.common.kdsvc"
bill_query_url = domain_url + r"ServicesStub.DynamicFormService.ExecuteBillQuery.common.kdsvc"
bill_get_url = domain_url + r"ServicesStub.DynamicFormService.View.common.kdsvc"
bill_audit_url = domain_url + r"ServicesStub.DynamicFormService.Audit.common.kdsvc"
bill_submit_url = domain_url + r"ServicesStub.DynamicFormService.Submit.common.kdsvc"

login_data = {'acctid': '', 'username': '', 'password': '', 'lcid': 2052} # 2052 简体中文


def login():
    response = requests.post(url=login_url, data=login_data)
    print(response.text)
    return response.cookies


def bill_query(cookies):
    post_data = {"data": json.dumps(
        {"FormId": ""
            , "FieldKeys": ""
            , "FilterString": " = ''"}
    )}
    response = requests.post(url=bill_query_url, data=post_data, cookies=cookies)
    return response.text


def bill_get(cookies):
    post_data = {"FormId": "", "Data": json.dumps({"Number": ""})}
    response = requests.post(url=bill_get_url, data=post_data, cookies=cookies)
    return response.text


def bill_audit(cookies):
    post_data = {"FormId": "", "Data": json.dumps({"IDS": [""]})}
    response = requests.post(url=bill_audit_url, data=post_data, cookies=cookies)
    return response.text


def bill_submit(cookies):
    post_data = {"FormId": "", "Data": json.dumps({"IDS": [""]})}
    response = requests.post(url=bill_submit_url, data=post_data, cookies=cookies)
    return response.text


if __name__ == '__main__':
    k3_cookies = login()
    # bill_list = bill_query(k3_cookies)
    # print(bill_list)
    bill = bill_get(k3_cookies)
    print(bill)
    # submit_result = bill_submit(k3_cookies)
    # print(submit_result)
    # audit_result = bill_audit(k3_cookies)
    # print(audit_result)
