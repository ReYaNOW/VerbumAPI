# from typing import AsyncGenerator
#
# from fastapi import Depends
# from sqlalchemy.ext.asyncio import (
#     AsyncSession,
#     async_sessionmaker,
#     create_async_engine,
# )
#
# from stats_counter.config import DATABASE_URL
#
#
# engine = create_async_engine(DATABASE_URL)
# async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
#
#
# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session
#
#
# async def get_user_db(session: AsyncSession = Depends(get_async_session)):
#     yield SQLAlchemyUserDatabase(session, User)
