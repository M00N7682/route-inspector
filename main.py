from compute_distance import run_analysis

if __name__ == "__main__":
    print("=== Distance Analyzer ===")
    file_name = input("Enter the Excel file name (e.g., F14-05.xlsx): ").strip()

    try:
        run_analysis(file_name)
    except Exception as e:
        print(f"[ERROR] {e}")
        input("Press Enter to exit...")  
