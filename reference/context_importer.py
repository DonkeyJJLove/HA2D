from __future__ import annotations
from hashlib import sha256
from contracts.context_snapshot import ContextSnapshot,ContextSnapshotError,ContextSource
def build_snapshot(*,snapshot_id,source_repository,source_commit,epoch,cutoff_ref,records):
 if not isinstance(records,(list,tuple)) or not records:raise ContextSnapshotError("records")
 sources=[];parts=[]
 for rec in records:
  if not isinstance(rec,dict) or set(rec)!={"source_ref","payload","epistemic_class"}:raise ContextSnapshotError("record")
  raw=rec["payload"]
  if not isinstance(raw,bytes):raise ContextSnapshotError("payload bytes")
  sources.append(ContextSource(rec["source_ref"],sha256(raw).hexdigest(),rec["epistemic_class"]).validate());parts.append(raw)
 payload_digest=sha256(b"\0".join(parts)).hexdigest()
 return ContextSnapshot("lion.context-snapshot/v1",snapshot_id,source_repository,source_commit,epoch,cutoff_ref,tuple(sorted(sources,key=lambda x:x.source_ref)),payload_digest).sealed()
def accept_snapshot(snapshot:ContextSnapshot,*,expected_repository:str,expected_commit:str,expected_epoch:int):
 snapshot.validate()
 if snapshot.source_repository!=expected_repository:raise ContextSnapshotError("repository substitution")
 if snapshot.source_commit!=expected_commit:raise ContextSnapshotError("commit stale")
 if snapshot.epoch!=expected_epoch:raise ContextSnapshotError("epoch stale")
 return snapshot
