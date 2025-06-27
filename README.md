# Dashboard Ações de Grandes Empresas de Petróleo em 2025
## [📖] Introdução
  Este projeto tem como objetivo analisar o desempenho das principais empresas de petróleo, como Saudi Aramco, BP, Chevron, Equinor, Shell, TotalEnergies e ExxonMobil. A análise foi feita com dados da API do Marketstack, mas, por limitações da ferramenta, algumas empresas como PetroChina, Petrobras e China Petroleum & Chemical Corp não puderam ser incluídas pois só são disponíveis para quem tem API Premium.
  
  Esse estudo ganha relevância no contexto atual de tensões no Oriente Médio, especialmente em relação ao Irã e ao Estreito de Ormuz. O estreito é uma das rotas mais importantes para o transporte de petróleo e qualquer instabilidade ali pode afetar todo o mercado. O objetivo aqui é mostrar como a localização das sedes dessas gigantes do petróleo se conecta diretamente a essa região crítica e entender como isso pode impactar suas ações.

  Fonte das top 10 empresas de petróleo: https://www.nordinvestimentos.com.br/blog/maiores-petroliferas-do-mundo/

## [⚙️] Tecnologias Utilizadas
- Power BI
- Pandas
- Python
- Figma
- API Marketstack (https://marketstack.com/)
  
## [💻] Desenvolvimento
  O projeto foi desenvolvido utilizando uma combinação de ferramentas e tecnologias, com o objetivo de analisar de forma eficiente os dados das grandes empresas de petróleo e seu desempenho no mercado de ações.
  
  **Integração de Dados:** A integração com a API do Marketstack foi feita utilizando Python, o que permitiu buscar as informações sobre 7 das 10 maiores empresas de petróleo e consultar as suas ações. Algumas empresas estavam limitadas pela API, como estava utilizando a        gratuita consegui apenas consultar 7 das 10 maiores empresas, mesmo assim a analise já traz uma boa visão sobre!
    
  **Tratamento e Processamento de Dados:** Após a coleta dos dados, foi realizado o tratamento e limpeza com a biblioteca Pandas, incluindo a conversão da moeda da Arábia Saudita para dólar americano para padronizar as       informações e todo o processo de atualização e ajustes, o código está no repositório caso queira consultar, com os dados exportados para CSV para facilitar a importação no Power BI.
  
  **Power BI:** No Power BI, os dados foram importados, alguns ajustes finais no PowerQuery e foram realizados os cálculos necessários com DAX para garantir que as análises fossem mais precisas e de fácil interpretação.
  
  **Design:** O design do dashboard foi criado no Figma, onde foram feitas as páginas e a estrutura visual. A integração entre o design e as análises foi feita de forma a garantir uma navegação fluida e intuitiva para o usuário e com o padrão visual de cada empresa.

  ### [📄] Páginas do dashboard:
  
  #### 👉 Página 1 (Home)
  
  Aqui basicamente aonde explico o objetivo da análise e o contexto a qual a análise é aplicada, logo em seguida pode escolher a empresa a qual deseja analisar
  
  ![Screenshot_11](https://github.com/user-attachments/assets/9bedd244-64ae-45c4-ada2-3a4a2509e91c)

  #### 👉 Página 2 (Análisando a Saudi Aramco)

  Analise sobre as ações da empresa Saudi Aramco em 2025, e sua comparação de local com o estreito de ormuz (cujo explicado já em home)
  
  ![2](https://github.com/user-attachments/assets/b883bdc3-31d5-4ef7-b98a-c4161153ad5b)

  #### 👉 Página 3 (Análisando a British Petroleum)

  Analise sobre as ações da empresa British Petroleum em 2025, e sua comparação de local com o estreito de ormuz (cujo explicado já em home)
  
  ![3](https://github.com/user-attachments/assets/03d750eb-a46c-409e-852d-8aaaf03d7c7d)

  #### 👉 Página 4 (Análisando a Chevron Corporation)

  Analise sobre as ações da empresa Chevron Corporation em 2025, e sua comparação de local com o estreito de ormuz (cujo explicado já em home)

  ![4](https://github.com/user-attachments/assets/3d31d6c8-8e84-491e-9960-aa7bb378e04d)

  #### 👉 Página 5 (Análisando a Equinor ASA)

  Analise sobre as ações da empresa Equinor ASA em 2025, e sua comparação de local com o estreito de ormuz (cujo explicado já em home)

  ![5](https://github.com/user-attachments/assets/c7a8e331-8ad3-459a-83ef-4f5edbb803cb)

  #### 👉 Página 6 (Análisando a Shell PLC)

  Analise sobre as ações da empresa Shell PLC em 2025, e sua comparação de local com o estreito de ormuz (cujo explicado já em home)

  ![6](https://github.com/user-attachments/assets/a416816c-43d2-43a7-adf3-b64de6491445)
  
  #### 👉 Página 7 (Análisando a TotalEnergies)

  Analise sobre as ações da empresa TotalEnergies em 2025, e sua comparação de local com o estreito de ormuz (cujo explicado já em home)

  ![7](https://github.com/user-attachments/assets/e1be170b-485f-41f2-86ac-becc7a2610a4)
  
  #### 👉 Página 8 (Análisando a Exxon Mobil)

  Analise sobre as ações da empresa Exxon Mobil em 2025, e sua comparação de local com o estreito de ormuz (cujo explicado já em home)

  ![8](https://github.com/user-attachments/assets/3c6743bf-80f3-496d-a955-39e2c746fd81)
  

## [📋] Conclusão

Este projeto proporcionou uma análise detalhada das ações de grandes empresas de petróleo em 2025, com um foco especial nas implicações geopolíticas da região do Oriente Médio, particularmente no que diz respeito ao Estreito de Ormuz. Através do uso da API Marketstack e das ferramentas como Python, Power BI e Figma, foi possível criar um dashboard intuitivo e informativo que conecta dados financeiros a um contexto geopolítico real e relevante para o mercado de petróleo, sem dúvidas o projeto mais completo que já fiz!

Apesar da limitação da API, que impediu a inclusão de três das maiores empresas, o dashboard ainda fornece uma visão robusta e representativa do desempenho das empresas analisadas. A visualização no Power BI e o uso de mapas interativos proporcionam um entendimento claro da relação entre as sedes das empresas e a importância estratégica do Estreito de Ormuz, um ponto crítico para o abastecimento de petróleo global.
