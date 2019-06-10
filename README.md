# Parser for telegram groups

An application for sending messages to telegram accounts via their ID's which is saved in example.txt

---

### How to use it

To begin, you must fill the 'tlt_conf_github.py' file with the following:

* app_id=111111    *- application id, [more info](https://core.telegram.org/api/obtaining_api_id)*
* app_hash='11xx11..' *- application hash, [more info](https://core.telegram.org/api/obtaining_api_id)*
* sess='xxx'        *- the name of your session to login in tlgrm with your acc*
* gr_name='xxx'     *- the name of a group where you get users to send messages from*

Then you need to prepare your example.txt. First line has to contain group link in "https://t.me/xxxxxx" format. Symbol "_" is used like separator. After first "_" on a new line goes person's ID, then on a new line message (until next separator) you want to send to them. Separator at the very end is not needed.



After saving the file, you can run the program in folder where its saved as follows: "python3 tlthn2.py .

All errors and successful sendings you can observe in file "log.txt".

File "si.py" is needed to log in in your telegram account and to get a "SOMENAME.session" file (to be able to log in telegram immediately in the future).
---

### Used libraries

* [xlrd](https://github.com/python-excel/xlrd)
* [telethon](https://github.com/LonamiWebs/Telethon)

