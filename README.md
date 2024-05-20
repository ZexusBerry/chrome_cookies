# chrome_cookies
What does it do? Loads cookies used by your web browser into a cookiejar object.
Why is it useful? This means you can use python to download and get the same content you see in the web browser without needing to login.
Which browsers are supported? Chrome, Firefox, LibreWolf, Opera, Opera GX, Edge, Chromium, Brave, Vivaldi, and Safari.
How are the cookies stored? All currently-supported browsers store cookies in a sqlite database in your home directory.
# Install

#!python

> pip install chrome_cookies

-----------------------------------------------------------------------------------------------------------------------------------------------------

# Import

#!python

> from chrome_cookies import Cookies

-----------------------------------------------------------------------------------------------------------------------------------------------------

| How to use |

#!python

>>> from chrome_cookies import Cookies

>>> chrome_cookies = Cookies() # Create an instance of the Cookies class

>>> chrome_cookies.view_cookies() # Use the view_cookies() method to view cookies


-----------------------------------------------------------------------------------------------------------------------------------------------------


for example

#!python

>>> from chrome_cookies import Cookies

>>> a = chrome_cookies = Cookies()
>>> b = chrome_cookies.view_cookies()
>>> print({a}, {b})

-----------------------------------------------------------------------------------------------------------------------------------------------------
