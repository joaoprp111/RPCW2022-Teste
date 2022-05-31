'''Antes de iniciar o aquecimento utilizei o postman para fazer o POST login e obter o token.

Coloquei este json no body:
{
    "username": "rpcw2022@gmail.com",
    "password": "2022"
}

... depois obtive a seguinte resposta:
{
    "token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyOTRlY2VhNmI1ZDVjMjQ3NmNmMDhiMSIsImxldmVsIjozLjUsImVudGlkYWRlIjoiZW50X0EzRVMiLCJlbWFpbCI6InJwY3cyMDIyQGdtYWlsLmNvbSIsImlhdCI6MTY1NDAxMzQzOCwiZXhwIjoxNjU0MDQyMjM4fQ.ywPwGgXaLqUpreD3xumGfHSEwWHVr00N1dvxEAcoig-mMYwdVdbYiJBUs_IhPV3zBxzgbin0l6VyxKzXLbjGTVPmTWOCmHe5CttV5QhiF5oXNIl7Mprxdg37j0C70JQ-G1hTSG9x9-TiaqZOMFFWd90WiFDnRwmmSycUGLj5qCfr8zbr4g5oqsO-SqcehSSVhWtl1IOVhMlIgMufbe6bKC8Sbxf7lcCZSZlhVCC_6wCHNdiiN2tTGT8wAqmmYjw1eRFXDpB29XEPINKaTJRds3WL3ta4Cd6rzlnIa2YlYD3ZzawvKnLtTYVA2nM00zukOj_qkxL5nR7l_niuDX8Arw",
    "name": "rpcw2022",
    "entidade": "ent_A3ES"
}
'''

import requests

token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyOTRlY2VhNmI1ZDVjMjQ3NmNmMDhiMSIsImxldmVsIjozLjUsImVudGlkYWRlIjoiZW50X0EzRVMiLCJlbWFpbCI6InJwY3cyMDIyQGdtYWlsLmNvbSIsImlhdCI6MTY1NDAxMzQzOCwiZXhwIjoxNjU0MDQyMjM4fQ.ywPwGgXaLqUpreD3xumGfHSEwWHVr00N1dvxEAcoig-mMYwdVdbYiJBUs_IhPV3zBxzgbin0l6VyxKzXLbjGTVPmTWOCmHe5CttV5QhiF5oXNIl7Mprxdg37j0C70JQ-G1hTSG9x9-TiaqZOMFFWd90WiFDnRwmmSycUGLj5qCfr8zbr4g5oqsO-SqcehSSVhWtl1IOVhMlIgMufbe6bKC8Sbxf7lcCZSZlhVCC_6wCHNdiiN2tTGT8wAqmmYjw1eRFXDpB29XEPINKaTJRds3WL3ta4Cd6rzlnIa2YlYD3ZzawvKnLtTYVA2nM00zukOj_qkxL5nR7l_niuDX8Arw"

#1. Quantos processos (nível 3) e quais são (obtem uma lista em JSON; podes concatenar sublistas invocando várias queries), pertencentes à descendência da classe 750?
resQ1 = []
numDescendentes = 0
res = requests.get('http://clav-api.di.uminho.pt/v2/classes/c750/descendencia?token=' + token)
psNivel2 = res.json()

#[{'codigo': '750.10', 'titulo': 'Gestão do aluno/formando', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.10', 'status': 'A'}, {'codigo': '750.20', 'titulo': 'Gestão formativa e curricular', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.20', 'status': 'A'}, {'codigo': '750.30', 'titulo': 'Avaliação de aprendizagens', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.30', 'status': 'A'}]

res2 = requests.get('http://clav-api.di.uminho.pt/v2/classes/c750.10/descendencia?token=' + token).json()
numDescendentes += len(res2)
for r2 in res2:
    resQ1.append(r2['codigo'])
