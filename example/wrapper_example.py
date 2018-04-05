from staffy.wrapper import Wrapper


wrapper = Wrapper("staging.bots.pokerpod.io", 80, "test_key")
#wrapper = Wrapper("localhost", 80)

def main():
    username = "urbanon"

    # Create a document
    put_document = wrapper.put_document(username=username)
    print(put_document)


    # Modify the private part of the document
    patch_document = wrapper.patch_document(username=username, btc_address="f1ewrf23123wef1231wef23")
    print(patch_document)
    
    
    # Get the whole document 
    get_document = wrapper.get_document(username=username)
    print(get_document)

      
    # Modify the public data
    patch_profile = wrapper.patch_profile(username=username, title="Jr Python Developer")
    print(patch_profile)


    # Get the public data
    get_profile = wrapper.get_profile(username=username)
    print(get_profile)


    # Delete the document
    delete_document = wrapper.delete_document(username=username)
    print(delete_document)


    # Get the public data again (fails as it just deleted it)
    get_profile = wrapper.get_profile(username=username)
    print(get_profile)


if __name__ == '__main__':
    main()
