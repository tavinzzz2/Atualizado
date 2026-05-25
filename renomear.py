import os
import unicodedata

def limpar_nome(nome):
    # remove acentos
    nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII')
    
    # troca espaços por hífen
    nome = nome.replace(' ', '-')
    
    # deixa tudo minúsculo
    nome = nome.lower()
    
    return nome

def renomear_pasta(pasta):
    for root, dirs, files in os.walk(pasta):
        for nome in files:
            caminho_antigo = os.path.join(root, nome)
            
            novo_nome = limpar_nome(nome)
            caminho_novo = os.path.join(root, novo_nome)
            
            os.rename(caminho_antigo, caminho_novo)
        
        for nome in dirs:
            caminho_antigo = os.path.join(root, nome)
            
            novo_nome = limpar_nome(nome)
            caminho_novo = os.path.join(root, novo_nome)
            
            if caminho_antigo != caminho_novo:
                os.rename(caminho_antigo, caminho_novo)

# coloca o caminho da tua pasta aqui
pasta = "D:/meu-site""

renomear_pasta(pasta)

print("✅ Tudo renomeado com sucesso!")