from typing import Dict, List, Any


class JsonSquasher:
    def __init__(self, lossy: bool = False):
        self.lossy = lossy

    def squash(self, data: Dict[str, Any]) -> str:
        lines = []

        for key, value in data.items():
            if isinstance(value, dict):
                lines.extend(self._squash_object(key, value))

            elif isinstance(value, list):
                lines.extend(self._squash_list(key, value))

            else:
                lines.append(f"{key}: {value}")

        return "\n".join(lines)

    # ---------- helpers ----------

    def _squash_object(self, key: str, obj: Dict[str, Any]) -> List[str]:
        lines = [f"{key}:"]
        for k, v in obj.items():
            lines.append(f"  {k}: {v}")
        return lines

    def _squash_list(self, key: str, lst: List[Any]) -> List[str]:
        if not lst:
            return [f"{key}[0]:"]

        # list of primitives
        if not isinstance(lst[0], dict):
            values = ",".join(str(v) for v in lst)
            return [f"{key}[{len(lst)}]: {values}"]

        # list of objects
        return self._squash_object_list(key, lst)

    def _squash_object_list(self, key: str, lst: List[Dict[str, Any]]) -> List[str]:
        fields = list(lst[0].keys())
        schema = ",".join(fields)

        lines = [f"{key}[{len(lst)}]{{{schema}}}:"]
        for item in lst:
            row = ",".join(str(item[f]) for f in fields)
            lines.append(f"  {row}")

        return lines
