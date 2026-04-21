from legacydb.models import (
    Tblitems,
    Tblcompanybranchitems,
    Tblitemstoragelocations,
    Tblstockchanges,
    Tblstocktakes,
)


def _clean_values(values):
    """
    Convert values into a readable comma-separated string,
    while removing blanks and None values.
    """
    cleaned = [str(value) for value in values if value not in (None, "", " ")]
    return ", ".join(cleaned) if cleaned else "No sample values found."


def build_controlled_stock_facts(user_question: str) -> str:
    """
    Build a stricter set of stock facts from the real database.

    These facts are intended to be higher-trust than general free-form summaries.
    The assistant should rely on these facts first when answering.
    """
    question = user_question.lower()

    try:
        # Questions about quantity, batch, expiry, reorder, stock held
        if any(word in question for word in [
            "quantity", "available", "batch", "expiry", "reorder", "stored", "stock level"
        ]):
            qs = Tblitemstoragelocations.objects.using("medicentre")

            total_rows = qs.count()
            rows_with_batch = qs.exclude(batch__isnull=True).exclude(batch="").count()
            rows_with_expiry = qs.exclude(expirydate__isnull=True).count()
            sample_batches = list(qs.values_list("batch", flat=True)[:5])

            return f"""
Verified Stock Facts:
- Current stock position data is represented in tblitemstoragelocations.
- Total tblitemstoragelocations records: {total_rows}
- Records with batch values: {rows_with_batch}
- Records with expiry dates: {rows_with_expiry}
- Sample batch values: {_clean_values(sample_batches)}
- Key fields in tblitemstoragelocations include batch, totalquantity, availablequantity, expirydate, and reorderlevel.
""".strip()

        # Questions about movement, increase, decrease, sales, opening stock
        if any(word in question for word in [
            "movement", "increase", "decrease", "changed", "sale", "sales",
            "opening stock", "increment", "decrement"
        ]):
            qs = Tblstockchanges.objects.using("medicentre")

            total_rows = qs.count()
            increment_rows = qs.filter(isincrement=1).count()
            decrement_rows = qs.filter(isincrement=0).count()
            sample_references = list(qs.values_list("reference", flat=True)[:5])

            return f"""
Verified Stock Facts:
- Stock movement history is represented in tblstockchanges.
- Total tblstockchanges records: {total_rows}
- Records marked as increments: {increment_rows}
- Records marked as decrements: {decrement_rows}
- Sample references: {_clean_values(sample_references)}
- Key fields in tblstockchanges include quantitychanged, isincrement, reference, and datetimechanged.
""".strip()

        # Questions about stock takes, commit, freeze, verification
        if any(word in question for word in [
            "stock take", "stocktake", "commit", "committed", "freeze", "frozen", "verification"
        ]):
            qs = Tblstocktakes.objects.using("medicentre")

            total_rows = qs.count()
            committed_rows = qs.filter(hasbeencommittedtostock=1).count()
            uncommitted_rows = qs.filter(hasbeencommittedtostock=0).count()
            frozen_rows = qs.filter(isfrozen=1).count()

            return f"""
Verified Stock Facts:
- Stock take sessions are represented in tblstocktakes.
- Total tblstocktakes records: {total_rows}
- Committed stock take records: {committed_rows}
- Uncommitted stock take records: {uncommitted_rows}
- Frozen stock take records: {frozen_rows}
- Key fields in tblstocktakes include hasbeencommittedtostock, committedbysysuid, isfrozen, and datetimecreated.
""".strip()

        # Questions about items, branch items, barcode, code, category, class
        if any(word in question for word in [
            "item", "branch", "barcode", "code", "category", "class"
        ]):
            item_count = Tblitems.objects.using("medicentre").count()
            branch_item_count = Tblcompanybranchitems.objects.using("medicentre").count()

            sample_items = list(
                Tblitems.objects.using("medicentre").values_list("name", flat=True)[:5]
            )
            sample_codes = list(
                Tblcompanybranchitems.objects.using("medicentre").values_list("itemcode", flat=True)[:5]
            )

            return f"""
Verified Stock Facts:
- General item definitions are represented in tblitems.
- Branch-specific item setup is represented in tblcompanybranchitems.
- Total tblitems records: {item_count}
- Total tblcompanybranchitems records: {branch_item_count}
- Sample item names: {_clean_values(sample_items)}
- Sample item codes: {_clean_values(sample_codes)}
""".strip()

        # Default facts if the question is broad
        return f"""
Verified Stock Facts:
- General item definitions are represented in tblitems.
- Current stock position data is represented in tblitemstoragelocations.
- Stock movement history is represented in tblstockchanges.
- Stock take sessions are represented in tblstocktakes.
""".strip()

    except Exception as exc:
        return f"Verified Stock Facts could not be loaded: {exc}"