# Challenge CPTM - FIAP
Sistema de Monitoramento desenvolvido em conjunto com a FIAP como projeto acadêmico
**********

### 1. Instruções Iniciais

O sistema usará o **Sqlite** como banco de dados local.

Para a preparação do ambiente de desenvolvimento siga os seguintes passos:

- **1)** Criar um **ambiente virtual** para desenvolvimento. Nossa linguagem será **Python 3.7.5 com Django 3.1.3**.
- **2)** Rode `pip install -r requirements.txt`.
- **3)** Rode `python manage.py migrate`. Se não ocorrer erros, prossiga;
- **4)** Rode `python manage.py runserver`;

### 2. Arquitetura

3 níveis

**Nível 0 - Core**
* Contém os arquivos de configuração do projeto (settings, urls, wsgi)
* Contém as bibliotecas de JavaScript 
* Contém as definições de css
* Contém arquivos base de telas, forms e listas
* Contém widgets

**Nível 1 - Apps**
* Contém um app para cada módulo do sistema

Os apps possuem pastas static e template (para telas de uso específico)

**Nível 2 - Subapps**
* Contém os subapps de cada projeto do nível 1

### 3. Menu de Navegação e Views

Na pasta templates do core temos o `base.html`, trata-se da master page do sistema. Praticamente todos os templates irão herdar (direta ou indiretamente) deste arquivo.

Para incluir o `base.html` em suas páginas, basta adicionar a linha de código `{% extends 'base.html' %}` no inicio do arquivo html.

Como o menu de navegação é sensível ao app, as views de cada app precisam passar o seu template de menu através da variável "menu_navbar" que é utilizada no seguinte trecho do base: `{% include menu_navbar %}`

### 4. Models

Em um mesmo app (nível 1) não podem existir modelos com nome duplicado. Todos os models precisam ter o atributo `app_label = '<nome_do_app>'` em sua `class Meta`.

### 5. Grupos e Permissões

#### Grupos
Os grupos específicos para cada App devem ser nomeados da seguinte forma `<nome_do_app>.<nome_do_grupo>`. 
Ex: `core.admin`.

#### Permissões - Apps

As permissões devem ser referenciadas da seguinte forma: `<nome_do_app>.<nome_da_permissão>`.

Obs: não podem existir permissões com nome duplicado no mesmo app (nível 1)

### 6. Referências a templates e url's

As referências a um template devem ser feitas com o caminho absoluto. Se o template estiver no core basta utilizar o seu nome.

ex1: `template_name = "base_list.html"`
ex2: `{% extends "base.html" %}` (neste caso base está na pasta templates do core)
ex3: `reverse("home")` Página Inicial

A estrutura de templates dentro dos apps deve ser:

nível1: `templates/<nome_do_app>`
nível2: `templates/<nome_do_app>/<nome_do_subapp>`

### 7. JavaScript e Css

As bibliotecas e definições de javascript e css que são de utilidade geral estão na pasta static raiz.

Para utilização de featutes específicas, deve-se implementar no nível da folha os blocos `{% block css %}`, `{% block js %}` e `{% block base_js %}`. 

### 8. Tutorial de Criação de Novo App

- **1** - Dentro da pasta raiz do projeto, execute o comando: `./manage.py startapp [nome_do_app]`


- **2** - No arquivo `core/settings.py`, adicione na variável INSTALLED_APPS:

```
'[nome_do_app]',
'[nome_do_app].[nome_do_subapp]',
```

**3)** No arquivo `core/urls.py`, adicione a linha:
	path('[nome-do-app]', include('[nome-do-app].urls'), name='[nome-do-app]'),
