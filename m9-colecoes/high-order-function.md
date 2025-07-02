>>> 
>>> def run(funcao):
...     print('Início')
...     funcao()
...     print('End')
...     
>>> def hello():
...     print('Olá Rogério, tudo bem?!')
...     
>>> hello()
Olá Rogério, tudo bem?!
>>> run(hello)
Início
Olá Rogério, tudo bem?!
End
>>> 