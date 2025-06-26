import pandas as pd
import re
import os

def carregar_dados_projetos():
    """Carrega e processa os dados dos projetos da feira."""
    try:
        # Caminho relativo ao diretório do script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, "..", "data", "projects_data.csv")
        
        # Carrega a planilha com duas tabelas (esquerda/direita)
        df = pd.read_csv(csv_path)

        # Trata a tabela da esquerda
        tabela1 = df[["Ano", "Turma", "Curso", "Proposta de Produção (descrever)", "Espaço do CC", "Tipo"]]
        tabela1 = tabela1.dropna(subset=["Proposta de Produção (descrever)"])

        # Trata a tabela da direita
        tabela2 = df[["Ano.1", "Turma.1", "Curso.1", "Proposta de Produção (descrever).1", "Espaço do CC.1", "Tipo.1"]]
        tabela2.columns = ["Ano", "Turma", "Curso", "Proposta de Produção (descrever)", "Espaço do CC", "Tipo"]
        tabela2 = tabela2.dropna(subset=["Proposta de Produção (descrever)"])

        # Junta e normaliza
        tabela = pd.concat([tabela1, tabela2], ignore_index=True)
        for col in ["Turma", "Curso", "Proposta de Produção (descrever)", "Espaço do CC", "Tipo"]:
            tabela[col] = tabela[col].astype(str).str.strip().str.lower()

        return tabela
    except Exception as e:
        print(f"❌ Erro ao carregar dados dos projetos: {e}")
        return None

def buscar_projeto(pergunta: str, tabela):
    """Busca informações sobre projetos baseado na pergunta."""
    if tabela is None:
        return "❌ Dados dos projetos não disponíveis."
    
    pergunta = pergunta.lower().strip()
    
    # Busca por projeto específico (palavras-chave no nome)
    palavras_chave = pergunta.split()
    for _, row in tabela.iterrows():
        projeto = row["Proposta de Produção (descrever)"]
        if any(palavra in projeto for palavra in palavras_chave if len(palavra) > 3):
            return (
                f"📌 Projeto: {row['Proposta de Produção (descrever)'].title()}\n"
                f"📍 Local: {row['Espaço do CC'].title()}\n"
                f"🎯 Tipo: {row['Tipo'].title()}\n"
                f"📚 Curso: {row['Curso'].upper()}\n"
                f"👥 Turma: {row['Turma']}"
            )

    # Busca por curso
    cursos = re.findall(r"\b(iot|adm|ti|mmd|cdd|chs|mkt|mkd|ia)\b", pergunta)
    if cursos:
        curso = cursos[0]
        encontrados = tabela[tabela['Curso'].str.contains(curso, na=False)]
        if not encontrados.empty:
            resposta = [f"📘 Projetos do curso {curso.upper()}:"]
            for _, row in encontrados.head(5).iterrows():  # Limita a 5 resultados
                resposta.append(f"• {row['Proposta de Produção (descrever)'].title()} - {row['Espaço do CC'].title()}")
            if len(encontrados) > 5:
                resposta.append(f"... e mais {len(encontrados) - 5} projetos")
            return "\n".join(resposta)

    # Busca por turma
    turma_match = re.search(r"turma\s*(\d+)", pergunta)
    if turma_match:
        turma_num = turma_match.group(1)
        encontrados = tabela[tabela['Turma'].str.contains(turma_num, na=False)]
        if not encontrados.empty:
            resposta = [f"👥 Projetos da turma {turma_num}:"]
            for _, row in encontrados.head(5).iterrows():
                resposta.append(f"• {row['Proposta de Produção (descrever)'].title()} - {row['Espaço do CC'].title()}")
            if len(encontrados) > 5:
                resposta.append(f"... e mais {len(encontrados) - 5} projetos")
            return "\n".join(resposta)

    # Busca por local/espaço
    espacos = ["saguão", "auditório", "multiuso", "mezanino", "cavalo", "lab", "área externa"]
    for espaco in espacos:
        if espaco in pergunta:
            encontrados = tabela[tabela['Espaço do CC'].str.contains(espaco, na=False)]
            if not encontrados.empty:
                resposta = [f"📍 Projetos no {espaco.title()}:"]
                for _, row in encontrados.head(5).iterrows():
                    resposta.append(f"• {row['Proposta de Produção (descrever)'].title()} ({row['Curso'].upper()})")
                if len(encontrados) > 5:
                    resposta.append(f"... e mais {len(encontrados) - 5} projetos")
                return "\n".join(resposta)

    return None  # Retorna None se não encontrar nada

# 🚀 Teste do módulo (só roda se executar este arquivo diretamente)
if __name__ == "__main__":
    print("🎤 Agente de localização da Feira")
    tabela = carregar_dados_projetos()
    
    if tabela is not None:
        print(f"✅ {len(tabela)} projetos carregados!")
        
        while True:
            pergunta = input("\n❓ Faça sua pergunta (ou 'sair'): ").strip()
            if pergunta.lower() in ["sair", "exit", "quit"]:
                print("👋 Encerrando agente.")
                break
            
            resultado = buscar_projeto(pergunta, tabela)
            if resultado:
                print("\n" + resultado)
            else:
                print("\n❌ Nenhum projeto encontrado para sua busca.")
    else:
        print("❌ Não foi possível carregar os dados dos projetos.")
