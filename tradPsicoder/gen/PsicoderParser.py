# Generated from C:/Users/a-zam/OneDrive/Documentos/Universidad/Lenguajes de programacion/traductor/TraductorPsicoder/tradPsicoder/grammar\Psicoder.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u0159\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \3\2\3\2\7\2C\n\2\f\2\16\2F\13\2\3\2\3")
        buf.write("\2\3\2\7\2K\n\2\f\2\16\2N\13\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6k\n\6\f\6\16\6n\13\6")
        buf.write("\3\6\5\6q\n\6\3\7\3\7\3\7\7\7v\n\7\f\7\16\7y\13\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u0083\n\b\f\b\16\b\u0086")
        buf.write("\13\b\3\b\3\b\3\t\3\t\3\t\5\t\u008d\n\t\3\n\3\n\3\n\3")
        buf.write("\n\5\n\u0093\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u009f\n\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\5\r\u00ad\n\r\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u00b3\n\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u00e0\n\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\5\27\u00f7\n\27\3")
        buf.write("\27\3\27\7\27\u00fb\n\27\f\27\16\27\u00fe\13\27\3\27\3")
        buf.write("\27\3\27\3\30\3\30\3\30\5\30\u0106\n\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\7\32\u0111\n\32\f\32\16")
        buf.write("\32\u0114\13\32\3\32\5\32\u0117\n\32\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0123\n\33\3\33")
        buf.write("\3\33\3\33\7\33\u0128\n\33\f\33\16\33\u012b\13\33\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0142")
        buf.write("\n\36\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u014a\n\36\f")
        buf.write("\36\16\36\u014d\13\36\3\37\3\37\3 \3 \3 \7 \u0154\n \f")
        buf.write(" \16 \u0157\13 \3 \2\4\64:!\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>\2\4\4\2\61\61\65")
        buf.write("\65\5\2\22\22\36!\65\65\2\u0164\2D\3\2\2\2\4Q\3\2\2\2")
        buf.write("\6U\3\2\2\2\b`\3\2\2\2\np\3\2\2\2\fr\3\2\2\2\16|\3\2\2")
        buf.write("\2\20\u008c\3\2\2\2\22\u0092\3\2\2\2\24\u009e\3\2\2\2")
        buf.write("\26\u00a0\3\2\2\2\30\u00ac\3\2\2\2\32\u00ae\3\2\2\2\34")
        buf.write("\u00bd\3\2\2\2\36\u00c1\3\2\2\2 \u00c9\3\2\2\2\"\u00d1")
        buf.write("\3\2\2\2$\u00df\3\2\2\2&\u00e1\3\2\2\2(\u00e7\3\2\2\2")
        buf.write("*\u00ec\3\2\2\2,\u00f2\3\2\2\2.\u0105\3\2\2\2\60\u0107")
        buf.write("\3\2\2\2\62\u0116\3\2\2\2\64\u0122\3\2\2\2\66\u012c\3")
        buf.write("\2\2\28\u0130\3\2\2\2:\u0141\3\2\2\2<\u014e\3\2\2\2>\u0150")
        buf.write("\3\2\2\2@C\5\6\4\2AC\5\f\7\2B@\3\2\2\2BA\3\2\2\2CF\3\2")
        buf.write("\2\2DB\3\2\2\2DE\3\2\2\2EG\3\2\2\2FD\3\2\2\2GL\5\4\3\2")
        buf.write("HK\5\6\4\2IK\5\f\7\2JH\3\2\2\2JI\3\2\2\2KN\3\2\2\2LJ\3")
        buf.write("\2\2\2LM\3\2\2\2MO\3\2\2\2NL\3\2\2\2OP\7\2\2\3P\3\3\2")
        buf.write("\2\2QR\7\3\2\2RS\5\22\n\2ST\7\4\2\2T\5\3\2\2\2UV\7\5\2")
        buf.write("\2VW\5<\37\2WX\7\65\2\2XY\7&\2\2YZ\5\n\6\2Z[\7\'\2\2[")
        buf.write("\\\7\6\2\2\\]\5\22\n\2]^\5\b\5\2^_\7\7\2\2_\7\3\2\2\2")
        buf.write("`a\7\b\2\2ab\5:\36\2bc\7,\2\2c\t\3\2\2\2de\5<\37\2el\7")
        buf.write("\65\2\2fg\7-\2\2gh\5<\37\2hi\7\65\2\2ik\3\2\2\2jf\3\2")
        buf.write("\2\2kn\3\2\2\2lj\3\2\2\2lm\3\2\2\2mq\3\2\2\2nl\3\2\2\2")
        buf.write("oq\3\2\2\2pd\3\2\2\2po\3\2\2\2q\13\3\2\2\2rs\7\t\2\2s")
        buf.write("w\7\65\2\2tv\5\16\b\2ut\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx")
        buf.write("\3\2\2\2xz\3\2\2\2yw\3\2\2\2z{\7\n\2\2{\r\3\2\2\2|}\5")
        buf.write("<\37\2}~\7\65\2\2~\u0084\5\20\t\2\177\u0080\7-\2\2\u0080")
        buf.write("\u0081\7\65\2\2\u0081\u0083\5\20\t\2\u0082\177\3\2\2\2")
        buf.write("\u0083\u0086\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0085\3")
        buf.write("\2\2\2\u0085\u0087\3\2\2\2\u0086\u0084\3\2\2\2\u0087\u0088")
        buf.write("\7,\2\2\u0088\17\3\2\2\2\u0089\u008a\7\13\2\2\u008a\u008d")
        buf.write("\5:\36\2\u008b\u008d\3\2\2\2\u008c\u0089\3\2\2\2\u008c")
        buf.write("\u008b\3\2\2\2\u008d\21\3\2\2\2\u008e\u008f\5\24\13\2")
        buf.write("\u008f\u0090\5\22\n\2\u0090\u0093\3\2\2\2\u0091\u0093")
        buf.write("\3\2\2\2\u0092\u008e\3\2\2\2\u0092\u0091\3\2\2\2\u0093")
        buf.write("\23\3\2\2\2\u0094\u009f\5\26\f\2\u0095\u009f\5\32\16\2")
        buf.write("\u0096\u009f\5 \21\2\u0097\u009f\5\36\20\2\u0098\u009f")
        buf.write("\5\"\22\2\u0099\u009f\5\16\b\2\u009a\u009f\5(\25\2\u009b")
        buf.write("\u009f\5*\26\2\u009c\u009f\5,\27\2\u009d\u009f\5\60\31")
        buf.write("\2\u009e\u0094\3\2\2\2\u009e\u0095\3\2\2\2\u009e\u0096")
        buf.write("\3\2\2\2\u009e\u0097\3\2\2\2\u009e\u0098\3\2\2\2\u009e")
        buf.write("\u0099\3\2\2\2\u009e\u009a\3\2\2\2\u009e\u009b\3\2\2\2")
        buf.write("\u009e\u009c\3\2\2\2\u009e\u009d\3\2\2\2\u009f\25\3\2")
        buf.write("\2\2\u00a0\u00a1\7\f\2\2\u00a1\u00a2\7&\2\2\u00a2\u00a3")
        buf.write("\5\64\33\2\u00a3\u00a4\7\'\2\2\u00a4\u00a5\7\r\2\2\u00a5")
        buf.write("\u00a6\5\22\n\2\u00a6\u00a7\5\30\r\2\u00a7\u00a8\7\16")
        buf.write("\2\2\u00a8\27\3\2\2\2\u00a9\u00aa\7\17\2\2\u00aa\u00ad")
        buf.write("\5\22\n\2\u00ab\u00ad\3\2\2\2\u00ac\u00a9\3\2\2\2\u00ac")
        buf.write("\u00ab\3\2\2\2\u00ad\31\3\2\2\2\u00ae\u00af\7\20\2\2\u00af")
        buf.write("\u00b2\7&\2\2\u00b0\u00b3\5(\25\2\u00b1\u00b3\5\34\17")
        buf.write("\2\u00b2\u00b0\3\2\2\2\u00b2\u00b1\3\2\2\2\u00b3\u00b4")
        buf.write("\3\2\2\2\u00b4\u00b5\7,\2\2\u00b5\u00b6\5\64\33\2\u00b6")
        buf.write("\u00b7\7,\2\2\u00b7\u00b8\t\2\2\2\u00b8\u00b9\7\'\2\2")
        buf.write("\u00b9\u00ba\7\6\2\2\u00ba\u00bb\5\22\n\2\u00bb\u00bc")
        buf.write("\7\21\2\2\u00bc\33\3\2\2\2\u00bd\u00be\7\22\2\2\u00be")
        buf.write("\u00bf\7\65\2\2\u00bf\u00c0\5\20\t\2\u00c0\35\3\2\2\2")
        buf.write("\u00c1\u00c2\7\6\2\2\u00c2\u00c3\5\22\n\2\u00c3\u00c4")
        buf.write("\7\23\2\2\u00c4\u00c5\7&\2\2\u00c5\u00c6\5\64\33\2\u00c6")
        buf.write("\u00c7\7\'\2\2\u00c7\u00c8\7,\2\2\u00c8\37\3\2\2\2\u00c9")
        buf.write("\u00ca\7\23\2\2\u00ca\u00cb\7&\2\2\u00cb\u00cc\5\64\33")
        buf.write("\2\u00cc\u00cd\7\'\2\2\u00cd\u00ce\7\6\2\2\u00ce\u00cf")
        buf.write("\5\22\n\2\u00cf\u00d0\7\24\2\2\u00d0!\3\2\2\2\u00d1\u00d2")
        buf.write("\7\25\2\2\u00d2\u00d3\7&\2\2\u00d3\u00d4\7\65\2\2\u00d4")
        buf.write("\u00d5\7\'\2\2\u00d5\u00d6\7\26\2\2\u00d6\u00d7\5$\23")
        buf.write("\2\u00d7\u00d8\7\27\2\2\u00d8#\3\2\2\2\u00d9\u00da\5&")
        buf.write("\24\2\u00da\u00db\5$\23\2\u00db\u00e0\3\2\2\2\u00dc\u00dd")
        buf.write("\7\30\2\2\u00dd\u00de\7\31\2\2\u00de\u00e0\5\22\n\2\u00df")
        buf.write("\u00d9\3\2\2\2\u00df\u00dc\3\2\2\2\u00e0%\3\2\2\2\u00e1")
        buf.write("\u00e2\7\32\2\2\u00e2\u00e3\5:\36\2\u00e3\u00e4\7\31\2")
        buf.write("\2\u00e4\u00e5\5\22\n\2\u00e5\u00e6\5.\30\2\u00e6\'\3")
        buf.write("\2\2\2\u00e7\u00e8\5> \2\u00e8\u00e9\7\13\2\2\u00e9\u00ea")
        buf.write("\5:\36\2\u00ea\u00eb\7,\2\2\u00eb)\3\2\2\2\u00ec\u00ed")
        buf.write("\7\33\2\2\u00ed\u00ee\7&\2\2\u00ee\u00ef\5> \2\u00ef\u00f0")
        buf.write("\7\'\2\2\u00f0\u00f1\7,\2\2\u00f1+\3\2\2\2\u00f2\u00f3")
        buf.write("\7\34\2\2\u00f3\u00f6\7&\2\2\u00f4\u00f7\5:\36\2\u00f5")
        buf.write("\u00f7\5\60\31\2\u00f6\u00f4\3\2\2\2\u00f6\u00f5\3\2\2")
        buf.write("\2\u00f7\u00fc\3\2\2\2\u00f8\u00f9\7-\2\2\u00f9\u00fb")
        buf.write("\5:\36\2\u00fa\u00f8\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00ff\3\2\2\2")
        buf.write("\u00fe\u00fc\3\2\2\2\u00ff\u0100\7\'\2\2\u0100\u0101\7")
        buf.write(",\2\2\u0101-\3\2\2\2\u0102\u0103\7\35\2\2\u0103\u0106")
        buf.write("\7,\2\2\u0104\u0106\3\2\2\2\u0105\u0102\3\2\2\2\u0105")
        buf.write("\u0104\3\2\2\2\u0106/\3\2\2\2\u0107\u0108\7\65\2\2\u0108")
        buf.write("\u0109\7&\2\2\u0109\u010a\5\62\32\2\u010a\u010b\7\'\2")
        buf.write("\2\u010b\u010c\7,\2\2\u010c\61\3\2\2\2\u010d\u0112\5:")
        buf.write("\36\2\u010e\u010f\7-\2\2\u010f\u0111\5:\36\2\u0110\u010e")
        buf.write("\3\2\2\2\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113\u0117\3\2\2\2\u0114\u0112\3\2\2\2")
        buf.write("\u0115\u0117\3\2\2\2\u0116\u010d\3\2\2\2\u0116\u0115\3")
        buf.write("\2\2\2\u0117\63\3\2\2\2\u0118\u0119\b\33\1\2\u0119\u0123")
        buf.write("\5\66\34\2\u011a\u0123\58\35\2\u011b\u011c\7&\2\2\u011c")
        buf.write("\u011d\5\64\33\2\u011d\u011e\7\'\2\2\u011e\u0123\3\2\2")
        buf.write("\2\u011f\u0120\7(\2\2\u0120\u0123\5\64\33\4\u0121\u0123")
        buf.write("\5:\36\2\u0122\u0118\3\2\2\2\u0122\u011a\3\2\2\2\u0122")
        buf.write("\u011b\3\2\2\2\u0122\u011f\3\2\2\2\u0122\u0121\3\2\2\2")
        buf.write("\u0123\u0129\3\2\2\2\u0124\u0125\f\b\2\2\u0125\u0126\7")
        buf.write("+\2\2\u0126\u0128\5\64\33\t\u0127\u0124\3\2\2\2\u0128")
        buf.write("\u012b\3\2\2\2\u0129\u0127\3\2\2\2\u0129\u012a\3\2\2\2")
        buf.write("\u012a\65\3\2\2\2\u012b\u0129\3\2\2\2\u012c\u012d\5:\36")
        buf.write("\2\u012d\u012e\7*\2\2\u012e\u012f\5:\36\2\u012f\67\3\2")
        buf.write("\2\2\u0130\u0131\5:\36\2\u0131\u0132\7)\2\2\u0132\u0133")
        buf.write("\5:\36\2\u01339\3\2\2\2\u0134\u0135\b\36\1\2\u0135\u0136")
        buf.write("\7&\2\2\u0136\u0137\5:\36\2\u0137\u0138\7\'\2\2\u0138")
        buf.write("\u0142\3\2\2\2\u0139\u0142\5\60\31\2\u013a\u0142\5> \2")
        buf.write("\u013b\u0142\7\60\2\2\u013c\u0142\7\61\2\2\u013d\u0142")
        buf.write("\7\64\2\2\u013e\u0142\7\62\2\2\u013f\u0142\7\65\2\2\u0140")
        buf.write("\u0142\7\63\2\2\u0141\u0134\3\2\2\2\u0141\u0139\3\2\2")
        buf.write("\2\u0141\u013a\3\2\2\2\u0141\u013b\3\2\2\2\u0141\u013c")
        buf.write("\3\2\2\2\u0141\u013d\3\2\2\2\u0141\u013e\3\2\2\2\u0141")
        buf.write("\u013f\3\2\2\2\u0141\u0140\3\2\2\2\u0142\u014b\3\2\2\2")
        buf.write("\u0143\u0144\f\r\2\2\u0144\u0145\7.\2\2\u0145\u014a\5")
        buf.write(":\36\16\u0146\u0147\f\f\2\2\u0147\u0148\7/\2\2\u0148\u014a")
        buf.write("\5:\36\r\u0149\u0143\3\2\2\2\u0149\u0146\3\2\2\2\u014a")
        buf.write("\u014d\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2")
        buf.write("\u014c;\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u014f\t\3\2")
        buf.write("\2\u014f=\3\2\2\2\u0150\u0155\7\65\2\2\u0151\u0152\7\"")
        buf.write("\2\2\u0152\u0154\7\65\2\2\u0153\u0151\3\2\2\2\u0154\u0157")
        buf.write("\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156")
        buf.write("?\3\2\2\2\u0157\u0155\3\2\2\2\33BDJLlpw\u0084\u008c\u0092")
        buf.write("\u009e\u00ac\u00b2\u00df\u00f6\u00fc\u0105\u0112\u0116")
        buf.write("\u0122\u0129\u0141\u0149\u014b\u0155")
        return buf.getvalue()


