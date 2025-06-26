import unittest
from utils.helpers import (
    format_study_plan,
    validate_text_input,
    format_markdown
)

class TestHelpers(unittest.TestCase):
    def setUp(self):
        self.sample_plan = {
            "main_concepts": ["Python", "Data Types"],
            "topics": ["Variables", "Control Flow"],
            "exercises": ["Hello World"],
            "resources": ["Python Docs"]
        }
        
        self.sample_text = "Este é um texto de exemplo."
        self.sample_markdown = "Primeira linha\nSegunda linha"

    def test_format_study_plan(self):
        formatted = format_study_plan(self.sample_plan)
        
        # Verificar se todas as secções estão presentes
        self.assertIn("## Conceitos Principais", formatted)
        self.assertIn("## Tópicos", formatted)
        self.assertIn("## Exercícios Sugeridos", formatted)
        self.assertIn("## Recursos", formatted)
        
        # Verificar se os itens estão presentes
        self.assertIn("- Python", formatted)
        self.assertIn("- Variables", formatted)
        self.assertIn("- Hello World", formatted)
        self.assertIn("- Python Docs", formatted)

    def test_validate_text_input(self):
        # Testar texto válido
        self.assertTrue(validate_text_input(self.sample_text))
        
        # Testar texto muito curto
        self.assertFalse(validate_text_input("Curto"))
        
        # Testar texto vazio
        self.assertFalse(validate_text_input(""))
        
        # Testar texto com apenas espaços
        self.assertFalse(validate_text_input("   "))

    def test_format_markdown(self):
        formatted = format_markdown(self.sample_markdown)
        
        # Verificar se as quebras de linha foram formatadas corretamente
        self.assertIn("  \n", formatted)
        
        # Testar formatação de pontos finais
        text_with_periods = "Primeira frase. Segunda frase."
        formatted = format_markdown(text_with_periods)
        self.assertIn(".  ", formatted)

if __name__ == '__main__':
    unittest.main() 