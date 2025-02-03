# banpay
Este challenge es una oportunidad para que muestres tu código
más limpio, que demuestres cómo solucionas problemas.
• Escribe el código como si fuera a producción
• No importa el stack tech que emplees, con qué herramienta o
lenguaje la soluciones
• Asegúrate de dejar instrucciones claras de cómo ejecutar tu
código como si fuera a desplegarse en producción

Challenge
Desarrollar un API REST de usuarios, considerando al menos los
siguientes servicios:
• Creación de usuario
• Obtención de todos los usuarios
• Obtención de un usuario específico
• Actualización de un usuario
• Borrado de usuario(s)
Los usuarios deben tener un rol (admin, films, people, locations,
species, vehicles) y poder consumir un GET de Studio Ghibli API, de
acuerdo a su rol
Necesitamos que la solución al reto la entregues en un repositorio
público de GitHub, Bitbucket o GitLab.
Lo que revisaremos en este reto es:
• Arquitectura
• Claridad
• Calidad del código
• Seguridad
• Decisiones técnicas
• Escalabilidad
• Distribución

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
