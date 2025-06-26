import requests
import json
from typing import Dict, List, Optional

class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url
        self.model = "llama2"  # Modelo padrão

    def set_model(self, model_name: str):
        """Define o modelo a ser utilizado."""
        self.model = model_name

    def generate_response(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """
        Gera uma resposta utilizando o modelo Ollama.
        
        Args:
            prompt: O prompt do utilizador
            system_prompt: Instruções do sistema (opcional)
            
        Returns:
            str: Resposta gerada pelo modelo
        """
        try:
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
            
            if system_prompt:
                payload["system"] = system_prompt

            response = requests.post(f"{self.base_url}/api/generate", json=payload)
            response.raise_for_status()
            
            return response.json()["response"]

        except requests.ConnectionError:
            print(f"Erro de ligação: Não foi possível ligar a {self.base_url}")
            return "Erro de ligação: Verifique se o Ollama está em execução e acessível."
            
        except Exception as e:
            print(f"Erro ao gerar resposta: {str(e)}")
            return "Desculpe, ocorreu um erro ao processar a sua solicitação."

    def generate_summary(self, text: str) -> str:
        """
        Gera um resumo do texto fornecido.
        
        Args:
            text: Texto a ser resumido
            
        Returns:
            str: Resumo gerado
        """
        prompt = f"""Por favor, gere um resumo conciso do seguinte texto, destacando os pontos principais:

{text}

Resumo:"""
        
        return self.generate_response(prompt)

    def answer_question(self, question: str, context: str) -> str:
        """
        Responde a uma pergunta com base no contexto fornecido.
        
        Args:
            question: Pergunta a ser respondida
            context: Contexto para a resposta
            
        Returns:
            str: Resposta gerada
        """
        prompt = f"""Com base no seguinte contexto, responda à pergunta de forma clara e concisa:

Contexto:
{context}

Pergunta: {question}

Resposta:"""
        
        return self.generate_response(prompt)

    def generate_study_plan(self, topic: str) -> Dict:
        """
        Gera um plano de estudos para um tópico específico.
        
        Args:
            topic: Tópico de estudo
            
        Returns:
            Dict: Plano de estudos estruturado
        """
        prompt = f"""Gere um plano de estudos detalhado para o tópico: {topic}

O plano deve incluir:
1. Conceitos principais
2. Tópicos a serem estudados
3. Sugestões de exercícios
4. Recursos recomendados

Formate a resposta em JSON com as seguintes chaves:
- main_concepts: lista de conceitos principais
- topics: lista de tópicos
- exercises: lista de exercícios
- resources: lista de recursos"""

        response = self.generate_response(prompt)
        try:
            return json.loads(response)
        except:
            return {
                "main_concepts": [],
                "topics": [],
                "exercises": [],
                "resources": []
            } 