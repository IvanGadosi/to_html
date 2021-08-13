### About The Project
The purpose of this project is to create a script, that allows anyone to create their own html files entirely in python.

### Input
```sh
  from htmlmkr import *
  x=HtmlFile()
  x.add_element("style", "p {color:blue;} .content{margin:50px;}")
  x.add_element("title", "my site")
  x.add_element("div", "content")
  x.add_element("p", "ha, i am blue")
  x.add_element("a", "my text", "https://manganato.com/")
  x.add_element("br")
  x.add_element("hr")
  x.add_element("strong", "strong text")
  x.add_element("end div")
  x.add_element("comment", "cant see me")
  x.create_file()
```

### Output
```sh
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset='utf-8'>
    <style>
    p {color:blue;} .content{margin:50px;}
    </style>
    <title>my site</title>
  </head>
  <body>
    <div class='content'>
    <p>ha, i am blue</p>
    <a href='https://manganato.com/'>my text</a>
    <br>
    <hr>
    <strong>strong text</strong>
    </div>
    <!--cant see me-->
  </body>
  </html>
```
