import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token','5361466307:AAEW1J_jmSu5gCIiEtmKPzwapGSUxXeDvvw')
API_ID =  os.environ.get('api_id','28341593')
API_HASH = os.environ.get('api_hash','13b1607f156d7a7f0c755dbf4ea5061a')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','iamcracks').split(';')
PROXY = ProxyCloud.parse(os.environ.get('proxy_enc','socks5://KDDKKGYJJIJFGFYIJFGJGGYFJEJIKKRGDJLKDFLH'))

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
