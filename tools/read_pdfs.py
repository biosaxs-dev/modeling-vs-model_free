import sys

try:
    from pypdf import PdfReader
    print("pypdf imported successfully", flush=True)
    
    # Read Paper 1
    print("Reading Paper 1...", flush=True)
    reader1 = PdfReader(r'E:\GitHub\modeling-vs-model_free\reference_papers\2021, Steve P. Meisburger.pdf')
    text1 = '\n'.join([page.extract_text() for page in reader1.pages])
    print(f"Paper 1: {len(reader1.pages)} pages, {len(text1)} chars", flush=True)
    
    # Read Paper 2
    print("Reading Paper 2...", flush=True)
    reader2 = PdfReader(r'E:\GitHub\modeling-vs-model_free\reference_papers\2024, Griffin Chure.pdf')
    text2 = '\n'.join([page.extract_text() for page in reader2.pages])
    print(f"Paper 2: {len(reader2.pages)} pages, {len(text2)} chars", flush=True)
    
    # Write to file in tools folder
    print("Writing to file...", flush=True)
    with open(r'E:\GitHub\modeling-vs-model_free\tools\extracted_papers.txt', 'w', encoding='utf-8') as f:
        f.write("PAPER 1: 2021, Steve P. Meisburger\n")
        f.write("=" * 80 + "\n\n")
        f.write(text1)
        f.write("\n\n\n")
        f.write("PAPER 2: 2024, Griffin Chure\n")
        f.write("=" * 80 + "\n\n")
        f.write(text2)
    
    print("SUCCESS! Saved to tools/extracted_papers.txt", flush=True)
    
except Exception as e:
    print(f"ERROR: {e}", file=sys.stderr, flush=True)
    import traceback
    traceback.print_exc()
    sys.exit(1)
