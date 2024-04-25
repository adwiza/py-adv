from gorse import Gorse

client = Gorse('http://127.0.0.1:8088', '')

test = client.get_recommend('1daful', n=10)

print(test)