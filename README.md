# som-notify

## Purpose

som-notify is a little application that notifies you when:

* New partner joins Som Energia
* New contract is made with Som Energia
* Some news are updated from wakelet generation plants news.

## Python Requeriments

* `pip install plyer`
* `sudo apt-get install libnotify-bin notification-daemon dbus`

## Run

* `python get_partners_and_contracts.py`


=======

## Linux requirements

* Be sure libnotify-bin and notification-daemon are installed. For example, on Raspbian images it doesn't come with the image, but can be easy installed with apt command:

`sudo apt-get install libnotify-bin notification-daemon dbus`

If you try to manually start the notification daemon:

'/usr/lib/notification-daemon/notification-daemon'

you will get an error and the daemon will not start. The error message is something like this:
	
~~~~
Error retrieving accessibility bus address: org.freedesktop.DBus.Error.ServiceUnknown: 
The name org.a11y.Bus was not provided by any .service files	
~~~~
To fix this install the at-spi2-core package:

'sudo apt install at-spi2-core'
confirm the fix by invoking the daemon:

'/usr/lib/notification-daemon/notification-daemon'
and then from a separate terminal window send a test message:

'notify-send "Test" "It works!"'


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

