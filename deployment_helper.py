import os
import sys


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def install_rvm():
    print("Downloading GPG Signatures")
    os.system(
        "gpg --keyserver hkp://keys.gnupg.net --recv-keys \
         409B6B1796C275462A1703113804BB82D39DC0E3")
    print("\n\nInstalling RVM ..........")
    os.system("\curl -sSL https://get.rvm.io | bash -s stable")
    print("\n\nLoading RVM ........")
    os.system("source ~/.rvm/scripts/rvm")
    print("\n\nInstalling RVM Dependencies....")
    os.system("rvm requirements")
    os.system("rvmsudo /usr/bin/apt-get install build-essential openssl libreadline6 libreadline6-dev curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf libc6-dev ncurses-dev automake libtool bison subversion")
    print("\n\nFinished install")


def install_ror():
    print("Installing Ruby 2.3.1")
    os.system('rvm install 2.3.1')
    print("\n\nSetting version 2.3.1 as default")
    os.system("rvm use 2.3.1 --default")
    print("\n\nInstalling Ruby Gems")
    os.system("rvm rubygems current --force")
    print("\n\nInstalling Rails")
    os.system("gem install rails -v 4.2.7 --no-ri --no-rdoc")


def main():
    try:
        if sys.argv[1] == "-install-rvm":
            install_rvm()
        elif sys.argv[1] == '-install-ror':
            install_ror
    except IndexError:
        print("Possible Arguments")
        print('\t-install-rvm')
        print('\t-install-ror')


if __name__ == '__main__':
    clear()
    print("Welcome to Rails Deployment Helper")
    main()
