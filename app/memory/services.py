class MemoryService:
    def __init__(self, db):
        self.db = db

    def store_memories(self, user_id, memories):
        created = []
        for m in memories:
            mem = Memory(
                user_id=user_id,
                type=m["type"],
                content=m["content"]
            )
            self.db.add(mem)
            self.db.flush()
            created.append(mem)

        # links
        for i, m in enumerate(memories):
            for j in m.get("links", []):
                self.db.add(
                    MemoryLink(
                        from_id=created[i].id,
                        to_id=created[j].id,
                        relation="related"
                    )
                )

        self.db.commit()

