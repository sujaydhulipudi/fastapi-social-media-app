from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

import schemas, models, oauth2, database

router = APIRouter(
    prefix="/vote",
    tags=["vote"],
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    if(vote.dir == 1):
        vote_query = db.query(models.Vote).filter(models.Vote.post_id==vote.post_id, models.Vote.user_id == current_user.id)
        found_vote = vote_query.first()