#6
#[{'codigo': '750.10.001', 'titulo': 'Seleção e seriação para ingresso no ensino ou formação', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.10.001', 'status': 'A'}, {'codigo': '750.10.002', 'titulo': 'Processamento de matrículas ou inscrições no ensino ou em formação', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.10.002', 'status': 'A'}, {'codigo': '750.10.300', 'titulo': 'Processamento dos dados cadastrais de alunos ou formandos', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.10.300', 'status': 'A'}, {'codigo': '750.10.600', 'titulo': 'Controlo de assiduidade de alunos ou formandos', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.10.600', 'status': 'A'}, {'codigo': '750.10.601', 'titulo': 'Processamento de marcação e admissão a provas de avaliação', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.10.601', 'status': 'A'}, {'codigo': '750.10.602', 'titulo': 'Integração e acompanhamento de alunos com necessidades educativas especiais', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.10.602', 'status': 'A'}]

res3 = requests.get('http://clav-api.di.uminho.pt/v2/classes/c750.20/descendencia?token=' + token).json()
numDescendentes += len(res3)
for r3 in res3:
    resQ1.append(r3['codigo'])
#7 
#[{'codigo': '750.20.001', 'titulo': 'Conceção, revisão e extinção de currículos e planos de estudos', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.20.001', 'status': 'A'}, {'codigo': '750.20.002', 'titulo': 'Conceção, revisão e extinção de planos de ações de formação', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.20.002', 'status': 'A'}, {'codigo': '750.20.003', 'titulo': 'Avaliação da atividade pedagógica', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.20.003', 'status': 'H'}, {'codigo': '750.20.300', 'titulo': 'Produção e seleção de recursos didático-pedagógicos', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.20.300', 'status': 'A'}, {'codigo': '750.20.301', 'titulo': 'Distribuição de atividades de ensino ou formação', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.20.301', 'status': 'A'}, {'codigo': '750.20.600', 'titulo': 'Realização de atividades de ensino ou formação', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.20.600', 'status': 'A'}, {'codigo': '750.20.601', 'titulo': 'Realização de atividades de formação e treino animal', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.20.601', 'status': 'A'}]

res4 = requests.get('http://clav-api.di.uminho.pt/v2/classes/c750.30/descendencia?token=' + token).json()
numDescendentes += len(res4)
for r4 in res4:
    resQ1.append(r4['codigo'])
#5
#[{'codigo': '750.30.001', 'titulo': 'Conceção e revisão dos métodos de avaliação de aprendizagens', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.30.001', 'status': 'A'}, {'codigo': '750.30.300', 'titulo': 'Elaboração de instrumentos de avaliação de aprendizagens', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.30.300', 'status': 'A'}, {'codigo': '750.30.600', 'titulo': 'Aplicação de instrumentos de avaliação de aprendizagens', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.30.600', 'status': 'A'}, {'codigo': '750.30.601', 'titulo': 'Processamento e comunicação de resultados de avaliação', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.30.601', 'status': 'A'}, {'codigo': '750.30.602', 'titulo': 'Reconhecimento, creditação e validação de competências e qualificações', 'id': 'http://jcr.di.uminho.pt/m51-clav#c750.30.602', 'status': 'A'}]

print('Resposta 1: Existem ' + str(len(resQ1)) + ' processos descendentes da classe 750 e são os seguintes: ' + str(resQ1))
#R: 18, [750.10.001, 750.10.002, 750.10.300, 750.10.600, 750.10.601, 750.10.602, 750.20.001, 750.20.002, 750.20.003,
# 750.20.300, 750.20.301, 750.20.600, 750.20.601, 750.30.001, 750.30.300, 750.30.600, 750.30.601, 750.30.602]

# 2. Quantas entidades estão catalogadas?
res = requests.get('http://clav-api.di.uminho.pt/v2/entidades?token=' + token).json()

print('Resposta 2: Estão catalogadas ' + str(len(res)) + ' entidades')
#R: 647

# 3. Quantos processos (classes de nível 3) se encontram na descendência de 750.20?

#R: 7, respondido na 1

#4. Quantos processos (classes de nível 3) estão relacionados com 750.20.600?
resQ4 = requests.get('http://clav-api.di.uminho.pt/v2/classes/c750.20.600/procRel?token=' + token).json()
print(str(len(resQ4)))

#R: 24