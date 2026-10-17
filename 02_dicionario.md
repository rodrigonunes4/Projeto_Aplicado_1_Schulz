# Dicionário de Dados do Sistema - SQLite

### Tabela: `tecnico`
| Campo / Atributo | Tipo de Dado | Restrições | Descrição |
| :--- | :--- | :--- | :--- |
| `id_tecnico` | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador único do técnico. |
| `nome_tecnico` | TEXT | NOT NULL | Nome do técnico executante. |
| `cargo` | TEXT | NOT NULL | Cargo/função do técnico. |
| `departamento` | TEXT | NOT NULL | Departamento do técnico executante. |

---

### Tabela: `equipamento`
| Campo / Atributo | Tipo de Dado | Restrições | Descrição |
| :--- | :--- | :--- | :--- |
| `id_equipamento` | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador de cada equipamento. |
| `codigo_tag` | TEXT | NOT NULL, UNIQUE | Código/patrimônio gravado na ferramenta. |
| `nome_equipamento` | TEXT | NOT NULL | Descrição da ferramenta/instrumento. |
| `modelo` | TEXT | NOT NULL | Modelo da ferramenta. |
| `data_aquisicao` | DATE | NOT NULL | Data de aquisição do instrumento. |

---

### Tabela: `medicao`
| Campo / Atributo | Tipo de Dado | Restrições | Descrição |
| :--- | :--- | :--- | :--- |
| `id_medicao` | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador único do evento de medição. |
| `id_equipamento` | INTEGER | FOREIGN KEY NOT NULL | Vínculo com a tabela `equipamento` (Chave Estrangeira). |
| `id_tecnico` | INTEGER | FOREIGN KEY NOT NULL | Vínculo com a tabela `tecnico` (Chave Estrangeira). |
| `parametro_medido` | TEXT | NOT NULL | Variável/cota aferida no ensaio. |
| `valor_nominal` | REAL | NOT NULL | Valor teórico de referência. |
| `tolerancia_min` | REAL | NOT NULL | Limite inferior para o ensaio. |
| `tolerancia_max` | REAL | NOT NULL | Limite superior para o ensaio. |
| `valor_obtido` | REAL | NOT NULL | Leitura real coletada durante a medição. |
| `status` | TEXT | CHECK (status IN ('APROVADO', 'REPROVADO')) | Resultado da avaliação frente às tolerâncias. |
| `data_medicao` | DATETIME | DEFAULT CURRENT_TIMESTAMP | Data e hora em que a calibração foi realizada. |
