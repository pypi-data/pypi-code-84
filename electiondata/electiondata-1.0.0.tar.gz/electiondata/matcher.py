from abc import ABC, abstractmethod

import attr

from fuzzy_match import match

from .errors import DataError, error, check, replace_vars


class PartialMap(ABC):
    @abstractmethod
    def transform(self, x, context):
        """
        Returns (True, transformed_x) if x is a valid entry to the map, or (False, error) otherwise.

        The context can be used to inform the transformation.
        """
        pass

    def __call__(self, x, context):
        valid, result = self.transform(x, context)
        if valid:
            return result
        else:
            error(result)
            return x

    def apply_to_df(self, df, col_in, col_out, *, var_name="$var"):
        out = df.apply(lambda row: self(row[col_in], row), axis=1)
        if check(match=var_name):
            df[col_out] = out


@attr.s
class DictionaryMap(PartialMap):
    mapper = attr.ib()
    error_prefix = attr.ib(default=None)
    default_rewrite = attr.ib(default=None)

    def close_miss(self, x):
        if not hasattr(self, "_close_miss_cache"):
            setattr(self, "_close_miss_cache", {})
        close_miss_cache = getattr(self, "_close_miss_cache")
        if x not in close_miss_cache:
            close_miss_cache[x] = self.close_miss_uncached(x)
        return close_miss_cache[x]

    def close_miss_uncached(self, x):
        result = match.extractOne(x, list(self.mapper))
        if result is None:
            return None, -1
        replacement, confidence = result
        confidence -= 0.25
        return replacement, confidence

    def transform(self, x, context):
        if x in self.mapper:
            return True, self.mapper[x]
        message = f"{x} does not exist"
        if self.error_prefix is not None:
            message = self.error_prefix + " : " + message

        replacement, confidence = self.close_miss(x)

        if confidence < 0 and self.default_rewrite is not None:
            replacement = self.default_rewrite
            confidence = 0

        if confidence >= 0:
            fix = f"$rewrite[{x!r}] = {replacement!r}"
        else:
            fix = None

        return False, DataError(message, fix, confidence)


@attr.s
class BlackBoxMap(PartialMap):
    matcher = attr.ib()
    transformer = attr.ib()

    def transform(self, x, context):
        if self.matcher(x, context):
            return "True", self.transformer(x, context)
        return False, DataError(f"no match found for {x}", None)


@attr.s
class UniqueMatch(PartialMap):
    rewrite = attr.ib()
    partial_maps = attr.ib()

    def transform(self, x, context):
        xs = set(self.rewrite(x))
        results = {
            (name, x): pmap.transform(x, context)
            for name, pmap in self.partial_maps.items()
            for x in xs
        }
        num_valid = sum(bool(valid) for valid, _ in results.values())
        if num_valid > 1:
            return False, DataError(
                f"Expected only one valid match but multiple matches: {tuple((name, x) for (name, x), (v, _) in results.items() if v)}",
                None,
            )
        if num_valid == 1:
            [y] = [v for valid, v in results.values() if valid]
            return True, y
        assert num_valid == 0
        name, most_fixable_error = max(
            [(n, e) for (n, _), (_, e) in results.items()],
            key=lambda x: x[1].fixability,
        )
        return False, DataError(
            f"{name}: {most_fixable_error.message}",
            replace_vars(most_fixable_error.fix, dict(rewrite="$match.rewrite")),
            most_fixable_error.fixability,
        )


@attr.s
class Dispatcher(PartialMap):
    dispatch_key_extractor = attr.ib()
    get_sub_map = attr.ib()
    _cache = attr.ib(default=attr.Factory(dict))

    def transform(self, x, context):
        key = self.dispatch_key_extractor(context)
        if key not in self._cache:
            self._cache[key] = self.get_sub_map(key)
        return self._cache[key].transform(x, context)
