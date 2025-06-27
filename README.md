# Dashboard Ações de Grandes Empresas do Petróleo em 2025
  👉 Este projeto tem como objetivo analisar o desempenho das principais empresas de petróleo, como Saudi Aramco, BP, Chevron, Equinor, Shell, TotalEnergies e ExxonMobil. A análise foi feita com dados da API do Marketstack, mas, por limitações da ferramenta, algumas empresas como PetroChina, Petrobras e China Petroleum & Chemical Corp não puderam ser incluídas pois só são disponíveis para quem tem API Premium.
  Esse estudo ganha relevância no contexto atual de tensões no Oriente Médio, especialmente em relação ao Irã e ao Estreito de Ormuz. O estreito é uma das rotas mais importantes para o transporte de petróleo e qualquer instabilidade ali pode afetar todo o mercado. O objetivo aqui é mostrar como a localização das sedes dessas gigantes do petróleo se conecta diretamente a essa região crítica e entender como isso pode impactar suas ações.

# Desenvolvimento e Tecnologias Utilizadas
  Este projeto foi desenvolvido utilizando uma combinação de ferramentas e tecnologias, com o objetivo de analisar de forma eficiente os dados das grandes empresas de petróleo e seu desempenho no mercado de ações.
    Integração de Dados: A integração com a API do Marketstack foi feita utilizando Python, o que permitiu buscar as informações sobre 7 das 10 maiores empresas de petróleo e consultar as suas ações. Algumas empresas estavam limitadas pela API, como estava utilizando a        gratuita consegui apenas consultar 7 das 10 maiores empresas, mesmo assim a analise já traz uma boa visão sobre!
    
    Tratamento e Processamento de Dados: Após a coleta dos dados, foi realizado o tratamento e limpeza com a biblioteca Pandas, incluindo a conversão da moeda da Arábia Saudita para dólar americano para padronizar as informações e todo o processo de atualização e ajustes      também em Python utilizando pandas, o código está no repositório caso queira consultar, com os dados exportados para CSV para facilitar a importação no Power BI.
    
    Power BI: No Power BI, os dados foram importados, alguns ajustes finais no PowerQuery e foram realizados os cálculos necessários com DAX para garantir que as análises fossem mais precisas e de fácil interpretação.
    
    Design: O design do dashboard foi criado no Figma, onde foram feitas as páginas e a estrutura visual. A integração entre o design e as análises foi feita de forma a garantir uma navegação fluida e intuitiva para o usuário.
