#code-utf8
#mytokennumber
#2bd8227c955edab62e6ac3e0f5a5299d876a347c

import bitly_api
import requests
banner="""


██╗     ██╗███╗   ██╗██╗  ██╗    ██╗  ██╗██╗███████╗ █████╗ ██╗  ████████╗███╗   ███╗ █████╗ 
██║     ██║████╗  ██║██║ ██╔╝    ██║ ██╔╝██║██╔════╝██╔══██╗██║  ╚══██╔══╝████╗ ████║██╔══██╗
██║     ██║██╔██╗ ██║█████╔╝     █████╔╝ ██║███████╗███████║██║     ██║   ██╔████╔██║███████║
██║     ██║██║╚██╗██║██╔═██╗     ██╔═██╗ ██║╚════██║██╔══██║██║     ██║   ██║╚██╔╝██║██╔══██║
███████╗██║██║ ╚████║██║  ██╗    ██║  ██╗██║███████║██║  ██║███████╗██║   ██║ ╚═╝ ██║██║  ██║
                                                                                                                                                                                                                  
"""

print(banner)
print("\n")

Access_Token="2bd8227c955edab62e6ac3e0f5a5299d876a347c"
connection=bitly_api.Connection(access_token=Access_Token)
url=input("URL GİRİNİZ : ")
print("\n")
shorten_url=connection.shorten(url)

print("URL: ",shorten_url.get("url"))
print("Linkiniz kısaltılmıştır.")
print("naber")