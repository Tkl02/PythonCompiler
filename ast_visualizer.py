import Interpreter.ast_nodes as ast
from Interpreter.token import TokenType
import html

class ASTVisualizer:

    def __init__(self):
        self.html_lines = []

    def generate_html(self, ast_root, file_name= "ast_tree.html"):
        self.html_lines = []
        self._add_header()

        self.html_lines.append('<ul class="tree">')

        if ast_root:
            self.visit(ast_root)
        else:
            self.html_lines.append("<li>AST vazia (possivel erro no parsing)</>")
        
        self.html_lines.append("</ul>")
        self._add_footer()

        try:
            with open(file_name, "w", encoding="utf-8") as f:
                f.write("\n".join(self.html_lines))
            print(f"✓ Arquivo '{file_name}' gerado com sucesso!")
        except Exception as e:
            print(f"✗ Erro ao gerar arquivo: {e}")

    def visit(self, node):
        if node is None:
            self.html_lines.append("<li>(NIL/Vazio)</li>")
            return
        
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)
    
    def generic_visit(self, node):
        self.html_lines.append(f"<li><span>(Nó genérico: {type(node).__name__})</span></li>")

    def _add_leaf(self, name, value):
        safe_value = html.escape(str(value))
        self.html_lines.append(f"<li><span><strong>{name}:</strong> {safe_value}</span></li>")
    
    def visit_NumberNode(self, node: ast.NumberNode):
        self._add_leaf("Number", node.value)

    def visit_StringNode(self, node: ast.StringNode):
        self._add_leaf("String", f'"{node.value}"')

    def visit_BooleanNode(self, node: ast.BooleanNode):
        self._add_leaf("Boolean", "true" if node.value else "false")
    
    def visit_VarAccessNode(self, node: ast.VarAccessNode):
        self._add_leaf("VarAccess", node.var_name_token.value)
    
    def visit_BreakNode(self, node: ast.BreakNode):
        self.html_lines.append("<li><span><strong>Break</strong></span></li>")
    
    def visit_BinOpNode(self, node: ast.BinOpNode):
        self.html_lines.append(f"<li><span><strong>BinOp</strong> {node.op_token.type.name} </span>")
        self.html_lines.append("<ul>")
        self.visit(node.left_node)
        self.visit(node.right_node)
        self.html_lines.append("</ul></li>")

    def visit_UnaryOpNode(self, node: ast.UnaryOpNode):
        self.html_lines.append(f"<li><span><strong>UnaryOp:</strong> {node.op_token.type.name} </span>")
        self.html_lines.append(f"<ul>")
        self.visit(node.expr_node)
        self.html_lines.append("</ul></li>")
    
    def visit_VarAssignNode(self, node: ast.VarAssignNode):
        self.html_lines.append(f"<li><span><strong>Assign</strong> {html.escape(node.var_name_token.value)}</span>")
        self.html_lines.append("<ul>")
        self.html_lines.append("<li><span><em>Value</em></span><ul>")
        self.visit(node.value_node)
        self.html_lines.append("</ul></li>")
        self.html_lines.append("</ul></li>")
    
    def visit_PrintNode(self, node: ast.PrintNode):
        self.html_lines.append("<li><span><strong>Print</strong></span>")
        self.html_lines.append("<ul>")
        self.html_lines.append("<li><span><em>Expr</em></span><ul>")
        self.visit(node.expr_node)
        self.html_lines.append("</ul></li>")
        self.html_lines.append("</ul></li>")
    
    def visit_IfNode(self, node: ast.IfNode):
        self.html_lines.append("<li><span><strong>If</strong></span>")
        self.html_lines.append("<ul>")
        self.html_lines.append("<li><span><em>Condition</em></span><ul>")
        self.visit(node.condition_node)
        self.html_lines.append("</ul></li>")
        self.html_lines.append("<li><span><em>Then Block</em></span><ul>")
        self.visit(node.then_block)
        self.html_lines.append("</ul></li>")
        if node.else_block: # Só adiciona o nó "Else" se ele não for nulo
            self.html_lines.append("<li><span><em>Else Block</em></span><ul>")
            self.visit(node.else_block)
            self.html_lines.append("</ul></li>")
        self.html_lines.append("</ul></li>")
    
    def visit_WhileNode(self, node: ast.WhileNode):
        self.html_lines.append("<li><span><strong>While</strong></span>")
        self.html_lines.append("<ul>")
        self.html_lines.append("<li><span><em>Condition</em></span><ul>")
        self.visit(node.condition_node)
        self.html_lines.append("</ul></li>")
        self.html_lines.append("<li><span><em>Body Block</em></span><ul>")
        self.visit(node.body_node)
        self.html_lines.append("</ul></li>")
        self.html_lines.append("</ul></li>")
    
    def visit_CompoundNode(self, node: ast.CompoundNode):
        if not node or not node.children:
            self.html_lines.append("<li><span>Compound (Vazio)</span></li>")
            return
            
        self.html_lines.append("<li><span><strong>Compound (Bloco)</strong></span>")
        self.html_lines.append("<ul>")
        for child in node.children:
            self.visit(child)
        self.html_lines.append("</ul></li>")
    
    def _add_header(self):
        self.html_lines.append("<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\" />")
        self.html_lines.append("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />")
        self.html_lines.append("<title>Visualização da AST</title>")
        self.html_lines.append("<style>")
        self.html_lines.append(
            """
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #333;
                padding: 20px;
                margin: 0;
                min-height: 100vh;
            }
            
            h1 {
                color: white;
                text-align: center;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                margin-bottom: 30px;
            }
            
            .tree-container {
                background: white;
                border-radius: 10px;
                padding: 30px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.2);
                overflow-x: auto;
                max-width: 100%;
            }
            
            .tree, .tree ul, .tree li {
                list-style: none;
                margin: 0;
                padding: 0;
                position: relative;
            }
            
            .tree {
                margin: 20px 0;
                text-align: center;
                min-width: max-content;
            }
            
            .tree ul {
                padding-top: 20px;
                position: relative;
                transition: all 0.3s;
                display: flex;
                justify-content: center;
                gap: 10px;
            }
            
            .tree li {
                display: inline-block;
                text-align: center;
                padding: 0 10px;
                position: relative;
                vertical-align: top;
            }
            
            /* Linhas conectoras */
            .tree li::before,
            .tree li::after {
                content: '';
                position: absolute;
                top: -10px;
                right: 50%;
                border-top: 2px solid #667eea;
                width: 50%;
                height: 10px;
            }
            
            .tree li::after {
                right: auto;
                left: 50%;
                border-left: 2px solid #667eea;
            }
            
            .tree li:only-child::after,
            .tree li:only-child::before {
                display: none;
            }
            
            .tree li:only-child {
                padding-top: 0;
            }
            
            .tree li:first-child::before,
            .tree li:last-child::after {
                border: 0 none;
            }
            
            .tree li:last-child::before {
                border-right: 2px solid #667eea;
                border-radius: 0 5px 0 0;
            }
            
            .tree li:first-child::after {
                border-radius: 5px 0 0 0;
            }
            
            /* Linha vertical do pai */
            .tree ul ul::before {
                content: '';
                position: absolute;
                top: -10px;
                left: 50%;
                border-left: 2px solid #667eea;
                width: 0;
                height: 10px;
            }
            
            /* Remover linhas no nó raiz */
            .tree > li {
                margin-top: 0;
            }
            
            .tree > li::before,
            .tree > li::after {
                border: 0 none;
            }
            
            /* Estilo dos nós */
            .tree span {
                border: 2px solid #667eea;
                border-radius: 8px;
                display: inline-block;
                padding: 8px 15px;
                position: relative;
                background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
                box-shadow: 0 3px 10px rgba(102, 126, 234, 0.2);
                transition: all 0.3s ease;
                cursor: default;
                white-space: nowrap;
                max-width: 300px;
                overflow: hidden;
                text-overflow: ellipsis;
            }
            
            .tree span:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
                z-index: 10;
            }
            
            /* Rótulos (ex: "Condition", "Value") */
            .tree span em {
                font-style: normal;
                font-weight: 600;
                color: #4a5568;
                font-size: 0.85em;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }
            
            /* Nomes dos Nós (ex: "If", "BinOp") */
            .tree span strong {
                color: #667eea;
                font-weight: bold;
                font-size: 1em;
            }
            
            /* Tipos diferentes de nós */
            .tree .node-if strong { color: #f093fb; }
            .tree .node-while strong { color: #4facfe; }
            .tree .node-print strong { color: #43e97b; }
            .tree .node-binop strong { color: #fa709a; }
            .tree .node-assign strong { color: #feca57; }
            .tree .node-number strong { color: #48dbfb; }
            .tree .node-string strong { color: #ff9ff3; }
            .tree .node-boolean strong { color: #54a0ff; }
            
            /* Melhorar legibilidade em estruturas profundas */
            .tree ul ul ul {
                padding-top: 25px;
            }
            
            .tree ul ul ul span {
                font-size: 0.95em;
                padding: 6px 12px;
            }
            
            .tree ul ul ul ul span {
                font-size: 0.9em;
                padding: 5px 10px;
            }
            
            /* Scrollbar customizada */
            .tree-container::-webkit-scrollbar {
                height: 10px;
            }
            
            .tree-container::-webkit-scrollbar-track {
                background: #f1f1f1;
                border-radius: 5px;
            }
            
            .tree-container::-webkit-scrollbar-thumb {
                background: #667eea;
                border-radius: 5px;
            }
            
            .tree-container::-webkit-scrollbar-thumb:hover {
                background: #764ba2;
            }
            """
        )
        self.html_lines.append("</style></head><body>")
        self.html_lines.append("<h1>🌳 Visualização da Árvore Sintática Abstrata (AST)</h1>")
        self.html_lines.append("<div class=\"tree-container\">")

    def _add_footer(self):
        self.html_lines.append("</div>")
        self.html_lines.append("<script>")
        self.html_lines.append("""
            // Adicionar classes CSS baseadas no tipo de nó
            document.addEventListener('DOMContentLoaded', function() {
                document.querySelectorAll('.tree span').forEach(function(span) {
                    const text = span.textContent.toLowerCase();
                    if (text.includes('if')) span.classList.add('node-if');
                    else if (text.includes('while')) span.classList.add('node-while');
                    else if (text.includes('print')) span.classList.add('node-print');
                    else if (text.includes('binop')) span.classList.add('node-binop');
                    else if (text.includes('assign')) span.classList.add('node-assign');
                    else if (text.includes('number')) span.classList.add('node-number');
                    else if (text.includes('string')) span.classList.add('node-string');
                    else if (text.includes('boolean')) span.classList.add('node-boolean');
                });
            });
        """)
        self.html_lines.append("</script>")
        self.html_lines.append("</body></html>")