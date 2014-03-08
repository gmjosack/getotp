
import json
import onetimepass as otp
import os

from version import __version__


class Error(Exception):
    pass


class Secrets(object):
    def __init__(self, filename, secrets):
        self.filename = filename
        self._secrets = secrets

    @staticmethod
    def from_file(filename):
        try:
            with open(os.path.expanduser(filename)) as secrets_file:
                secrets = json.loads(secrets_file.read())
        except IOError:
            secrets = {}

        return Secrets(filename, secrets)

    def save(self):
        with open(os.path.expanduser(self.filename), "w") as secrets_file:
            secrets_file.write(json.dumps(self._secrets))

    def add(self, name, secret):
        if name in self._secrets:
            raise Error("Secret %s already exists." % name)
        self._secrets[name] = secret

    def edit(self, name, secret):
        self._secrets[name] = secret

    def show_all(self):
        return self._secrets.keys()

    def show(self, name):
        if name not in self._secrets:
            raise Error("No such secret (%s)" % name)

        return otp.get_totp(self._secrets[name])
