import os

from youqu_html.conf import setting


def install_depends():
    for p in [
        "openjdk-11-jdk-headless",
    ]:
        if "未找到命令" in os.popen("java --version").read().strip():
            os.system(f"echo '{setting.PASSWORD}' | sudo -S apt update > /dev/null 2>&1")
            os.system(f"echo '{setting.PASSWORD}' | sudo -S apt install {p} -y > /dev/null 2>&1")


if __name__ == '__main__':
    install_depends()
