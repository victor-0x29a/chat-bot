# The engine

<center>
  
  ## Creating actions
  
  ###### To create actions or responses, just go to the file /config/data.py and add them to the "PhRaseActions" list. See its structure below.

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

 ###### Leave the UUID field as the total size of the list minus one. The "Words" list is responsible for identifying the phrase and redirecting to the action or response. Let's take an example: if we want the user to say, "Generate a value between 5 and 4," then add the words "generate," "value," "between," "5," and "4" to the "Words" list.

 ###### Adding these values to the "Words" list, let's move on to the "Actions" section. Leave the "url" field empty and add the main vector in the "vectors" field, which will capture the values. In the example given, we need to capture the values 5 and 4. The word preceding these values is "entre," so add the word "entre" to the "vectors" field. Now, set the "type" field as "str," leave the "payload" and "response" fields empty, and in the "action" field, input the function that receives the values "5 and 4," which will be captured after the "entre" vector.

 ###### With that, simply complete your function by removing non-numeric values and continue your action. After completing your function, return by speaking with the speak() function. Inside speak(), use getPhrase(). Within getPhrase(), include a list of possible responses!
</center>
<hr/>

<center>
  
  ## Creating responses
  
  ###### To create actions or responses, just go to the file /config/data.py and add them to the "PhRaseActions" list. Here is its structure.

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

 ###### Leave the UUID field as the total size of the list minus one. The "Words" list is responsible for identifying the phrase and redirecting to the action or response. Let's take an example: if we want the user to say, "Who is your creator?" then add the words "who," "creator," and "your" to the "Words" list.

 ###### Adding these values to the "Words" list, let's move on to the "Actions" section. Leave the "url" and "vectors" fields empty. Set the "type" field as "str," leave the "payload" field as an empty list "[]". In the "response" field, provide possible responses, and in the "action" field, set it as False.

 ###### After this, the algorithm will automatically recognize that it is a response question and will respond with a random answer from the "response" vector!
  
</center>

<hr/>

> Fun Facts
> * Developed in less than two days.
> * In future versions, I will integrate it with NodeJS.
> 
<br/>

> Libraries
> * os
> * pyautogui
> * gtts
> * playsound
> * math
> * random
> * time

<br/>
    
 ###### Python Version Used: 3.11
 ###### Repository Version: 1.0

