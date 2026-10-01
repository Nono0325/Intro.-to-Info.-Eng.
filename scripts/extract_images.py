import pypdfium2 as pdfium
import os

def render_pages(pdf_path, pages_dict, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    pdf = pdfium.PdfDocument(pdf_path)
    for p_num, name in pages_dict.items():
        if p_num <= len(pdf):
            page = pdf[p_num - 1]
            img = page.render(scale=2).to_pil()
            out_file = os.path.join(out_dir, f"{name}.png")
            img.save(out_file)
            print(f"Saved: {out_file} ({img.size[0]}x{img.size[1]})")

# Module 0
m0_pages = {
    1: "m0_title",
    2: "m0_logistics",
    4: "m0_objectives_bloom",
    9: "m0_grading_policy",
    14: "m0_academic_ethics_ai",
    17: "m0_ai_usage_rules"
}
render_pages("IIE_module_0_syllubus_一甲(5).pdf", m0_pages, "images/module0")

# Module 1
m1_pages = {
    1: "m1_title",
    4: "m1_terminology_pipeline",
    7: "m1_euclidean_algorithm_gcd",
    9: "m1_computing_history_overview",
    15: "m1_nine_big_ideas",
    17: "m1_abstraction_concept",
    21: "m1_programming_pipeline",
    24: "m1_internet_cloud_deepfake",
    25: "m1_impact_ethics_framework",
    27: "m1_google_maps_example"
}
render_pages("IIE_module_1_introduction(5).pdf", m1_pages, "images/module1")

# Module 2
m2_pages = {
    1: "m2_title",
    6: "m2_algorithm_formal_definition",
    11: "m2_origami_example",
    12: "m2_origami_primitives",
    14: "m2_pseudocode_to_python",
    21: "m2_python_function_greetings",
    28: "m2_polya_problem_solving",
    33: "m2_children_age_analysis",
    42: "m2_iteration_vs_recursion_def",
    48: "m2_sequential_search_pseudocode",
    52: "m2_repetitive_control_components",
    53: "m2_insertion_sort_pseudocode",
    54: "m2_insertion_sort_trace",
    58: "m2_binary_search_strategy",
    61: "m2_binary_search_pseudocode",
    62: "m2_recursive_search_concept",
    63: "m2_recursive_trace_1",
    64: "m2_recursive_trace_2",
    71: "m2_insertion_sort_worst_case",
    72: "m2_insertion_sort_graph",
    73: "m2_binary_search_graph",
    77: "m2_big_o_polynomial_theorem",
    80: "m2_complexity_terminology",
    81: "m2_complexity_execution_times",
    83: "m2_chain_problem_3_cuts",
    84: "m2_chain_problem_1_cut",
    87: "m2_loop_invariant_definition",
    88: "m2_loop_invariant_example"
}
render_pages("IIE_module_2_algorithms(7).pdf", m2_pages, "images/module2")

print("Rendering completed!")
