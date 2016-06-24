'''
Created on 2016年3月22日

@author: lyt
'''
# import httplib2
# import httplib 
# import urllib  
#   
#    
# def sendhttp():  
#     data = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})     
#     headers = {"Content-type": "application/x-www-form-urlencoded",  
#                "Accept": "text/plain"}  
#     conn = httplib.HTTPConnection('bugs.python.org')  
#     conn.request('POST', '/', data, headers)  
#     httpres = conn.getresponse()  
#     print httpres.status  
#     print httpres.reason   
#     print httpres.read()  
#              
#                 
# if __name__ == '__main__':    
#     sendhttp()    





# Requests is an Apache2 Licensed HTTP library, written in Python, for human beings.

# Python’s standard urllib2 module provides most of the HTTP capabilities you need, but the API is thoroughly broken. It was built for a different time — and a different web. It requires an enormous amount of work (even method overrides) to perform the simplest of tasks.

# Things shouldn’t be this way. Not in Python.

# >>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# >>> r.status_code
# 200
# >>> r.headers['content-type']
# 'application/json; charset=utf8'
# >>> r.encoding
# 'utf-8'
# >>> r.text
# u'{"type":"User"...'
# >>> r.json()
# {u'private_gists': 419, u'total_private_repos': 77, ...}