class PsicoderParser ( Parser ):

    grammarFileName = "Psicoder.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'funcion_principal'", "'fin_principal'", 
                     "'funcion'", "'hacer'", "'fin_funcion'", "'retornar'", 
                     "'estructura'", "'fin_estructura'", "'='", "'si'", 
                     "'entonces'", "'fin_si'", "'si_no'", "'para'", "'fin_para'", 
                     "'entero'", "'mientras'", "'fin_mientras'", "'seleccionar'", 
                     "'entre'", "'fin_seleccionar'", "'defecto'", "':'", 
                     "'caso'", "'leer'", "'imprimir'", "'romper'", "'caracter'", 
                     "'cadena'", "'real'", "'booleano'", "'.'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "'!'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMMENT", "LINE_COMMENT", "WS", "PIZQ", 
                      "PDER", "NEG", "ROI", "ROP", "ROL", "SMCOLON", "COMA", 
                      "MULOP", "SUMOP", "DOUBLE", "INT", "STRING", "BOOLEANO", 
                      "CONST", "ID" ]

    RULE_s = 0
    RULE_funcion_principal = 1
    RULE_funcion = 2
    RULE_retornar = 3
    RULE_parametros = 4
    RULE_estructura = 5
    RULE_declaracion = 6
    RULE_asignacion = 7
    RULE_comandos = 8
    RULE_comando = 9
    RULE_si = 10
    RULE_si_no = 11
    RULE_para = 12
    RULE_asignacion_entero = 13
    RULE_hacer_mientras = 14
    RULE_mientras = 15
    RULE_seleccionar = 16
    RULE_casos = 17
    RULE_caso = 18
    RULE_asignacion_id = 19
    RULE_leer = 20
    RULE_imprimir = 21
    RULE_romper = 22
    RULE_llamar_funcion = 23
    RULE_pasar_parametros = 24
    RULE_expresion_logica = 25
    RULE_expresion_rop = 26
    RULE_expresion_roi = 27
    RULE_expr = 28
    RULE_tipo = 29
    RULE_id_pos_estruct = 30

    ruleNames =  [ "s", "funcion_principal", "funcion", "retornar", "parametros", 
                   "estructura", "declaracion", "asignacion", "comandos", 
                   "comando", "si", "si_no", "para", "asignacion_entero", 
                   "hacer_mientras", "mientras", "seleccionar", "casos", 
                   "caso", "asignacion_id", "leer", "imprimir", "romper", 
                   "llamar_funcion", "pasar_parametros", "expresion_logica", 
                   "expresion_rop", "expresion_roi", "expr", "tipo", "id_pos_estruct" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    COMMENT=33
    LINE_COMMENT=34
    WS=35
    PIZQ=36
    PDER=37
    NEG=38
    ROI=39
    ROP=40
    ROL=41
    SMCOLON=42
    COMA=43
    MULOP=44
    SUMOP=45
    DOUBLE=46
    INT=47
    STRING=48
    BOOLEANO=49
    CONST=50
    ID=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcion_principal(self):
            return self.getTypedRuleContext(PsicoderParser.Funcion_principalContext,0)


        def EOF(self):
            return self.getToken(PsicoderParser.EOF, 0)

        def funcion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PsicoderParser.FuncionContext)
            else:
                return self.getTypedRuleContext(PsicoderParser.FuncionContext,i)


        def estructura(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PsicoderParser.EstructuraContext)
            else:
                return self.getTypedRuleContext(PsicoderParser.EstructuraContext,i)


        def getRuleIndex(self):
            return PsicoderParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = PsicoderParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PsicoderParser.T__2 or _la==PsicoderParser.T__6:
                self.state = 64
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [PsicoderParser.T__2]:
                    self.state = 62
                    self.funcion()
                    pass
                elif token in [PsicoderParser.T__6]:
                    self.state = 63
                    self.estructura()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self.funcion_principal()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PsicoderParser.T__2 or _la==PsicoderParser.T__6:
                self.state = 72
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [PsicoderParser.T__2]:
                    self.state = 70
                    self.funcion()
                    pass
                elif token in [PsicoderParser.T__6]:
                    self.state = 71
                    self.estructura()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
            self.match(PsicoderParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcion_principalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comandos(self):
            return self.getTypedRuleContext(PsicoderParser.ComandosContext,0)


        def getRuleIndex(self):
            return PsicoderParser.RULE_funcion_principal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion_principal" ):
                listener.enterFuncion_principal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion_principal" ):
                listener.exitFuncion_principal(self)




    def funcion_principal(self):

        localctx = PsicoderParser.Funcion_principalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcion_principal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(PsicoderParser.T__0)
            self.state = 80
            self.comandos()
            self.state = 81
            self.match(PsicoderParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(PsicoderParser.TipoContext,0)


        def ID(self):
            return self.getToken(PsicoderParser.ID, 0)

        def PIZQ(self):
            return self.getToken(PsicoderParser.PIZQ, 0)

        def parametros(self):
            return self.getTypedRuleContext(PsicoderParser.ParametrosContext,0)


        def PDER(self):
            return self.getToken(PsicoderParser.PDER, 0)

        def comandos(self):
            return self.getTypedRuleContext(PsicoderParser.ComandosContext,0)


        def retornar(self):
            return self.getTypedRuleContext(PsicoderParser.RetornarContext,0)


        def getRuleIndex(self):
            return PsicoderParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)




    def funcion(self):

        localctx = PsicoderParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(PsicoderParser.T__2)
            self.state = 84
            self.tipo()
            self.state = 85
            self.match(PsicoderParser.ID)
            self.state = 86
            self.match(PsicoderParser.PIZQ)
            self.state = 87
            self.parametros()
            self.state = 88
            self.match(PsicoderParser.PDER)
            self.state = 89
            self.match(PsicoderParser.T__3)
            self.state = 90
            self.comandos()
            self.state = 91
            self.retornar()
            self.state = 92
            self.match(PsicoderParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetornarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PsicoderParser.ExprContext,0)


        def SMCOLON(self):
            return self.getToken(PsicoderParser.SMCOLON, 0)

        def getRuleIndex(self):
            return PsicoderParser.RULE_retornar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetornar" ):
                listener.enterRetornar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetornar" ):
                listener.exitRetornar(self)




    def retornar(self):

        localctx = PsicoderParser.RetornarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_retornar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(PsicoderParser.T__5)
            self.state = 95
            self.expr(0)
            self.state = 96
            self.match(PsicoderParser.SMCOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PsicoderParser.TipoContext)
            else:
                return self.getTypedRuleContext(PsicoderParser.TipoContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PsicoderParser.ID)
            else:
                return self.getToken(PsicoderParser.ID, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(PsicoderParser.COMA)
            else:
                return self.getToken(PsicoderParser.COMA, i)

        def getRuleIndex(self):
            return PsicoderParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)




    def parametros(self):

        localctx = PsicoderParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PsicoderParser.T__15, PsicoderParser.T__27, PsicoderParser.T__28, PsicoderParser.T__29, PsicoderParser.T__30, PsicoderParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.tipo()
                self.state = 99
                self.match(PsicoderParser.ID)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PsicoderParser.COMA:
                    self.state = 100
                    self.match(PsicoderParser.COMA)
                    self.state = 101
                    self.tipo()
                    self.state = 102
                    self.match(PsicoderParser.ID)
                    self.state = 108
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [PsicoderParser.PDER]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EstructuraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PsicoderParser.ID, 0)

        def declaracion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PsicoderParser.DeclaracionContext)
            else:
                return self.getTypedRuleContext(PsicoderParser.DeclaracionContext,i)


        def getRuleIndex(self):
            return PsicoderParser.RULE_estructura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstructura" ):
                listener.enterEstructura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstructura" ):
                listener.exitEstructura(self)




    def estructura(self):

        localctx = PsicoderParser.EstructuraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_estructura)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(PsicoderParser.T__6)
            self.state = 113
            self.match(PsicoderParser.ID)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PsicoderParser.T__15) | (1 << PsicoderParser.T__27) | (1 << PsicoderParser.T__28) | (1 << PsicoderParser.T__29) | (1 << PsicoderParser.T__30) | (1 << PsicoderParser.ID))) != 0):
                self.state = 114
                self.declaracion()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.match(PsicoderParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(PsicoderParser.TipoContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PsicoderParser.ID)
            else:
                return self.getToken(PsicoderParser.ID, i)

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PsicoderParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(PsicoderParser.AsignacionContext,i)


        def SMCOLON(self):
            return self.getToken(PsicoderParser.SMCOLON, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(PsicoderParser.COMA)
            else:
                return self.getToken(PsicoderParser.COMA, i)

        def getRuleIndex(self):
            return PsicoderParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)




    def declaracion(self):

        localctx = PsicoderParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_declaracion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.tipo()
            self.state = 123
            self.match(PsicoderParser.ID)
            self.state = 124
            self.asignacion()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PsicoderParser.COMA:
                self.state = 125
                self.match(PsicoderParser.COMA)
                self.state = 126
                self.match(PsicoderParser.ID)
                self.state = 127
                self.asignacion()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
            self.match(PsicoderParser.SMCOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PsicoderParser.ExprContext,0)


        def getRuleIndex(self):
            return PsicoderParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = PsicoderParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_asignacion)
        try:
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PsicoderParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(PsicoderParser.T__8)
                self.state = 136
                self.expr(0)
                pass
            elif token in [PsicoderParser.SMCOLON, PsicoderParser.COMA]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self):
            return self.getTypedRuleContext(PsicoderParser.ComandoContext,0)


        def comandos(self):
            return self.getTypedRuleContext(PsicoderParser.ComandosContext,0)


        def getRuleIndex(self):
            return PsicoderParser.RULE_comandos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandos" ):
                listener.enterComandos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandos" ):
                listener.exitComandos(self)




    def comandos(self):

        localctx = PsicoderParser.ComandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comandos)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.comando()
                self.state = 141
                self.comandos()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def si(self):
            return self.getTypedRuleContext(PsicoderParser.SiContext,0)


        def para(self):
            return self.getTypedRuleContext(PsicoderParser.ParaContext,0)


        def mientras(self):
            return self.getTypedRuleContext(PsicoderParser.MientrasContext,0)


        def hacer_mientras(self):
            return self.getTypedRuleContext(PsicoderParser.Hacer_mientrasContext,0)


        def seleccionar(self):
            return self.getTypedRuleContext(PsicoderParser.SeleccionarContext,0)


        def declaracion(self):
            return self.getTypedRuleContext(PsicoderParser.DeclaracionContext,0)


        def asignacion_id(self):
            return self.getTypedRuleContext(PsicoderParser.Asignacion_idContext,0)


        def leer(self):
            return self.getTypedRuleContext(PsicoderParser.LeerContext,0)


        def imprimir(self):
            return self.getTypedRuleContext(PsicoderParser.ImprimirContext,0)


        def llamar_funcion(self):
            return self.getTypedRuleContext(PsicoderParser.Llamar_funcionContext,0)


        def getRuleIndex(self):
            return PsicoderParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = PsicoderParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comando)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.si()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.para()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.mientras()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                self.hacer_mientras()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 150
                self.seleccionar()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 151
                self.declaracion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 152
                self.asignacion_id()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 153
                self.leer()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 154
                self.imprimir()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 155
                self.llamar_funcion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIZQ(self):
            return self.getToken(PsicoderParser.PIZQ, 0)

        def expresion_logica(self):
            return self.getTypedRuleContext(PsicoderParser.Expresion_logicaContext,0)


        def PDER(self):
            return self.getToken(PsicoderParser.PDER, 0)

        def comandos(self):
            return self.getTypedRuleContext(PsicoderParser.ComandosContext,0)


        def si_no(self):
            return self.getTypedRuleContext(PsicoderParser.Si_noContext,0)


        def getRuleIndex(self):
            return PsicoderParser.RULE_si

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSi" ):
                listener.enterSi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSi" ):
                listener.exitSi(self)




    def si(self):

        localctx = PsicoderParser.SiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_si)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(PsicoderParser.T__9)
            self.state = 159
            self.match(PsicoderParser.PIZQ)
            self.state = 160
            self.expresion_logica(0)
            self.state = 161
            self.match(PsicoderParser.PDER)
            self.state = 162
            self.match(PsicoderParser.T__10)
            self.state = 163
            self.comandos()
            self.state = 164
            self.si_no()
            self.state = 165
            self.match(PsicoderParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Si_noContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comandos(self):
            return self.getTypedRuleContext(PsicoderParser.ComandosContext,0)


        def getRuleIndex(self):
            return PsicoderParser.RULE_si_no

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSi_no" ):
                listener.enterSi_no(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSi_no" ):
                listener.exitSi_no(self)




    def si_no(self):

        localctx = PsicoderParser.Si_noContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_si_no)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PsicoderParser.T__12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(PsicoderParser.T__12)
                self.state = 168
                self.comandos()
                pass
            elif token in [PsicoderParser.T__11]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIZQ(self):
            return self.getToken(PsicoderParser.PIZQ, 0)

        def SMCOLON(self, i:int=None):
            if i is None:
                return self.getTokens(PsicoderParser.SMCOLON)
            else:
                return self.getToken(PsicoderParser.SMCOLON, i)

        def expresion_logica(self):
            return self.getTypedRuleContext(PsicoderParser.Expresion_logicaContext,0)


        def PDER(self):
            return self.getToken(PsicoderParser.PDER, 0)

        def comandos(self):
            return self.getTypedRuleContext(PsicoderParser.ComandosContext,0)


        def INT(self):
            return self.getToken(PsicoderParser.INT, 0)

        def ID(self):
            return self.getToken(PsicoderParser.ID, 0)

        def asignacion_id(self):
            return self.getTypedRuleContext(PsicoderParser.Asignacion_idContext,0)


        def asignacion_entero(self):
            return self.getTypedRuleContext(PsicoderParser.Asignacion_enteroContext,0)


        def getRuleIndex(self):
            return PsicoderParser.RULE_para

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPara" ):
                listener.enterPara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPara" ):
                listener.exitPara(self)




    def para(self):

        localctx = PsicoderParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(PsicoderParser.T__13)
            self.state = 173
            self.match(PsicoderParser.PIZQ)
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PsicoderParser.ID]:
                self.state = 174
                self.asignacion_id()
                pass
            elif token in [PsicoderParser.T__15]:
                self.state = 175
                self.asignacion_entero()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 178
            self.match(PsicoderParser.SMCOLON)
            self.state = 179
            self.expresion_logica(0)
            self.state = 180
            self.match(PsicoderParser.SMCOLON)
            self.state = 181
            _la = self._input.LA(1)
            if not(_la==PsicoderParser.INT or _la==PsicoderParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 182
            self.match(PsicoderParser.PDER)
            self.state = 183
            self.match(PsicoderParser.T__3)
            self.state = 184
            self.comandos()
            self.state = 185
            self.match(PsicoderParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asignacion_enteroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PsicoderParser.ID, 0)

        def asignacion(self):
            return self.getTypedRuleContext(PsicoderParser.AsignacionContext,0)


        def getRuleIndex(self):
            return PsicoderParser.RULE_asignacion_entero

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion_entero" ):
                listener.enterAsignacion_entero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion_entero" ):
                listener.exitAsignacion_entero(self)




    def asignacion_entero(self):

        localctx = PsicoderParser.Asignacion_enteroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_asignacion_entero)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(PsicoderParser.T__15)
            self.state = 188
            self.match(PsicoderParser.ID)
            self.state = 189
            self.asignacion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hacer_mientrasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comandos(self):
            return self.getTypedRuleContext(PsicoderParser.ComandosContext,0)


        def PIZQ(self):
            return self.getToken(PsicoderParser.PIZQ, 0)

        def expresion_logica(self):
            return self.getTypedRuleContext(PsicoderParser.Expresion_logicaContext,0)


        def PDER(self):
            return self.getToken(PsicoderParser.PDER, 0)

        def SMCOLON(self):
            return self.getToken(PsicoderParser.SMCOLON, 0)

        def getRuleIndex(self):
            return PsicoderParser.RULE_hacer_mientras

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHacer_mientras" ):
                listener.enterHacer_mientras(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHacer_mientras" ):
                listener.exitHacer_mientras(self)




    def hacer_mientras(self):

        localctx = PsicoderParser.Hacer_mientrasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_hacer_mientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(PsicoderParser.T__3)
            self.state = 192
            self.comandos()
            self.state = 193
            self.match(PsicoderParser.T__16)
            self.state = 194
            self.match(PsicoderParser.PIZQ)
            self.state = 195
            self.expresion_logica(0)
            self.state = 196
            self.match(PsicoderParser.PDER)
            self.state = 197
            self.match(PsicoderParser.SMCOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MientrasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIZQ(self):
            return self.getToken(PsicoderParser.PIZQ, 0)

        def expresion_logica(self):
            return self.getTypedRuleContext(PsicoderParser.Expresion_logicaContext,0)


        def PDER(self):
            return self.getToken(PsicoderParser.PDER, 0)

        def comandos(self):
            return self.getTypedRuleContext(PsicoderParser.ComandosContext,0)


        def getRuleIndex(self):
            return PsicoderParser.RULE_mientras

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMientras" ):
                listener.enterMientras(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMientras" ):
                listener.exitMientras(self)




    def mientras(self):

        localctx = PsicoderParser.MientrasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_mientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(PsicoderParser.T__16)
            self.state = 200
            self.match(PsicoderParser.PIZQ)
            self.state = 201
            self.expresion_logica(0)
            self.state = 202
            self.match(PsicoderParser.PDER)
            self.state = 203
            self.match(PsicoderParser.T__3)
            self.state = 204
            self.comandos()
            self.state = 205
            self.match(PsicoderParser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeleccionarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIZQ(self):
            return self.getToken(PsicoderParser.PIZQ, 0)

        def ID(self):
            return self.getToken(PsicoderParser.ID, 0)

        def PDER(self):
            return self.getToken(PsicoderParser.PDER, 0)

        def casos(self):
            return self.getTypedRuleContext(PsicoderParser.CasosContext,0)


        def getRuleIndex(self):
            return PsicoderParser.RULE_seleccionar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeleccionar" ):
                listener.enterSeleccionar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeleccionar" ):
                listener.exitSeleccionar(self)




    def seleccionar(self):

        localctx = PsicoderParser.SeleccionarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_seleccionar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(PsicoderParser.T__18)
            self.state = 208
            self.match(PsicoderParser.PIZQ)
            self.state = 209
            self.match(PsicoderParser.ID)
            self.state = 210
            self.match(PsicoderParser.PDER)
            self.state = 211
            self.match(PsicoderParser.T__19)
            self.state = 212
            self.casos()
            self.state = 213
            self.match(PsicoderParser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CasosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def caso(self):
            return self.getTypedRuleContext(PsicoderParser.CasoContext,0)


        def casos(self):
            return self.getTypedRuleContext(PsicoderParser.CasosContext,0)


        def comandos(self):
            return self.getTypedRuleContext(PsicoderParser.ComandosContext,0)


        def getRuleIndex(self):
            return PsicoderParser.RULE_casos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCasos" ):
                listener.enterCasos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCasos" ):
                listener.exitCasos(self)




    def casos(self):

        localctx = PsicoderParser.CasosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_casos)
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PsicoderParser.T__23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.caso()
                self.state = 216
                self.casos()
                pass
            elif token in [PsicoderParser.T__21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.match(PsicoderParser.T__21)
                self.state = 219
                self.match(PsicoderParser.T__22)
                self.state = 220
                self.comandos()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CasoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PsicoderParser.ExprContext,0)


        def comandos(self):
            return self.getTypedRuleContext(PsicoderParser.ComandosContext,0)


        def romper(self):
            return self.getTypedRuleContext(PsicoderParser.RomperContext,0)


        def getRuleIndex(self):
            return PsicoderParser.RULE_caso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaso" ):
                listener.enterCaso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaso" ):
                listener.exitCaso(self)




    def caso(self):

        localctx = PsicoderParser.CasoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_caso)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(PsicoderParser.T__23)
            self.state = 224
            self.expr(0)
            self.state = 225
            self.match(PsicoderParser.T__22)
            self.state = 226
            self.comandos()
            self.state = 227
            self.romper()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asignacion_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_pos_estruct(self):
            return self.getTypedRuleContext(PsicoderParser.Id_pos_estructContext,0)


        def expr(self):
            return self.getTypedRuleContext(PsicoderParser.ExprContext,0)


        def SMCOLON(self):
            return self.getToken(PsicoderParser.SMCOLON, 0)

        def getRuleIndex(self):
            return PsicoderParser.RULE_asignacion_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion_id" ):
                listener.enterAsignacion_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion_id" ):
                listener.exitAsignacion_id(self)




    def asignacion_id(self):

        localctx = PsicoderParser.Asignacion_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_asignacion_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.id_pos_estruct()
            self.state = 230
            self.match(PsicoderParser.T__8)
            self.state = 231
            self.expr(0)
            self.state = 232
            self.match(PsicoderParser.SMCOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIZQ(self):
            return self.getToken(PsicoderParser.PIZQ, 0)

        def id_pos_estruct(self):
            return self.getTypedRuleContext(PsicoderParser.Id_pos_estructContext,0)


        def PDER(self):
            return self.getToken(PsicoderParser.PDER, 0)

        def SMCOLON(self):
            return self.getToken(PsicoderParser.SMCOLON, 0)

        def getRuleIndex(self):
            return PsicoderParser.RULE_leer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeer" ):
                listener.enterLeer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeer" ):
                listener.exitLeer(self)




    def leer(self):

        localctx = PsicoderParser.LeerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_leer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(PsicoderParser.T__24)
            self.state = 235
            self.match(PsicoderParser.PIZQ)
            self.state = 236
            self.id_pos_estruct()
            self.state = 237
            self.match(PsicoderParser.PDER)
            self.state = 238
            self.match(PsicoderParser.SMCOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImprimirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIZQ(self):
            return self.getToken(PsicoderParser.PIZQ, 0)

        def PDER(self):
            return self.getToken(PsicoderParser.PDER, 0)

        def SMCOLON(self):
            return self.getToken(PsicoderParser.SMCOLON, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PsicoderParser.ExprContext)
            else:
                return self.getTypedRuleContext(PsicoderParser.ExprContext,i)


        def llamar_funcion(self):
            return self.getTypedRuleContext(PsicoderParser.Llamar_funcionContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(PsicoderParser.COMA)
            else:
                return self.getToken(PsicoderParser.COMA, i)

        def getRuleIndex(self):
            return PsicoderParser.RULE_imprimir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprimir" ):
                listener.enterImprimir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprimir" ):
                listener.exitImprimir(self)




    def imprimir(self):

        localctx = PsicoderParser.ImprimirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_imprimir)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(PsicoderParser.T__25)
            self.state = 241
            self.match(PsicoderParser.PIZQ)
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 242
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 243
                self.llamar_funcion()
                pass


            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PsicoderParser.COMA:
                self.state = 246
                self.match(PsicoderParser.COMA)
                self.state = 247
                self.expr(0)
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 253
            self.match(PsicoderParser.PDER)
            self.state = 254
            self.match(PsicoderParser.SMCOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RomperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SMCOLON(self):
            return self.getToken(PsicoderParser.SMCOLON, 0)

        def getRuleIndex(self):
            return PsicoderParser.RULE_romper

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRomper" ):
                listener.enterRomper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRomper" ):
                listener.exitRomper(self)




    def romper(self):

        localctx = PsicoderParser.RomperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_romper)
        try:
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PsicoderParser.T__26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(PsicoderParser.T__26)
                self.state = 257
                self.match(PsicoderParser.SMCOLON)
                pass
            elif token in [PsicoderParser.T__21, PsicoderParser.T__23]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Llamar_funcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PsicoderParser.ID, 0)

        def PIZQ(self):
            return self.getToken(PsicoderParser.PIZQ, 0)

        def pasar_parametros(self):
            return self.getTypedRuleContext(PsicoderParser.Pasar_parametrosContext,0)


        def PDER(self):
            return self.getToken(PsicoderParser.PDER, 0)

        def SMCOLON(self):
            return self.getToken(PsicoderParser.SMCOLON, 0)

        def getRuleIndex(self):
            return PsicoderParser.RULE_llamar_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamar_funcion" ):
                listener.enterLlamar_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamar_funcion" ):
                listener.exitLlamar_funcion(self)




    def llamar_funcion(self):

        localctx = PsicoderParser.Llamar_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_llamar_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(PsicoderParser.ID)
            self.state = 262
            self.match(PsicoderParser.PIZQ)
            self.state = 263
            self.pasar_parametros()
            self.state = 264
            self.match(PsicoderParser.PDER)
            self.state = 265
            self.match(PsicoderParser.SMCOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pasar_parametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PsicoderParser.ExprContext)
            else:
                return self.getTypedRuleContext(PsicoderParser.ExprContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(PsicoderParser.COMA)
            else:
                return self.getToken(PsicoderParser.COMA, i)

        def getRuleIndex(self):
            return PsicoderParser.RULE_pasar_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPasar_parametros" ):
                listener.enterPasar_parametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPasar_parametros" ):
                listener.exitPasar_parametros(self)




    def pasar_parametros(self):

        localctx = PsicoderParser.Pasar_parametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_pasar_parametros)
        self._la = 0 # Token type
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PsicoderParser.PIZQ, PsicoderParser.DOUBLE, PsicoderParser.INT, PsicoderParser.STRING, PsicoderParser.BOOLEANO, PsicoderParser.CONST, PsicoderParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.expr(0)
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PsicoderParser.COMA:
                    self.state = 268
                    self.match(PsicoderParser.COMA)
                    self.state = 269
                    self.expr(0)
                    self.state = 274
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [PsicoderParser.PDER]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expresion_logicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion_rop(self):
            return self.getTypedRuleContext(PsicoderParser.Expresion_ropContext,0)


        def expresion_roi(self):
            return self.getTypedRuleContext(PsicoderParser.Expresion_roiContext,0)


        def PIZQ(self):
            return self.getToken(PsicoderParser.PIZQ, 0)

        def expresion_logica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PsicoderParser.Expresion_logicaContext)
            else:
                return self.getTypedRuleContext(PsicoderParser.Expresion_logicaContext,i)


        def PDER(self):
            return self.getToken(PsicoderParser.PDER, 0)

        def NEG(self):
            return self.getToken(PsicoderParser.NEG, 0)

        def expr(self):
            return self.getTypedRuleContext(PsicoderParser.ExprContext,0)


        def ROL(self):
            return self.getToken(PsicoderParser.ROL, 0)

        def getRuleIndex(self):
            return PsicoderParser.RULE_expresion_logica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion_logica" ):
                listener.enterExpresion_logica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion_logica" ):
                listener.exitExpresion_logica(self)



    def expresion_logica(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PsicoderParser.Expresion_logicaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expresion_logica, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 279
                self.expresion_rop()
                pass

            elif la_ == 2:
                self.state = 280
                self.expresion_roi()
                pass

            elif la_ == 3:
                self.state = 281
                self.match(PsicoderParser.PIZQ)
                self.state = 282
                self.expresion_logica(0)
                self.state = 283
                self.match(PsicoderParser.PDER)
                pass

            elif la_ == 4:
                self.state = 285
                self.match(PsicoderParser.NEG)
                self.state = 286
                self.expresion_logica(2)
                pass

            elif la_ == 5:
                self.state = 287
                self.expr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 295
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PsicoderParser.Expresion_logicaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion_logica)
                    self.state = 290
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 291
                    self.match(PsicoderParser.ROL)
                    self.state = 292
                    self.expresion_logica(7) 
                self.state = 297
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expresion_ropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PsicoderParser.ExprContext)
            else:
                return self.getTypedRuleContext(PsicoderParser.ExprContext,i)


        def ROP(self):
            return self.getToken(PsicoderParser.ROP, 0)

        def getRuleIndex(self):
            return PsicoderParser.RULE_expresion_rop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion_rop" ):
                listener.enterExpresion_rop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion_rop" ):
                listener.exitExpresion_rop(self)




    def expresion_rop(self):

        localctx = PsicoderParser.Expresion_ropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expresion_rop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.expr(0)
            self.state = 299
            self.match(PsicoderParser.ROP)
            self.state = 300
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expresion_roiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PsicoderParser.ExprContext)
            else:
                return self.getTypedRuleContext(PsicoderParser.ExprContext,i)


        def ROI(self):
            return self.getToken(PsicoderParser.ROI, 0)

        def getRuleIndex(self):
            return PsicoderParser.RULE_expresion_roi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion_roi" ):
                listener.enterExpresion_roi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion_roi" ):
                listener.exitExpresion_roi(self)




    def expresion_roi(self):

        localctx = PsicoderParser.Expresion_roiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expresion_roi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.expr(0)
            self.state = 303
            self.match(PsicoderParser.ROI)
            self.state = 304
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIZQ(self):
            return self.getToken(PsicoderParser.PIZQ, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PsicoderParser.ExprContext)
            else:
                return self.getTypedRuleContext(PsicoderParser.ExprContext,i)


        def PDER(self):
            return self.getToken(PsicoderParser.PDER, 0)

        def llamar_funcion(self):
            return self.getTypedRuleContext(PsicoderParser.Llamar_funcionContext,0)


        def id_pos_estruct(self):
            return self.getTypedRuleContext(PsicoderParser.Id_pos_estructContext,0)


        def DOUBLE(self):
            return self.getToken(PsicoderParser.DOUBLE, 0)

        def INT(self):
            return self.getToken(PsicoderParser.INT, 0)

        def CONST(self):
            return self.getToken(PsicoderParser.CONST, 0)

        def STRING(self):
            return self.getToken(PsicoderParser.STRING, 0)

        def ID(self):
            return self.getToken(PsicoderParser.ID, 0)

        def BOOLEANO(self):
            return self.getToken(PsicoderParser.BOOLEANO, 0)

        def MULOP(self):
            return self.getToken(PsicoderParser.MULOP, 0)

        def SUMOP(self):
            return self.getToken(PsicoderParser.SUMOP, 0)

        def getRuleIndex(self):
            return PsicoderParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PsicoderParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 307
                self.match(PsicoderParser.PIZQ)
                self.state = 308
                self.expr(0)
                self.state = 309
                self.match(PsicoderParser.PDER)
                pass

            elif la_ == 2:
                self.state = 311
                self.llamar_funcion()
                pass

            elif la_ == 3:
                self.state = 312
                self.id_pos_estruct()
                pass

            elif la_ == 4:
                self.state = 313
                self.match(PsicoderParser.DOUBLE)
                pass

            elif la_ == 5:
                self.state = 314
                self.match(PsicoderParser.INT)
                pass

            elif la_ == 6:
                self.state = 315
                self.match(PsicoderParser.CONST)
                pass

            elif la_ == 7:
                self.state = 316
                self.match(PsicoderParser.STRING)
                pass

            elif la_ == 8:
                self.state = 317
                self.match(PsicoderParser.ID)
                pass

            elif la_ == 9:
                self.state = 318
                self.match(PsicoderParser.BOOLEANO)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 329
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 327
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = PsicoderParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 321
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 322
                        self.match(PsicoderParser.MULOP)
                        self.state = 323
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = PsicoderParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 324
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 325
                        self.match(PsicoderParser.SUMOP)
                        self.state = 326
                        self.expr(11)
                        pass

             
                self.state = 331
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PsicoderParser.ID, 0)

        def getRuleIndex(self):
            return PsicoderParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = PsicoderParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PsicoderParser.T__15) | (1 << PsicoderParser.T__27) | (1 << PsicoderParser.T__28) | (1 << PsicoderParser.T__29) | (1 << PsicoderParser.T__30) | (1 << PsicoderParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_pos_estructContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PsicoderParser.ID)
            else:
                return self.getToken(PsicoderParser.ID, i)

        def getRuleIndex(self):
            return PsicoderParser.RULE_id_pos_estruct

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_pos_estruct" ):
                listener.enterId_pos_estruct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_pos_estruct" ):
                listener.exitId_pos_estruct(self)




    def id_pos_estruct(self):

        localctx = PsicoderParser.Id_pos_estructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_id_pos_estruct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(PsicoderParser.ID)
            self.state = 339
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 335
                    self.match(PsicoderParser.T__31)
                    self.state = 336
                    self.match(PsicoderParser.ID) 
                self.state = 341
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[25] = self.expresion_logica_sempred
        self._predicates[28] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_logica_sempred(self, localctx:Expresion_logicaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         




