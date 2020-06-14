# ocw-api-wrapper

This is an API Wrapper for GraphQL access to [Our Canadian Wiki](https://wiki.ourcanadian.ca).

To install and use this Ocwa you need have [git](https://git-scm.com/downloads), [python3](https://www.python.org/downloads/), and [pip3](https://vgkits.org/blog/pip3-windows-howto/) installed (these are all included in Mac dev-tools but will need to be added manually on Windows).


Open your command terminal in the directory in which you would like to Ocwa and clone the repo.
```
git clone url
```

Enter the repo and install the neccassary libraries.
```
cd ocw-api-wrapper
pip3 install -r requirements.txt
```

Check to make sure everything worked by running a connection test.
```
python3 test-connection.py
```

In order to get to the good stuff, you will need an API Token, which can only be created by an admin. Request an API Token from an admin or via rylancole@ourcanadian.ca. Once you have an API Token, it must be securely stored as an eviroment variable. I will detail how to do this on a UNIX system.

Write the the ```.bashrc``` file.
```
vim ~/.bashrc
```

Add the export line, replacing ```YOUR_API_TOKEN``` with your API Token.
```
export OCWA_TOKEN="YOUR_API_TOKEN"
```
You can use a name other than ```OCWA_TOKEN```, just be sure to remember it for later.

Refresh.
```
source ~/.bashrc
```

Now you can test that your API Token.
```
python3 test-token.py
```
Or if you used a name other than the default ```OCWA_TOKEN``` add it as arguement.
```
python3 test-token.py VAR_NAME
```





