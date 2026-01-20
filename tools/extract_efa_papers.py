import sys
import os

try:
    from pypdf import PdfReader
    print("pypdf imported successfully", flush=True)
    
    # Get the script directory and construct paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.dirname(script_dir)
    ref_dir = os.path.join(repo_dir, 'reference_papers')
    
    # Read Paper 1 - Maeder 1988
    print("Reading Maeder 1988...", flush=True)
    pdf1_path = os.path.join(ref_dir, '1988, Marcel Maeder.pdf')
    reader1 = PdfReader(pdf1_path)
    text1 = '\n'.join([page.extract_text() for page in reader1.pages])
    print(f"Maeder 1988: {len(reader1.pages)} pages, {len(text1)} chars", flush=True)
    
    # Read Paper 2 - Keller 1991
    print("Reading Keller 1991...", flush=True)
    pdf2_path = os.path.join(ref_dir, '1991, H.R. Keller.pdf')
    reader2 = PdfReader(pdf2_path)
    text2 = '\n'.join([page.extract_text() for page in reader2.pages])
    print(f"Keller 1991: {len(reader2.pages)} pages, {len(text2)} chars", flush=True)
    
    # Write to file in tools folder
    print("Writing to efa_papers.txt...", flush=True)
    output_path = os.path.join(script_dir, 'efa_papers.txt')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("PAPER 1: Maeder & Zilian (1988) - EFA Original Paper\n")
        f.write("=" * 80 + "\n")
        f.write("Title: Evolving factor analysis, a new multivariate technique in chromatography\n")
        f.write("Journal: Chemometrics and Intelligent Laboratory Systems, 3, 205-213\n")
        f.write("=" * 80 + "\n\n")
        f.write(text1)
        f.write("\n\n\n")
        f.write("PAPER 2: Keller & Massart (1991) - EFA Tutorial\n")
        f.write("=" * 80 + "\n")
        f.write("Title: Evolving factor analysis\n")
        f.write("Journal: Chemometrics and Intelligent Laboratory Systems, 12, 209-224\n")
        f.write("=" * 80 + "\n\n")
        f.write(text2)
    
    print(f"SUCCESS! Saved to {output_path}", flush=True)
    
except Exception as e:
    print(f"ERROR: {e}", file=sys.stderr, flush=True)
    import traceback
    traceback.print_exc()
    sys.exit(1)
