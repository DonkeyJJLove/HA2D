from __future__ import annotations
from dataclasses import asdict,dataclass,replace
from hashlib import sha256
import json,re
from typing import Mapping,Any,Sequence
SHA=re.compile(r"^[0-9a-f]{64}$");GIT=re.compile(r"^[0-9a-f]{40}$");ID=re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/-]{0,255}$")
class ContextSnapshotError(ValueError):pass
def canon(v):return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
@dataclass(frozen=True)
class ContextSource:
 source_ref:str;source_digest:str;epistemic_class:str
 def validate(self):
  if not isinstance(self.source_ref,str) or ID.fullmatch(self.source_ref) is None:raise ContextSnapshotError("source_ref")
  if not isinstance(self.source_digest,str) or SHA.fullmatch(self.source_digest) is None:raise ContextSnapshotError("source_digest")
  if self.epistemic_class not in {"OBSERVED","DERIVED","SIMULATED","ASSUMED","HYPOTHESIS","RESEARCH_CORPUS"}:raise ContextSnapshotError("epistemic_class")
  return self
@dataclass(frozen=True)
class ContextSnapshot:
 schema:str;snapshot_id:str;source_repository:str;source_commit:str;epoch:int;cutoff_ref:str;sources:tuple[ContextSource,...];payload_digest:str;authority_effect:str="NONE";memory_commit_effect:str="NONE";snapshot_digest:str=""
 def payload(self):d=asdict(self);d.pop("snapshot_digest",None);return d
 def compute(self):return sha256(b"LION/CONTEXT-SNAPSHOT/1\0"+canon(self.payload())).hexdigest()
 def validate(self,req=True):
  if self.schema!="lion.context-snapshot/v1" or not isinstance(self.snapshot_id,str) or ID.fullmatch(self.snapshot_id) is None:raise ContextSnapshotError("identity")
  if not isinstance(self.source_repository,str) or "/" not in self.source_repository or not isinstance(self.source_commit,str) or GIT.fullmatch(self.source_commit) is None:raise ContextSnapshotError("source")
  if isinstance(self.epoch,bool) or not isinstance(self.epoch,int) or self.epoch<1:raise ContextSnapshotError("epoch")
  if not isinstance(self.cutoff_ref,str) or not self.cutoff_ref:raise ContextSnapshotError("cutoff")
  if not isinstance(self.sources,tuple) or not self.sources:raise ContextSnapshotError("sources")
  for s in self.sources:s.validate()
  if tuple(s.source_ref for s in self.sources)!=tuple(sorted(s.source_ref for s in self.sources)):raise ContextSnapshotError("source order")
  if len({s.source_ref for s in self.sources})!=len(self.sources):raise ContextSnapshotError("duplicate source")
  if not isinstance(self.payload_digest,str) or SHA.fullmatch(self.payload_digest) is None:raise ContextSnapshotError("payload_digest")
  if self.authority_effect!="NONE" or self.memory_commit_effect!="NONE":raise ContextSnapshotError("effects")
  if req and (not isinstance(self.snapshot_digest,str) or SHA.fullmatch(self.snapshot_digest) is None or self.snapshot_digest!=self.compute()):raise ContextSnapshotError("snapshot_digest")
  return self
 def sealed(self):return replace(self,snapshot_digest=self.compute()).validate()
