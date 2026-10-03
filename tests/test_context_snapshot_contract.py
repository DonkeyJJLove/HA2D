import unittest
from reference.context_importer import build_snapshot,accept_snapshot
from contracts.context_snapshot import ContextSnapshotError
class ContextSnapshotTests(unittest.TestCase):
 def snap(self):
  return build_snapshot(snapshot_id="snapshot:1",source_repository="DonkeyJJLove/HA2D",source_commit="1"*40,epoch=3,cutoff_ref="cutoff:fixture",records=[{"source_ref":"source:a","payload":b"a","epistemic_class":"OBSERVED"},{"source_ref":"source:b","payload":b"b","epistemic_class":"DERIVED"}])
 def test_ordered_digest_bound_snapshot(self):
  s=self.snap();self.assertEqual(tuple(x.source_ref for x in s.sources),("source:a","source:b"));self.assertEqual((s.authority_effect,s.memory_commit_effect),("NONE","NONE"))
 def test_stale_epoch_and_commit_denied(self):
  s=self.snap()
  with self.assertRaises(ContextSnapshotError):accept_snapshot(s,expected_repository="DonkeyJJLove/HA2D",expected_commit="2"*40,expected_epoch=3)
  with self.assertRaises(ContextSnapshotError):accept_snapshot(s,expected_repository="DonkeyJJLove/HA2D",expected_commit="1"*40,expected_epoch=4)
 def test_payload_must_be_bytes_and_epistemic_class_is_explicit(self):
  with self.assertRaises(ContextSnapshotError):build_snapshot(snapshot_id="snapshot:1",source_repository="DonkeyJJLove/HA2D",source_commit="1"*40,epoch=1,cutoff_ref="c",records=[{"source_ref":"a","payload":"not-bytes","epistemic_class":"OBSERVED"}])
  simulated=build_snapshot(snapshot_id="snapshot:sim",source_repository="DonkeyJJLove/HA2D",source_commit="1"*40,epoch=1,cutoff_ref="c",records=[{"source_ref":"simulation:1","payload":b"sim","epistemic_class":"SIMULATED"}])
  self.assertEqual(simulated.sources[0].epistemic_class,"SIMULATED")
if __name__=="__main__":unittest.main()
