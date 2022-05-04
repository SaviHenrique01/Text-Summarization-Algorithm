import re
import nltk
import string
import heapq
import math

# nltk.download('punkt')
# nltk.download('stopwords')

# LISTA DE PASSOS
# PRÉ-PROCESSAMENTO DOS TEXTOS

stopwords = nltk.corpus.stopwords.words('portuguese')
texto_original = '''A inteligência artificial é a inteligência similar à humana.
                    Definem como o estudo de agente artificial com inteligência.
                    Ciência e engenharia de produzir máquinas com inteligência.
                    Resolver problemas e possuir inteligência.
                    Relacionada ao comportamento inteligente.
                    Construção de máquinas para raciocinar.
                    Aprender com os erros e acertos.
                    Inteligência artificial é raciocinar nas situações do cotidiano.'''

texto_original = re.sub(r'\s+',' ',texto_original)

def preprocessamento(texto):
  texto_formatado = texto.lower()
  tokens = []
  for token in nltk.word_tokenize(texto_formatado):
    tokens.append(token)
  
  tokens = [palavra for palavra in tokens if palavra not in stopwords and palavra not in string.punctuation]
  texto_formatado = ' '.join([str(elemento) for elemento in tokens])

  return texto_formatado

texto_formatado = preprocessamento(texto_original)

# FREQUÊNCIA DAS PALAVRAS
frequencia_palavras = nltk.FreqDist(nltk.word_tokenize(texto_formatado))

# FREQUÊNCIA PROPORCIONAL DAS PALAVRAS
frequencia_maxima = max(frequencia_palavras.values())
for palavra in frequencia_palavras.keys():
  frequencia_palavras[palavra] = (frequencia_palavras[palavra] / frequencia_maxima)

# TOKENIZAÇÃO DAS SENTENÇAS
lista_sentencas = nltk.sent_tokenize(texto_original)

# NOTA PARA AS SENTENÇAS
nota_sentencas = {}
for sentenca in lista_sentencas:
  for palavra in nltk.word_tokenize(sentenca.lower()):
    if palavra in frequencia_palavras.keys():
      if sentenca not in nota_sentencas.keys():
        nota_sentencas[sentenca] = frequencia_palavras[palavra]
      else:
        nota_sentencas[sentenca] += frequencia_palavras[palavra]

# ORDENAÇÃO DAS MELHORES SENTENÇAS
quantidadeSentencas = 4
melhores_sentencas = heapq.nlargest(quantidadeSentencas, nota_sentencas, key=nota_sentencas.get)

# GERAÇÃO DO RESUMO
resumo = ' '.join(melhores_sentencas)

# VISUALIZAÇÃO DO RESUMO COM HTML
from IPython.core.display import HTML
texto = ''

display(HTML(f'<h1>Resumo do Texto</h1>'))
for sentenca in lista_sentencas:
  #texto += sentenca
  if sentenca in melhores_sentencas:
    texto += str(sentenca).replace(sentenca, f"<mark>{sentenca}</mark>")
  else:
    texto += sentenca
display(HTML(f"""{texto}"""))

# TEXTOS DE EXEMPLO PARA TESTAR
texto_contratualismo = '''O contratualismo é um modelo teórico criado para explicar o surgimento da sociedade. Esta teoria é baseada na ideia de que os seres humanos viviam em um estado pré-social, chamado de estado de natureza e abandonaram-no para firmar um pacto, o contrato social.
                   As teorias do contratualismo surgem da necessidade de explicar o fato dos seres humanos terem se organizado em torno de sociedades regidas por leis criadas pelo Estado.
                   Os pensadores que desenvolveram essa escola de pensamento são conhecidos como filósofos contratualistas. Os contratualistas afirmam que antes do contrato social, todos os seres humanos eram livres e iguais, vivendo de acordo com as leis da natureza.
                   Entretanto, vão firmar um pacto social e abandonar a sua liberdade natural para a construção de uma sociedade que lhes garantam o direito à propriedade.
                   Assim, o contratualismo vai representar o abandono da liberdade natural o surgimento da liberdade civil submetida às leis. O Estado nasce com a função de formular leis às quais todos os indivíduos devem seguir.'''

texto_inicial = '''A inteligência artificial é a inteligência similar à humana.
                    Definem como o estudo de agente artificial com inteligência.
                    Ciência e engenharia de produzir máquinas com inteligência.
                    Resolver problemas e possuir inteligência.
                    Relacionada ao comportamento inteligente.
                    Construção de máquinas para raciocinar.
                    Aprender com os erros e acertos.
                    Inteligência artificial é raciocinar nas situações do cotidiano.'''

