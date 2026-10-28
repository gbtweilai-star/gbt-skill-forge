"""The capability contract, copied verbatim from the GBT V8 registry.

Do not hand-edit: ``tests/test_spec.py`` pins every field against the
registry snapshot so drift fails the build instead of shipping quietly.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

_RAW = r"""{
 "name": "skill_forge",
 "domain": "recon",
 "desc": "**技能蒸馏五式**（主人令 2026-10-16：把五个 skill 蒸成我们的原生能力）：蒸自五个 MIT 仓的思想—— ① **女娃**（nuwa-skill）不是复制人、是提炼思维框架（心智模型/决策启发式/表达 DNA/边界）② **last30days**：agent 主导的搜索、按投票与真实金额计分（非编辑评分），跨 Reddit/X/YouTube/HN/Polymarket/web ③ **同事**（distilly）：经验/对话→可复用技能 ④ **前任**（ex-skill）：原材料→说话方式 DNA ⑤ **反蒸馏**（anti-distill）：交出版消毒 + **私有备份留核心**。op=think/radar/experience/style/anti/check/route（**全只读·零作用域·不出网**）；边界：MIT 只蒸思想 · **隐私**（原材料不外发、第三方脱敏、不做人脸声纹建模）· **不冒充真人**。",
 "handler": "skill_forge",
 "safe": false,
 "external": false,
 "requires_params": false,
 "params": [],
 "params_hint": "",
 "multi_op": true,
 "ops": [
  "think",
  "radar",
  "experience",
  "style",
  "anti",
  "check",
  "route"
 ],
 "ops_hint": ""
}"""


@dataclass(frozen=True)
class CapSpec:
    """Immutable description of one capability bit."""

    name: str
    domain: str
    desc: str
    handler: str
    safe: bool
    external: bool
    requires_params: bool
    params: Tuple[str, ...] = ()
    params_hint: str = ""
    multi_op: bool = False
    ops: Tuple[str, ...] = ()
    ops_hint: str = ""

    @property
    def gated(self) -> bool:
        """True when the registry marks this bit ``safe: false``.

        Gated does not mean "dangerous"; it means the action can change state
        that cannot be restored by running the inverse action.
        """
        return not self.safe

    @property
    def summary(self) -> str:
        """First clause of the description, for one-line listings."""
        for sep in ("\uff08", "\uff1b", "\u3002", ";"):
            if sep in self.desc:
                head = self.desc.split(sep, 1)[0].strip()
                if head:
                    return head
        return self.desc.strip()

    def as_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "domain": self.domain,
            "desc": self.desc,
            "handler": self.handler,
            "safe": self.safe,
            "gated": self.gated,
            "external": self.external,
            "requires_params": self.requires_params,
            "params": list(self.params),
            "params_hint": self.params_hint,
            "multi_op": self.multi_op,
            "ops": list(self.ops),
            "ops_hint": self.ops_hint,
        }


_data = json.loads(_RAW)

SPEC = CapSpec(
    name=_data["name"],
    domain=_data["domain"],
    desc=_data["desc"],
    handler=_data["handler"],
    safe=_data["safe"],
    external=_data["external"],
    requires_params=_data["requires_params"],
    params=tuple(_data["params"]),
    params_hint=_data["params_hint"],
    multi_op=_data["multi_op"],
    ops=tuple(_data["ops"]),
    ops_hint=_data["ops_hint"],
)
