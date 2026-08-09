# from __future__ import annotations

# import json
# import subprocess
# import sys

# MODULES = (
#     (
#         "dynamic",
#         "test.qlogicae_logis.v1.benchmark.memory_usage.imports.dynamic",
#     ),
#     (
#         "static",
#         "test.qlogicae_logis.v1.benchmark.memory_usage.imports.static",
#     ),
# )

# SCRIPT = r"""
# import importlib
# import json
# import sys
# import time

# import psutil
# from pympler import asizeof

# process = psutil.Process()

# rss_before = process.memory_info().rss

# start = time.perf_counter_ns()
# module = importlib.import_module("{module}")
# import_time = time.perf_counter_ns() - start

# rss_after_import = process.memory_info().rss

# shallow = sys.getsizeof(module)
# deep = asizeof.asizeof(module)

# start = time.perf_counter_ns()
# module.sum(1, 2)
# first_call = time.perf_counter_ns() - start

# rss_after_first = process.memory_info().rss

# start = time.perf_counter_ns()
# module.sum(1, 2)
# second_call = time.perf_counter_ns() - start

# rss_after_second = process.memory_info().rss

# print(
#     json.dumps(
#         {{
#             "import_time": import_time,
#             "first_call": first_call,
#             "second_call": second_call,
#             "rss_import": rss_after_import - rss_before,
#             "rss_first": rss_after_first - rss_after_import,
#             "rss_second": rss_after_second - rss_after_first,
#             "shallow": shallow,
#             "deep": deep,
#         }}
#     )
# )
# """


# def benchmark(
#     module_name: str,
# ) -> dict[str, int]:
#     result = subprocess.run(
#         (
#             sys.executable,
#             "-c",
#             SCRIPT.format(module=module_name),
#         ),
#         capture_output=True,
#         text=True,
#         check=True,
#     )

#     return json.loads(result.stdout)


# def main() -> None:
#     print(
#         f"{'Module':<10}"
#         f"{'Import(ns)':>15}"
#         f"{'1st(ns)':>15}"
#         f"{'2nd(ns)':>15}"
#         f"{'RSS Import':>15}"
#         f"{'RSS 1st':>15}"
#         f"{'RSS 2nd':>15}"
#         f"{'Shallow':>12}"
#         f"{'Deep':>12}"
#     )

#     print("-" * 126)

#     for name, module in MODULES:
#         result = benchmark(module)

#         print(
#             f"{name:<10}"
#             f"{result['import_time']:>15,}"
#             f"{result['first_call']:>15,}"
#             f"{result['second_call']:>15,}"
#             f"{result['rss_import']:>15,}"
#             f"{result['rss_first']:>15,}"
#             f"{result['rss_second']:>15,}"
#             f"{result['shallow']:>12,}"
#             f"{result['deep']:>12,}"
#         )


# if __name__ == "__main__":
#     main()
