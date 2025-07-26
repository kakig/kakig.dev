# Classic calculation style
#
# text_size = 1.125
#
# minor_second = 1.067
# major_second = 1.125
# minor_third = 1.2
# major_third = 1.25
# perfect_fourth = 1.333
# augmented_fourth = 1.414
# perfect_fifth = 1.5
# golden_ratio = 1.618
#
# multiplier = major_third
#
# small = text_size / multiplier
# p = text_size
# h6 = text_size * multiplier
# h5 = h6 * multiplier
# h4 = h5 * multiplier
# h3 = h4 * multiplier
# h2 = h3 * multiplier
# h1 = h2 * multiplier
#
# print(f"small: {small:.3f}rem")
# print(f"    p: {p:.3f}rem")
# print(f"   h6: {h6:.3f}rem")
# print(f"   h5: {h5:.3f}rem")
# print(f"   h4: {h4:.3f}rem")
# print(f"   h3: {h3:.3f}rem")
# print(f"   h2: {h2:.3f}rem")
# print(f"   h1: {h1:.3f}rem")
#
# print()
#
# print(f"""
# CSS:
# h1 {{ font-size: {h1:.4f}em; }}
# h2 {{ font-size: {h2:.4f}em; }}
# h3 {{ font-size: {h3:.4f}em; }}
# h4 {{ font-size: {h4:.4f}em; }}
# h5 {{ font-size: {h5:.4f}em; }}
# h6 {{ font-size: {h6:.4f}em; }}
# small {{ font-size: {small:.4f}em; }}
#
# html {{
#   font-size: {text_size:.4f}em;
#   font-family: 'Liberation Sans';
# }}
# """.strip())
#
#
# """
# /* html {{ font-size: clamp(1em, .4167vw + .8875em, 1.125em); }}
#
# h1, h2, h3, h4, h5, h6 {{
#     font-weight: normal;
#     }} */
# """


