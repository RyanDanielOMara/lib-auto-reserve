# lib-auto-reserve
A Python script that uses Selenium to automatically reserve library rooms

Dependencies:
  Selenium - (assuming pip is installed): pip install selenium
  Chrome Driver - must download the latest release from:
    https://sites.google.com/a/chromium.org/chromedriver/downloads
    Make sure it is in your PATH (place it in usr/bin or usr/local/bin)


Setup for lib.sh:
	Place "lib.sh" into "Home" Directory:
		Update the location of lib-auto-reserve in line 3 of lib.sh
			cd /'''Directory to main.py'''/

Setup for crontab:

	Open Terminal and edit crontab:
		(Optional)
		$ export EDITOR=nano
		(Open with nano, if excluded, crontab will open with VIM by default)

		$ crontab -e

	Update the location of lib.sh and paste the Following into crontab:
		0 0 * * * bash -c 'cd /'''Directory of lib.sh'''/ && sh lib.sh'
		(0 minutes at 0 hours AKA 12 A.M., execute the following)
