# banpay
El proyecto consiste en desarrollar un bot que se apalanque de LLMs para simular el comportamiento de un agente comercial.

Este bot tiene las siguientes capacidades:
- API en Python
- Responder información básica sobre la propuesta de valor
- Reducir las alucinaciones dentro del chatbot
- Tolerancia a errores en la redacción y ortografia
- Brindar recomendaciones


## Requisitos
- Python 3.11+
- Docker
- MongoDB

### Acerca del proyecto
aqui desglosare cosas


### Clonar el repositorio
```bash
git clone https://github.com/GerardoX1/banpay
cd banpay

```

## Dockerización
Con Docker configurado en tu PC, lo único que tienes que hacer es ejecutar el comando:
```bash
docker-compose up
```

## Servicios en Docker
- Aplicación Web: Disponible en [http://localhost:8080](http://localhost:8080)
- Base de Datos MongoDB [http://localhost:27017](http://localhost:27017)

## Configuración de desarrollo
Es importante primero ejecutar la dockerizacion para tener las bases de datos arrancando antes de comenzar a realizar la carga de informacion.
tambien es recomendable validar el estado de estos contenedores cuando se hacen pruebas locales.


### Crear y activar un entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate # En Windows usa venv\Scripts\activate
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Ejecutar el servidor de desarrollo
```bash
python main.py
```

### Ejecutar pruebas unitarias
```bash
pytest
```

## Información Personal
### Sobre Mí
Soy esclavo moderno de dos gatos asi que necesito más dinerito 🐈‍⬛🐈💵

### Contacto
- **Nombre**: Luis Gerardo Fosado Baños
- **Email**: [yeralway1@gmail.com](mailto:yeralway1@gmail.com)
- **LinkedIn**: [www.linkedin.com/in/gerardo-fosado-0ab957165](https://www.linkedin.com/in/gerardo-fosado-0ab957165)
- **GitHub**: [https://github.com/GerardoX1](https://github.com/GerardoX1)

bueno es todo gracias!!
