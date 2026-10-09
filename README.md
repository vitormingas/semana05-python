# Sistema de Análise e Validação de Dados

Projeto prático desenvolvido para validar informações extraídas de arquivos utilizando Expressões Regulares (Regex) e tratamento de erros no Python.

## Estrutura do Projeto

- `dados.csv`: Arquivo de entrada com os dados cadastrais.
- `main.py`: Script Python com o fluxo de leitura, validação e relatório.
- `README.md`: Documentação técnica das decisões do projeto.

---

## 1. Expressões Regulares Aplicadas

- **E-mail:** `^[\w\.-]+@[\w\.-]+\.\w+$`  
  Aceita caracteres alfanuméricos, pontos e traços antes e depois do `@`, terminando com a extensão de domínio.
- **CPF:** `^\d{3}\.\d{3}\.\d{3}-\d{2}$`  
  Exige o formato pontuado padrão com dígitos numéricos (`000.000.000-00`).
- **Telefone:** `^\(\d{2}\) \d{5}-\d{4}$`  
  Verifica o formato com DDD entre parênteses, espaço, 5 dígitos, hífen e 4 dígitos.
- **Data:** `^\d{2}/\d{2}/\d{4}$`  
  Valida o padrão nacional de datas no formato dia/mês/ano (`DD/MM/AAAA`).

---

## 2. Tratamento de Exceções

O script utiliza a estrutura completa `try / except / else / finally`:

- `FileNotFoundError`: Capturado caso o caminho ou o nome do arquivo informado não exista.
- `KeyError`: Disparado se o cabeçalho do arquivo CSV estiver faltando colunas essenciais (`nome`, `email`, `cpf`, etc.).
- `FormatoInvalidoError`: Classe personalizada herdada de `Exception` para sinalizar cadastros que descumprem os padrões de regex exigidos pelas regras de negócio.
- `else`: Executado somente quando todo o arquivo é lido e validado com sucesso.
- `finally`: Bloco garantido que compila as métricas e exibe o relatório final na tela.

---

## 3. Exemplo de Entrada e Saída

### Entrada (`dados.csv`):

```csv
nome,email,cpf,telefone,data
Lucas Silva,lucas.silva@email.com,123.456.789-00,(11) 98765-4321,15/03/2024
Ana Souza,ana_souza@provedor.com.br,987.654.321-11,(21) 91234-5678,01/01/2023
Carlos Lima,carlos.email.com,111.222.333-44,(31) 8888-9999,10/12/2022
```
