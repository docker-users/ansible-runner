#! /usr/bin/env python3
import os
import sys

def setup_ssh():
    print("[ansible-runner] setup ssh")
    return SSHKey(env_name="SSH_DEPLOY_KEY")

def setup_ansible_vault():
    print("[ansible-runner] setup ansible vault")
    return AnsibleVault(env_name="ANSIBLE_VAULT_ID")

def main(args):
    if not args:
        print("missing args")
        return
    if not args[0].startswith("ansible"):
        code = os.system(" ".join(args))
        exit(code)
        return
    with setup_ssh(), setup_ansible_vault():
        code = os.system(" ".join(args))
        pass
    exit(code)
    pass

if __name__ == '__main__':
    main(sys.argv[1:])
    pass


class SSHKey:
    def __init__(self, env_name="SSH_DEPLOY_KEY"):
        privateKey = os.environ.get(env_name)
        if not privateKey:
            raise Exception(f"missing environment var '{env_name}'")
        self.privateKey = privateKey
        self.fpath = os.path.expanduser("~/.ssh/id_rsa")
        pass

    def __enter__(self):
        print(f"[ansible-runner] create ssh key file: {self.fpath}")
        os.makedirs(os.path.dirname(self.fpath), exist_ok=True, mode=0o700)
        with open(self.fpath, "w") as fp:
            fp.write(self.privateKey)
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        os.remove(self.fpath)
        print(f"[ansible-runner] remove ssh key file: {self.fpath}")
        pass


class AnsibleVault:
    def __init__(self, env_name="ANSIBLE_VAULT_ID"):
        vault_passwd = os.environ.get(env_name)
        if not vault_passwd:
            raise Exception(f"missing environment var '{env_name}'")
        self.password = vault_passwd
        self.fpath = os.environ.get("ANSIBLE_PASSWORD_FILE", self._default_path())
        pass

    def _default_path(self):
        return os.path.expanduser("~/.ansible-vault")

    def __enter__(self):
        with open(self.fpath, "w") as fp:
            fp.write(self.password)
        print(f"[ansible-runner] create vault password file: {self.fpath}")
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        os.remove(self.fpath)
        print(f"[ansible-runner] remove vault password file: {self.fpath}")
        pass
