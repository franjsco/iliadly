<h1 align="center">iliadly 📱</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/franjsco/iliadly/graphs/commit-activity" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
  <a href="https://github.com/franjsco/iliadly/blob/master/LICENSE" target="_blank">
    <img alt="License: GPL--3.0--or--later" src="https://img.shields.io/github/license/franjsco/tomadoro" />
  </a>
  <a href="https://twitter.com/franjsco" target="_blank">
    <img alt="Twitter: franjsco" src="https://img.shields.io/twitter/follow/franjsco.svg?style=social" />
  </a>
</p>


>  Consulta i contatori della tua offerta iliad direttamente dal terminale.



Per utilizzarlo è necessario essere connessi con rete iliad.

<a href="https://asciinema.org/a/J0b6ypguvXvDl51QqkIxLQnw6" target="_blank"><img src="https://asciinema.org/a/J0b6ypguvXvDl51QqkIxLQnw6.svg" /></a>


## Installazione

1. Clonare il repository:
    ```sh
    git clone https://github.com/franjsco/iliadly ~/.iliadly

    cd ~/.iliadly
    ```

2. Installare le dipendenze
    ```sh
    pip install -r requirements.txt
    ```

3. Concedere i permessi di esecuzione allo script
    ```sh
    chmod +x iliadly.py
    ```

4. Creare collegamento simbolico in /usr/local/bin:
    ```sh
    cd /usr/local/bin
    sudo ln -s ~/.iliadly/iliadly.py iliadly
    ```


## Utilizzo

Per mostrare i contatori, aprire il terminale e lanciare il comando:
```sh
iliadly
```
