import spacy 
import string

def janela(nome,polaridades,noticias):
    janela_palavras = list()
    num_ocurr = 0
    nlp = spacy.load('en_core_web_md')
    for n in noticias:
        doc = nlp(n)
        for i, token in enumerate(doc):
            if token.text.lower() == nome.lower():
                num_ocurr += 1
                for j in range(1,6):
                    if i+j <= len(doc)-1 and doc[i+j].text not in string.punctuation:
                        janela_palavras.append(doc[i+j].text)
                    if i-j >= 0 and doc[i-j].text not in string.punctuation:
                        janela_palavras.append(doc[i-j].text)
    
    print(janela_palavras)
    polaridade = 0
    for palavra in janela_palavras:
        if palavra in polaridades.keys():
            polaridade += polaridades[palavra]
    polaridade = polaridade / num_ocurr

    return polaridade

nome = 'Ronaldo'

noticias = ["Cristiano Ronaldo picks up Man Utd award days after being snubbed by team-mates",
"5 Man Utd players set to benefit from Cristiano Ronaldo's new roleunder Erik ten Hag",
"Real Madrid star Karim Benzema has hailed Cristiano Ronaldo's vital role in his stunning season for the Spanish champions. The French forward has been a pivotal player to Los Blancos this term, with them winning the league and Champions League. He scored a stunning 44 goals in 46 games in all competitions this season - including an astounding 15 on the European stage. That form has seen Benzema re-establish himself as one of the greatest strikers in world football at the current time having regularly been in the shadow of Ronaldo during the pairs time together at the Santiago Bernabeu. However, Benzema has claimed that the Portuguese has been key to his late-career renaissance.",
"He may have said his goodbyes to Manchester United under a cloud, but Paul Pogba's relationship with Red Devils talisman Cristiano Ronaldo remains stronger than ever. The French midfielder failed to truly live up to expectations since he returned to Old Trafford for the second time in 2016. The World Cup winner cost the club a record fee of £89million but he fell remarkably short of justifying that fee during his time in Manchester. Pogba was one of the most high-profile figures at the club during a turbulent last season that saw the Red Devils finish with their worst points tally of the Premier League era. Another, undeniably more famous face within the dressing room was Ronaldo - meaning reports of a rift between the pair as they jostled for power within the ranks became common.",
"Portugal manager Fernando Santos defended his decision to drop Cristiano Ronaldo from the starting line-up for their Nations League opener against Spain, saying he was confident that the forward could make a greater impact off the bench. Ronaldo, his country's record goal-scorer, came on in the 62nd minute but failed to find the net as a late Ricardo Horta strike salvaged a 1-1 draw for Portugal.'Cristiano Ronaldo? They often ask why he is a starter. It's the million-dollar question,' said Santos after Thursday's result. 'I understood that for this game it was better to use the players I used.'"]

polaridades = {
    'Man': 1,
    'midfielder': 0,
    'winner': 1,
    'Utd': 1,
    'Fernando': 1,
    'Santos': 1,
    'late': -1,
    'picks': 0,
    'Cristiano': 1,
    'up': 0,
    'award': 1,
    'Benzema': 1
}

print(janela(nome, polaridades, noticias))