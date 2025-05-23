

**Trabalho da disciplina de Quality Assurance**



Nome: Pedro Henrique  
Curso:** ADS  
Semestre: 5 semestre 

Durante essa disciplina, aprendi conceitos essenciais sobre qualidade de software, planejamento de testes e automação. Foi uma experiência muito útil para entender a importância de garantir que sistemas funcionem corretamente antes de serem entregues ao usuário.

---

## 2. O que é Quality Assurance (QA)?

Quality Assurance é um conjunto de práticas e processos que garantem a qualidade do software durante todo o seu desenvolvimento. O objetivo do QA é evitar falhas, prevenir bugs e garantir que o produto final atenda aos requisitos esperados. É como revisar cada etapa de um projeto para garantir que tudo esteja funcionando corretamente, de forma contínua.

---

## 3. Conceitos Aprendidos Durante o Semestre

- **Qualidade em software:** Aprendi que qualidade vai além de “não ter bugs”. Envolve usabilidade, desempenho, segurança e satisfação do usuário.
- **Tipos de teste:** Exploramos testes unitários, de integração, sistema, aceitação, regressão e exploratórios. Cada um tem seu papel para garantir qualidade em diferentes fases do projeto.
- **Planejamento de testes:** Entendi como definir critérios de aceitação e elaborar planos e casos de testes claros.
- **Ferramentas utilizadas:** Utilizamos Google Colab, GitHub e ferramentas de automação e versionamento.
- **Automação e CI/CD:** Vimos como integrar testes automatizados em pipelines de entrega contínua.
- **Monitoramento:** Conheci o uso de métricas, rastreamento de bugs e ferramentas de observabilidade.

---

## 4. Ferramentas e Sites Utilizados

https://reqres.in/ – API pública para testes de requisições HTTP

https://colab.research.google.com/ – Ambiente Python online para escrever e executar código

https://github.com/ – Controle de versão e colaboração de código

https://uptimerobot.com/ – Monitoramento de disponibilidade de aplicações

https://httpstat.us/ – Gerador de respostas HTTP específicas para testes

https://jsonplaceholder.typicode.com/ – API falsa usada para testes e prototipagem

https://pytest.org/ – Documentação da principal biblioteca de testes Python

https://pypi.org/project/requests/ – Biblioteca Requests para testes de APIs

https://docs.github.com/actions – Integração contínua (CI) com GitHub Actions

https://postman.com/ – Testes de APIs com interface gráfica (caso tenha utilizado)

---

## 5. Explicação dos Testes Entregues

### ✅ Teste 01 – Verificação de status da API ReqRes
- **Biblioteca:** Requests  
- **Objetivo:** Verificar se o endpoint retorna status HTTP 200  
- **Resultado esperado:** Teste passa com sucesso se o status for 200  
- **Arquivo:** testes/teste_01.py  

### ✅ Teste 02 – Verificação de dados retornados pela API
- **Biblioteca:** Requests  
- **Objetivo:** Verificar se os dados do usuário com ID 2 estão corretos  
- **Resultado esperado:** O JSON retornado deve conter `id = 2` e campo `email`  
- **Arquivo:** testes/teste_02.py  

### ✅ Teste 03 – Simulação de criação de usuário com POST
- **Biblioteca:** Requests  
- **Objetivo:** Testar se a criação de um novo usuário com método POST está funcionando  
- **Resultado esperado:** Retorno do status 201 e nome igual ao enviado  
- **Arquivo:** testes/teste_03.py  

---

## 6. Conclusão Final

O aprendizado mais importante foi entender que o QA não é apenas "testar", mas garantir a confiança no software. QA tem um papel estratégico dentro das equipes. No meu futuro profissional, vejo a área de QA como essencial, especialmente com automação e CI/CD integrando desenvolvimento e testes. A ferramenta que mais me chamou atenção foi o **GitHub**, por permitir versionamento, colaboração e integração de testes automatizados.
