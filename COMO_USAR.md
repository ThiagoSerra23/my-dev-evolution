# Guia de Uso - Dev Daily Evolution 📘

Este guia explica como configurar, executar e manter o seu repositório de evolução contínua.

## 🚀 1. Configuração Inicial (GitHub)

Para que a automação funcione, este código precisa estar hospedado no GitHub.

1.  **Crie um novo repositório** no GitHub (ex: `my-dev-evolution`).
2.  **Envie o código** para lá:

    Abra o terminal na pasta `dev-daily-evolution` e execute:

    ```bash
    # Inicializa o git se ainda não fez
    git init
    
    # Adiciona todos os arquivos
    git add .
    
    # Primeiro commit
    git commit -m "feat: initial commit of evolution system"
    
    # Renomeia a branch principal para main (boa prática)
    git branch -M main
    
    # Conecta com seu repositório remoto (substitua a URL)
    git remote add origin https://github.com/ThiagoSerra23/my-dev-evolution.git
    
    # Envia para o GitHub
    git push -u origin main
    ```

3.  **Ative o GitHub Actions**:
    *   No GitHub, vá na aba **Actions**.
    *   Você deve ver o workflow "Auto Evolution" listado.
    *   Se necessário, clique em "Enable workflow".
    *   **Importante**: A automação só roda automaticamente em repositórios públicos ou se você tiver minutos de Actions (contas gratuitas têm limites).

---

## 🤖 2. Como a Automação Funciona

O sistema roda "sozinho" com base no arquivo `.github/workflows/auto-evolution.yml`.

*   **Horário**: A cada 30 minutos.
*   **Dias**: Segunda a Sexta (dias úteis).
*   **Janela**: 09:00 às 18:00 (UTC, ajuste o fuso no workflow se quiser).

Quando roda, ele executa o script `scripts/auto_evolution.py`, que decide aleatoriamente o que fazer:
*   50% de chance de escrever um **Log** (`logs/`).
*   30% de chance de escrever um **Estudo** (`studies/`).
*   10% de chance de criar/editar código **Backend**.
*   10% de chance de criar/editar código **Frontend**.

---

## 🛠 3. Personalização (Faça do seu jeito!)

Para que o repositório pareça **SEU**, você deve personalizar os tópicos.

### Mudar os temas de estudo
Edite o arquivo `scripts/auto_evolution.py`:

Procure pela função `update_studies()` e altere a lista `topics`:

```python
topics = [
    ("Kubernetes", "Pods são a menor unidade de deploy."),
    ("AWS Lambda", "Serverless reduz custo de infra ociosa."),
    # Adicione seus interesses reais aqui!
]
```

### Mudar os logs de atividade
Procure pela função `update_log()` e mude a lista `activities`:

```python
activities = [
    "Estudando Terraform",
    "Praticando algoritmos no LeetCode",
    "Melhorando acessibilidade do site pessoal",
]
```

---

## ▶️ 4. Execução Manual

Se você quiser forçar uma atualização agora mesmo (sem esperar o agendamento):

**Opção A: Via GitHub**
1.  Vá na aba **Actions**.
2.  Selecione **Auto Evolution**.
3.  Clique em **Run workflow**.

**Opção B: Localmente (Se tiver Python instalado)**
1.  Abra o terminal na pasta do projeto.
2.  Execute:
    ```bash
    python scripts/auto_evolution.py
    ```
3.  Confira os arquivos modificados e faça o commit manual se quiser:
    ```bash
    git add .
    git commit -m "study: atualização manual"
    git push
    ```

---

## ❓ Perguntas Frequentes

**Isso vai sujar meu gráfico de contribuições?**
Vai preenchê-lo com quadrados verdes nos dias úteis. Como as mensagens de commit seguem um padrão (`study:`, `feat:`, `docs:`), fica claro que é um repositório organizado.

**Posso ser banido do GitHub?**
Não. Isso é atividade legítima de código e documentação. Não estamos usando bots para dar "stars" falsas ou spam. É um diário de estudos automatizado.

**Como paro a automação?**
Basta ir no arquivo `.github/workflows/auto-evolution.yml` e remover as linhas de `schedule` (cron), ou desativar o workflow na aba Actions do GitHub.
