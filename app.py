from src import app

import src.application.route.endpoint

import os
import logging

def main():
    init_logging()

    try:
        app_port = os.getenv('APP_PORT', default=3000)

        logging.info("Aplicativo jira rodando na porta: '{}'".format(app_port))
        
        app.run(debug=True, host='0.0.0.0', port=int(app_port))
    except Exception as ex:
        logging.error('Ocorreu um erro ao tentar iniciar o apliactivo: {}'.format(ex))

def init_logging():
    logging.basicConfig(level=os.getenv('LOG_LEVEL', default='INFO'), filemode='jira-app.log',
                        format="(%(asctime)s - %(levelname)s - %(message)s)")

    
if __name__ == '__main__':
    main()