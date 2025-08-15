# InfoFarma
Tema
Farmácia
1. Cadastro e autenticação
RF01: Qualquer pessoa poderá criar uma conta informando e-mail e senha.
RF02: Usuário poderá fazer login e logout.
RF03: As senhas devem ser armazenadas utilizando hash seguro.
RF04: Apenas usuários autenticados poderão acessar as páginas de gerenciamento
de medicamentos e perfil.
2. Gerenciamento de Perfil
RF05: O usuário poderá visualizar seus dados de perfil.
RF06: O usuário poderá editar seu próprio e-mail e senha.
RF07: O usuário poderá excluir sua conta.
3. Gerenciamento de Medicamentos
RF08: O usuário autenticado poderá visualizar a lista de medicamentos cadastrados
por ele.
RF09: O usuário autenticado poderá cadastrar novos medicamentos, informando
nome e descrição.
RF10: O usuário autenticado poderá editar nome e descrição de medicamentos que
ele mesmo cadastrou.
RF11: O usuário autenticado poderá excluir medicamentos que ele mesmo
cadastrou.
4. Banco de Dados
RF12: O sistema utilizará SQLite para armazenar:
●
Usuários (id, email, senha)
●
Medicamentos (id, nome, descrição, user_id)
RF13: Cada medicamento estará vinculado a um usuário através de
user_id.
5. Templates e Páginas
doc_requisitos.md 2025-08-08
RF14: Uso de extends/includes para o layout.
RF15: Páginas de erro personalizadas (404 e 500).
RF16: Páginas estáticas: Produtos, Promoções e Sobre.
6. Requisitos Técnicos
RF17: Uso de request, redirect, url_for, make_response.
RF18: Código versionado no GitHub com entregas semanais.
RF19: README com instruções de execução e estrutura do sistema.
