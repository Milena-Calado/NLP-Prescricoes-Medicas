import pgf

gr = pgf.readPGF('/media/mcsa2/6824EAA724EA7788/Users/mcsa2/Documents/dev/NLP-Prescricoes-Medicas/PrescAbs.pgf')
eng = gr.languages["PrescConcEng"]
por = gr.languages["PrescConcBra"]

while True:
    print("Exepmplos de frases em Portugues: /n")
    print("Aplicar 1 dose de benzetacil 20ml de 8 em 8 horas")
    print("Tomar 1 comprimido de paracetamol 50mg de 12 em 12 horas")
    print("Tomar 2 comprimidos de dipirona 50mg de 8 em 8 horas")
    print("Exepmplos de frases em Inglês: /n")
    print("Take 1 pill in paracetamol 50mg every 12 hours")
    print("Apply 1 injection in profenid 10ml every 12 hours")
   
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
        except pgf.ParseError:
            print("Prescrição Inválida, tente novamente")
    else:
        try:
            i = por.parse(name)
            p, e = i.__next__()
            print("Prescrição Válida: " + por.linearize(e))
        except pgf.ParseError:
            print("Prescrição Inválida, tente novamente")
