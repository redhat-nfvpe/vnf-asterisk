# Sippy Cup

Sippy cup is a Ruby application that can be used to generate SIPp scenario
files, making the execution of different SIP call scenarios significantly
simpler. The real trick is that you have to deal with Ruby...

## Installing Ruby

First, you need to grab a newer version of Ruby than what comes with CentOS
7. If you're on Fedora then maybe this step will be unnecessary and you can
install from `dnf`.

Assuming you're on CentOS 7, run the following commands.

```
\curl -sSL https://get.rvm.io | bash -s stable
source /etc/profile.d/rvm.sh
rvm reload
rvm install 2.3.0
```

## Installing Sippy Cup

Next up is to install Sippy Cup.

```
yum install libpcap-devel -y
gem install packetfu -v 1.1.11  # latest version breaks sippy cup
gem install sippy_cup
```

## Running a Scenario

Now you can run a scenario against your Asterisk box at 127.0.0.1.

```
cd ~/src/vnf-asterisk/resources/sippy_cup/
sippy_cup -r test_scenario.yml
```
