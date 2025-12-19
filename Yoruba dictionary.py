print("Welcome to the Language Dictionary")
language = input("What language dictionary would you like to use? edo, hausa, idoma, igbo or yoruba?\n")

yoruba = yoruba_dict = {
    "Favour": "Ọ̀nugba",
    "God": "Olọ́run",
    "Time": "Àkókò",
    "Faith": "Ìgbàgbọ́",
    "Prosper": "Yọ̀",
    "Longevity ": "Gbigbe laaye",
    "Family": "Ebi ",
    "Love": " Ifẹ́",
    "King": "Ọba",
    "Queen": "Ọba ẹbi",
    "Prince": "Ọmọba",
    "Princess": "Ọmọbinrin",
    "Joy": " Ayọ̀",
    "Wisdom": "Ọgbọ́n",
    "Fortune": "Ọrẹ",
    "Happiness": "Alafia ",
    "Beauty": "Ẹ̀wà",
    "Excellence": "Àṣe",
    "Strength": "Agbara",
    "Success":"Asese"

}
print("Welcome to the Yoruba Dictionary, there are 20 registered words in this dictionary.Please select the English word you would like to translate to Yoruba:")


key = input("Favour, God, Time, Faith, Prosper, Longevity, Family, Love, King, Queen, Prince, Princess, Joy, Wisdom, Fortune, Happiness, Beauty, Excellence, Strength, Success\n")
if key in yoruba:
    print(f"The meaning of {key} in yoruba is {yoruba[key]} ")


else:
    print("This word is not registered in this dictionary")