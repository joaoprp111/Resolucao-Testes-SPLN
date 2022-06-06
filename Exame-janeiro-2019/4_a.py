import spacy 

def extrai_frase(nome, polaridades, noticias):
    num_noticia = 1 
    num_frase = 1 
    ocorrencias_nome = dict()
    nlp = spacy.load('pt_core_news_lg')
    for n in noticias:
        doc = nlp(n)
        for sent in doc.sents:
            for ent in sent.ents:
                if ent.text == nome:
                    chave = str(num_noticia) + '-' + str(num_frase)
                    ocorrencias_nome[chave] = sent.text 
            num_frase += 1 
        num_frase = 1
        num_noticia += 1

    print(str(ocorrencias_nome))

nome = 'José Mourinho'
polaridades = []
noticias = [
'Escreve o The Telegraph neste sábado que o PSG está de olho em José Mourinho. A intenção deverá ter partido de Luís Campos com quem o Special One trabalhou no Real Madrid e com quem mantém uma relação de amizade conhecida publicamente. Mourinho não será, no entanto, o único concorrente pelo lugar. Diz a mesma fonte que Christophe Galtier, do Nice, está igualmente na lista. O técnico francês trabalhou com Luís Campos no Lille, num projeto que culminou no título de campeão de França.',

'Campeão da Conference League com a Roma, o português José Mourinho, de 59 anos de idade, campeão de tudo que disputou no velho continente, pode estar voltando à elite do futebol na próxima temporada. Apesar de ter contrato com a Roma, até julho de 2024, o futuro pode estar na França. Mourinho chegou à Roma desacreditado depois de não conseguir brilhar na Premier League. Uma temporada depois de chegar ao clube italiano, ele conquistou a Conference League, mas pode estar de saída da Roma para assumir o PSG.',

'O campeão francês estará interessado na contratação de José Mourinho para o comando técnico. Segundo o jornal "Telegraph", o treinador português, atualmente na Roma e que recentemente conquistou a Liga Conferência, é um dos favoritos para render Mauricio Pochettino. Segundo a mesma publicação, ter o "Special One" no PSG é um pedido expresso de Luís Campos, conselheiro desportivo dos parisienses, que mantém uma grande relação com Mourinho desde que trabalharam juntos no Real Madrid.'
]

extrai_frase(nome,polaridades,noticias)
