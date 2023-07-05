import json
import boto3


ssm = boto3.client('ssm')

jenkins1_token = ssm.get_parameter(Name='/jenkins1', WithDecryption=True)
jenkins2_token = ssm.get_parameter(Name='/jenkins2', WithDecryption=True)

data = {
    "Authpoint": {
        "jenkins__url": "http://54.159.150.76:8080/manage/credentials/store/system/domain/_/",
        "jenkins_name":"Authpoint",
        "auth__username": "admin",
        "auth__password": jenkins1_token,
        "select": 0,
        "crumbIssuer": "http://54.159.150.76:8080//crumbIssuer/api/json"
    },
    "PANDA": {
        "jenkins__url": "http://18.212.170.204:8080/manage/credentials/store/system/domain/_/",
        "jenkins_name":"PANDA",
        "auth__username": "admin",
        "auth__password": "1197ec2bee6171fd5bc3e3663125ed1ffa",
        "select": 0,
        "crumbIssuer": "http://18.212.170.204:8080//crumbIssuer/api/json"
    }
}
