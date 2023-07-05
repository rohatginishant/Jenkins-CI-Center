import requests
import json
from jenkins_login import data


class Credentials:

    def __init__(self, jenkins_url, auth_username, auth_token, crumb_url):
        self.jenkins_url = jenkins_url
        self.auth_username = auth_username
        self.auth_token = auth_token
        self.jenkins_crumb = requests.get(crumb_url)
        self.crumb = self.jenkins_crumb.json()["crumb"]

    def create_username_with_password(self, id, username, password, usernameSecret, description, crumb_url):
        jenkins_url_createfunction = self.jenkins_url + 'createCredentials'
        jenkins_crumb = requests.get(crumb_url)
        crumb = jenkins_crumb.json()["crumb"]
        # print(f"Jenkins crumb data = {jenkins_crumb.json()}")

        Head = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Jenkins_Crumb': crumb
        }

        username_set = username
        id_set = id
        password_set = password
        usernamesecret_set = usernameSecret
        description_set = description

        data = {
            "": "0",
            "credentials": {
                "scope": "GLOBAL",
                "username": username_set,
                "usernameSecret": usernamesecret_set,
                "password": password_set,
                "$redact": "password",
                "id": id_set,
                "description": description_set,
                "stapler-class": "com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl",
                "$class": "com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl"
            }
        }

        data = json.dumps(data)

        response = requests.post(
            jenkins_url_createfunction,
            auth=(self.auth_username, self.auth_token),
            headers=Head,
            data={'json': data}
        )
        if response.status_code == 200:
            print("Credentials created ")
            return "hello , you have created username-password successfully !!! "

    def create_ssh_with_private_key(self, id, description, username, privatekey, usernameSecret, crumb_url):
        jenkins_url_createfunction = self.jenkins_url + 'createCredentials'

        jenkins_crumb = requests.get(crumb_url)
        crumb = jenkins_crumb.json()["crumb"]

        Headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Jenkins_Crumb': crumb
        }

        username_set = username
        id_set = id
        private_key_set = privatekey
        description_set = description
        usernameSecret_set = usernameSecret

        data = {
            "": "3",
            "credentials": {
                "scope": "GLOBAL",
                "id": id_set,
                "description": description_set,
                "username": username_set,
                "usernameSecret": usernameSecret_set,
                "privateKeySource":
                    {
                        "value": "0",
                        "privateKey": private_key_set,
                        "stapler-class": "com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey$DirectEntryPrivateKeySource",
                        "$class": "com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey$DirectEntryPrivateKeySource"
                    },
                "passphrase": "passphrase",
                "$redact": "passphrase",
                "stapler-class": "com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey",
                "$class": "com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey"
            },
        }

        data = json.dumps(data)

        response = requests.post(jenkins_url_createfunction,
                                 auth=(self.auth_username, self.auth_token),
                                 headers=Headers,
                                 data={'json': data})

        if response.status_code == 200:
            print("Credentials created ")
            return "hello , you have created ssh credentials successfully !!! "

    def update_username_with__password(self, id, username, password, usernameSecret, description):
        # id = input("Enter id : ")

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Jenkins-Crumb': self.crumb
        }

        update_url = self.jenkins_url + f"credential/{id}/updateSubmit"

        username_set = username
        id_set = id
        password_set = password
        usernamesecret_set = usernameSecret
        description_set = description

        data = {
            "stapler-class": "com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl",
            "scope": "GLOBAL",
            "username": username_set,
            "usernameSecret": usernamesecret_set,
            "password": password_set,
            "$redact": "password",
            "id": id_set,
            "description": description_set,
            "Submit": "",
        }

        data = json.dumps(data)

        response3 = requests.post(update_url, auth=(self.auth_username, self.auth_token),
                                  headers=headers,
                                  data={'json': data})

        if response3.status_code == 200:
            print("Updated successfully!!")

        return response3

    def update_ssh_with__privatekey(self, id, username, privatekey, usernameSecret, description, passphrase):
        # id = input("Enter id : ")

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Jenkins-Crumb': self.crumb
        }

        update_url = self.jenkins_url + f"credential/{id}/updateSubmit"

        username_set = username
        id_set = id
        privatekey_set = privatekey
        usernamesecret_set = usernameSecret
        description_set = description
        passphrase_set = passphrase

        data = {
            "stapler-class": "com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey",
            "scope": "GLOBAL",
            "id": id_set,
            "description": description_set,
            "username": username_set,
            "usernameSecret": usernamesecret_set,
            "privateKeySource": {
                "value": "0",
                "privateKey": privatekey_set,
                "stapler-class": "com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey$DirectEntryPrivateKeySource",
                "$class": "com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey$DirectEntryPrivateKeySource"
            },
            "passphrase": passphrase_set,
            "$redact": "passphrase",
            "Submit": ""
        }

        data = json.dumps(data)

        response3 = requests.post(update_url, auth=(self.auth_username, self.auth_token),
                                  headers=headers,
                                  data={'json': data})

        if response3.status_code == 200:
            print("Updated successfully!!")

        return response3

    def delete(self, id, crumb_url):

        jenkins_crumb = requests.get(crumb_url)
        crumb = jenkins_crumb.json()["crumb"]
        Headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Jenkins-Crumb': crumb
        }


        jenkins_url_deletefunction = self.jenkins_url + f'credential/{id}/doDelete'
        response3 = requests.post(jenkins_url_deletefunction, auth=(self.auth_username, self.auth_token),
                                  headers=Headers)
        print(response3.status_code)
        if response3.status_code == 200:
            return ' Credentials Deleted '

    def get_credentials(self):

        url = self.jenkins_url + 'api/json?tree=credentials[id,description,typeName,displayName]'
        response = requests.get(url)
        return response

# url = 'http://44.212.71.109:8080/manage/credentials/store/system/domain/_/'
#
# with open('config.xml', 'r') as file:
#     xml_data = file.read()
#
# obj1 = credentials(url, 'admin', '1187c4bb500c1cf2595c14fde4f06e0668')
# obj1.create('ppppp', 'bbbbbbbbbb', 'ccccccc')
