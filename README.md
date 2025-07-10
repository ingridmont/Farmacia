# InfoFarma
tema: farmácia

1. Cadastro e autenticação
RF01: Qualquer pessoa poderá criar uma conta como cliente informando e-mail e senha.

RF02:  Atendentes e gerente terão contas criadas previamente pelo gerente.

RF03: Todos os usuários poderão fazer login e logout.

RF04: As senhas devem ser armazenadas com hash seguro.

RF05: O sistema deverá validar o tipo de usuário (cliente, atendente, gerente) após o login.

RF06: Apenas usuários autenticados poderão acessar funcionalidades específicas conforme seu papel.

3. Gerenciamento do recurso do cliente:
RF07: O cliente poderá visualizar a lista de medicamentos disponíveis.

RF08: O cliente poderá pesquisar medicamentos por nome.

RF09: O cliente poderá realizar pedidos de medicamentos.

RF10: O cliente poderá visualizar o histórico de pedidos realizados.

RF11: O cliente poderá editar seus próprios dados (nome, e-mail, senha).

RF12: O cliente não terá acesso ao gerenciamento de estoque ou usuários.

4. Gerenciamento do recurso do atendente:
RF13: O atendente poderá visualizar e listar todos os medicamentos.

RF14: O atendente poderá cadastrar novos medicamentos.

RF15: O atendente poderá editar os dados de medicamentos (nome, preço, quantidade).

RF16: O atendente poderá excluir medicamentos do estoque.

RF17: O atendente poderá registrar pedidos para clientes diretamente (venda presencial).

RF18: O atendente poderá visualizar a lista de pedidos realizados.

RF19: O atendente não poderá alterar dados de outros usuários nem adicionar atendentes.

5. Gerenciamento do recurso do gerente:
RF20: O gerente poderá cadastrar, editar e excluir contas de atendentes.

RF21: O gerente poderá visualizar relatórios de vendas e estoque.

RF22: O gerente poderá visualizar todos os pedidos.

RF23: O gerente poderá visualizar e editar os dados dos medicamentos.

RF24: O gerente poderá redefinir senhas dos atendentes.

RF25: O gerente não poderá realizar pedidos como cliente.

6. Banco de Dados:
RF26: O sistema utilizará o banco SQLite para armazenar:
●	Usuários (clientes, atendentes, gerente)
●	Medicamentos
●	Pedidos
●	Itens dos pedidos

RF27: Cada medicamento terá: nome, descrição, preço e quantidade em estoque.

RF28: Cada pedido terá: cliente, data, medicamentos e valores totais.

7. Templates
RF29: Uso de extends/includes para layout.RF30: Páginas de erro personalizadas. 

8. Requisitos Técnicos 
RF30: Uso de request, redirect, url_for, make_response.
RF31: Código versionado no GitHub com entregas semanais. 
RF32: README com instruções de execução e estrutura do sistema.
