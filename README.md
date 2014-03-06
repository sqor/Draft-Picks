### NOTE: very early prototype

# # Gotchas: change the sleep values if you have slow loading sites.
Works on linux, on mac there are some more tweaks to make.
```
sleep in differ.py and get.js 
```
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


### The report
The report will be generated into a directory with prefix: report_*


Since we are loading the report.json with ajax you can run a quick and simple
http server:

``` 
python -m SimpleHTTPServer 8080
```
Then point your browser to: localhost:8080/

There your directory report_* will be listed.


You should see somethign like this when you click on the repor folder, you
should see:


###  Diff Shot
Each row is red if there are differences for that site comparison
On mouse over the red, you will see the actual diff between the two pages

![](https://raw.github.com/sqor/Draft-Picks/master/diff.png)

### Page 01
This is the first page used for the above diff shot, in this case /sport/mlb  
![](https://raw.github.com/sqor/Draft-Picks/master/page01.png)

### Page 02
This is the second page used for the diff shot, in this case /sport/ufc
![](https://raw.github.com/sqor/Draft-Picks/master/page02.png)

## Deps:
--------------------
sudo apt-get install phantomjs

### Install in OSX

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


