import requests

payload = [('rm','88894' ), ('senha','wOgIW59FEk' )]
r = requests.post('https://dc1-2021.glitch.me/getHash', payload)

print(r.text)