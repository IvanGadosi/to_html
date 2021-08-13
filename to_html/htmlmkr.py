_head_tags={
  "title": "<title>{}</title>",
  "style": "<style>\n  {}\n  </style>",
  "link": "<link rel='{}' href='{}'>"
}
_body_tags={
  "a": "<a href='{1}'>{0}</a>",
  "b": "<b>{}</b>",
  "br": "<br>",
  "button": "<button>{}</button>",
  "canvas": "<canvas id='{}'></canvas>",
  "caption": "<caption>{}</caption>",
  "footer": "<footer>{}</footer>",
  "h1": "<h1>{}</h1>",
  "h2": "<h2>{}</h2>",
  "h3": "<h3>{}</h3>",
  "h4": "<h4>{}</h4>",
  "h5": "<h5>{}</h5>",
  "h6": "<h6>{}</h6>",
  "hr": "<hr>",
  "img": "<img src='{}'>",
  "p": "<p>{}</p>",
  "pre": "<pre>{}</pre>",
  "script": "<script>\n  {}\n  </script>",
  "small": "<small>{}</small>",
  "strong": "<strong>{}</strong>",
  "label": "<label for='{1}'>{0}</label>",

  "comment": "<!--{}-->",

  "address": "<address>",
  "end address": "</address>",

  "article": "<article>",
  "end article": "</article>",

  "aside": "<aside>",
  "end aside": "</aside>",

  "details": "<details>",
  "end details": "</details>",

  "div": "<div class='{}'>",
  "end div": "</div>",

  "form": "<form action='{}' method='{}'>",
  "end form": "</form>",

  "header": "<header>",
  "end header": "</header>",

  "nav": "<nav>",
  "end nav": "</nav>",

  "picture": "<picture>",
  "end picture": "</picture>",
}
_html_tags={**_head_tags,**_body_tags}



class HtmlFile:
  """
  Create html tags entirely in python
  """
  def __init__(self):
    self.head=[]
    self.body=[]

  def add_element(self, tag, *args):
    """
    One required argument 'tag'
    """
    text_with_tag="{}".format(_html_tags[tag].format(*args))
    if tag in _head_tags.keys():
      self.head.append(f"\n  {text_with_tag}")
    else:
      self.body.append(f"\n  {text_with_tag}")

  def create_file(self, file_name="result", extension="html"):
    """
    Saves created html into file, default file name 'result', default file extension 'html'
    """
    with open(f"{file_name}.{extension}", "a") as f:
      f.write("<!DOCTYPE html>\n<html>\n<head>\n  <meta charset='utf-8'>")
      for head_element in self.head:
        f.write(head_element)
      f.write("\n</head>\n<body>")
      for body_element in self.body:
        f.write(body_element)
      f.write("\n</body>\n</html>")


def main():
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

if __name__=="__main__":
  main()