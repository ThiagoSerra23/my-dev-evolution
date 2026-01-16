import os
import random
import datetime

# Configurações de diretórios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
STUDIES_DIR = os.path.join(BASE_DIR, 'studies')
BACKEND_DIR = os.path.join(BASE_DIR, 'backend', 'snippets')
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend', 'components')

# Garantir que diretórios existam
for directory in [LOGS_DIR, STUDIES_DIR, BACKEND_DIR, FRONTEND_DIR]:
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

def main():
    # 50% chance de log, 30% estudo, 10% backend, 10% frontend
    rand = random.random()
    
    commit_msg = ""
    if rand < 0.5:
        commit_msg = update_log()
    elif rand < 0.8:
        commit_msg = update_studies()
    elif rand < 0.9:
        commit_msg = create_backend_snippet()
    else:
        commit_msg = create_frontend_snippet()
        
    # Salvar mensagem de commit para ser usada pelo Action (opcional, ou printar)
    # Vamos criar um arquivo auxiliar para a mensagem
    with open(os.path.join(os.path.dirname(__file__), 'last_commit_msg.txt'), 'w', encoding='utf-8') as f:
        f.write(commit_msg)
    
    print(f"Action executed: {commit_msg}")

if __name__ == "__main__":
    main()
