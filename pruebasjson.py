import json

def calcular_rewards(data):
    
    usuario = [] 
          
        





data ={
  "users": [
    {
      "id": 1,
      "name": "Juan Pérez",
      "transactions": [
        {
          "id": "T1",
          "amount": 200,
          "date": "2024-01-15",
          "category": "groceries"
        },
        {
          "id": "T2",
          "amount": 450,
          "date": "2024-02-20",
          "category": "entertainment"
        }
      ],
      "rewards": [
        {
          "type": "bonus",
          "points": 50
        }
      ]
    },
    {
      "id": 2,
      "name": "María García",
      "transactions": [
        {
          "id": "T3",
          "amount": 150,
          "date": "2024-03-10",
          "category": "groceries"
        },
        {
          "id": "T4",
          "amount": 300,
          "date": "2024-04-05",
          "category": "travel"
        }
      ],
      "rewards": []
    }
  ]
}

"""Aquí tienes un ejercicio más avanzado basado en el ejemplo anterior. Este ejercicio implica trabajar con JSON anidado, 
cálculos adicionales y la creación de un informe estructurado.

Ejercicio:
Dado el siguiente JSON que representa usuarios, transacciones y detalles adicionales sobre puntos y recompensas, 
escribe una función en Python que procese la información y genere un informe en forma de JSON.

Requisitos:
Calcula el total de puntos para cada usuario, considerando que:

Cada transacción en la categoría "groceries" otorga 1 punto por cada 10 unidades de amount.
Cada transacción en la categoría "entertainment" otorga 2 puntos por cada 10 unidades de amount.
Cada transacción en la categoría "travel" otorga 3 puntos por cada 10 unidades de amount.
Suma los puntos de recompensas adicionales en la clave "rewards" a los puntos calculados de las transacciones.

Genera un informe en JSON con el siguiente formato:
[
    {
        "user_id": 1,
        "name": "Juan Pérez",
        "total_points": 145,
        "details": {
            "groceries_points": 20,
            "entertainment_points": 90,
            "travel_points": 0,
            "bonus_points": 50
        }
    },
    {
        "user_id": 2,
        "name": "María García",
        "total_points": 90,
        "details": {
            "groceries_points": 15,
            "entertainment_points": 0,
            "travel_points": 75,
            "bonus_points": 0
        }
    }
]

Instrucciones:
Define una función generar_informe(data) que reciba como entrada el JSON de datos.
Para cada usuario, calcula los puntos de cada categoría (groceries, entertainment, travel) y los puntos adicionales (bonus).
Suma los puntos para calcular el total_points y agrega los detalles de puntos de cada categoría en el informe.
Devuelve el informe como un JSON.

Puntos adicionales a considerar:
Asegúrate de manejar usuarios sin transacciones o sin recompensas ("rewards": []).
Incluye una estructura clara y utiliza variables temporales para calcular cada parte, como los puntos de cada categoría y el total.
Este ejercicio te ayudará a profundizar en el recorrido de JSONs complejos, en la lógica condicional para sumar puntos, 
y en la construcción de JSONs estructurados a partir de datos procesados. ¡Intenta resolverlo y avísame si necesitas ayuda!



"""