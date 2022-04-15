# CI/CD con GitHub Actions y Azure Web Apps

---

## About Me

> Juan Pablo Yamamoto Zazueta
>
> Computer Science & Maths @ Ciencias, UNAM
>
> GitHub Campus Expert

Note: speaker notes FTW!

---

## ¿CI / CD?

---

- Optimizar tiempo de desarrollo
- Automatizar otras tareas
- Grandes equipos de desarrollo

Note: Cuando trabajamos en equipos con metodologías ágiles, queremos enfocarnos en generar nuevos componentes de software y minimizar al máximo (mediante la automatización) aquellos procesos que se enfocan en el lanzamiento del producto, pero que no representan tareas creativas: compilación, ejecutar pruebas unitarias, migraciones a la bdd, desplegar en un servidor, etc.

---

### CI

> Continuous Integration

---

Procesos para incorporar nuevos componentes a un producto final.

- Compilación.
- Ejecución de pruebas unitarias.
- Control de versiones.

---

- Detectar lo antes posible fallos en el desarrollo.
- Verificar la correcta funcionalidad antes de incorporar los cambios.
- Ser transparentes al resto del equipo con respecto al estado del sistema.

---

### CD

> Continuous Delivery

---

Procesos para publicar de manera constante nuevas versiones de un producto, en incrementos pequeños.

- Desplegar en un servidor.
- Migraciones a la base de datos.

---

- Avanzar de manera constante.
- Presentar cambios al cliente.

---

En mi computadora sí funciona...

---

![Docker](http://blogs.encamina.com/por-una-nube-sostenible/wp-content/uploads/sites/19/2015/11/docker-logo.png) <!-- .element height="50%" width="50%" -->

---

## Docker

Contenedores

Entornos consistentes y replicables.

Note: Si corre en una configuración de Docker, corre en cualquier otra máquina replicando la configuración de Docker.

---

### ¿Máquinas virtuales?

No.

---

<pre><code data-line-numbers="1|3-4|6|8|10|12">FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
</code></pre>

Note: Dockerfile. Lenguaje declarativo para describir entornos de contenedores.

---

Necesitamos:

- Una plataforma colaborativa.
- Un entorno que nos permita ejecutar código (preferentemente en Docker).
- Con capacidades para programar *pipelines* personalizados.

---

## GitHub Actions

![GitHub Actions](https://miro.medium.com/max/400/1*txwKGJOoQ2W0ka_9htbu0Q.png) <!-- .element height="20%" width="20%" -->

---

> GitHub Actions facilita la automatización de tus procesos de software, ... Construye, prueba y despliega tu código directamente desde GitHub.

Note: GH Actions corre sobre Docker. GH Actions proveé un *marketplace* para acceder a procesos pre-configurados. GitHub Actions no es un servicio de backend. Tenemos límites sobre el tiempo y recursos a los que podemos acceder. Necesitamos un ambiente en donde podamos desplegar nuestro proyecto.

---

## Azure Web Apps

![Azure Web Apps](https://ms-azuretools.gallerycdn.vsassets.io/extensions/ms-azuretools/vscode-azureappservice/0.23.1/1645759494097/Microsoft.VisualStudio.Services.Icons.Default) <!-- .element height="20%" width="20%" -->

---

> Cree e implemente aplicaciones web críticas que se escalen a la par que su negocio.

Note: AWA nos proveé un entorno para desplegar nuestras aplicaciones, de una manera escalable y segura. Lo mejor, funciona con Docker.

---

<!-- .slide: data-background="https://inplasoft.com/wp-content/uploads/github-azure.png" -->

---

### Demo Time
