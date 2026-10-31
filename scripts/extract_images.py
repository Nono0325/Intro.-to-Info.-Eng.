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

# Module 3
m3_pages = {
    1: "m3_title",
    4: "m3_assembly_language_mnemonics",
    6: "m3_machine_vs_assembly_code",
    7: "m3_python_vs_arm_assembly",
    9: "m3_language_generations",
    10: "m3_programming_paradigms",
    11: "m3_paradigm_evolution",
    12: "m3_functional_checkbook_example",
    15: "m3_imperative_unit_structure",
    19: "m3_2d_array_row_major",
    21: "m3_python_2d_array",
    22: "m3_struct_employee_concept",
    23: "m3_python_struct_class",
    25: "m3_goto_vs_structured_control",
    29: "m3_python_match_case",
    30: "m3_for_loop_structure",
    35: "m3_function_control_flow",
    36: "m3_c_project_population",
    37: "m3_python_project_population",
    38: "m3_call_by_value_1",
    39: "m3_call_by_value_2",
    40: "m3_call_by_value_3",
    41: "m3_call_by_reference_1",
    42: "m3_call_by_reference_2",
    43: "m3_call_by_reference_3",
    44: "m3_c_cylinder_volume",
    45: "m3_python_cylinder_volume",
    48: "m3_oop_laser_gun_class",
    50: "m3_oop_program_structure",
    51: "m3_oop_constructor",
    52: "m3_oop_encapsulation_integrity",
    53: "m3_oop_java_laser_class",
    54: "m3_python_laser_class",
    55: "m3_oop_inheritance_polymorphism_def",
    56: "m3_python_inheritance",
    57: "m3_python_overloading",
    58: "m3_python_overriding",
    60: "m3_summary"
}
render_pages("IIE_module_3_programming_languages(12).pdf", m3_pages, "images/module3")

print("Rendering completed!")

