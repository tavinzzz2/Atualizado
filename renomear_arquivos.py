"""
PEDAÇO MODERNO — Script de Renomeação (versão correta)
=======================================================
Renomeia as pastas e arquivos diretamente na raiz do projeto.

COMO USAR:
1. Este script já está na pasta do index.html
2. No CMD (já aberto nessa pasta), execute:
       python renomear_arquivos.py
3. Pronto — suba tudo para o Vercel.
"""

import os
import unicodedata
import re

def slugify(texto):
    """Minúsculo + sem acento + hífens."""
    texto = unicodedata.normalize('NFKD', texto)
    texto = texto.encode('ascii', 'ignore').decode('ascii')
    texto = texto.lower()
    texto = re.sub(r'\s+', '-', texto.strip())
    texto = re.sub(r'[^a-z0-9\-\.]', '', texto)
    return texto

# Mapeamento exato: nome atual → nome novo
PASTAS = {
    "calça bri m acetinado slim":         "calca-bri-m-acetinado-slim",
    "calça chino":                        "calca-chino",
    "calça de alfaiataria com regulagem": "calca-de-alfaiataria-com-regulagem",
    "calça de alfaiataria":               "calca-de-alfaiataria",
    "calça jeans":                        "calca-jeans",
    "calça sarja":                        "calca-sarja",
    "camisa colarinho italiano":          "camisa-colarinho-italiano",
    "camisa gola polo":                   "camisa-gola-polo",
    "camiseta basica gola tradicional":   "camiseta-basica-gola-tradicional",
    "camiseta gola media premium":        "camiseta-gola-media-premium",
    "costumes (terno)":                   "costumes-terno",
}

def renomear_arquivos_dentro(pasta):
    """Renomeia cada arquivo dentro da pasta para slug."""
    for nome in os.listdir(pasta):
        caminho = os.path.join(pasta, nome)
        if os.path.isfile(caminho):
            base, ext = os.path.splitext(nome)
            novo_nome = slugify(base) + ext.lower()
            novo_caminho = os.path.join(pasta, novo_nome)
            if caminho != novo_caminho:
                os.rename(caminho, novo_caminho)
                print(f"    arquivo: '{nome}' -> '{novo_nome}'")

def main():
    print("=" * 52)
    print("  PEDACO MODERNO - Renomeacao de Pastas/Arquivos")
    print("=" * 52)
    print()

    erros = []

    for nome_atual, nome_novo in PASTAS.items():
        if os.path.isdir(nome_atual):
            print(f"Pasta: '{nome_atual}'")
            renomear_arquivos_dentro(nome_atual)
            os.rename(nome_atual, nome_novo)
            print(f"  -> '{nome_novo}'\n")

        elif os.path.isdir(nome_novo):
            print(f"Pasta '{nome_novo}' ja renomeada, verificando arquivos...")
            renomear_arquivos_dentro(nome_novo)
            print()

        else:
            erros.append(nome_atual)
            print(f"AVISO: '{nome_atual}' nao encontrada (pulando)\n")

    print("=" * 52)
    if erros:
        print(f"Pastas nao encontradas: {erros}")
    else:
        print("Tudo renomeado! Pode subir para o Vercel.")
    print("=" * 52)
    input("\nPressione Enter para fechar...")

if __name__ == "__main__":
    main()
