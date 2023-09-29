import pgf

gr = pgf.readPGF('/media/mcsa2/6824EAA724EA7788/Users/mcsa2/Documents/dev/NLP-Prescricoes-Medicas/PrescAbs.pgf')

por = gr.languages["PrescConc"]

while True:
    print("Exepmplos de frases: /n")
    print("Aplicar 1 dose de benzetacil 20ml de 8 em 8 horas")
    print("Tomar 1 comprimido de paracetamol 50mg de 12 em 12 horas")
    print("Tomar 2 comprimidos de dipirona 50mg de 8 em 8 horas")
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
