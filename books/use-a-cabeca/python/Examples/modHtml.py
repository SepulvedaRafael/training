import html

# Codificando os sinais de maiores ou menores
print(html.escape('Esse fragmento de HTML contém uma tag <script>script</script>.'))
print(html.unescape('Eu &hearts; Python &lt;e suas bibliotecas padrões&gt;.'))