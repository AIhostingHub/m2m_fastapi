
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Device
from app.schemas import DeviceCreate, DeviceOut, DeviceUpdate
from app.auth import get_current_user

router = APIRouter(prefix="/devices", tags=["devices"], dependencies=[Depends(get_current_user)])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=DeviceOut, status_code=status.HTTP_201_CREATED)
def create_device(payload: DeviceCreate, db: Session = Depends(get_db)):
    exists = db.query(Device).filter(Device.ip == str(payload.ip)).first()
    if exists:
        raise HTTPException(status_code=409, detail="Device with this IP already exists")
    dev = Device(
        type=payload.type,
        model=payload.model,
        ip=str(payload.ip),
        sn=payload.sn,
        active=payload.active,
        live=payload.live,
        moniter=payload.moniter,
        row_pos=payload.row_pos,
        rack=payload.rack,
        location=payload.location,
        lastcheck=payload.lastcheck
    )
    db.add(dev)
    db.commit()
    db.refresh(dev)
    return dev

@router.get("", response_model=List[DeviceOut])
def list_devices(db: Session = Depends(get_db), limit: int = 100, offset: int = 0):
    return db.query(Device).order_by(Device.id).limit(limit).offset(offset).all()

@router.get("/{device_id}", response_model=DeviceOut)
def get_device(device_id: int, db: Session = Depends(get_db)):
    dev = db.query(Device).filter(Device.id == device_id).first()
    if not dev:
        raise HTTPException(status_code=404, detail="Device not found")
    return dev

@router.put("/{device_id}", response_model=DeviceOut)
def update_device(device_id: int, payload: DeviceCreate, db: Session = Depends(get_db)):
    dev = db.query(Device).filter(Device.id == device_id).first()
    if not dev:
        raise HTTPException(status_code=404, detail="Device not found")

    new_ip = str(payload.ip)
    if new_ip != dev.ip:
        exists = db.query(Device).filter(Device.ip == new_ip).first()
        if exists:
            raise HTTPException(status_code=409, detail="Another device with this IP already exists")

    dev.type = payload.type
    dev.model = payload.model
    dev.ip = new_ip
    dev.sn = payload.sn
    dev.active = payload.active
    dev.live = payload.live
    dev.moniter = payload.moniter
    dev.row_pos = payload.row_pos
    dev.rack = payload.rack
    dev.location = payload.location
    dev.lastcheck = payload.lastcheck

    db.add(dev)
    db.commit()
    db.refresh(dev)
    return dev

@router.patch("/{device_id}", response_model=DeviceOut)
def patch_device(device_id: int, payload: DeviceUpdate, db: Session = Depends(get_db)):
    dev = db.query(Device).filter(Device.id == device_id).first()
    if not dev:
        raise HTTPException(status_code=404, detail="Device not found")

    def set_if(value, setter):
        if value is not None:
            setter(value)

    if payload.ip is not None:
        new_ip = str(payload.ip)
        if new_ip != dev.ip:
            exists = db.query(Device).filter(Device.ip == new_ip).first()
            if exists:
                raise HTTPException(status_code=409, detail="Another device with this IP already exists")
        dev.ip = new_ip

    set_if(payload.type, lambda v: setattr(dev, 'type', v))
    set_if(payload.model, lambda v: setattr(dev, 'model', v))
    set_if(payload.sn, lambda v: setattr(dev, 'sn', v))
    set_if(payload.active, lambda v: setattr(dev, 'active', v))
    set_if(payload.live, lambda v: setattr(dev, 'live', v))
    set_if(payload.moniter, lambda v: setattr(dev, 'moniter', v))
    set_if(payload.row_pos, lambda v: setattr(dev, 'row_pos', v))
    set_if(payload.rack, lambda v: setattr(dev, 'rack', v))
    set_if(payload.location, lambda v: setattr(dev, 'location', v))
    set_if(payload.lastcheck, lambda v: setattr(dev, 'lastcheck', v))

    db.add(dev)
    db.commit()
    db.refresh(dev)
    return dev

@router.delete("/{device_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_device(device_id: int, db: Session = Depends(get_db)):
    dev = db.query(Device).filter(Device.id == device_id).first()
    if not dev:
        raise HTTPException(status_code=404, detail="Device not found")
    db.delete(dev)
    db.commit()
    return
