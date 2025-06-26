import json
from typing import Dict, List, Optional
import streamlit as st

def format_study_plan(plan: Dict) -> str:
    """
    Formata um plano de estudos numa string legível.
    
    Args:
        plan: Dicionário contendo o plano de estudos
        
    Returns:
        str: Plano formatado
    """
    formatted = []
    
    if plan["main_concepts"]:
        formatted.append("## Conceitos Principais")
        for concept in plan["main_concepts"]:
            formatted.append(f"- {concept}")
        formatted.append("")
    
    if plan["topics"]:
        formatted.append("## Tópicos")
        for topic in plan["topics"]:
            formatted.append(f"- {topic}")
        formatted.append("")
    
    if plan["exercises"]:
        formatted.append("## Exercícios Sugeridos")
        for exercise in plan["exercises"]:
            formatted.append(f"- {exercise}")
        formatted.append("")
    
    if plan["resources"]:
        formatted.append("## Recursos")
        for resource in plan["resources"]:
            formatted.append(f"- {resource}")
    
    return "\n".join(formatted)

def validate_text_input(text: str, min_length: int = 10) -> bool:
    """
    Valida se o texto de entrada tem o comprimento mínimo necessário.
    
    Args:
        text: Texto a ser validado
        min_length: Comprimento mínimo necessário
        
    Returns:
        bool: True se o texto é válido, False caso contrário
    """
    return len(text.strip()) >= min_length

def display_error(message: str):
    """
    Exibe uma mensagem de erro no Streamlit.
    
    Args:
        message: Mensagem de erro
    """
    st.error(message)

def display_success(message: str):
    """
    Exibe uma mensagem de sucesso no Streamlit.
    
    Args:
        message: Mensagem de sucesso
    """
    st.success(message)

def display_warning(message: str):
    """
    Exibe uma mensagem de aviso no Streamlit.
    
    Args:
        message: Mensagem de aviso
    """
    st.warning(message)

def display_info(message: str):
    """
    Exibe uma mensagem informativa no Streamlit.
    
    Args:
        message: Mensagem informativa
    """
    st.info(message)

def format_markdown(text: str) -> str:
    """
    Formata o texto para exibição em Markdown.
    
    Args:
        text: Texto a ser formatado
        
    Returns:
        str: Texto formatado
    """
    # Substitui quebras de linha por espaços duplos + quebra de linha
    text = text.replace("\n", "  \n")
    
    # Adiciona espaços extras após pontos finais
    text = text.replace(". ", ".  ")
    
    return text 