# Synopsis
This wrapper connects to our staff database backend.

# Installation
To install it, use pip.
```pip install git+https://github.com/fat-whale/staffy.git ```

# Usage
After that, you need to import it and initialize the wrapper class with the current port and host of the backend.
```
from staffy.wrapper import Wrapper

wrapper = Wrapper("localhost", 80, "your_key")
```
From there, you will be able use the following methods.

Have in mind the current sets of keys and your current security level.
```
    # Public keys
    [
        "discord", 
        "username",
        "discord_id", 
        "blubber", 
        "blubber_id",  
        "pulse_id", 
        "github",
        "fullname", 
        "alias",
        "title",
        "team", 
        "introduction", 
        "email", 
        "status", 
        "location",
        "avatar", 
        "timezone",
        "availability", 
        "color",
        "updates",
        "doc_id"
    ]

    # Private keys
    [
        phone
    ]

    # Protected keys
    [
        btc_address
    ]

```
## get_profile
Params:
Any from the keys lists.

Returns:
A list with the documents that match to the query.
False if didn't found any document.

Example:
```
profile = wrapper.get_profile(username="username")
```

## patch_profile (pending remake)
Params:
Any from public keys


Returns:
True if changed a profile.
False if didn't found any document.

Example:
```
profile = wrapper.patch_profile(username="username", title="Jr Python Developer")
```

Notice that you need at least two parameters to change something.

## get_document 
Params:
Any from the keys lists.

Returns:
A list with the documents that match to the query.
False if didn't found any profile or you don't have rights.

Example:
```
document = wrapper.get_document(username="username", title="Jr Python Developer")
```

Notice that you need at least two parameters to change something.

## put_document
Params:
Any from the keys lists.

Returns:
True if the document was saved.
False if you don't have rights.

Example:
```
wrapper.put_document(username="username")
```


## patch_document
Params:
Any from the keys lists.

Returns:
A list with the documents that match to the query.
False if didn't found any document or you don't have rights.

Example:
```
wrapper.patch_document(username="username", phone="3456345")
```

## delete_document
Params:
Any from the keys lists.

Returns:
True if deleted a document.
False if didn't found any document or you don't have rights.

Example:
```
wrapper.delete_document(username="username")
```