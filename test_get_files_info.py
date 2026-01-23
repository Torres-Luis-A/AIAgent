from functions.get_files_info import get_files_info

def test_get_files_info():
    result_dir = get_files_info("calculator", ".")
    result_pkg = get_files_info("calculator", "pkg")
    result_bin = get_files_info("calculator", "/bin")
    result_outside = get_files_info("calculator", "../")
    print("Result for current directory:")
    print(result_dir)
    print("Result for 'pkg' directory:")
    print(result_pkg)
    print("Result for '/bin' directory:")
    print(result_bin)
    print("Result for '../' directory:")
    print(result_outside)
    return result_dir, result_pkg, result_bin, result_outside

if __name__ == "__main__":
    test_get_files_info()

