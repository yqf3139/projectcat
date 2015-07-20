import signal, sys, ssl
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer, SimpleSSLWebSocketServer
from optparse import OptionParser

class SimpleEcho(WebSocket):

   def handleMessage(self):
      print(self.data)

   def handleConnected(self):
      print('handleConnected')

   def handleClose(self):
      print('handleClose')

if __name__ == "__main__":

   cls = SimpleEcho

   server = SimpleWebSocketServer('127.0.0.1', 8888, cls)

   def close_sig_handler(signal, frame):
      server.close()
      sys.exit()

   signal.signal(signal.SIGINT, close_sig_handler)

   server.serveforever()
