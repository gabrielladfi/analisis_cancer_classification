import matplotlib.pyplot as plt
from collections import Counter

tipos= [
        "Cáncer de estómago",
        "Cáncer de útero",
        "Cáncer de colon con metástasis",
        "Cáncer de parótida",
        "Cáncer de útero",
        "Sarcoma de Ewing",
        "Mieloma múltiple",
        "Cáncer de cuello uterino",
        "Melanoma ocular",
        "Cáncer de pulmón",
        "Cáncer de mama",
        "Cáncer de próstata",
        "Cáncer ginecológico",
        "Cáncer de pulmón",
        "Cáncer de pulmón",
        "Cáncer de mama",
        "Cáncer de riñón",
        "Cáncer de timo",
        "Cáncer de mama",
        "Cáncer de cuello uterino",
        "Cáncer de próstata metastásico",
        "Cáncer de mama",
        "Cáncer de mama",
        "Cáncer de vesícula",
        "Cáncer de mama",
        "otro",
        "Cáncer de estómago",
        "Cáncer de páncreas",
        "Cáncer de cuello uterino",
        "Cáncer de mama",
        "Cáncer de cuello uterino",
        "Cáncer",
        "Cáncer gástrico",
        "Cáncer cerebral",
        "Cáncer de útero",
        "Cáncer de colon",
        "otro",
        "Cáncer de útero",
        "Cáncer de vesícula",
        "Cáncer de endometrio",
        "Cáncer de cuello uterino",
        "otro",
        "Linfoma de Hodgkin",
        "Cáncer de útero",
        "Cáncer de colon",
        "otro",
        "otro",
        "otro",
        "Cáncer de mama",
        "Cáncer de pulmón",
        "Cáncer de ovario",
        "Cáncer de origen desconocido",
        "Cáncer de útero",
        "Cáncer de mama",
        "Cáncer colorrectal",
        "Cáncer de riñón",
        "otro",
        "Cáncer de ovario",
        "Cáncer de estómago",
        "Cáncer de pulmón",
        "Cáncer de próstata",
        "Leucemia",
        "Cáncer de útero",
        "otro",
        "Cáncer de próstata",
        "Cáncer de mama",
        "Cáncer de mama",
        "Cáncer colorrectal",
        "Cáncer de mama",
        "Cáncer gástrico",
        "Cáncer de páncreas",
        "Cáncer de hígado",
        "Cáncer de mama",
        "Cáncer de útero",
        "otro",
        "Cáncer de colon",
        "Cáncer de mama",
        "Cáncer de colon",
        "Cáncer de origen desconocido",
        "Cáncer de endometrio",
        "Cáncer de mama",
        "Cáncer de hígado",
        "Cáncer de hígado",
        "Cáncer de mama",
        "otro",
        "Cáncer de mama",
        "Cáncer de mama",
        "Leucemia linfocítica crónica",
        "Cáncer de mama",
        "Cáncer de mama",
        "Cáncer ductal in situ",
        "Cáncer de cuello uterino",
        "otro",
        "Cáncer de colon",
        "Cáncer de vagina",
        "Cáncer de mama",
        "Cáncer de pulmón",
        "Cáncer de vejiga",
        "otro",
        "Cáncer de ovario",
        "Cáncer de hígado",
        "Cáncer de ovario",
        "Cáncer de mama",
        "Cáncer de ovario",
        "otro",
        "Cáncer de cavidad oral",
        "Cáncer colorrectal",
        "Cáncer de pulmón",
        "Cáncer de páncreas",
        "Cáncer cerebral",
        "Cáncer de colon",
        "Cáncer de vías biliares",
        "Cáncer de mama",
        "Cáncer de próstata",
        "Cáncer de mama",
        "Cáncer de ovario",
        "Cáncer de pulmón",
        "Sarcoma de Ewing",
        "Cáncer de pulmón",
        "Cáncer de riñón",
        "Cáncer de mama",
        "Cáncer colorrectal",
        "otro",
        "Cáncer de riñón",
        "Cáncer de mama",
        "Cáncer de mama",
        "otro",
        "Mieloma múltiple",
        "Cáncer de estómago",
        "Cáncer de colon",
        "otro",
        "Cáncer de próstata",
        "Cáncer de mama"
    ]


word_counts = Counter(tipos)

# Extraer las palabras y sus frecuencias
labels = list(word_counts.keys())
sizes = list(word_counts.values())

# Función para filtrar etiquetas menores al 3%
def autopct_filter(percent):
    return ('%1.1f%%' % percent) if percent >= 3 else ''

# Crear la gráfica pastel
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct=autopct_filter, startangle=140)
plt.axis('equal')  # Para asegurar que el gráfico sea un círculo
plt.title('Tipos de cáncer detectados en los Clientes')

# Mostrar la gráfica
plt.show()