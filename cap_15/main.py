import requests

payload = [('rm','{user}' ), ('senha','{pass}' )]
r = requests.post('https://dc1-2021.glitch.me/getHash', payload)

print(r.text)