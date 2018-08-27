#!/usr/local/bin/python3
print("content-type:text/html; charset=utf-8\n")
import cgi, os, view

'''
for value in files :
        print ('<li><a href="index.py?id={name}">{name}</a></li>'.format(name=value))
#print로 출력하는것보다 listStr을 사용한 이유는 출력을 밑에서 하기위해서 인듯하다.
'''
form = cgi.FieldStorage()
if 'id' in form : #폼에 아이디값이 있냐 없냐? 
        pageId = form["id"].value
        description = open('data/'+pageId,'r').read()
else :
          pageId='Welcome'   
          description='hello web'

print('''
<!doctype HTML>
<html>
<head>
        <title>WEB</title>
        <meta charset="utf-8"> 
        <link rel="stylesheet" href="style.css">
</head>
<body>
       <h1><u><a href="index.py">WEB</a></u></h1>
<ol>
{listStr}
</ol>
<a href="create.py">create</a>
<form action="process_update.py" method="post">
    <input type="hidden" name=pageId value={form_default_title}>
    <p><input type="text" name="title" placeholder="title" value={form_default_title}></p>
    <p><textarea rows="4" name="description" placeholder="description">{form_default_desc}</textarea></p>
    <p><input type="submit"></p>
</form>
</body>
</html>
'''.format(title=pageId,desc=description,listStr=view. getList(),form_default_title=pageId,form_default_desc=description))


