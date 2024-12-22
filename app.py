from fastapi import FastAPI

app = FastAPI(title="Translate-re API", description="API to translate words between different languages", version="1.0.0", docs_url=None, redoc_url=None)

translations = {
    "br": {
        "fr": {
            "ola": "Salut",
            "bom dia": "Bonjour",
            "boa tarde": "Bon après-midi",
            "boa noite": "Bonne nuit",
            "tchau": "Au revoir",
            "cafe": "Café"
        },
        "en": {
            "ola": "Hello",
            "bom dia": "Good morning",
            "boa tarde": "Good afternoon",
            "boa noite": "Good night",
            "tchau": "Bye",
            "cafe": "Coffee"
        },
        "es": {
            "ola": "Hola",
            "bom dia": "Buenos días",
            "boa tarde": "Buenas tardes",
            "boa noite": "Buenas noches",
            "tchau": "Adiós",
            "cafe": "Café"
        },
        "it": {
            "ola": "Ciao",
            "bom dia": "Buongiorno",
            "boa tarde": "Buon pomeriggio",
            "boa noite": "Buona notte",
            "tchau": "Addio",
        },
        "viatinamita": {
            "ola": "Xin chào",
            "bom dia": "Chào buổi sáng",
            "boa tarde": "Chào buổi chiều",
            "boa noite": "Chúc ngủ ngon",
            "tchau": "Tạm biệt"
        }
    },
    "en": {
        "br": {
            "hello": "Ola",
            "good morning": "Bom dia",
            "good afternoon": "Boa tarde",
            "good night": "Boa noite",
            "bye": "Tchau"
        },
        "fr": {
            "hello": "Salut",
            "good morning": "Bonjour",
            "good afternoon": "Bon après-midi",
            "good night": "Bonne nuit",
            "bye": "Au revoir"
        },
        "es": {
            "hello": "Hola",
            "good morning": "Buenos días",
            "good afternoon": "Buenas tardes",
            "good night": "Buenas noches",
            "bye": "Adiós"
        },
        "it": {
            "hello": "Ciao",
            "good morning": "Buongiorno",
            "good afternoon": "Buon pomeriggio",
            "good night": "Buona notte",
            "bye": "Addio"
        },
        "viatinamita": {
            "hello": "Xin chào",
            "good morning": "Chào buổi sáng",
            "good afternoon": "Chào buổi chiều",
            "good night": "Chúc ngủ ngon",
            "bye": "Tạm biệt"
        }
    },
    "fr": {
        "br": {
            "salut": "Ola",
            "bonjour": "Bom dia",
            "bon après-midi": "Boa tarde",
            "bonne nuit": "Boa noite",
            "au revoir": "Tchau"
        },
        "en": {
            "salut": "Hello",
            "bonjour": "Good morning",
            "bon après-midi": "Good afternoon",
            "bonne nuit": "Good night",
            "au revoir": "Bye"
        },
        "es": {
            "salut": "Hola",
            "bonjour": "Buenos días",
            "bon après-midi": "Buenas tardes",
            "bonne nuit": "Buenas noches",
            "au revoir": "Adiós"
        },
        "it": {
            "salut": "Ciao",
            "bonjour": "Buongiorno",
            "bon après-midi": "Buon pomeriggio",
            "bonne nuit": "Buona notte",
            "au revoir": "Addio"
        },
        "viatinamita": {
            "salut": "Xin chào",
            "bonjour": "Chào buổi sáng",
            "bon après-midi": "Chào buổi chiều",
            "bonne nuit": "Chúc ngủ ngon",
            "au revoir": "Tạm biệt"
        }
    },
    "es": {
        "br": {
            "hola": "Ola",
            "buenos días": "Bom dia",
            "buenas tardes": "Boa tarde",
            "buenas noches": "Boa noite",
            "adiós": "Tchau"
        },
        "en": {
            "hola": "Hello",
            "buenos días": "Good morning",
            "buenas tardes": "Good afternoon",
            "buenas noches": "Good night",
            "adiós": "Bye"
        },
        "fr": {
            "hola": "Salut",
            "buenos días": "Bonjour",
            "buenas tardes": "Bon après-midi",
            "buenas noches": "Bonne nuit",
            "adiós": "Au revoir"
        },
        "it": {
            "hola": "Ciao",
            "buenos días": "Buongiorno",
            "buenas tardes": "Buon pomeriggio",
            "buenas noches": "Buona notte",
            "adiós": "Addio"
        },
        "viatinamita": {
            "hola": "Xin chào",
            "buenos días": "Chào buổi sáng",
            "buenas tardes": "Chào buổi chiều",
            "buenas noches": "Chúc ngủ ngon",
            "adiós": "Tạm biệt"
        }
    },
    "it": {
        "br": {
            "ciao": "Ola",
            "buongiorno": "Bom dia",
            "buon pomeriggio": "Boa tarde",
            "buona notte": "Boa noite",
            "addio": "Tchau"
        },
        "en": {
            "ciao": "Hello",
            "buongiorno": "Good morning",
            "buon pomeriggio": "Good afternoon",
            "buona notte": "Good night",
            "addio": "Bye"
        },
        "fr": {
            "ciao": "Salut",
            "buongiorno": "Bonjour",
            "buon pomeriggio": "Bon après-midi",
            "buona notte": "Bonne nuit",
            "addio": "Au revoir"
        },
        "es": {
            "ciao": "Hola",
            "buongiorno": "Buenos días",
            "buon pomeriggio": "Buenas tardes",
            "buona notte": "Buenas noches",
            "addio": "Adiós"
        },
        "viatinamita": {
            "ciao": "Xin chào",
            "buongiorno": "Chào buổi sáng",
            "buon pomeriggio": "Chào buổi chiều",
            "buona notte": "Chúc ngủ ngon",
            "addio": "Tạm biệt"
        }
    },
    "viatinamita": {
        "br": {
            "xin chào": "Ola",
            "chào buổi sáng": "Bom dia",
            "chào buổi chiều": "Boa tarde",
            "chúc ngủ ngon": "Boa noite",
            "tạm biệt": "Tchau"
        },
        "en": {
            "xin chào": "Hello",
            "chào buổi sáng": "Good morning",
            "chào buổi chiều": "Good afternoon",
            "chúc ngủ ngon": "Good night",
            "tạm biệt": "Bye"
        },
        "fr": {
            "xin chào": "Salut",
            "chào buổi sáng": "Bonjour",
            "chào buổi chiều": "Bon après-midi",
            "chúc ngủ ngon": "Bonne nuit",
            "tạm biệt": "Au revoir"
        },
        "es": {
            "xin chào": "Hola",
            "chào buổi sáng": "Buenos días",
            "chào buổi chiều": "Buenas tardes",
            "chúc ngủ ngon": "Buenas noches",
            "tạm biệt": "Adiós"
        },
        "it": {
            "xin chào": "Ciao",
            "chào buổi sáng": "Buongiorno",
            "chào buổi chiều": "Buon pomeriggio",
            "chúc ngủ ngon": "Buona notte",
            "tạm biệt": "Addio"
        }
    }
}

@app.get("/")
def home():
    try:
        return {"message": "API is running",
            "status": "success",
            "API": "Traslate"
            }
    except Exception as e:
        return {"Message": "An error occurred"}

@app.get("/database")
def database():
    return translations

@app.get("/translate/{idioma}/{idioma_traduzir}/{palavra}")
def translate(idioma: str, idioma_traduzir: str, palavra: str):
    try:
        return {"Traduction": translations[idioma][idioma_traduzir][palavra]}
    except Exception as e:
        return {"message": "Word not found in the database"}
