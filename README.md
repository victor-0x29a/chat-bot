# chat-bot


## Como o nome diz, eu criei um simples algoritmo de chat-bot, onde no arquivo principal "index.py" contém uma classe que serve como o motor do algoritmo.


<center>Criar ações</center>
 ###### Para criar ações ou resposta basta ir no arquivo /config/data.py e adicionar na lista "PhRaseActions", segue o corpo dela.
 
```
 {
   "UUID": 4, 
   "Words": [""], 
   "Actions": {"url": "", "vetores": []},
   "type": "str",
   "payload": [], 
   "response": [""], 
   "action": Math
 }
```

###### O campo UUID deixe como o tamanho total da lista subtraindo um, a lista "Words" fica responsável por identificar a frase e redirecionar para a ação ou resposta, então vamos para um exemplo, caso vamos querer que o usuário fale - "Gere um valor entre 5 e 4"; Então vamos adicionar na "Words" as palavras "gere", "valor", "entre", "um";

###### Adicionando esses valores na lista "Words", vamos partir para o valor "Actions", com isso deixe o campo "url" vazia e adicione no campo "vetores" o vetor principal que vai pegar os valores, como no exemplo passado, vamos ter que pegar o valor 5 e 4, então a palavra anterior a esses valores é a palavra "entre", com isso, basta adicionar a palavra "entre" no campo "vetores"; Deixe agora o campo "type" como "str", deixe o campo "payload" e "response" vazio e no campo "action", coloque a função que pega recebe os valores "5 e 4" que vai ser pego após o vetor "entre".

###### Com isso basta finalizar sua função retirando os valores que não são núméricos e continuar sua ação, após concluir sua função, basta retornar falando com a função speak() e dentro de speak getPhrase(), dentro de "getPhrase()" coloque uma lista de possíveis respostas!
