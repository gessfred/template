from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Sequence
import os
from dependencies import Base

schema = os.getenv("MAIN_APP_SCHEMA")