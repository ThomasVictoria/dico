import sqlite3

class Data(object):

	def __init__(self, word, letter, definition):
		self.word = word
		self.definition = definition
		self.letter = letter
		self.init_tables()
		self.save_word()
		
	def init_tables(self):
		self.open_connection()
		self.c.execute("CREATE TABLE if not exists words (id integer PRIMARY KEY, word text)")
		self.c.execute("CREATE TABLE if not exists definitions (id integer PRIMARY KEY, word_id integer NOT NULL, definition text)")
		self.conn.commit()
		self.conn.close()

	def open_connection(self):
		self.conn = sqlite3.connect('data.db')
		self.c = self.conn.cursor()

	def save_word(self):
		self.open_connection()
		self.c.execute("INSERT INTO words(word) VALUES ('"+self.word+"')")
		self.conn.commit()
		save = self.c.execute("SELECT id FROM words WHERE id = (SELECT MAX(id)  FROM words)")
		self.save_def(save.fetchone()[0])
		self.conn.close()

	def save_def(self, index):
		self.open_connection()
		index = str(index)
		for item in self.definition:
			yolo = item.text_content().encode('utf-8')
			print(yolo)
			# self.c.execute("INSERT INTO definitions(word_id,definition) VALUES ('"+index+"','"+str(yolo)+"')")
		self.conn.commit()
		self.conn.close()
