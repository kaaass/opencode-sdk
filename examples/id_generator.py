from opencode_sdk import IDGenerator

if __name__ == '__main__':
    gen = IDGenerator()

    # Generate various ID types
    print("Ascending IDs:")
    print(f"  Session:    {gen.ascending('session')}")
    print(f"  Message:    {gen.ascending('message')}")
    print(f"  User:       {gen.ascending('user')}")
    print(f"  Part:       {gen.ascending('part')}")
    print(f"  Permission: {gen.ascending('permission')}")

    print("\nDescending IDs:")
    print(f"  Session:    {gen.descending('session')}")
    print(f"  Message:    {gen.descending('message')}")

    # Test monotonic property
    print("\nMonotonic test (10 consecutive session IDs):")
    ids = [gen.ascending('session') for _ in range(10)]
    for i, id_str in enumerate(ids, 1):
        print(f"  {i:2d}. {id_str}")

    # Verify they're sorted
    is_sorted = ids == sorted(ids)
    print(f"\nIDs are monotonically increasing: {is_sorted}")

    # Test validation
    print("\nPrefix validation:")
    test_id = gen.ascending('session')
    print(f"  ID: {test_id}")
    print(f"  Valid session prefix: {gen.validate_prefix(test_id, 'session')}")
    print(f"  Valid message prefix: {gen.validate_prefix(test_id, 'message')}")

    # Test with given ID
    print("\nUsing existing ID:")
    existing = "ses_18d4f5a3b2c1AbCd1234567890XyZw"
    result = gen.ascending('session', given=existing)
    print(f"  Given:  {existing}")
    print(f"  Result: {result}")
    print(f"  Same:   {existing == result}")

    # Test error handling
    print("\nError handling:")
    try:
        gen.ascending('session', given='msg_wrongprefix')
    except ValueError as e:
        print(f"  ✓ Caught error: {e}")
