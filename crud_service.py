from sqlalchemy.orm import Session
from typing import List

import models, schemas

def get_all_persons(db: Session):
       return db.query(models.Persons).all()

# auto generated route, get a record
def get_persons_by_rollnumber(db: Session, rollnumber: int):
      return db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()

def create_persons(db: Session, rollnumber: str, fullname: str, age: str, profession: str):
      record_to_be_added = {'rollnumber': rollnumber, 'fullname': fullname, 'age': age, 'profession': profession}
      new_persons = models.Persons(**record_to_be_added)
      db.add(new_persons)
      db.commit()
      return new_persons

def update_persons_by_rollnumber(db: Session, rollnumber: str, fullname: str, age: str, profession: str):
      record_to_update = db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()
      for key, value in {'rollnumber': rollnumber, 'fullname': fullname, 'age': age, 'profession': profession}.items():
          setattr(record_to_update, key, value)
      db.commit()
      db.refresh(record_to_update)
      return record_to_update


def delete_persons_by_rollnumber(db: Session, rollnumber: int):
      record_to_delete = db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()

      if record_to_delete:
          db.delete(record_to_delete)
          db.commit()

      return record_to_delete

def get_all_addresses(db: Session):
       return db.query(models.Addresses).all()

# auto generated route, get a record
def get_addresses_by_id(db: Session, id: int):
      return db.query(models.Addresses).filter(models.Addresses.id == id).first()

def create_addresses(db: Session, id: str, street: str, city: str, state: str, country: str, postal_code: str, created_at: str, updated_at: str):
      record_to_be_added = {'id': id, 'street': street, 'city': city, 'state': state, 'country': country, 'postal_code': postal_code, 'created_at': created_at, 'updated_at': updated_at}
      new_addresses = models.Addresses(**record_to_be_added)
      db.add(new_addresses)
      db.commit()
      return new_addresses

def update_addresses_by_id(db: Session, id: str, street: str, city: str, state: str, country: str, postal_code: str, created_at: str, updated_at: str):
      record_to_update = db.query(models.Addresses).filter(models.Addresses.id == id).first()
      for key, value in {'id': id, 'street': street, 'city': city, 'state': state, 'country': country, 'postal_code': postal_code, 'created_at': created_at, 'updated_at': updated_at}.items():
          setattr(record_to_update, key, value)
      db.commit()
      db.refresh(record_to_update)
      return record_to_update


def delete_addresses_by_id(db: Session, id: int):
      record_to_delete = db.query(models.Addresses).filter(models.Addresses.id == id).first()

      if record_to_delete:
          db.delete(record_to_delete)
          db.commit()

      return record_to_delete

