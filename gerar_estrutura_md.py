# ==============================================================================
# UNIDADE CURRICULAR: PROJETO APLICADO I
# EMPRESA PARCEIRA: SCHULZ S.A.
# SCRIPT DE GERAÇÃO AUTOMÁTICA DA DOCUMENTAÇÃO EM MARKDOWN (01_estrutura.md)
# ==============================================================================
conteudo_markdown = """# Estruturação e Modelagem do Banco de Dados Relacional (SQLite)
**Projeto:** Automação da Emissão de Certificados de Calibração (Schulz S.A.)  
**Equipe:** Bruno Henridson Galvão, Lucas Jean Pacheco, Mateus Junior Consoli, Rodrigo Nunes, Sthefane Passos Pita  

---

## 1. Contexto e Problematização (Transição de Planilhas para BD)
Na Entrega 01, mapeamos que o laboratório de metrologia da Schulz S.A. realiza cerca de 600 calibrações mensais utilizando arquivos em Excel com múltiplas abas dependentes entre si. Esse modelo apresenta riscos operacionais críticos, tais como:
- Necessidade recorrente de ajuste manual de linhas conforme a quantidade de características da peça inspecionada;
- Ocorrência de erros de fórmulas em linhas vazias ou referências quebradas (#VALUE!, #REF!, #DIV/0!);
- Falta de validação consistente de dados;
- Duplicidade no cadastro de equipamentos e técnicos em diferentes arquivos.

A ausência de um Sistema Gerenciador de Banco de Dados compromete a rastreabilidade histórica dos certificados emitidos e expõe as regras de negócio a edições manuais indevidas. A migração para um banco de dados relacional em SQLite elimina essas fragilidades ao unificar e persistir os dados cadastrais e as medições, assegurando integridade referencial, padronização de tipos de dados e um histórico auditável para a emissão automatizada dos certificados em PDF.

---

## 2. Divisão do Banco de Dados em 3 Entidades Principais
Para eliminar redundâncias e garantir a integridade das informações metrológicas, o banco foi estruturado em três entidades fundamentais:

### 2.1. Entidade 1: `tecnico`
Armazena os dados cadastrais dos técnicos e metrologistas responsáveis pelas medições e calibrações.
- **id_tecnico:** Chave Primária (INTEGER AUTOINCREMENT), identificador único do técnico.
- **nome_tecnico:** Nome completo do profissional (TEXT NOT NULL).
- **cargo:** Função/cargo ocupado pelo técnico (TEXT NOT NULL).
- **departamento:** Setor de atuação do técnico (TEXT NOT NULL).

### 2.2. Entidade 2: `equipamento`
Registra os instrumentos e dispositivos da fábrica submetidos a medições e calibrações.
- **id_equipamento:** Chave Primária (INTEGER AUTOINCREMENT), identificador do instrumento.
- **codigo_tag:** Código gravado no instrumento/patrimônio (TEXT NOT NULL, UNIQUE).
- **nome_equipamento:** Descrição/denominação do instrumento (TEXT NOT NULL).
- **modelo:** Modelo do equipamento (TEXT NOT NULL).
- **data_aquisicao:** Data em que o equipamento foi integrado à planta (DATE NOT NULL).

### 2.3. Entidade 3: `medicao`
Tabela transacional que conecta o técnico executante ao equipamento aferido, registrando o evento metrológico.
- **id_medicao:** Chave Primária (INTEGER AUTOINCREMENT).
- **id_equipamento:** Chave Estrangeira referenciando a tabela `equipamento` (INTEGER NOT NULL).
- **id_tecnico:** Chave Estrangeira referenciando a tabela `tecnico` (INTEGER NOT NULL).
- **parametro_medido:** Grandeza ou cota inspecionada (TEXT NOT NULL).
- **valor_nominal:** Valor de projeto/referência (REAL NOT NULL).
- **tolerancia_min:** Limite inferior de tolerância (REAL NOT NULL).
- **tolerancia_max:** Limite superior de tolerância (REAL NOT NULL).
- **valor_obtido:** Leitura real registrada na medição (REAL NOT NULL).
- **status:** Situação da medição, restrita a 'APROVADO' ou 'REPROVADO' (TEXT CHECK).
- **data_medicao:** Registro temporal da execução (DATETIME DEFAULT CURRENT_TIMESTAMP).

---

## 3. Justificativa da Eliminação de Dados Duplicados
A normalização do banco em tabelas separadas resolve os problemas identificados na Fase 01:
1. **Garantia de Qualidade e Histórico:** Toda medição fica permanentemente vinculada ao equipamento exato e ao técnico responsável, atendendo às normas metrológicas.
2. **Eficiência no Armazenamento:** Técnicos e equipamentos são cadastrados apenas uma vez, evitando redigitação manual e inconsistências ortográficas a cada nova calibração.
3. **Integridade Referencial:** Impede o registro órfão de medições vinculadas a instrumentos ou técnicos inexistentes no sistema.
"""
# Execução da gravação do arquivo .md
nome_arquivo = "01_estrutura.md"
try:
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo_markdown)
    print("=" * 60)
    print(f"SUCCESS: O arquivo '{nome_arquivo}' foi gerado com sucesso!")
    print("Abra o VS Code, selecione o arquivo e pressione 'Ctrl + Shift + V'")
    print("para visualizar a documentacao formatada.")
    print("=" * 60)
except Exception as e:
    print(f"ERRO ao gerar o arquivo: {e}")