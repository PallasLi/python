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