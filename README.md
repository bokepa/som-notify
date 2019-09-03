# som-notify

## Purpose

som-notify is a little application that notifies you when:

* New partner joins Som Energia
* New contract is made with Som Energia
* Some news are updated from wakelet generation plants news.

## Python Requeriments

`pip install plyer`
`sudo apt-get install libnotify-bin notification-daemon dbus`

## Run

`python get_partners_and_contracts.py`

## ToDo

- Detect new values on a simple while loop
- When value, alert to console
- When change, notify thorugh module
- Settings
- Time Delay config (in secs)
- Outputs
	- Macos Notification
	- Twitter
	- Send Mail
	- Sing a Song