biografia_Francis_Bacon = '''Francis Bacon foi um filósofo, político inglês e um dos fundadores do método indutivo de investigação científica, 
                o qual estava baseado no Empirismo. Seus estudos contribuíram para a história da ciência moderna. Filho de Nicholas Bacon e Ann Cooke Bacon, 
                Francis Bacon nasceu em Londres em 22 de janeiro de 1561 no seio de uma família de nobres. Estudou Direito na Universidade de Cambridge e teve 
                um papel preponderante na política inglesa, sendo eleito o 1.° Visconde de Alban e também embaixador inglês na França.
                Além disso foi conselheiro, procurador-geral, fiscal, grande chanceler e guarda do selo. No entanto, foi acusado de corrupção em 1621, o que o levou ao pagamento de uma multa.
                Em pouco tempo, Bacon conseguiu fama em seu país, sendo um homem respeitado não somente por sua posição política mas por suas contribuições nas áreas jurídica e filosófica.
                Foi um dos mais importantes pensadores da filosofia moderna, criando um método de investigação filosófica. Por esse motivo é considerado o "Pai do Método Experimental".
                Faleceu em 9 de abril de 1626 na cidade de Highate no Reino Unido, vítima de bronquite.
                Para Francis a ciência era uma técnica e os conhecimentos científicos deveriam ser considerados instrumentos práticos de controle da natureza.
                Ele pretendia demostrar sua grande preocupação com os conhecimentos científicos na vida prática. A ciência deveria valorizar a pesquisa experimental baseada na corrente empirista.
                Segundo Bacon, a figura dos ídolos estava baseada em falsas noções e hábitos mentais incutidos na mentalidade dos homens. Para ele, a crença nos ídolos prejudicava o avanço da ciência e da racionalidade humana.
                Dessa forma, rejeitou o pensamento da filosofia medieval escolástica, a qual esteve baseada em noções abstratas.
                Foi em sua obra “Novum Organum” (Novo Instrumento) que ele apresentou os quatro gêneros de ídolos que geram falsas noções:
                Ídolos da tribo: provenientes das limitações da espécie humana.
                Ídolos da caverna: o nome dessa categoria está relacionado com o “mito da caverna” de Platão, proveniente das falsas noções do ser humano.
                Ídolos do mercado ou do foro: provenientes da linguagem e da comunicação
                Ídolos do teatro: provenientes do campo cultural, filosófico e científico.
                Bacon criou um modelo de investigação através do método da indução, o qual estava baseado na observação precisa e minuciosa dos fenômenos naturais.
                Com o intuito de combater os erros provocados pelas crenças nos “ídolos”, Bacon propõe o método indutivo. Segundo ele, essa metodologia estaria dividida em quatro etapas:
                Coleta de informações a partir da observação rigorosa da natureza;
                Reunião, organização sistemática e racional dos dados recolhidos;
                Formulação de hipóteses segundo a análise dos dados recolhidos;
                Comprovação das hipóteses a partir de experimentações.'''

texto_Ciencia = '''Ciência é o conhecimento que explica os fenômenos obedecendo a leis que foram verificadas por métodos experimentais.
                  A ciência baseia-se na regularidade, na previsão e no controle de fenômenos que podem ser observados.
                  Conceito de Ciência A ciência é um modo de conhecer fundamentado em um método, o método científico. O método é o modo de funcionamento das ciências, é fundamentado na observação, na experimentação e na produção de teorias e leis.
                  As teorias são constantemente testadas, visando sua comprovação ou substituição por outra teoria que resista à checagem.
                  O objetivo da ciência é explicar, descrever e prever os fenômenos a partir do desenvolvimento de procedimentos metodológicos que possam ser constantemente verificados e reproduzidos.
                  Características da ciência: Objetiva: a ciência é um conhecimento que pressupõe uma objetividade, ou seja, busca ser imparcial, com a mínima influência dos interesses pessoais, com linguagem clara, rigorosa e precisa para evitar ambiguidades.
                  Verificável: todas as teorias científicas são postas à prova. Teorias que não resiste à verificação são descartadas. A verificação deve ser realizada pelo próprio cientista ou por qualquer pessoa e também passa pelo julgamento da comunidade científica.
                  Controlada: todos os elementos das ciências devem ser controladas para possibilitar a sua verificação e reprodução.
                  Lógica: a ciência é um conhecimento baseado na lógica, não aceita contradições.'''

textoSelecionado = texto_original
divisaoSentencas = textoSelecionado.split('.')
quantSentencas = len(divisaoSentencas)
sentencasIdeaisResumo = math.ceil((quantSentencas * 40) / 100)
