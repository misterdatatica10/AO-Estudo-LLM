import unittest
from unittest.mock import patch, MagicMock
from backend.ollama_client import OllamaClient

class TestOllamaClient(unittest.TestCase):
    def setUp(self):
        self.client = OllamaClient()
        self.sample_text = "Este é um texto de exemplo para teste."
        self.sample_question = "Qual é a capital de Portugal?"
        self.sample_context = "Portugal é um país da Europa."
        self.sample_topic = "Python Programming"

    @patch('requests.post')
    def test_generate_response(self, mock_post):
        # Configurar o mock
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": "Resposta de teste"}
        mock_post.return_value = mock_response

        # Testar a função
        response = self.client.generate_response("Teste")
        self.assertEqual(response, "Resposta de teste")

    @patch('requests.post')
    def test_generate_summary(self, mock_post):
        # Configurar o mock
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": "Resumo de teste"}
        mock_post.return_value = mock_response

        # Testar a função
        summary = self.client.generate_summary(self.sample_text)
        self.assertEqual(summary, "Resumo de teste")

    @patch('requests.post')
    def test_answer_question(self, mock_post):
        # Configurar o mock
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": "Lisboa"}
        mock_post.return_value = mock_response

        # Testar a função
        answer = self.client.answer_question(self.sample_question, self.sample_context)
        self.assertEqual(answer, "Lisboa")

    @patch('requests.post')
    def test_generate_study_plan(self, mock_post):
        # Configurar o mock
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "response": """{
                "main_concepts": ["Python Basics", "Data Types"],
                "topics": ["Variables", "Control Flow"],
                "exercises": ["Write a Hello World program"],
                "resources": ["Python Documentation"]
            }"""
        }
        mock_post.return_value = mock_response

        # Testar a função
        plan = self.client.generate_study_plan(self.sample_topic)
        self.assertIn("main_concepts", plan)
        self.assertIn("topics", plan)
        self.assertIn("exercises", plan)
        self.assertIn("resources", plan)

    def test_set_model(self):
        # Testar a função
        self.client.set_model("mistral")
        self.assertEqual(self.client.model, "mistral")

if __name__ == '__main__':
    unittest.main() 