import pgf

gr = pgf.readPGF('/media/mcsa2/6824EAA724EA7788/Users/mcsa2/Documents/dev/NLP-Prescricoes-Medicas/PrescAbs.pgf')

por = gr.languages["PrescConc"]

while True:
    name = input("Digite a frase ou digite 'exit' para sair: ")

    if name.lower() == 'exit':
        print("Saindo do programa.")
        break

    try:
        i = por.parse(name)
        p, e = i.__next__()
        print("Prescrição Válida: " + por.linearize(e))
    except pgf.ParseError:
        print("Prescrição Inválida, tente novamente")
