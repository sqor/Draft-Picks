# Draft Picks

A simple tool to help you make sure the changes you intended to make are
the only changes (visually at least) that have been made.



### Usage:
-----------------------

Modify sites.json with your own pages.

```
python differ.py
```


In the following sites.json example file, the pages that
would be compared are:

sqor.com/ vs. stage.sqor.com
sqor.com/sport/mlb vs stage.sqor.com/sport/ufc

```

{
    "pages": [
        [ "/",  "/sport/nfl", "/sport/mlb"]
        ,[  "/", "/sport/nba", "/sport/ufc" ]
    ]

    ,   "siteBase01": "http://sqor.com"
    ,   "siteBase02": "http://stage.sqor.com"
}

```


## Deps:
--------------------
sudo apt-get install phantomjs

### Install in OSX, Windowz

http://phantomjs.org/download.html

Mac OS X

Download phantomjs-1.9.7-macosx.zip (9.0 MB) and extract (unzip) the content.

The binary bin/phantomjs is ready to use.

Note: For this static build, the binary is self-contained with no external dependency. It will run on a fresh install of Snow Leopard or later versions. There is no requirement to install Qt or any other libraries.

Alternative installation using Homebrew:

brew update && brew install phantomjs





git clone utils
# Get the path to utils
export PYTHONPATH=/Users/jason/playground/util/python


Testing
python -c "import lib.cmds"

_ = last command in python

?shell.exec_cmd ===> info about that function


dir(obj)


