# skill_forge

**One capability bit from GBT V8, packaged standalone.** No. 202 of 341,
`recon` domain (Recon).

<p>
<img alt="python" src="https://img.shields.io/badge/python-3.9%2B-blue">
<img alt="license" src="https://img.shields.io/badge/license-MIT-green">
<img alt="deps" src="https://img.shields.io/badge/runtime%20dependencies-0-brightgreen">
</p>

> **技能蒸馏五式**（主人令 2026-10-16：把五个 skill 蒸成我们的原生能力）：蒸自五个 MIT 仓的思想—— ① **女娃**（nuwa-skill）不是复制人、是提炼思维框架（心智模型/决策启发式/表达 DNA/边界）② **last30days**：agent 主导的搜索、按投票与真实金额计分（非编辑评分），跨 Reddit/X/YouTube/HN/Polymarket/web ③ **同事**（distilly）：经验/对话→可复用技能 ④ **前任**（ex-skill）：原材料→说话方式 DNA ⑤ **反蒸馏**（anti-distill）：交出版消毒 + **私有备份留核心**。op=think/radar/experience/style/anti/check/route（**全只读·零作用域·不出网**）；边界：MIT 只蒸思想 · **隐私**（原材料不外发、第三方脱敏、不做人脸声纹建模）· **不冒充真人**。

That description is copied verbatim from the registry. `tests/test_spec.py` pins it,
so documentation drift fails the build instead of shipping quietly.

## What this package actually is

It is the **contract** for one capability: its name, its parameters, the values it
accepts, and whether it can change state that cannot be restored. It is not the
implementation — that lives in the runtime this bit was extracted from.

So `run()` goes through a narrow `Backend` protocol, and the default backend is a
stub that **says so**:

```
status="validated"   backend="stub"   data={"executed": false}
```

Never `status="ok"`. A stub that reports success is worse than no stub, because the
caller stops looking for the real thing.

## Install

```bash
git clone https://github.com/gbtweilai-star/gbt-skill-forge.git
cd gbt-skill-forge
python -m pip install -e ".[dev]"
```

## Use

```bash
python -m gbt_skill_forge info                  # capability card
python -m gbt_skill_forge spec --json           # machine-readable contract
python -m gbt_skill_forge check --payload '{}'
python -m gbt_skill_forge run   --payload '{}'
```

Real `info` output from this machine:

```text
skill_forge  (recon)  v1.0.0
----------------------------------------
**技能蒸馏五式**（主人令 2026-10-16：把五个 skill 蒸成我们的原生能力）：蒸自五个 MIT 仓的思想—— ① **女娃**（nuwa-skill）不是复制人、是提炼思维框架（心智模型/决策启发式/表达 DNA/边界）② **last30days**：agent 主导的搜索、按投票与真实金额计分（非编辑评分），跨 Reddit/X/YouTube/HN/Polymarket/web ③ **同事**（distilly）：经验/对话→可复用技能 ④ **前任**（ex-skill）：原材料→说话方式 DNA ⑤ **反蒸馏**（anti-distill）：交出版消毒 + **私有备份留核心**。op=think/radar/experience/style/anti/check/route（**全只读·零作用域·不出网**）；边界：MIT 只蒸思想 · **隐私**（原材料不外发、第三方脱敏、不做人脸声纹建模）· **不冒充真人**。

gated      : True   <- needs explicit consent
external   : False
multi-op   : True
params     : (none)
values     : think, radar, experience, style, anti, check, route
```

Wire a real implementation:

```python
from gbt_skill_forge import run

class MyBackend:
    name = "my-backend"
    def invoke(self, cap, payload):
        return {"cap": cap, "handled": sorted(payload)}

result = run({}, backend=MyBackend())
assert result.status == "ok"
```

## Parameters

| name | required | notes |
|---|---|---|
| — | no | the registry declares no required parameters |

Registry hint (`params_hint`): (empty)

**注册表登记的取值 / 子动作（7 个）**：`think`、`radar`、`experience`、`style`、`anti`、`check`、`route`

Types are deliberately absent: the registry does not declare them, and an invented
type is worse than no type, because callers believe it.

## Boundaries

- Gated: this bit is marked `safe: false` in the registry — it can change state that no inverse action restores.
- No external service dependency declared.
- Multi-op (`multi_op: true`): several sub-actions share one name — read `op` before calling.
- No implementation ships here. Bring a backend; the protocol is one method.

## What this is not

Not a wrapper around a hosted API. Not a model. Not a promise that calling it does
anything on its own. It is the typed seam plus the validation, which is the part that
stays correct even when the implementation changes.

## Tests

```bash
python -m pytest
```

```text
20 passed, 3 skipped in 0.14s
```

## Provenance

| field | value |
|---|---|
| capability | `skill_forge` |
| domain | `recon` |
| handler | `skill_forge` |
| safe | `False` (gated = `True`) |
| external | `False` |
| atlas page | [recon/skill_forge](https://github.com/gbtweilai-star/gbt-caps/blob/main/caps/recon/skill_forge.md) |
| full index | [https://github.com/gbtweilai-star/gbt-caps](https://github.com/gbtweilai-star/gbt-caps) |

The parent README says 348 capabilities; an AST pass over the registry enumerates
`341 + 0 unimplemented + 0 disabled = 341`. The extra 7 are historical duplicates.
Numbering here follows 341 and matches the `gbt-caps` index one-to-one.

## License

MIT.
