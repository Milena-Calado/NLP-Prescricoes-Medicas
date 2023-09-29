concrete PrescConc of PrescAbs = {

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
    Do Acao Instrucao = {s = Acao.s ++ "pela" ++ Instrucao.s} ;

    Tomar Quantidade Medicamento Dosagem = {s = "Tomar" ++ Quantidade.s ++ "comprimido" + copula(Quantidade.n) ++ "de" ++ Medicamento.s ++ Dosagem.s } ;
    Aplicar Quantidade MedicamentoInjetavel DosagemInjetavel = {s = "Aplicar" ++ Quantidade.s ++ "dose"  + copula(Quantidade.n) ++ "de" ++ MedicamentoInjetavel.s ++ DosagemInjetavel.s } ; 
    
    Dipirona = {s = "dipirona"} ;
    Paracetamol = {s = "paracetamol"} ;
    Ibuprofeno = {s = "ibuprofeno"} ;

    Benzetacil = {s = "benzetacil"} ;

    Manha = {s = "manhã"} ;
    Tarde = {s = "tarde"} ;
    Noite = {s = "noite"} ;

    Um = {s = "1" ; n = Sg} ;
    Dois = {s = "2" ; n = Pl} ;
    Tres = {s = "3" ; n = Pl} ;

    Cinquenta = {s = "(50mg)" ; n = Sg} ;
    Cem = {s = "(100mg)" ; noite = Sg} ;

    Dez = {s = "(10ml)" ; n = Sg} ;
    Vinte = {s = "(20ml)" ; n = Sg} ;

}