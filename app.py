import random

story_elements = {
    "aventura": {
        "characters_m": [
            "um viajante", "um mago", "um cavaleiro", "um príncipe", "um explorador",
            "um anão", "um dragão", "um ogro", "um pirata", "um assassino",
            "um guerreiro", "um bobo da corte", "um rei", "um ladrão", "um plebeu", "um tritão"
        ],
        "characters_f": [
            "uma viajante", "uma maga", "uma cavaleira", "uma princesa", "uma exploradora",
            "uma anã", "uma dragoa", "uma ogra", "uma pirata", "uma assassina",
            "uma guerreira", "uma boba da corte", "uma rainha", "uma ladra", "uma plebeia", "uma sereia"
        ],
        "settings": [
            "em uma floresta misteriosa", "num castelo antigo", "em uma ilha perdida",
            "em uma montanha congelante", "em um deserto", "em uma cidade medieval",
            "no mar aberto", "em um parque de diversão mágico", "numa arena lendária",
            "em um reino distante", "em uma batalha sangrenta"
        ],
        "conflicts": [
            "em busca de um tesouro escondido", "lutando contra forças sombrias",
            "tentando salvar o reino", "ajudando os necessitados", "batalhando entre reinos",
            "enfrentando um inimigo traiçoeiro", "tentando escapar de uma armadilha",
            "num casamento arranjado", "preso num abismo sem fim"
        ],
        "resolutions": [
            "e encontrou a verdadeira coragem.", "mas acabou descobrindo a sua própria força.",
            "e mudou o destino de todos.", "mas terminou da mesma forma que começou.",
            "mas se voltou para o lado inimigo.", "mas não soube lidar com seu orgulho.",
            "e encontrou seu verdadeiro eu.", "mas usou de artimanhas desonestas.",
            "e terminou sozinho."
        ]
    },

    "romance": {
        "characters_m": [
            "um poeta solitário", "um viajante romântico", "um príncipe",
            "um músico apaixonado", "um jovem sonhador"
        ],
        "characters_f": [
            "uma jovem sonhadora", "uma princesa", "uma bailarina",
            "uma artista", "uma escritora romântica"
        ],
        "settings": [
            "em um jardim florido", "num baile encantado", "à beira-mar",
            "em uma pequena vila", "num café aconchegante"
        ],
        "conflicts": [
            "em busca do amor verdadeiro", "tentando superar a distância",
            "vivendo um amor proibido", "enfrentando segredos do passado"
        ],
        "resolutions": [
            "e descobriram que o amor sempre vence.",
            "mas aprenderam a importância da entrega.",
            "e viveram felizes para sempre.",
            "mas entenderam que nem todo amor dura para sempre."
        ]
    },

    "terror": {
        "characters_m": [
            "um detetive", "um cientista", "um padre", "um viajante solitário",
            "um caçador de criaturas"
        ],
        "characters_f": [
            "uma garota sozinha", "uma investigadora", "uma médium",
            "uma jovem corajosa", "uma sobrevivente"
        ],
        "settings": [
            "em uma mansão abandonada", "num hospital assombrado", "em uma floresta escura",
            "num cemitério antigo", "em uma cabana isolada"
        ],
        "conflicts": [
            "tentando escapar de uma presença maligna", "investigando acontecimentos estranhos",
            "lutando contra seus maiores medos", "preso em um pesadelo sem fim"
        ],
        "resolutions": [
            "mas nunca mais foram os mesmos.", "e descobriram um segredo aterrorizante.",
            "mas a escuridão ainda os observava.", "e perceberam que o mal nunca descansa."
        ]
    }
}

def generate_story(genre, gender_choice):
    """Gera uma história aleatória com base no gênero da história e do personagem"""
    elements = story_elements[genre]

    if gender_choice == "m":
        character = random.choice(elements["characters_m"])
    elif gender_choice == "f":
        character = random.choice(elements["characters_f"])
    else:
        all_characters = elements["characters_m"] + elements["characters_f"]
        character = random.choice(all_characters)

    setting = random.choice(elements['settings'])
    conflict = random.choice(elements['conflicts'])
    resolution = random.choice(elements['resolutions'])

    story = f'Era uma vez {character} que estava {setting}, {conflict} {resolution}'
    return story

if __name__ == "__main__":
    print("Bem-vindo ao Gerador de Histórias! \n")

    while True:
        print("Escolha o gênero da história: ")
        print("1 - Aventura")
        print("2 - Romance")
        print("3 - Terror")
        print('4 - Aleatório')

        choice = input("\nDigite o número do gênero:")
        genres = {"1": "aventura", "2": "romance", "3": "terror", "4": "aleatório"}

        if choice not in genres:
            print('\nOpção inválida! Tente novamente. \n')
            continue
        if genres[choice] == "aleatório":
            genre = random.choice(["aventura", "romance", "terror"])
            print(f"\nO gênero escolhido foi: {genre.capitalize()}!\n")
        else:
            genre = genres[choice]

        print("Escolha o gênero do personagem principal:")
        print("m - Masculino")
        print("f - Feminino")
        print("a - Aleatório")
        gender_choice = input("\nDigite sua escolha: ").lower()

        if gender_choice not in ['m', 'f', 'a']:
            print("\nOpção inválida! Usando 'aleatório' por padrão. \n")

        print('\n' + generate_story(genre, gender_choice) + "\n")

        other_history = input("Você quer gerar outra história? (s/n): ")
        if other_history.lower() == "n":
            print('\nObrigado por jogar o Gerador de histórias!')
            break
        if other_history.lower() == "s":
            continue
        else:
            print("\nOpção inválida. Tente novamente")