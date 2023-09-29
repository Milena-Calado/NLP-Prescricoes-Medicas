from pgf import PGF
from pgf import modules
from pgf import categories

# Carregue a gramática GF
gf = PGF('C:\Users\mcsa2\Documents\dev\NLP-Prescricoes-Medicas\MedicamentsRGL.gf')

# Obtenha os módulos relevantes
lexicon = modules['PrescricaoMedicaLexicon']
grammar = modules['PrescricaoMedicaGrammar']

# Obtenha as categorias gramaticais
Medicamento = categories['Medicamento']
Dosagem = categories['Dosagem']
Acao = categories['Acao']
Instrucao = categories['Instrucao']

# Função para gerar a prescrição médica
def gerar_prescricao(medicamento, dosagem, acao, instrucao):
    try:
        # Analise a entrada do usuário usando a função da gramática
        resultado = gf.parse(f'GerarPrescricaoMedica {medicamento} {dosagem} {acao} {instrucao}')
        # Recupere a frase gerada
        frase = resultado.get_linearizations('PrescricaoMedica')[0]
        return frase
    except Exception as e:
        return f"Erro na entrada: {str(e)}"

# Aceite entradas do usuário
medicamento = input("Digite o medicamento: ")
dosagem = input("Digite a dosagem: ")
acao = input("Digite a ação (Tomar, Ingerir, Aplicar): ")
instrucao = input("Digite a instrução (por exemplo, 'uma vez ao dia'): ")

# Gere a prescrição médica
resultado = gerar_prescricao(medicamento, dosagem, acao, instrucao)

# Imprima a prescrição médica gerada ou o erro
print(resultado)
