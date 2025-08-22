import pdfplumber
import re
import os
import pandas as pd

def extracao_infos(pasta, arquivo_resultado):

    df_lido = pd.read_excel(arquivo_resultado)
    arquivos_lidos = df_lido['ARQUIVO'].unique()
    arquivos_totais = os.listdir(pasta)

    # organizar os dados
    resultados = []
    for file in arquivos_totais:

        if file in arquivos_lidos:
            continue
        else:
            
            print(f"Lendo arquivo: {file}")
            # caminho do PDF
            pdf_path = f"data/{file}"

            # regex para capturar o bloco
            # - PROCESSO (até a quebra de linha seguinte)
            # - RAMO DO DIREITO (até a quebra de linha seguinte)
            # - TEMA (até a quebra de linha seguinte)
            # - DESTAQUE (texto abaixo, até antes de PROCESSO seguinte ou fim)
            pattern = re.compile(
                r"PROCESSO\s+(.*?)\s+RAMO DO DIREITO\s+(.*?)\s+TEMA\s+(.*?)\s+DESTAQUE\s+(.*?)(?=INFORMAÇÕES DO INTEIRO TEOR)",
                re.DOTALL
            )

            with pdfplumber.open(pdf_path) as pdf:
                all_text = ""
                for page in pdf.pages:
                    all_text += page.extract_text() + "\n"

            # aplicar regex
            matches = pattern.findall(all_text)

            for processo, ramo, tema, destaque in matches:
                # limpar espaços e quebras de linha
                dados = {
                    "PROCESSO": " ".join(processo.split()),
                    "RAMO_DO_DIREITO": " ".join(ramo.split()),
                    "TEMA": " ".join(tema.split()),
                    "DESTAQUE": " ".join(destaque.split()),
                    'ARQUIVO': file
                }
                resultados.append(dados)
                print('Arquivo lido com sucesso!')

            # imprimir ou salvar
            #    print("="*80)
            #for r in resultados:
            #    print("PROCESSO:", r["PROCESSO"])
            #    print("RAMO DO DIREITO:", r["RAMO_DO_DIREITO"])
            #    print("TEMA:", r["TEMA"])
            #    print("DESTAQUE:", r["DESTAQUE"])

    df_novo = pd.DataFrame(resultados)

    if df_novo.empty:
    
        return 'Todos os arquivos já haviam sido lidos.'

    else:

        df_novo['LINK'] = 'https://processo.stj.jus.br/SCON/GetPDFINFJ?edicao=' + df_novo['ARQUIVO'].str.replace('Inf','').str.replace('.pdf','')
        df_final = pd.concat([df_lido,df_novo])

        df_final.to_excel("output/jurisprudencia_extraida.xlsx", index=False)
        return 'Arquivo jurisprudencia_extraida.xlsx atualizado com as informações dos novos PDFs.'