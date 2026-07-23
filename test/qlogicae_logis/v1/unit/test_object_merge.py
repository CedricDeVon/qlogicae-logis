# from __future__ import annotations

# from copy import deepcopy

# import pytest


# def handle_deep_merging_recursive(
#     left: Any,
#     right: Any,
# ) -> Any:
#     if left is None:
#         return deepcopy(right)

#     if right is None:
#         return deepcopy(left)

#     if isinstance(left, dict) and isinstance(right, dict):
#         result = deepcopy(left)

#         for key, value in right.items():
#             if key in result:
#                 result[key] = handle_deep_merging_recursive(
#                     result[key],
#                     value,
#                 )
#             else:
#                 result[key] = deepcopy(value)

#         return result

#     if isinstance(left, list) and isinstance(right, list):
#         return deepcopy(left) + deepcopy(right)

#     return deepcopy(right)


# def handle_deep_merging_iterative(
#     left: Any,
#     right: Any,
# ) -> Any:
#     if left is None:
#         return deepcopy(right)

#     if right is None:
#         return deepcopy(left)

#     if not (isinstance(left, dict) and isinstance(right, dict)):
#         if isinstance(left, list) and isinstance(right, list):
#             return deepcopy(left) + deepcopy(right)

#         return deepcopy(right)

#     result = deepcopy(left)

#     stack: list[tuple[dict[str, Any], dict[str, Any]]] = [
#         (
#             result,
#             right,
#         ),
#     ]

#     while stack:
#         current_left, current_right = stack.pop()

#         for key, right_value in current_right.items():
#             if key not in current_left:
#                 current_left[key] = deepcopy(right_value)
#                 continue

#             left_value = current_left[key]

#             if isinstance(left_value, dict) and isinstance(right_value, dict):
#                 stack.append(
#                     (
#                         left_value,
#                         right_value,
#                     ),
#                 )

#             elif isinstance(left_value, list) and isinstance(right_value, list):
#                 current_left[key] = deepcopy(left_value) + deepcopy(right_value)

#             else:
#                 current_left[key] = deepcopy(
#                     right_value,
#                 )

#     return result


# def make_nested(
#     depth: int,
#     width: int,
# ):
#     if depth == 0:
#         return {f"item{i}": list(range(20)) for i in range(width)}

#     return {
#         f"level{i}": make_nested(
#             depth - 1,
#             width,
#         )
#         for i in range(width)
#     }


# @pytest.fixture(scope="session")
# def large_merge_data():
#     left = make_nested(
#         depth=5,
#         width=5,
#     )

#     right = make_nested(
#         depth=5,
#         width=5,
#     )

#     right["new"] = {
#         "hello": "world",
#     }

#     return left, right


# def test_recursive_large(
#     benchmark,
#     large_merge_data,
# ):
#     left, right = large_merge_data

#     benchmark(
#         handle_deep_merging_recursive,
#         deepcopy(left),
#         deepcopy(right),
#     )


# def test_iterative_large(
#     benchmark,
#     large_merge_data,
# ):
#     left, right = large_merge_data

#     benchmark(
#         handle_deep_merging_iterative,
#         deepcopy(left),
#         deepcopy(right),
#     )
