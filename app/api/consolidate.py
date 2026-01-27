@router.post("/consolidate")
def consolidate(req: MessagesRequest, user=Depends(current_user), db=Depends(get_db)):
    cutter = MemoryCutterService()
    identity = IdentityService()
    memory_service = MemoryService(db)

    memories = cutter.cut(req.messages)
    memory_service.store_memories(user.id, memories)

    identity_memory = identity.condense_identity(req.messages)
    memory_service.store_memories(user.id, [{
        "type": "identity",
        "content": identity_memory
    }])

    return {"status": "ok"}

