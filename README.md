# chrome_cookies
What does it do? Loads cookies used by your web browser into a cookiejar object.
Why is it useful? This means you can use python to download and get the same content you see in the web browser without needing to login.
Which browsers are supported? Chrome.
How are the cookies stored? All currently-supported browsers store cookies in a sqlite database in your home directory.

```python
import os
print(os.getcwd())
```

# Install

<pre>
pip install chrome_cookies
</pre>
-----------------------------------------------------------------------------------------------------------------------------------------------------

# Import

<pre>
from chrome_cookies import Cookies
</pre>
-----------------------------------------------------------------------------------------------------------------------------------------------------

# | How to use |

<pre>
from chrome_cookies import Cookies

chrome_cookies = Cookies() # Create an instance of the Cookies class

chrome_cookies.view_cookies() # Use the view_cookies() method to view cookies
</pre>

-----------------------------------------------------------------------------------------------------------------------------------------------------


# for example

<pre>
from chrome_cookies import Cookies

a = chrome_cookies = Cookies()
b = chrome_cookies.view_cookies()
print({a}, {b})
</pre>
-----------------------------------------------------------------------------------------------------------------------------------------------------
