from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.cybersecurity_threat_hunter.schemas import AgenticCybersecurityThreatHunterSessionCreate, AgenticCybersecurityThreatHunterSessionResponse
from app.domain.cybersecurity_threat_hunter.service import AgenticCybersecurityThreatHunterService

router = APIRouter(prefix="/api/v1/cybersecurity_threat_hunter", tags=["Agentic Cybersecurity Threat Hunter Domain"])

@router.post("/sessions", response_model=AgenticCybersecurityThreatHunterSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticCybersecurityThreatHunterSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Cybersecurity Threat Hunter.
    """
    return AgenticCybersecurityThreatHunterService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticCybersecurityThreatHunterSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticCybersecurityThreatHunterService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
