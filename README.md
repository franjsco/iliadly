# iliadly
>  Consulta i contatori della tua offerta iliad direttamente dal terminale..

Per utilizzarlo è necessario essere connessi con rete iliad.



<a href="https://asciinema.org/a/pvb8xqDtOczwuZjahN08wosWY" target="_blank"><img src="https://asciinema.org/a/pvb8xqDtOczwuZjahN08wosWY.svg"/></a>


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
