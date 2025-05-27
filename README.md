** aws_credentials_robot


<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Selenium-4.x-green?style=for-the-badge&logo=selenium" alt="Selenium Version">
  <img src="https://img.shields.io/badge/AWS-Credentials-orange?style=for-the-badge&logo=amazon-aws" alt="AWS Credentials">
  <img src="https://img.shields.io/badge/LocalStack-4.x.x-purple?style=for-the-badge&logo=localstack" alt="LocalStack Version">
</p>

# 🚀 AWS Dev Credential & SQS LocalSync 🚀

Un proyecto robusto en Python que automatiza la actualización de **credenciales de AWS** y la **sincronización de colas SQS** desde un entorno de desarrollo remoto hacia tu instancia local de **LocalStack**. Simplifica el desarrollo local y las pruebas al replicar la configuración de SQS de tu entorno de desarrollo.

---

## 🌟 Tabla de Contenidos

* [✨ Características Principales](#-características-principales)
* [🛠️ Requisitos](#%EF%B8%8F-requisitos)
* [⚙️ Configuración](#%EF%B8%8F-configuración)
    * [Configuración de Entorno](#configuración-de-entorno)
    * [Navegador y WebDriver](#navegador-y-webdriver)
* [🚀 Uso](#-uso)
* [🤝 Contribución](#-contribución)
* [📜 Licencia](#-licencia)

---

## ✨ Características Principales

* **🔄 Refresco Automatizado de Credenciales:** Utiliza **Selenium** para navegar por la consola de AWS y obtener las credenciales temporales de desarrollo (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`).
* **🌐 Sincronización de Colas SQS:** Importa dinámicamente las colas SQS de tu entorno de desarrollo AWS y las recrea en tu instancia local de **LocalStack**.
* **🔒 Seguridad Robusta:** Maneja las credenciales de forma segura, evitando su exposición en el código.
* **🧪 Entorno de Desarrollo Simplificado:** Facilita las pruebas y el desarrollo local al proporcionar un entorno SQS que refleja el de tu entorno de desarrollo.
* **🐍 Python y Selenium:** Construido con Python para la lógica de negocio y Selenium para la interacción con la interfaz web de AWS.

---

## 🛠️ Requisitos

Antes de ejecutar este proyecto, asegúrate de tener los siguientes componentes instalados:

* **Python 3.9+**
* **pip** (el gestor de paquetes de Python)
* **LocalStack** (versión 0.14.x o superior recomendada, con Docker ejecutándose)
* **Google Chrome** (o el navegador de tu elección compatible con Selenium)
* **WebDriver** para tu navegador (por ejemplo, ChromeDriver)

Puedes verificar la instalación de LocalStack ejecutando:
**# aws_credentials_robot


<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Selenium-4.x-green?style=for-the-badge&logo=selenium" alt="Selenium Version">
  <img src="https://img.shields.io/badge/AWS-Credentials-orange?style=for-the-badge&logo=amazon-aws" alt="AWS Credentials">
  <img src="https://img.shields.io/badge/LocalStack-4.x.x-purple?style=for-the-badge&logo=localstack" alt="LocalStack Version">
</p>

# 🚀 Python && AWS Dev Credential  🚀

Un proyecto robusto en Python que automatiza la actualización de **credenciales de AWS** y la **sincronización de colas SQS** desde un entorno de desarrollo remoto hacia tu instancia local de **LocalStack**. Simplifica el desarrollo local y las pruebas al replicar la configuración de SQS de tu entorno de desarrollo.


## 🌟 INDICE

* [✨ Características Principales](#-características-principales)
* [🛠️ Requisitos](#%EF%B8%8F-requisitos)
* [🤝 Contribución](#-contribución)


## ✨ Características Principales

* **🔄 Refresco Automatizado de Credenciales:** Utiliza **Selenium** para navegar por la consola de AWS y obtener las credenciales temporales de desarrollo (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`).
* **🌐 Sincronización de Colas SQS:** Importa dinámicamente las colas SQS de tu entorno de desarrollo AWS y las recrea en tu instancia local de **LocalStack**.
* **🔒 Seguridad Robusta:** Maneja las credenciales de forma segura, evitando su exposición en el código utilizando variables de entorno.
* **🧪 Entorno de Desarrollo Simplificado:** Facilita las pruebas y el desarrollo local al proporcionar un entorno SQS que refleja el de tu entorno de desarrollo.
* **🐍 Python y Selenium:** Construido con Python para la lógica de negocio y Selenium para la interacción con la interfaz web de AWS.

## 🛠️ Requisitos

Antes de ejecutar este proyecto, asegúrate de tener los siguientes componentes instalados:

* **Python 3.9+**
* **pip** (el gestor de paquetes de Python)
* **LocalStack** (versión 0.14.x o superior recomendada, con Docker ejecutándose)
* **Google Chrome** (o el navegador de tu elección compatible con Selenium)
* **WebDriver** para tu navegador (por ejemplo, ChromeDriver)

## 🤝 Contribución

Para mas información mirar el **README** dentro del proyecto.



Hecho con ❤️ por [Jesús Suárez López](#-https://github.com/jsuarez1994)
