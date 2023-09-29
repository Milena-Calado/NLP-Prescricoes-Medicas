concrete PrescConcEng of PrescAbsEng = {

  param
    Number = Sg | Pl ; 

  lincat

    Phrase, Acao, Medicamento, MedicamentoInjetavel, Instrucao, Dosagem, DosagemInjetavel  = {s : Str } ;
    Quantidade  = {s : Str ; n : Number} ;
  
  oper

    singularPlural : Number -> Number =
        \n -> case n of { Sg => Sg ; Pl => Pl } ;  

    copula : Number -> Str =
        \n -> case n of { Sg => " " ; Pl => "s" } ;

  lin
    Do Acao Instrucao = {s = Acao.s ++ Instrucao.s} ;

    Tomar Quantidade Medicamento Dosagem = {s = "Take" ++ Quantidade.s ++ "pill" + copula(Quantidade.n) ++ "in" ++ Medicamento.s ++ Dosagem.s } ;
    Aplicar Quantidade MedicamentoInjetavel DosagemInjetavel = {s = "Apply" ++ Quantidade.s ++ "injection"  + copula(Quantidade.n) ++ "in" ++ MedicamentoInjetavel.s ++ DosagemInjetavel.s } ; 
    
    Dipirona = {s = "dipiron"} ;
    Paracetamol = {s = "paracetamol"} ;
    Ibuprofeno = {s = "ibuprofen"} ;

    Benzetacil = {s = "benzetacil"} ;
    Profenid = {s = "profenid"} ;

    Manha = {s = "every 8 hours"} ;
    Tarde = {s = "every 12 hours"} ;
    Noite = {s = "after dinner"} ;

    Um = {s = "1" ; n = Sg} ;
    Dois = {s = "2" ; n = Pl} ;
    Tres = {s = "3" ; n = Pl} ;

    Cinquenta = {s = "50mg" ; n = Sg} ;
    Cem = {s = "100mg" ; noite = Sg} ;

    Dez = {s = "10ml" ; n = Sg} ;
    Vinte = {s = "20ml" ; n = Sg} ;

}