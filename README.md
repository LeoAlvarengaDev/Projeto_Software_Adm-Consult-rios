# Projeto_Software_Adm-Consult-rios
Documentação do Projeto
Código Construído
Link:

Premessas Assumidas
1) Poderá ser permitido o cadastro de clientes sem necessidade de consulta prévia.
2) Você pode obter um código telefônico por cliente.
3) Os alimentos relacionados incluem todos os presentes na pirâmide alimentar.

Decisões de Projeto
Modelagem
caso de uso

Clientes Checar: Esta ação permite obter informações verificadas sobre os clientes registrados sem sistema. Este código inclui detalhes como nome, e-mail, dados de nascimento e nomes de telefone. Uma capacidade de verificação de informações de clientes é fundamental para serviços de personalização e atualizados.
Clientes de removedor: O autor tem uma capacidade de removedor de clientes do sistema. Esse código pode ser necessário em situações em que um cliente não é mais atendido ou solicita uma remessa de informações adicionais do sistema.
Cadastrar Clientes: Ação que permite a autorização de informações de novos clientes sem sistema. Isso é essencial para expandir uma base de clientes e gerar um registro atualizado das pessoas que usam os serviços do sistema.
Atualizar Dados do Cliente: O autor pode ser exibido como informações dos clientes existentes no sistema. Isso é útil para corrigir erros, avaliar dados precisos e solicitar informações sobre clientes.
Consultas de carros: Essa é uma permissão para obter informações verificadas relacionadas às consultas realizadas pelos clientes. Este código inclui dados de consulta, horários, pesos, mordura corporal, sensações físicas e restritas alimentares.
Realizar consultas: Permita um registrador autor como informações de uma consulta realizada com um cliente. Isso é essencial para acompanhar o progresso e a orientação pessoal.
Atualizar Dieta: Uma ação de dieta atualizada é importante para fazer ajustes nas combinações alimentares ou metas de calorias de acordo com as necessidades do cliente.
Cadastrar Dieta: O autor pode codificar e inserir informações sobre dietas sem sistema. Isso envolve os produtos alimentares, as metas calóricas e os cartões planos para os clientes.
Checar Dieta: Esta ação permite um autor verificado como informações relacionadas às dietas existentes no sistema. Pode inclui detalhes sobre os alimentos, metas calóricas e composições das dietas.
Cadastrar Alimento: Permite um autor adicionar novos alimentos ao sistema, associando-os a grupos alimentares apropriados. Isso é essencial para o gerente de um banco de dados de alimentos disponíveis para inclusão nas dietas.

Banco
 
Clientes: Esta tabela armazena informa sobre os clientes, como nome, email, dados de nascimento, e nomes de telefone. O campo idClientes é uma chave primária da tabela, que pode ser usada para identificar exclusivamente cada cliente.
Endreco: Essa tabela está relacionada aos clientes, usando uma coluna Clientes_idClientes como a cadeia de caracteres para estabilizar essa relação. Ela arma os detalhes dos clientes, como número, CEP, bairro, cidade, rua e UF (Unidade Federativa) .Consultas: Uma tabela de consultas está vinculada aos clientes, usando um chave estrangeira Clientes_idClientes. Ela registra informações sobre consultas de clientes, como dados de consulta, horário, peso, gordura corporal, sensação física e restrições alimentares.
Grupos_Alimentares: Esta tabela contém informações sobre os alimentos. Cada grupo de pessoas que se encontra com o grupo de pessoas primárias e um nome de grupo, armazenado na coluna nomeGrupo.
Alimentos: Os alimentos são relacionados aos alimentos alimentares dos alimentos utilizados para o grupo de negócios Grupo_idGrupo. Esta tabela armazena informa sobre alimentos, incluindo nome, carga calórica e um grupo pertinente.
Dieta: Uma guia Dieta é usada para criar combinações alimentares para clientes. Possui campos relacionados a três grupos alimentares diferentes (Grupo_Alimentar1_idGrupo, Grupo_Alimentar2_idGrupo e Grupo_Alimentar3_idGrupo), um campo para registrar uma meta de calorias, e um campo para criar um cartão. Um chave estrangeira Clientes_idClientes está presente para uma dieta a um cliente específico.

Instrumentos para Instalação e Execução do Sistema
1) Passo: Execute o código bancário.py para inicializar o banco de dados.

2) Passo: Registrador de alimentos no banco de dados e combinações de gênero para suas dietas personalizadas.

3) Passo: Explore e utilize como demais opções disponíveis.
