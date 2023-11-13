import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

database = client["main"]

accounts = database["accounts"]

books = database["books"]

authors = database["authors"]

def db_format(string):
	return string.lower().replace(" ","")

def db_add_book(title, author, genres, edges):
	#search for book

	#if found display error

	#else add book
	book_id = title + "_" + author
	t_dict = { "_id": book_id, 
	"title": title, 
	"author": author,
	"genres": genres,
	"edges": edges}
	books.insert_one(t_dict)

def db_add_edge(book1, book2):
	query1 = { "_id": book1 }
	book1_dict = books.find(query1)
	for b in book1_dict:
		print(b)
	return False
