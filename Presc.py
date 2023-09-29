import pgf

gr = pgf.readPGF('/media/mcsa2/6824EAA724EA7788/Users/mcsa2/Documents/dev/NLP-Prescricoes-Medicas/PrescAbsBra.pgf')
eng = gr.languages["PrescConcEng"]
por = gr.languages["PrescConcBra"]


while True:
      
    name = input("Digite a frase ou digite 's' para sair: ")

    if name.lower() == 's':
        print("Saindo do programa.")
        break

     # Verifica se a frase contém palavras em inglês
    if any(word in name.lower() for word in ["take", "pill", "injection"]):
        try:
            i = eng.parse(name)
            p, e = i.__next__()
            print("Prescrição Válida: " + eng.linearize(e))
            break
        except pgf.ParseError:
            print("Prescrição Inválida, tente novamente")
    else:
        try:
            i = por.parse(name)
            p, e = i.__next__()
            print("Prescrição Válida: " + por.linearize(e))
            break
        except pgf.ParseError:
            print("Prescrição Inválida, tente novamente")
