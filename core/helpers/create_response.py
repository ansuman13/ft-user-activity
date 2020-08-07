def create_response(success, data=None, item=None, items=None, err_name=None,
                    err_message=None):
    if success:
        if data is not None:
            return {
                "ok": True,
                "members": data
            }
        elif item is not None:
            return {
                "ok": True,
                "members": {
                    "item": item
                }
            }
        elif items is not None:
            return {
                "ok": True,
                "members": {
                    "items": items
                }
            }
    else:
        return {
            "ok": False,
            "error": {
                "name": err_name,
                "message": err_message
            }
        }