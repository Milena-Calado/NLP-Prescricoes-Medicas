abstract PrescAbs = {

 flags
    startcat = Phrase ;
 cat
    Phrase ; Acao ; Medicamento ;  Instrucao ; Quantidade ; MedicamentoInjetavel ; Dosagem ; DosagemInjetavel ;
    
 fun
    Do : Acao -> Instrucao -> Phrase ;

    Tomar : Quantidade -> Medicamento -> Dosagem -> Acao ;  

    Aplicar : Quantidade -> MedicamentoInjetavel -> DosagemInjetavel -> Acao ;    
    
    Dipirona, Paracetamol, Ibuprofeno : Medicamento ;
    Benzetacil, Profenid : MedicamentoInjetavel ;
    Manha, Tarde, Noite : Instrucao ;
    Cinquenta, Cem : Dosagem ;
    Dez, Vinte : DosagemInjetavel ;
    Um, Dois, Tres : Quantidade ;
    
}