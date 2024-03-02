import os
from pyngrok import ngrok
from threading import Thread

class Streamlit:
  def __init__(self,
               auth_token = '',
               app_path = 'app.py',
               port = 8000):
    self.auth_token = auth_token
    self.app_path = app_path
    self.port = port

  def deploy(self):
      ngrok.set_auth_token(self.auth_token)
      def run_streamlit():
        os.system('streamlit run ' + self.app_path + ' --server.port ' + str(self.port))
      thread = Thread(target=run_streamlit)
      thread.start()
      public_url = ngrok.connect(addr=str(self.port), proto='http', bind_tls=True)
      return public_url

  def undeploy(self):
      ngrok.kill()
