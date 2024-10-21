from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud_service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/persons/', response_model=List[schemas.Persons])
def get_all_persons(db: Session = Depends(get_db)):
    return crud_service.get_all_persons(db)

@router.get('/persons/rollnumber', response_model=schemas.Persons)
def get_persons_by_rollnumber(rollnumber: int, first_name: str, db: Session = Depends(get_db)):
    return crud_service.get_persons_by_rollnumber(db, rollnumber, first_name)

@router.post('/persons/', response_model=schemas.Persons)
def create_persons(rollnumber: str, fullname: str, age: str, profession: str, db: Session = Depends(get_db)):
    return crud_service.create_persons(db, rollnumber, fullname, age, profession)

@router.put('/persons/rollnumber/', response_model=schemas.Persons)
def update_persons_by_rollnumber(rollnumber: str, fullname: str, age: str, profession: str, db: Session = Depends(get_db)):
    return crud_service.update_persons_by_rollnumber(db, rollnumber, fullname, age, profession)

@router.delete('/persons/rollnumber', response_model=schemas.Persons)
def delete_persons_by_rollnumber(rollnumber: int, db: Session = Depends(get_db)):
    return crud_service.delete_persons_by_rollnumber(db, rollnumber)

@router.get('/addresses/', response_model=List[schemas.Addresses])
def get_all_addresses(db: Session = Depends(get_db)):
    return crud_service.get_all_addresses(db)

@router.get('/addresses/id', response_model=schemas.Addresses)
def get_addresses_by_id(id: int, db: Session = Depends(get_db)):
    return crud_service.get_addresses_by_id(db, id)

@router.post('/addresses/', response_model=schemas.Addresses)
def create_addresses(id: str, street: str, city: str, state: str, country: str, postal_code: str, created_at: str, updated_at: str, db: Session = Depends(get_db)):
    return crud_service.create_addresses(db, id, street, city, state, country, postal_code, created_at, updated_at)

@router.put('/addresses/id/', response_model=schemas.Addresses)
def update_addresses_by_id(id: str, street: str, city: str, state: str, country: str, postal_code: str, created_at: str, updated_at: str, db: Session = Depends(get_db)):
    return crud_service.update_addresses_by_id(db, id, street, city, state, country, postal_code, created_at, updated_at)

@router.delete('/addresses/id', response_model=schemas.Addresses)
def delete_addresses_by_id(id: int, db: Session = Depends(get_db)):
    return crud_service.delete_addresses_by_id(db, id)

