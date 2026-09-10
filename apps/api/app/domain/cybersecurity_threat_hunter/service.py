from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.cybersecurity_threat_hunter.models import AgenticCybersecurityThreatHunterSession, AgenticCybersecurityThreatHunterItem
from app.domain.cybersecurity_threat_hunter.schemas import AgenticCybersecurityThreatHunterSessionCreate, AgenticCybersecurityThreatHunterItemCreate

class AgenticCybersecurityThreatHunterService:
    @staticmethod
    def create_session(db: Session, data: AgenticCybersecurityThreatHunterSessionCreate) -> AgenticCybersecurityThreatHunterSession:
        db_obj = AgenticCybersecurityThreatHunterSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticCybersecurityThreatHunterSession:
        return db.query(AgenticCybersecurityThreatHunterSession).filter(AgenticCybersecurityThreatHunterSession.id == session_id).first()
