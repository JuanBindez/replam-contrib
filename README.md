# REPLAM: Retention Plan Manager

<details open><summary><strong>English summary</strong></summary>

This repository contains the replam project, a system for managing computing resource backups and their retention plans.
The idea of retention plans and rules contained here are part of a technical test for a Python Backend Developer job.

<br>

### The business rules are:
1. Create a lib that receives a retention plan and a date, and it should tell if the snapshot for this date should be retained or deleted.

### The retention plans are:
1. Standard: 42 days retention
    - We will retain each snapshot daily for 42 days
2. Gold: 42 days and 12 months retention
    - We will retain each snapshot daily for 42 days
    - We will retain the last snapshot of the month for 12 months
3. Platinum: 42 days, 12 months and 7 years
    - We will retain each snapshot daily for 42 days
    - We will retain the last snapshot of the month for 12 months
    - We will retain the last snapshot of the year for 7 years

<br>

## Instructions for running the project
1. Python and pip installed on the machine
2. Locally cloned **replam** project
3. Access the project folder with the command `cd replam`
4. It is recommended to create a virtual environment, for that run the command `python -m venv .` and `.\Scripts\activate` to activate it
5. Install the dependencies with the command `pip install requirements.txt`

<hr>

## Pytesting 🧪
Tests can be done in two ways:
1. Run the test scripts with the command `pytest`

![pytest_all](https://github.com/pctmoraes/replam/blob/main/img/pytest.png)

2. Run each test script individually, here's an example running the `pytest .\test\test_snapshot.py`

![pytest_snapshot](https://github.com/pctmoraes/replam/blob/main/img/pytest_one.png)

<hr>

## Class diagram

The project has three classes: Resource, Snapshot and RetentionPlan, and below is the class diagram illustrating each of them in more details:

![class_diagram](https://github.com/pctmoraes/replam/blob/main/img/Replam_class_diag.jpg)

</details>

<hr>

<details><summary><strong>Sumário em português</strong></summary>

Este repositório contém o projeto replam, um sistema para gerenciamento de backups de recursos de computação e seus planos de retenção.
A ideia de planos de retenção e regras contidas aqui fazem parte de um teste técnico para uma vaga de Python Backend Developer.

<br>

### As regras de negócio são:
1. Crie uma biblioteca que receba um plano de retenção e uma data, e ela deve informar se o snapshot dessa data deve ser retido ou excluído.

### Os planos de retenção são:
1. Standard: retenção de 42 dias
    - Manteremos cada snapshot diariamente por 42 dias
2. Gold: retenção de 42 dias e 12 meses
    - Manteremos cada snapshot diariamente por 42 dias
    - Manteremos o último snapshot do mês por 12 meses
3. Platinum: (42 dias, 12 meses e 7 anos)
    - Manteremos cada snapshot diariamente por 42 dias
    - Manteremos o último snapshot do mês por 12 meses
    - Manteremos o último snapshot do ano por 7 anos

<br>


## Instruções para a execução do projeto
1. Python e pip instalados na máquina
2. Projeto **replam** clonado localmente
3. Acesse a pasta do projeto com o comando `cd replam`
4. Recomenda-se criar um ambiente virtual, para isso execute o comando `python -m venv .` e `.\Scripts\activate` para ativá-lo
5. Instale as dependências com o comando `pip install requirements.txt`

<hr>

## Pytesting 🧪
Os testes podem ser executados de duas formas:
1. Execute os scripts de teste com o comando `pytest`

![pytest_all](https://github.com/pctmoraes/replam/blob/main/img/pytest.png)

2. Execute os scripts de teste individualmente, exemplo da execução do `pytest .\test\test_snapshot.py`

![pytest_snapshot](https://github.com/pctmoraes/replam/blob/main/img/pytest_one.png)


<hr>

## Diagrama de classes

O projeto possui três classes: Resource, Snapshot e RetentionPlan, e abaixo está o diagrama de classes ilustrando cada uma delas com mais detalhes:

![class_diagram](https://github.com/pctmoraes/replam/blob/main/img/Replam_class_diag.jpg)


</details>
