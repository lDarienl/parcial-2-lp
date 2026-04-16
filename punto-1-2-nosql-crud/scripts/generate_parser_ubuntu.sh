# Configuración de rutas
ROOT_DIR=$(pwd)
JAR_URL="https://repo1.maven.org/maven2/org/antlr/antlr4/4.13.2/antlr4-4.13.2-complete.jar"
JAR_PATH="$ROOT_DIR/tools/antlr-4.13.2-complete.jar"
OUT_DIR="$ROOT_DIR/src/nosql_dsl/generated"
GRAMMAR="$ROOT_DIR/grammar/grammar1.g4"

# Crear carpetas si no existen
mkdir -p "$ROOT_DIR/tools"
mkdir -p "$OUT_DIR"

# Descargar el JAR de ANTLR si no está
if [ ! -f "$JAR_PATH" ]; then
    echo "Descargando ANTLR..."
    curl -L "$JAR_URL" -o "$JAR_PATH"
fi

# Generar código Python
echo "Generando Lexer, Parser y Visitor..."
java -jar "$JAR_PATH" -Dlanguage=Python3 -visitor -listener -o "$OUT_DIR" -Xexact-output-dir "$GRAMMAR"

echo "¡Listo!"