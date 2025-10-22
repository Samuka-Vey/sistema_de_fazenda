# Universidade Estadual do Piauí – UESPI  
**Curso:** Tecnologia em Sistemas de Computação  
**Disciplina:** Algoritmos e Programação Estruturada  
**Professor:** Eyder Rios  
## Integrantes do projeto
| Nome Completo | Matrícula |
|----------------|------------|
| Marcos Samuel Cornelio Barros | 2025027554 |
| João Pedro Aguiar Teixeira | 2025012506 |
| David de Carvalho Santos | 2025012373 |
| Bruno Vinicius dos Reis Souz | 2025034595 |

---

## Arquitetura do Projeto


```bash
farm/
│
├── src/
│   ├── main.py                
│   ├── files.py              
│   ├── reports.py            
│   │
│   ├── animals/
│   │   ├── animals.py        
│   │   └── manage_animals.py  
│   │
│   ├── plants/
│   │   ├── plants.py          
│   │   └── manage_plants.py   
│   │
│   ├── inputs/
│   │   ├── inputs.py          
│   │   └── manage_inputs.py   
│   │
│   ├── movements/
│   │   ├── movements.py       
│   │   └── manage_movements.py
│   │
│   └── utils/                 
│
├── data/
│   ├── animals.json
│   ├── plants.json
│   ├── inputs.json
│   └── movements.json
│
└── README.md