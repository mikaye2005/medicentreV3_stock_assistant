from legacydb.models import (
    Tblitems,
    Tblcompanybranchitems,
    Tblitemstoragelocations,
    Tblstockchanges,
    Tblstocktakes,
)


def _clean_join(values):
    """
    Join non-empty values into one readable comma-separated string.
    """
    cleaned = [str(value) for value in values if value not in (None, "", " ")]
    return ", ".join(cleaned) if cleaned else "No sample values found."


def build_live_stock_context(user_question: str) -> str:
    """
    Build a live database summary based on the user's question.

    This keeps the system read-only and only returns small safe summaries
    from the real stock tables.
    """
    try:
        question = user_question.lower()

        # General counts that are always useful
        item_count = Tblitems.objects.using("medicentre").count()
        branch_item_count = Tblcompanybranchitems.objects.using("medicentre").count()
        storage_record_count = Tblitemstoragelocations.objects.using("medicentre").count()
        stock_change_count = Tblstockchanges.objects.using("medicentre").count()
        stock_take_count = Tblstocktakes.objects.using("medicentre").count()

        base_summary = f"""
General live database summary:
- Total item records: {item_count}
- Total branch item records: {branch_item_count}
- Total item storage location records: {storage_record_count}
- Total stock change records: {stock_change_count}
- Total stock take records: {stock_take_count}
""".strip()

        # Quantity / batch / expiry / reorder questions
        if any(word in question for word in [
            "quantity", "available", "stock level", "batch", "expiry", "reorder", "stored"
        ]):
            sample_rows = list(
                Tblitemstoragelocations.objects.using("medicentre").values(
                    "batch",
                    "totalquantity",
                    "availablequantity",
                    "expirydate",
                    "reorderlevel",
                )[:5]
            )

            detail_lines = []
            for row in sample_rows:
                detail_lines.append(
                    f"Batch={row.get('batch')}, "
                    f"TotalQuantity={row.get('totalquantity')}, "
                    f"AvailableQuantity={row.get('availablequantity')}, "
                    f"ExpiryDate={row.get('expirydate')}, "
                    f"ReorderLevel={row.get('reorderlevel')}"
                )

            return f"""
{base_summary}

Focused live context for stock quantity/storage questions:
- The table tblitemstoragelocations currently contains records showing batch, quantity, available quantity, expiry date, and reorder level.
- Sample rows:
{chr(10).join(detail_lines) if detail_lines else "No sample rows found."}
""".strip()

        # Movement questions
        if any(word in question for word in [
            "movement", "increase", "decrease", "changed", "sale", "sales", "opening stock", "increment"
        ]):
            sample_rows = list(
                Tblstockchanges.objects.using("medicentre").values(
                    "quantitychanged",
                    "isincrement",
                    "reference",
                    "datetimechanged",
                )[:5]
            )

            detail_lines = []
            for row in sample_rows:
                detail_lines.append(
                    f"QuantityChanged={row.get('quantitychanged')}, "
                    f"IsIncrement={row.get('isincrement')}, "
                    f"Reference={row.get('reference')}, "
                    f"DateTimeChanged={row.get('datetimechanged')}"
                )

            return f"""
{base_summary}

Focused live context for stock movement questions:
- The table tblstockchanges currently contains movement records with quantity changed, increment/decrement status, reference, and date/time.
- Sample rows:
{chr(10).join(detail_lines) if detail_lines else "No sample rows found."}
""".strip()

        # Stock take questions
        if any(word in question for word in [
            "stock take", "stocktake", "commit", "committed", "freeze", "frozen", "verification"
        ]):
            sample_rows = list(
                Tblstocktakes.objects.using("medicentre").values(
                    "storagelocationid",
                    "hasbeencommittedtostock",
                    "committedbysysuid",
                    "isfrozen",
                    "datetimecreated",
                )[:5]
            )

            detail_lines = []
            for row in sample_rows:
                detail_lines.append(
                    f"StorageLocationID={row.get('storagelocationid')}, "
                    f"HasBeenCommittedToStock={row.get('hasbeencommittedtostock')}, "
                    f"CommittedBySysUID={row.get('committedbysysuid')}, "
                    f"IsFrozen={row.get('isfrozen')}, "
                    f"DateTimeCreated={row.get('datetimecreated')}"
                )

            return f"""
{base_summary}

Focused live context for stock take questions:
- The table tblstocktakes currently contains stock take session records with commit/freeze related fields.
- Sample rows:
{chr(10).join(detail_lines) if detail_lines else "No sample rows found."}
""".strip()

        # Item / branch questions
        if any(word in question for word in [
            "item", "branch", "barcode", "code", "category", "class"
        ]):
            sample_item_names = list(
                Tblitems.objects.using("medicentre").values_list("name", flat=True)[:5]
            )
            sample_branch_codes = list(
                Tblcompanybranchitems.objects.using("medicentre").values_list("itemcode", flat=True)[:5]
            )

            return f"""
{base_summary}

Focused live context for item/branch questions:
- Sample item names from tblitems: {_clean_join(sample_item_names)}
- Sample branch item codes from tblcompanybranchitems: {_clean_join(sample_branch_codes)}
""".strip()

        # Default general summary
        sample_items = list(
            Tblitems.objects.using("medicentre").values_list("name", flat=True)[:5]
        )

        return f"""
{base_summary}

General sample item names from tblitems:
{_clean_join(sample_items)}
""".strip()

    except Exception as exc:
        return f"Live database summary could not be loaded: {exc}"