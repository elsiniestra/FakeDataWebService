from typing import List, Optional


def is_valid_data_schema_columns_ordering(orders: List[int]) -> Optional[bool]:
    if (
            all(map(lambda x: x > 0, orders))  # non-negatives
            and len(set(orders)) == len(orders)  # duplicates
            and max(orders) - min(orders) + 1 == len(orders)  # correct sequence
    ):
        return True
