import tree_o as tree
import busca_p as busca

# Construindo a árvore
arvore = tree.Arvore_o("A")
arvore.add_child(tree.Arvore_o("B"))
arvore.children[0].add_child(tree.Arvore_o("D"))
arvore.children[0].children[0].add_child(tree.Arvore_o("H"))
arvore.children[0].children[0].add_child(tree.Arvore_o("I"))
arvore.add_child(tree.Arvore_o("E"))
arvore.children[1].add_child(tree.Arvore_o("J"))
arvore.children[1].children[0].add_child(tree.Arvore_o("N"))
arvore.children[1].children[0].add_child(tree.Arvore_o("O"))
arvore.add_child(tree.Arvore_o("C"))
arvore.children[2].add_child(tree.Arvore_o("F"))
arvore.children[2].children[0].add_child(tree.Arvore_o("K"))
arvore.children[2].add_child(tree.Arvore_o("G"))
arvore.children[2].children[1].add_child(tree.Arvore_o("L"))
arvore.children[2].children[1].add_child(tree.Arvore_o("M"))

# Imprimindo a árvore
print(arvore)

# Exemplo de uso:
element_to_search = "K"  # Elemento que você deseja procurar na árvore
result = busca.search_arvore(arvore, element_to_search)

if result:
    print(f"O elemento '{element_to_search}' foi encontrado na árvore.")
else:
    print(f"O elemento '{element_to_search}' não foi encontrado na árvore.")

# Destruir a árvore com uma mensagem
print(f"A árvore com raiz '{arvore.data}' foi destruída.")
arvore = None  # Isso efetivamente remove a referência à árvore