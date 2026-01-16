import os
import random
import datetime

# Configurações de diretórios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
STUDIES_DIR = os.path.join(BASE_DIR, 'studies')
BACKEND_DIR = os.path.join(BASE_DIR, 'backend', 'snippets')
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend', 'components')
DB_DIR = os.path.join(BASE_DIR, 'database', 'queries')
TESTS_DIR = os.path.join(BASE_DIR, 'tests')
LAB_DIR = os.path.join(BASE_DIR, 'lab', 'python')
STYLES_DIR = os.path.join(BASE_DIR, 'frontend', 'styles')

# Garantir que diretórios existam
for directory in [LOGS_DIR, STUDIES_DIR, BACKEND_DIR, FRONTEND_DIR, DB_DIR, TESTS_DIR, LAB_DIR, STYLES_DIR]:
    os.makedirs(directory, exist_ok=True)

def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def update_log():
    log_file = os.path.join(LOGS_DIR, 'activity-log.md')
    activities = [
        "Revisão de conceitos de Clean Architecture",
        "Refatoração de pequenos componentes",
        "Leitura sobre padrões de projeto em C#",
        "Estudo de hooks avançados no React",
        "Otimização de queries SQL",
        "Configuração de pipeline CI/CD",
        "Análise de performance no frontend",
        "Revisão de SOLID principles"
    ]
    activity = random.choice(activities)
    entry = f"\n### {get_timestamp()}\n- {activity}\n"
    
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(entry)
    
    return f"docs: update activity log with '{activity}'"

def update_studies():
    month_str = datetime.datetime.now().strftime("%Y-%m")
    study_file = os.path.join(STUDIES_DIR, f"{month_str}.md")
    
    topics = [
        ("Clean Architecture", "A dependência deve apontar para dentro, em direção às regras de negócio."),
        ("React Performance", "Use useMemo apenas quando o custo de re-renderização for alto."),
        ("C# AspNet Core", "Middlewares são executados em ordem de definição no pipeline."),
        ("SOLID - SRP", "Uma classe deve ter apenas uma razão para mudar."),
        ("Git Flow", "Feature branches facilitam o desenvolvimento paralelo."),
        ("TypeScript Generics", "Generics permitem componentes reutilizáveis e tipados."),
        ("Docker", "Multi-stage builds reduzem drasticamente o tamanho da imagem final.")
    ]
    topic, content = random.choice(topics)
    
    entry = f"\n## {topic}\n- {content}\n"
    
    # Se arquivo não existe, cria cabeçalho
    if not os.path.exists(study_file):
        with open(study_file, 'w', encoding='utf-8') as f:
            f.write(f"# Estudos de {month_str}\n")
            
    with open(study_file, 'a', encoding='utf-8') as f:
        f.write(entry)

    return f"study: add notes on {topic}"

def create_backend_snippet():
    snippets = [
        ("UserService.cs", """public class UserService
{
    public void Register(User user)
    {
        if (user == null) throw new ArgumentNullException(nameof(user));
        // Logic to register user
    }
}"""),
        ("OrderRepository.cs", """public class OrderRepository
{
    public Order GetById(int id)
    {
        // Simulate DB fetch
        return new Order { Id = id, Date = DateTime.Now };
    }
}"""),
        ("EmailValidator.cs", """public static class EmailValidator
{
    public static bool IsValid(string email)
    {
        return email.Contains("@") && email.Contains(".");
    }
}""")
    ]
    filename, content = random.choice(snippets)
    file_path = os.path.join(BACKEND_DIR, filename)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    return f"feat(backend): add/update {filename} snippet"

def create_frontend_snippet():
    snippets = [
        ("Button.tsx", """import React from 'react';

interface ButtonProps {
    label: string;
    onClick: () => void;
}

export const Button: React.FC<ButtonProps> = ({ label, onClick }) => {
    return <button onClick={onClick} className="btn-primary">{label}</button>;
};"""),
        ("Card.tsx", """import React from 'react';

export const Card = ({ children }: { children: React.ReactNode }) => {
    return <div className="card shadow-md p-4">{children}</div>;
};"""),
        ("Input.tsx", """import React from 'react';

export const Input = (props: React.InputHTMLAttributes<HTMLInputElement>) => {
    return <input className="border rounded p-2" {...props} />;
};""")
    ]
    filename, content = random.choice(snippets)
    file_path = os.path.join(FRONTEND_DIR, filename)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return f"feat(frontend): add/update {filename} component"

