### Tiny Reflections
 A reflection & journaling app using tinyllama. Takes your journalling and asks you thoughtful questions about it!
 
### Things you will need for this app

    - WSL2 or Ubuntu (currently Windows and macOS are not supported)
    - Python 3
    - Ollama
    - A local large language model that works with Ollama. This repository uses tinyllama, but you can change this in `app.py`.

### How to install this app

   1. Go to your terminal.
   2. Clone this repository using `git clone https://github.com/astrosnat/tinyreflections.git`.
   3. Change the working directory with the command `cd ~/tinyreflections`.
   4. Run `python3 -m venv venv`.
   5. Run `source venv/bin/activate`.
   6. Use `pip install -r requirements.txt`.
   7. In a new terminal window, run `ollama serve` to start ollama.
   8. In your original terminal window, run `streamlit run app.py`.
   9. Open your Streamlit app in your browser of choice.
   10. Have fun!

### Ethical concerns

This app uses a local large language model. It runs on your machine and does not talk to the internet, thus using a minimal amount of energy. To the best of my knowledge, tinyllama has no "memory" and will not remember anything you write.

Although this app cannot record or store what you write it is possible that the large language model may output something harmful or upsetting. I am trying my best to make it not do this, but as it is an alpha **use at your own risk**.

I copied some of the architecture and code from friendlydebateapp.

### Contributing

I welcome contributions. This project is MIT Licensed so do what you want with it :) Just make sure to write a nice and comprehensive description in your pull request.
