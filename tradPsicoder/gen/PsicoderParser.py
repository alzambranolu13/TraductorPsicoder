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
        buf.write("\u0166\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\3\2\7\2G\n\2\f\2\16")
        buf.write("\2J\13\2\3\2\3\2\3\2\7\2O\n\2\f\2\16\2R\13\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6o\n\6")
        buf.write("\f\6\16\6r\13\6\3\6\5\6u\n\6\3\7\3\7\3\7\7\7z\n\7\f\7")
        buf.write("\16\7}\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u0087")
        buf.write("\n\b\f\b\16\b\u008a\13\b\3\b\3\b\3\t\3\t\3\t\5\t\u0091")
        buf.write("\n\t\3\n\3\n\3\n\3\n\5\n\u0097\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00a3\n\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\5\r\u00b1\n\r")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u00b7\n\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00e4\n\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\5\30\u00ff\n\30\3\30\3\30\7\30\u0103\n")
        buf.write("\30\f\30\16\30\u0106\13\30\3\30\3\30\3\30\3\31\3\31\3")
        buf.write("\31\5\31\u010e\n\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\7\34\u011e\n\34\f")
        buf.write("\34\16\34\u0121\13\34\3\34\5\34\u0124\n\34\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0130\n\35")
        buf.write("\3\35\3\35\3\35\7\35\u0135\n\35\f\35\16\35\u0138\13\35")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \5 \u014f\n \3 \3 \3 \3 \3 \3")
        buf.write(" \7 \u0157\n \f \16 \u015a\13 \3!\3!\3\"\3\"\3\"\7\"\u0161")
        buf.write("\n\"\f\"\16\"\u0164\13\"\3\"\2\48>#\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@B\2\4\4")
        buf.write("\2\61\61\65\65\5\2\22\22\36!\65\65\2\u016f\2H\3\2\2\2")
        buf.write("\4U\3\2\2\2\6Y\3\2\2\2\bd\3\2\2\2\nt\3\2\2\2\fv\3\2\2")
        buf.write("\2\16\u0080\3\2\2\2\20\u0090\3\2\2\2\22\u0096\3\2\2\2")
        buf.write("\24\u00a2\3\2\2\2\26\u00a4\3\2\2\2\30\u00b0\3\2\2\2\32")
        buf.write("\u00b2\3\2\2\2\34\u00c1\3\2\2\2\36\u00c5\3\2\2\2 \u00cd")
        buf.write("\3\2\2\2\"\u00d5\3\2\2\2$\u00e3\3\2\2\2&\u00e5\3\2\2\2")
        buf.write("(\u00eb\3\2\2\2*\u00ef\3\2\2\2,\u00f4\3\2\2\2.\u00fa\3")
        buf.write("\2\2\2\60\u010d\3\2\2\2\62\u010f\3\2\2\2\64\u0114\3\2")
        buf.write("\2\2\66\u0123\3\2\2\28\u012f\3\2\2\2:\u0139\3\2\2\2<\u013d")
        buf.write("\3\2\2\2>\u014e\3\2\2\2@\u015b\3\2\2\2B\u015d\3\2\2\2")
        buf.write("DG\5\6\4\2EG\5\f\7\2FD\3\2\2\2FE\3\2\2\2GJ\3\2\2\2HF\3")
        buf.write("\2\2\2HI\3\2\2\2IK\3\2\2\2JH\3\2\2\2KP\5\4\3\2LO\5\6\4")
        buf.write("\2MO\5\f\7\2NL\3\2\2\2NM\3\2\2\2OR\3\2\2\2PN\3\2\2\2P")
        buf.write("Q\3\2\2\2QS\3\2\2\2RP\3\2\2\2ST\7\2\2\3T\3\3\2\2\2UV\7")
        buf.write("\3\2\2VW\5\22\n\2WX\7\4\2\2X\5\3\2\2\2YZ\7\5\2\2Z[\5@")
        buf.write("!\2[\\\7\65\2\2\\]\7&\2\2]^\5\n\6\2^_\7\'\2\2_`\7\6\2")
        buf.write("\2`a\5\22\n\2ab\5\b\5\2bc\7\7\2\2c\7\3\2\2\2de\7\b\2\2")
        buf.write("ef\5> \2fg\7,\2\2g\t\3\2\2\2hi\5@!\2ip\7\65\2\2jk\7-\2")
        buf.write("\2kl\5@!\2lm\7\65\2\2mo\3\2\2\2nj\3\2\2\2or\3\2\2\2pn")
        buf.write("\3\2\2\2pq\3\2\2\2qu\3\2\2\2rp\3\2\2\2su\3\2\2\2th\3\2")
        buf.write("\2\2ts\3\2\2\2u\13\3\2\2\2vw\7\t\2\2w{\7\65\2\2xz\5\16")
        buf.write("\b\2yx\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|~\3\2\2\2")
        buf.write("}{\3\2\2\2~\177\7\n\2\2\177\r\3\2\2\2\u0080\u0081\5@!")
        buf.write("\2\u0081\u0082\7\65\2\2\u0082\u0088\5\20\t\2\u0083\u0084")
        buf.write("\7-\2\2\u0084\u0085\7\65\2\2\u0085\u0087\5\20\t\2\u0086")
        buf.write("\u0083\3\2\2\2\u0087\u008a\3\2\2\2\u0088\u0086\3\2\2\2")
        buf.write("\u0088\u0089\3\2\2\2\u0089\u008b\3\2\2\2\u008a\u0088\3")
        buf.write("\2\2\2\u008b\u008c\7,\2\2\u008c\17\3\2\2\2\u008d\u008e")
        buf.write("\7\13\2\2\u008e\u0091\5> \2\u008f\u0091\3\2\2\2\u0090")
        buf.write("\u008d\3\2\2\2\u0090\u008f\3\2\2\2\u0091\21\3\2\2\2\u0092")
        buf.write("\u0093\5\24\13\2\u0093\u0094\5\22\n\2\u0094\u0097\3\2")
        buf.write("\2\2\u0095\u0097\3\2\2\2\u0096\u0092\3\2\2\2\u0096\u0095")
        buf.write("\3\2\2\2\u0097\23\3\2\2\2\u0098\u00a3\5\26\f\2\u0099\u00a3")
        buf.write("\5\32\16\2\u009a\u00a3\5 \21\2\u009b\u00a3\5\36\20\2\u009c")
        buf.write("\u00a3\5\"\22\2\u009d\u00a3\5\16\b\2\u009e\u00a3\5*\26")
        buf.write("\2\u009f\u00a3\5,\27\2\u00a0\u00a3\5.\30\2\u00a1\u00a3")
        buf.write("\5\64\33\2\u00a2\u0098\3\2\2\2\u00a2\u0099\3\2\2\2\u00a2")
        buf.write("\u009a\3\2\2\2\u00a2\u009b\3\2\2\2\u00a2\u009c\3\2\2\2")
        buf.write("\u00a2\u009d\3\2\2\2\u00a2\u009e\3\2\2\2\u00a2\u009f\3")
        buf.write("\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\25")
        buf.write("\3\2\2\2\u00a4\u00a5\7\f\2\2\u00a5\u00a6\7&\2\2\u00a6")
        buf.write("\u00a7\58\35\2\u00a7\u00a8\7\'\2\2\u00a8\u00a9\7\r\2\2")
        buf.write("\u00a9\u00aa\5\22\n\2\u00aa\u00ab\5\30\r\2\u00ab\u00ac")
        buf.write("\7\16\2\2\u00ac\27\3\2\2\2\u00ad\u00ae\7\17\2\2\u00ae")
        buf.write("\u00b1\5\22\n\2\u00af\u00b1\3\2\2\2\u00b0\u00ad\3\2\2")
        buf.write("\2\u00b0\u00af\3\2\2\2\u00b1\31\3\2\2\2\u00b2\u00b3\7")
        buf.write("\20\2\2\u00b3\u00b6\7&\2\2\u00b4\u00b7\5(\25\2\u00b5\u00b7")
        buf.write("\5\34\17\2\u00b6\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b8\3\2\2\2\u00b8\u00b9\7,\2\2\u00b9\u00ba\58\35\2")
        buf.write("\u00ba\u00bb\7,\2\2\u00bb\u00bc\t\2\2\2\u00bc\u00bd\7")
        buf.write("\'\2\2\u00bd\u00be\7\6\2\2\u00be\u00bf\5\22\n\2\u00bf")
        buf.write("\u00c0\7\21\2\2\u00c0\33\3\2\2\2\u00c1\u00c2\7\22\2\2")
        buf.write("\u00c2\u00c3\7\65\2\2\u00c3\u00c4\5\20\t\2\u00c4\35\3")
        buf.write("\2\2\2\u00c5\u00c6\7\6\2\2\u00c6\u00c7\5\22\n\2\u00c7")
        buf.write("\u00c8\7\23\2\2\u00c8\u00c9\7&\2\2\u00c9\u00ca\58\35\2")
        buf.write("\u00ca\u00cb\7\'\2\2\u00cb\u00cc\7,\2\2\u00cc\37\3\2\2")
        buf.write("\2\u00cd\u00ce\7\23\2\2\u00ce\u00cf\7&\2\2\u00cf\u00d0")
        buf.write("\58\35\2\u00d0\u00d1\7\'\2\2\u00d1\u00d2\7\6\2\2\u00d2")
        buf.write("\u00d3\5\22\n\2\u00d3\u00d4\7\24\2\2\u00d4!\3\2\2\2\u00d5")
        buf.write("\u00d6\7\25\2\2\u00d6\u00d7\7&\2\2\u00d7\u00d8\7\65\2")
        buf.write("\2\u00d8\u00d9\7\'\2\2\u00d9\u00da\7\26\2\2\u00da\u00db")
        buf.write("\5$\23\2\u00db\u00dc\7\27\2\2\u00dc#\3\2\2\2\u00dd\u00de")
        buf.write("\5&\24\2\u00de\u00df\5$\23\2\u00df\u00e4\3\2\2\2\u00e0")
        buf.write("\u00e1\7\30\2\2\u00e1\u00e2\7\31\2\2\u00e2\u00e4\5\22")
        buf.write("\n\2\u00e3\u00dd\3\2\2\2\u00e3\u00e0\3\2\2\2\u00e4%\3")
        buf.write("\2\2\2\u00e5\u00e6\7\32\2\2\u00e6\u00e7\5> \2\u00e7\u00e8")
        buf.write("\7\31\2\2\u00e8\u00e9\5\22\n\2\u00e9\u00ea\5\60\31\2\u00ea")
        buf.write("\'\3\2\2\2\u00eb\u00ec\7\65\2\2\u00ec\u00ed\7\13\2\2\u00ed")
        buf.write("\u00ee\5> \2\u00ee)\3\2\2\2\u00ef\u00f0\5B\"\2\u00f0\u00f1")
        buf.write("\7\13\2\2\u00f1\u00f2\5> \2\u00f2\u00f3\7,\2\2\u00f3+")
        buf.write("\3\2\2\2\u00f4\u00f5\7\33\2\2\u00f5\u00f6\7&\2\2\u00f6")
        buf.write("\u00f7\5B\"\2\u00f7\u00f8\7\'\2\2\u00f8\u00f9\7,\2\2\u00f9")
        buf.write("-\3\2\2\2\u00fa\u00fb\7\34\2\2\u00fb\u00fe\7&\2\2\u00fc")
        buf.write("\u00ff\5> \2\u00fd\u00ff\5\62\32\2\u00fe\u00fc\3\2\2\2")
        buf.write("\u00fe\u00fd\3\2\2\2\u00ff\u0104\3\2\2\2\u0100\u0101\7")
        buf.write("-\2\2\u0101\u0103\5> \2\u0102\u0100\3\2\2\2\u0103\u0106")
        buf.write("\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105")
        buf.write("\u0107\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0108\7\'\2\2")
        buf.write("\u0108\u0109\7,\2\2\u0109/\3\2\2\2\u010a\u010b\7\35\2")
        buf.write("\2\u010b\u010e\7,\2\2\u010c\u010e\3\2\2\2\u010d\u010a")
        buf.write("\3\2\2\2\u010d\u010c\3\2\2\2\u010e\61\3\2\2\2\u010f\u0110")
        buf.write("\7\65\2\2\u0110\u0111\7&\2\2\u0111\u0112\5\66\34\2\u0112")
        buf.write("\u0113\7\'\2\2\u0113\63\3\2\2\2\u0114\u0115\7\65\2\2\u0115")
        buf.write("\u0116\7&\2\2\u0116\u0117\5\66\34\2\u0117\u0118\7\'\2")
        buf.write("\2\u0118\u0119\7,\2\2\u0119\65\3\2\2\2\u011a\u011f\5>")
        buf.write(" \2\u011b\u011c\7-\2\2\u011c\u011e\5> \2\u011d\u011b\3")
        buf.write("\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u0120")
        buf.write("\3\2\2\2\u0120\u0124\3\2\2\2\u0121\u011f\3\2\2\2\u0122")
        buf.write("\u0124\3\2\2\2\u0123\u011a\3\2\2\2\u0123\u0122\3\2\2\2")
        buf.write("\u0124\67\3\2\2\2\u0125\u0126\b\35\1\2\u0126\u0130\5:")
        buf.write("\36\2\u0127\u0130\5<\37\2\u0128\u0129\7&\2\2\u0129\u012a")
        buf.write("\58\35\2\u012a\u012b\7\'\2\2\u012b\u0130\3\2\2\2\u012c")
        buf.write("\u012d\7(\2\2\u012d\u0130\58\35\4\u012e\u0130\5> \2\u012f")
        buf.write("\u0125\3\2\2\2\u012f\u0127\3\2\2\2\u012f\u0128\3\2\2\2")
        buf.write("\u012f\u012c\3\2\2\2\u012f\u012e\3\2\2\2\u0130\u0136\3")
        buf.write("\2\2\2\u0131\u0132\f\b\2\2\u0132\u0133\7+\2\2\u0133\u0135")
        buf.write("\58\35\t\u0134\u0131\3\2\2\2\u0135\u0138\3\2\2\2\u0136")
        buf.write("\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u01379\3\2\2\2\u0138")
        buf.write("\u0136\3\2\2\2\u0139\u013a\5> \2\u013a\u013b\7*\2\2\u013b")
        buf.write("\u013c\5> \2\u013c;\3\2\2\2\u013d\u013e\5> \2\u013e\u013f")
        buf.write("\7)\2\2\u013f\u0140\5> \2\u0140=\3\2\2\2\u0141\u0142\b")
        buf.write(" \1\2\u0142\u0143\7&\2\2\u0143\u0144\5> \2\u0144\u0145")
        buf.write("\7\'\2\2\u0145\u014f\3\2\2\2\u0146\u014f\5\64\33\2\u0147")
        buf.write("\u014f\5B\"\2\u0148\u014f\7\60\2\2\u0149\u014f\7\61\2")
        buf.write("\2\u014a\u014f\7\64\2\2\u014b\u014f\7\62\2\2\u014c\u014f")
        buf.write("\7\65\2\2\u014d\u014f\7\63\2\2\u014e\u0141\3\2\2\2\u014e")
        buf.write("\u0146\3\2\2\2\u014e\u0147\3\2\2\2\u014e\u0148\3\2\2\2")
        buf.write("\u014e\u0149\3\2\2\2\u014e\u014a\3\2\2\2\u014e\u014b\3")
        buf.write("\2\2\2\u014e\u014c\3\2\2\2\u014e\u014d\3\2\2\2\u014f\u0158")
        buf.write("\3\2\2\2\u0150\u0151\f\r\2\2\u0151\u0152\7.\2\2\u0152")
        buf.write("\u0157\5> \16\u0153\u0154\f\f\2\2\u0154\u0155\7/\2\2\u0155")
        buf.write("\u0157\5> \r\u0156\u0150\3\2\2\2\u0156\u0153\3\2\2\2\u0157")
        buf.write("\u015a\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2")
        buf.write("\u0159?\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u015c\t\3\2")
        buf.write("\2\u015cA\3\2\2\2\u015d\u0162\7\65\2\2\u015e\u015f\7\"")
        buf.write("\2\2\u015f\u0161\7\65\2\2\u0160\u015e\3\2\2\2\u0161\u0164")
        buf.write("\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("C\3\2\2\2\u0164\u0162\3\2\2\2\33FHNPpt{\u0088\u0090\u0096")
        buf.write("\u00a2\u00b0\u00b6\u00e3\u00fe\u0104\u010d\u011f\u0123")
        buf.write("\u012f\u0136\u014e\u0156\u0158\u0162")
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
    RULE_asignacion_id_para = 19
    RULE_asignacion_id = 20
    RULE_leer = 21
    RULE_imprimir = 22
    RULE_romper = 23
    RULE_llamar_funcion_dentro_imp = 24
    RULE_llamar_funcion = 25
    RULE_pasar_parametros = 26
    RULE_expresion_logica = 27
    RULE_expresion_rop = 28
    RULE_expresion_roi = 29
    RULE_expr = 30
    RULE_tipo = 31
    RULE_id_pos_estruct = 32

    ruleNames =  [ "s", "funcion_principal", "funcion", "retornar", "parametros", 
                   "estructura", "declaracion", "asignacion", "comandos", 
                   "comando", "si", "si_no", "para", "asignacion_entero", 
                   "hacer_mientras", "mientras", "seleccionar", "casos", 
                   "caso", "asignacion_id_para", "asignacion_id", "leer", 
                   "imprimir", "romper", "llamar_funcion_dentro_imp", "llamar_funcion", 
                   "pasar_parametros", "expresion_logica", "expresion_rop", 
                   "expresion_roi", "expr", "tipo", "id_pos_estruct" ]

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
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PsicoderParser.T__2 or _la==PsicoderParser.T__6:
                self.state = 68
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [PsicoderParser.T__2]:
                    self.state = 66
                    self.funcion()
                    pass
                elif token in [PsicoderParser.T__6]:
                    self.state = 67
                    self.estructura()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
            self.funcion_principal()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PsicoderParser.T__2 or _la==PsicoderParser.T__6:
                self.state = 76
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [PsicoderParser.T__2]:
                    self.state = 74
                    self.funcion()
                    pass
                elif token in [PsicoderParser.T__6]:
                    self.state = 75
                    self.estructura()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
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
            self.state = 83
            self.match(PsicoderParser.T__0)
            self.state = 84
            self.comandos()
            self.state = 85
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
            self.state = 87
            self.match(PsicoderParser.T__2)
            self.state = 88
            self.tipo()
            self.state = 89
            self.match(PsicoderParser.ID)
            self.state = 90
            self.match(PsicoderParser.PIZQ)
            self.state = 91
            self.parametros()
            self.state = 92
            self.match(PsicoderParser.PDER)
            self.state = 93
            self.match(PsicoderParser.T__3)
            self.state = 94
            self.comandos()
            self.state = 95
            self.retornar()
            self.state = 96
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
            self.state = 98
            self.match(PsicoderParser.T__5)
            self.state = 99
            self.expr(0)
            self.state = 100
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
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PsicoderParser.T__15, PsicoderParser.T__27, PsicoderParser.T__28, PsicoderParser.T__29, PsicoderParser.T__30, PsicoderParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.tipo()
                self.state = 103
                self.match(PsicoderParser.ID)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PsicoderParser.COMA:
                    self.state = 104
                    self.match(PsicoderParser.COMA)
                    self.state = 105
                    self.tipo()
                    self.state = 106
                    self.match(PsicoderParser.ID)
                    self.state = 112
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
            self.state = 116
            self.match(PsicoderParser.T__6)
            self.state = 117
            self.match(PsicoderParser.ID)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PsicoderParser.T__15) | (1 << PsicoderParser.T__27) | (1 << PsicoderParser.T__28) | (1 << PsicoderParser.T__29) | (1 << PsicoderParser.T__30) | (1 << PsicoderParser.ID))) != 0):
                self.state = 118
                self.declaracion()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
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
            self.state = 126
            self.tipo()
            self.state = 127
            self.match(PsicoderParser.ID)
            self.state = 128
            self.asignacion()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PsicoderParser.COMA:
                self.state = 129
                self.match(PsicoderParser.COMA)
                self.state = 130
                self.match(PsicoderParser.ID)
                self.state = 131
                self.asignacion()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 137
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
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PsicoderParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.match(PsicoderParser.T__8)
                self.state = 140
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
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.comando()
                self.state = 145
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
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.si()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.para()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                self.mientras()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 153
                self.hacer_mientras()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 154
                self.seleccionar()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 155
                self.declaracion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 156
                self.asignacion_id()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 157
                self.leer()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 158
                self.imprimir()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 159
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
            self.state = 162
            self.match(PsicoderParser.T__9)
            self.state = 163
            self.match(PsicoderParser.PIZQ)
            self.state = 164
            self.expresion_logica(0)
            self.state = 165
            self.match(PsicoderParser.PDER)
            self.state = 166
            self.match(PsicoderParser.T__10)
            self.state = 167
            self.comandos()
            self.state = 168
            self.si_no()
            self.state = 169
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
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PsicoderParser.T__12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(PsicoderParser.T__12)
                self.state = 172
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

        def asignacion_id_para(self):
            return self.getTypedRuleContext(PsicoderParser.Asignacion_id_paraContext,0)


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
            self.state = 176
            self.match(PsicoderParser.T__13)
            self.state = 177
            self.match(PsicoderParser.PIZQ)
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PsicoderParser.ID]:
                self.state = 178
                self.asignacion_id_para()
                pass
            elif token in [PsicoderParser.T__15]:
                self.state = 179
                self.asignacion_entero()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 182
            self.match(PsicoderParser.SMCOLON)
            self.state = 183
            self.expresion_logica(0)
            self.state = 184
            self.match(PsicoderParser.SMCOLON)
            self.state = 185
            _la = self._input.LA(1)
            if not(_la==PsicoderParser.INT or _la==PsicoderParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 186
            self.match(PsicoderParser.PDER)
            self.state = 187
            self.match(PsicoderParser.T__3)
            self.state = 188
            self.comandos()
            self.state = 189
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
            self.state = 191
            self.match(PsicoderParser.T__15)
            self.state = 192
            self.match(PsicoderParser.ID)
            self.state = 193
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
            self.state = 195
            self.match(PsicoderParser.T__3)
            self.state = 196
            self.comandos()
            self.state = 197
            self.match(PsicoderParser.T__16)
            self.state = 198
            self.match(PsicoderParser.PIZQ)
            self.state = 199
            self.expresion_logica(0)
            self.state = 200
            self.match(PsicoderParser.PDER)
            self.state = 201
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
            self.state = 203
            self.match(PsicoderParser.T__16)
            self.state = 204
            self.match(PsicoderParser.PIZQ)
            self.state = 205
            self.expresion_logica(0)
            self.state = 206
            self.match(PsicoderParser.PDER)
            self.state = 207
            self.match(PsicoderParser.T__3)
            self.state = 208
            self.comandos()
            self.state = 209
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
            self.state = 211
            self.match(PsicoderParser.T__18)
            self.state = 212
            self.match(PsicoderParser.PIZQ)
            self.state = 213
            self.match(PsicoderParser.ID)
            self.state = 214
            self.match(PsicoderParser.PDER)
            self.state = 215
            self.match(PsicoderParser.T__19)
            self.state = 216
            self.casos()
            self.state = 217
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
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PsicoderParser.T__23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.caso()
                self.state = 220
                self.casos()
                pass
            elif token in [PsicoderParser.T__21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.match(PsicoderParser.T__21)
                self.state = 223
                self.match(PsicoderParser.T__22)
                self.state = 224
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
            self.state = 227
            self.match(PsicoderParser.T__23)
            self.state = 228
            self.expr(0)
            self.state = 229
            self.match(PsicoderParser.T__22)
            self.state = 230
            self.comandos()
            self.state = 231
            self.romper()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asignacion_id_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PsicoderParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(PsicoderParser.ExprContext,0)


        def getRuleIndex(self):
            return PsicoderParser.RULE_asignacion_id_para

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion_id_para" ):
                listener.enterAsignacion_id_para(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion_id_para" ):
                listener.exitAsignacion_id_para(self)




    def asignacion_id_para(self):

        localctx = PsicoderParser.Asignacion_id_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_asignacion_id_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(PsicoderParser.ID)
            self.state = 234
            self.match(PsicoderParser.T__8)
            self.state = 235
            self.expr(0)
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
        self.enterRule(localctx, 40, self.RULE_asignacion_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.id_pos_estruct()
            self.state = 238
            self.match(PsicoderParser.T__8)
            self.state = 239
            self.expr(0)
            self.state = 240
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
        self.enterRule(localctx, 42, self.RULE_leer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(PsicoderParser.T__24)
            self.state = 243
            self.match(PsicoderParser.PIZQ)
            self.state = 244
            self.id_pos_estruct()
            self.state = 245
            self.match(PsicoderParser.PDER)
            self.state = 246
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


        def llamar_funcion_dentro_imp(self):
            return self.getTypedRuleContext(PsicoderParser.Llamar_funcion_dentro_impContext,0)


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
        self.enterRule(localctx, 44, self.RULE_imprimir)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(PsicoderParser.T__25)
            self.state = 249
            self.match(PsicoderParser.PIZQ)
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 250
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 251
                self.llamar_funcion_dentro_imp()
                pass


            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PsicoderParser.COMA:
                self.state = 254
                self.match(PsicoderParser.COMA)
                self.state = 255
                self.expr(0)
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 261
            self.match(PsicoderParser.PDER)
            self.state = 262
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
        self.enterRule(localctx, 46, self.RULE_romper)
        try:
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PsicoderParser.T__26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.match(PsicoderParser.T__26)
                self.state = 265
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


    class Llamar_funcion_dentro_impContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return PsicoderParser.RULE_llamar_funcion_dentro_imp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamar_funcion_dentro_imp" ):
                listener.enterLlamar_funcion_dentro_imp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamar_funcion_dentro_imp" ):
                listener.exitLlamar_funcion_dentro_imp(self)




    def llamar_funcion_dentro_imp(self):

        localctx = PsicoderParser.Llamar_funcion_dentro_impContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_llamar_funcion_dentro_imp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(PsicoderParser.ID)
            self.state = 270
            self.match(PsicoderParser.PIZQ)
            self.state = 271
            self.pasar_parametros()
            self.state = 272
            self.match(PsicoderParser.PDER)
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
        self.enterRule(localctx, 50, self.RULE_llamar_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(PsicoderParser.ID)
            self.state = 275
            self.match(PsicoderParser.PIZQ)
            self.state = 276
            self.pasar_parametros()
            self.state = 277
            self.match(PsicoderParser.PDER)
            self.state = 278
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
        self.enterRule(localctx, 52, self.RULE_pasar_parametros)
        self._la = 0 # Token type
        try:
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PsicoderParser.PIZQ, PsicoderParser.DOUBLE, PsicoderParser.INT, PsicoderParser.STRING, PsicoderParser.BOOLEANO, PsicoderParser.CONST, PsicoderParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.expr(0)
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PsicoderParser.COMA:
                    self.state = 281
                    self.match(PsicoderParser.COMA)
                    self.state = 282
                    self.expr(0)
                    self.state = 287
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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expresion_logica, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 292
                self.expresion_rop()
                pass

            elif la_ == 2:
                self.state = 293
                self.expresion_roi()
                pass

            elif la_ == 3:
                self.state = 294
                self.match(PsicoderParser.PIZQ)
                self.state = 295
                self.expresion_logica(0)
                self.state = 296
                self.match(PsicoderParser.PDER)
                pass

            elif la_ == 4:
                self.state = 298
                self.match(PsicoderParser.NEG)
                self.state = 299
                self.expresion_logica(2)
                pass

            elif la_ == 5:
                self.state = 300
                self.expr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PsicoderParser.Expresion_logicaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion_logica)
                    self.state = 303
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 304
                    self.match(PsicoderParser.ROL)
                    self.state = 305
                    self.expresion_logica(7) 
                self.state = 310
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
        self.enterRule(localctx, 56, self.RULE_expresion_rop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.expr(0)
            self.state = 312
            self.match(PsicoderParser.ROP)
            self.state = 313
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
        self.enterRule(localctx, 58, self.RULE_expresion_roi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.expr(0)
            self.state = 316
            self.match(PsicoderParser.ROI)
            self.state = 317
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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 320
                self.match(PsicoderParser.PIZQ)
                self.state = 321
                self.expr(0)
                self.state = 322
                self.match(PsicoderParser.PDER)
                pass

            elif la_ == 2:
                self.state = 324
                self.llamar_funcion()
                pass

            elif la_ == 3:
                self.state = 325
                self.id_pos_estruct()
                pass

            elif la_ == 4:
                self.state = 326
                self.match(PsicoderParser.DOUBLE)
                pass

            elif la_ == 5:
                self.state = 327
                self.match(PsicoderParser.INT)
                pass

            elif la_ == 6:
                self.state = 328
                self.match(PsicoderParser.CONST)
                pass

            elif la_ == 7:
                self.state = 329
                self.match(PsicoderParser.STRING)
                pass

            elif la_ == 8:
                self.state = 330
                self.match(PsicoderParser.ID)
                pass

            elif la_ == 9:
                self.state = 331
                self.match(PsicoderParser.BOOLEANO)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 342
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 340
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = PsicoderParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 334
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 335
                        self.match(PsicoderParser.MULOP)
                        self.state = 336
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = PsicoderParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 337
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 338
                        self.match(PsicoderParser.SUMOP)
                        self.state = 339
                        self.expr(11)
                        pass

             
                self.state = 344
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
        self.enterRule(localctx, 62, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
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
        self.enterRule(localctx, 64, self.RULE_id_pos_estruct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(PsicoderParser.ID)
            self.state = 352
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 348
                    self.match(PsicoderParser.T__31)
                    self.state = 349
                    self.match(PsicoderParser.ID) 
                self.state = 354
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
        self._predicates[27] = self.expresion_logica_sempred
        self._predicates[30] = self.expr_sempred
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
         