def create_sql_snippet():
    snippets = [
        ("users_table.sql", "CREATE TABLE Users (\n    Id INT PRIMARY KEY IDENTITY,\n    Username VARCHAR(50) NOT NULL,\n    Email VARCHAR(100) UNIQUE,\n    CreatedAt DATETIME DEFAULT GETDATE()\n);"),
        ("orders_query.sql", "SELECT o.Id, u.Username, o.Total \nFROM Orders o \nJOIN Users u ON o.UserId = u.Id \nWHERE o.Total > 100 \nORDER BY o.CreatedAt DESC;"),
        ("indexes.sql", "CREATE INDEX IDX_Users_Email ON Users(Email);\n-- Melhora performance de busca por email"),
        ("procedures.sql", "CREATE PROCEDURE GetUserOrders (@UserId INT)\nAS\nBEGIN\n    SELECT * FROM Orders WHERE UserId = @UserId;\nEND;")
    ]
    filename, content = random.choice(snippets)
    file_path = os.path.join(DB_DIR, filename)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"db: add/update SQL query {filename}"

def create_test_snippet():
    snippets = [
        ("UserServiceTests.cs", "public class UserServiceTests {\n    [Fact]\n    public void Should_Register_User() {\n        // Arrange & Act & Assert\n    }\n}"),
        ("Button.test.tsx", "import { render, screen } from '@testing-library/react';\nimport { Button } from './Button';\n\ntest('renders button label', () => {\n  render(<Button label=\"Click me\" />);\n  expect(screen.getByText('Click me')).toBeInTheDocument();\n});"),
        ("MathUtilsTests.py", "import unittest\n\nclass TestMath(unittest.TestCase):\n    def test_sum(self):\n        self.assertEqual(1 + 1, 2)")
    ]
    filename, content = random.choice(snippets)
    file_path = os.path.join(TESTS_DIR, filename)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"test: add unit test {filename}"

def create_python_script():
    snippets = [
        ("data_processor.py", "import pandas as pd\n\ndef process_csv(file):\n    df = pd.read_csv(file)\n    print(df.describe())"),
        ("image_resizer.py", "from PIL import Image\n\ndef resize(path, size):\n    img = Image.open(path)\n    img.resize(size).save('resized.png')"),
        ("scraper.py", "import requests\nfrom bs4 import BeautifulSoup\n\ndef get_title(url):\n    res = requests.get(url)\n    soup = BeautifulSoup(res.text, 'html.parser')\n    return soup.title.string")
    ]
    filename, content = random.choice(snippets)
    file_path = os.path.join(LAB_DIR, filename)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"chore(lab): add python utility {filename}"

def create_css_snippet():
    snippets = [
        ("grid.css", ".grid-container {\n    display: grid;\n    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));\n    gap: 1rem;\n}"),
        ("animations.css", "@keyframes slideIn {\n    from { transform: translateX(-100%); }\n    to { transform: translateX(0); }\n}"),
        ("theme.css", ":root {\n    --primary-color: #007bff;\n    --secondary-color: #6c757d;\n    --spacing-md: 16px;\n}")
    ]
    filename, content = random.choice(snippets)
    file_path = os.path.join(STYLES_DIR, filename)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"style: add css snippet {filename}"

def main():
    # Probabilidades ajustadas:
    # 40% Log
    # 20% Estudo
    # 10% Backend
    # 10% Frontend
    # 5% DB
    # 5% Tests
    # 5% Python Lab
    # 5% CSS
    rand = random.random()
    
    commit_msg = ""
    if rand < 0.40:
        commit_msg = update_log()
    elif rand < 0.60:
        commit_msg = update_studies()
    elif rand < 0.70:
        commit_msg = create_backend_snippet()
    elif rand < 0.80:
        commit_msg = create_frontend_snippet()
    elif rand < 0.85:
        commit_msg = create_sql_snippet()
    elif rand < 0.90:
        commit_msg = create_test_snippet()
    elif rand < 0.95:
        commit_msg = create_python_script()
    else:
        commit_msg = create_css_snippet()
        
    # Salvar mensagem de commit para ser usada pelo Action (opcional, ou printar)
    # Vamos criar um arquivo auxiliar para a mensagem
    with open(os.path.join(os.path.dirname(__file__), 'last_commit_msg.txt'), 'w', encoding='utf-8') as f:
        f.write(commit_msg)
    
    print(f"Action executed: {commit_msg}")

if __name__ == "__main__":
    main()
