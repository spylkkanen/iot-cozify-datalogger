# Python Cozify Datalogger

## Installation

1. `sudo su`

2. `apt-get install python3-pip`

3. `apt-get install postfix`. https://askubuntu.com/questions/222512/cron-info-no-mta-installed-discarding-output-error-in-the-syslog
> In postfix confuguration you can choose "No configuration" option.

4. `pip3 install -U cozify`.
https://pypi.org/project/cozify/0.2/


## Authentication
Create authentication to Cozify.

1. Create device authentication key with command `python3 cloudauth.py`.
```
root@ubuntu:/home/ftpuser/cofizy-datalogger# python3 cloudauth.py
Enter your Cozify account email address: <YOUR_EMAIL>
OTP from your email: <ONE_TIME_PASSWORD_FROM_EMAIL>
root@ubuntu:/home/ftpuser/cofizy-datalogger#
```
> Authentication must be done before any Cozify data can be readed.

## Cozify devices

Example 1. Read all cozify devices `python3 devices_all.py`. Result is printed in JSON format.

Example 2. Read all `TEMPERATURE`, `MOTION` and `CONTACT` cozify devices `python3 devices.py`. Result is printed as plain text.


## Cozify temperature Datalogger (csv-file)

1. Schedule task with Crontab
https://vitux.com/how-to-schedule-tasks-on-ubuntu-using-crontab/

2. `crontab -e`
```
root@ubuntu:/home/ubuntu# crontab -e
no crontab for root - using an empty one

Select an editor.  To change later, run 'select-editor'.
  1. /bin/nano        <---- easiest
  2. /usr/bin/vim.basic
  3. /usr/bin/vim.tiny
  4. /bin/ed

Choose 1-4 [1]: 1
No modification made
root@ubuntu:/home/ubuntu#
```
> Choice 1 is easiest.

3. Add cron task to run cozify temperature sensor read on every 15 minutes.
https://crontab.guru/every-15-minutes

```
MAILTO=""
...
*/15 * * * * cd /home/ftpuser/cofizy-datalogger && python3 task_device_temperature.py >> /home/ftpuser/cofizy-datalogger/crontab.log
```
https://askubuntu.com/questions/222512/cron-info-no-mta-installed-discarding-output-error-in-the-syslog

4. Check cron errors after 15 minutes. `grep CRON /var/log/syslog`.

5. Csv result. `nano device_temperatures.csv`
```
"Keittiö","2020-04-19 18:53:26","24,1",""| Measurement saved.
"Lastenhuone","2020-04-19 18:53:38","23,3",""| Measurement saved.
"Työhuone","2020-04-19 18:53:23","24,1",""| Measurement saved.
root@ubuntu:/home/ftpuser/cofizy-datalogger#
```