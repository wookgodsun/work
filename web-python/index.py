#!/usr/local/bin/python3
print("content-type:text/html; charset=utf-8\n")
import cgi, os, view, html_sanitizer
sanitizer = html_sanitizer.Sanitizer()
'''
for value in files :
        print ('<li><a href="index.py?id={name}">{name}</a></li>'.format(name=value))
#print로 출력하는것보다 listStr을 사용한 이유는 출력을 밑에서 하기위해서 인듯하다. 
'''
form = cgi.FieldStorage()


if 'id' in form : #폼에 아이디값이 있냐 없냐? 
        pageId = form["id"].value
        description = open('data/'+pageId,'r').read()
        description = sanitizer.sanitize(description)
        
        update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
        delete_action = '''
        <form action="process_delete.py" method="post"> 
        <input type="hidden" name="pageId" value="{}">
        <input type="submit" value="delete">
        </form>
        '''.format(pageId)
        #form 첫번쨰줄은 process_delete라는 파일로 보내라는뜻이고 보이지않게 post방식을 이용 
        #전달되는 인자에 관한 설명은 input으로   value는 초기값, name은 넘어오는값 type은 보내지는 방식을 의미 
else :
          pageId='Welcome'   
          description='hello web'
          update_link=''
          delete_action=''

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
{update_link}
{delete_action}
<h2>{title}</h2>
{desc}
</body>
</html>
'''.format(title=pageId,
desc=description,listStr=view.getList(),
update_link=update_link,delete_action=delete_action))
