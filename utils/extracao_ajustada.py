import pdfplumber
import re
import os
import pandas as pd

def extracao_infos2(pasta, arquivo_resultado):

    df_lido = pd.read_excel(arquivo_resultado)
    arquivos_lidos = df_lido['ARQUIVO'].unique()
    arquivos_totais = os.listdir(pasta)

    resultados = []
    for file in arquivos_totais:

        if file in arquivos_lidos:
            continue
        else:
            
            print(f"Lendo arquivo: {file}")
            pdf_path = os.path.join(pasta, file)

            # regex para PROCESSO, RAMO, TEMA, DESTAQUE
            pattern_infos = re.compile(
                r"PROCESSO\s+(.*?)\s+RAMO DO DIREITO\s+(.*?)\s+TEMA\s+(.*?)\s+DESTAQUE\s+(.*?)(?=INFORMAÇÕES DO INTEIRO TEOR)",
                re.DOTALL
            )

            # regex para INFORMAÇÕES DO INTEIRO TEOR (até próxima seção)
            pattern_inteiro_teor = re.compile(
                r"INFORMAÇÕES DO INTEIRO TEOR\s+(.*?)(?=(?:\n(?:PROCESSO|DESTAQUE|PRIMEIRA|SEGUNDA|TERCEIRA|QUARTA|QUINTA|SEXTA|SÉTIMA|OITAVA|SEÇÃO|INFORMAÇÕES ADICIONAIS)|\Z))",
                re.DOTALL
            )

            # extrair texto de todas as páginas
            with pdfplumber.open(pdf_path) as pdf:
                all_text = ""
                for page in pdf.pages:
                    all_text += page.extract_text() + "\n"

            # aplicar regex PROCESSO, RAMO, TEMA, DESTAQUE
            matches_infos = pattern_infos.findall(all_text)

            # aplicar regex INTEIRO TEOR
            matches_inteiro_teor = pattern_inteiro_teor.findall(all_text)

            # pode haver mais de um bloco de inteiro teor no mesmo PDF
            for i, (processo, ramo, tema, destaque) in enumerate(matches_infos):
                inteiro_teor = matches_inteiro_teor[i] if i < len(matches_inteiro_teor) else ""

                dados = {
                    "PROCESSO": " ".join(processo.split()),
                    "RAMO_DO_DIREITO": " ".join(ramo.split()),
                    "TEMA": " ".join(tema.split()),
                    "DESTAQUE": " ".join(destaque.split()),
                    "INTEIRO_TEOR": " ".join(inteiro_teor.split()),
                    "ARQUIVO": file
                }
                resultados.append(dados)
                print("Bloco extraído com sucesso!")

    df_novo = pd.DataFrame(resultados)

    if df_novo.empty:
        return 'Todos os arquivos já haviam sido lidos.'
    else:
        # ACRESCENTAR O LINK DO PDF
        df_novo['LINK'] = 'https://processo.stj.jus.br/SCON/GetPDFINFJ?edicao=' + df_novo['ARQUIVO'].str.replace('Inf','').str.replace('.pdf','')

        # SEGREGAR O RAMO DO DIREITO EM VÁRIAS LINHAS 
        df_novo['RAMO_AJUSTE'] = df_novo['RAMO_DO_DIREITO'].str.split(',')
        df_novo = df_novo.explode('RAMO_AJUSTE').reset_index(drop=True)
        df_novo = df_novo.drop('RAMO_DO_DIREITO',axis=1)
        df_novo = df_novo.rename(columns={'RAMO_AJUSTE':'RAMO_DO_DIREITO'})

        # JUNTAR OS ARQUIVOS JÁ LIDOS COM AS NOVAS EXTRAÇÕES
        df_final = pd.concat([df_lido, df_novo])
        df_final.to_excel("output/jurisprudencia_extraida.xlsx", index=False)
        return 'Arquivo jurisprudencia_extraida.xlsx atualizado com as informações dos novos PDFs.'
