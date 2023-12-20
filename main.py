from fastapi import FastAPI
from models import Note

'''
    FastAPI has a fantastic feature that automatically generates Swagger/OpenAPI documentation for your API.
'''

# Use an in-memory database to store notes
app = FastAPI()
notes_db = []

# Include API routes for CRUD operations
@app.get("/notes/")
async def get_notes():
    return notes_db

@app.post("/notes/")
async def create_note(note: Note):
    notes_db.append(note)
    return {"message": "Note created successfully"}

@app.put("/notes/{note_id}")
async def update_note(note_id: int, note: Note):
    notes_db[note_id] = note
    return {"message": f"Note {note_id} updated successfully"}

@app.delete("/notes/{note_id}")
async def delete_note(note_id: int):
    notes_db.pop(note_id)
    return {"message": f"Note {note_id} deleted successfully"}
