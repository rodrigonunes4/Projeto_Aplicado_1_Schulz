-- ==============================================================================
-- UNIDADE CURRICULAR: PROJETO APLICADO I
-- EMPRESA PARCEIRA: SCHULZ S.A.
-- ITEM 03: SCRIPT DDL DE CRIAÇÃO DO BANCO DE DADOS RELACIONAL (SQLite)
-- Prof. MSc. Hugo Menezes Barra | Prof. Rodrigo Losina
-- ==============================================================================
-- Habilita o suporte a chaves estrangeiras no SQLite
PRAGMA foreign_keys = ON;

-- 1. Criação da tabela de Técnicos / Responsáveis
CREATE TABLE IF NOT EXISTS tecnico (
    id_tecnico INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_tecnico TEXT NOT NULL,
    cargo TEXT NOT NULL,
    departamento TEXT NOT NULL
);

-- 2. Criação da tabela de Equipamentos / Instrumentos
CREATE TABLE IF NOT EXISTS equipamento (
    id_equipamento INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_tag TEXT NOT NULL UNIQUE,
    nome_equipamento TEXT NOT NULL,
    modelo TEXT NOT NULL,
    data_aquisicao DATE NOT NULL
);

-- 3. Criação da tabela transacional de Medições
CREATE TABLE IF NOT EXISTS medicao (
    id_medicao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_equipamento INTEGER NOT NULL,
    id_tecnico INTEGER NOT NULL,
    parametro_medido TEXT NOT NULL,
    valor_nominal REAL NOT NULL,
    tolerancia_min REAL NOT NULL,
    tolerancia_max REAL NOT NULL,
    valor_obtido REAL NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('APROVADO', 'REPROVADO')),
    data_medicao DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_equipamento) REFERENCES equipamento (id_equipamento) ON DELETE RESTRICT,
    FOREIGN KEY (id_tecnico) REFERENCES tecnico (id_tecnico) ON DELETE RESTRICT
);