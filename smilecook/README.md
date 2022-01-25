# Exercitando-com-Python

Colocando em pratica meus conhecimento em Python

Aplicação consiste em contrução de perfil, consultas e publicações de receitas culinarias

A aplicação foi produzida utilizando flask e suas bibliotecas

Exemplo de solicitação via terminal
curl -i -X POST localhost:5000/recipes -H "Content-Type: application/json" -d '{"name":"Cheese Pizza", "description":"This is a lovely cheese pizza", "num_of_servings":2, "cook_time":30, "directions":"This is how you make it" }'
curl -i -X POST localhost:5000/recipes -H "Content-Type: application/json" -d '{"name":"Tomato Pasta", "description":"This is a lovely tomato pasta recipe", "num_of_servings":3, "cook_time":20, "directions":"This is how you make it"}'

recuperar receitas
curl -i -X GET localhost:5000/recipes 

publicar
curl -i -X PUT localhost:5000/recipes/1/publish 

atualizar
curl -i -X PUT localhost:5000/recipes/1 -H "Content-Type: application/json" -d '{"name":"Lovely Cheese Pizza", "description":"This is a lovely cheese pizza recipe", "num_of_servings":3, "cook_time":60, "directions":"This is how you make it"}'