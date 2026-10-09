import csv
import re


class FormatoInvalidoError(Exception):
    pass


def validar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.search(padrao, email))


def validar_cpf(cpf):
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    return bool(re.search(padrao, cpf))


def validar_telefone(telefone):
    padrao = r"^\(\d{2}\) \d{5}-\d{4}$"
    return bool(re.search(padrao, telefone))


def validar_data(data):
    padrao = r"^\d{2}/\d{2}/\d{4}$"
    return bool(re.search(padrao, data))


nome_arquivo = "dados.csv"
validos = []
invalidos = []

try:
    with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            nome = linha["nome"]
            email = linha["email"]
            cpf = linha["cpf"]
            tel = linha["telefone"]
            data = linha["data"]

            motivo = ""

            if not validar_email(email):
                motivo = "E-mail inválido"
            elif not validar_cpf(cpf):
                motivo = "CPF inválido"
            elif not validar_telefone(tel):
                motivo = "Telefone inválido"
            elif not validar_data(data):
                motivo = "Data inválida"

            if motivo != "":
                raise FormatoInvalidoError(f"{nome} descartado: {motivo}")

            validos.append(linha)

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
except KeyError as e:
    print(f"Erro: Coluna ausente no arquivo CSV: {e}")
except FormatoInvalidoError as erro_custom:
    print(f"Aviso de validação: {erro_custom}")
else:
    print("Processamento concluído sem interrupções críticas!")
finally:
    total_lidos = len(validos) + len(invalidos)

    print("\n" + "=" * 55)
    print("              RELATÓRIO DE VALIDAÇÃO")
    print("=" * 55)
    print(f"Total de registros analisados: {total_lidos}")
    print(f"Total de registros válidos:    {len(validos)}")
    print(f"Total de registros inválidos:  {len(invalidos)}")

    print("\nREGISTROS APROVADOS:")
    for reg in validos:
        print(f" • {reg['nome']:<15} | CPF: {reg['cpf']} | {reg['email']}")

    if invalidos:
        print("\nREGISTROS REJEITADOS:")
        for reg in invalidos:
            print(f" • {reg['nome']:<15} | Motivo: {reg['motivo']}")
    print("=" * 55)