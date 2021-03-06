// Generated from c:\Users\USER\Documents\LP-2021-1\TraductorPsicoder\tradPsicoder\grammar\Psicoder.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class PsicoderLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, COMMENT=33, LINE_COMMENT=34, WS=35, PIZQ=36, PDER=37, NEG=38, 
		ROI=39, ROP=40, ROL=41, SMCOLON=42, COMA=43, MULOP=44, SUMOP=45, DOUBLE=46, 
		INT=47, STRING=48, BOOLEANO=49, CONST=50, ID=51;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
			"T__17", "T__18", "T__19", "T__20", "T__21", "T__22", "T__23", "T__24", 
			"T__25", "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", "COMMENT", 
			"LINE_COMMENT", "WS", "PIZQ", "PDER", "NEG", "ROI", "ROP", "ROL", "SMCOLON", 
			"COMA", "MULOP", "SUMOP", "DOUBLE", "INT", "STRING", "BOOLEANO", "CONST", 
			"ID"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'funcion_principal'", "'fin_principal'", "'funcion'", "'hacer'", 
			"'fin_funcion'", "'retornar'", "'estructura'", "'fin_estructura'", "'='", 
			"'si'", "'entonces'", "'fin_si'", "'si_no'", "'para'", "'fin_para'", 
			"'entero'", "'mientras'", "'fin_mientras'", "'seleccionar'", "'entre'", 
			"'fin_seleccionar'", "'defecto'", "':'", "'caso'", "'leer'", "'imprimir'", 
			"'romper'", "'caracter'", "'cadena'", "'real'", "'booleano'", "'.'", 
			null, null, null, "'('", "')'", "'!'", null, null, null, "';'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, "COMMENT", "LINE_COMMENT", 
			"WS", "PIZQ", "PDER", "NEG", "ROI", "ROP", "ROL", "SMCOLON", "COMA", 
			"MULOP", "SUMOP", "DOUBLE", "INT", "STRING", "BOOLEANO", "CONST", "ID"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public PsicoderLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Psicoder.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65\u01ec\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64"+
		"\t\64\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3"+
		"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20"+
		"\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22"+
		"\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23"+
		"\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24"+
		"\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27"+
		"\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32"+
		"\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34"+
		"\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36"+
		"\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 "+
		"\3 \3!\3!\3\"\3\"\3\"\3\"\7\"\u0177\n\"\f\"\16\"\u017a\13\"\3\"\3\"\3"+
		"\"\3\"\3\"\3#\3#\3#\3#\7#\u0185\n#\f#\16#\u0188\13#\3#\3#\3$\6$\u018d"+
		"\n$\r$\16$\u018e\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3(\5(\u019d\n(\3)"+
		"\3)\3)\3)\3)\3)\5)\u01a5\n)\3*\3*\3*\3*\5*\u01ab\n*\3+\3+\3,\3,\3-\3-"+
		"\3-\3-\5-\u01b5\n-\3.\3.\3/\6/\u01ba\n/\r/\16/\u01bb\3/\3/\6/\u01c0\n"+
		"/\r/\16/\u01c1\3\60\6\60\u01c5\n\60\r\60\16\60\u01c6\3\61\3\61\7\61\u01cb"+
		"\n\61\f\61\16\61\u01ce\13\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3"+
		"\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u01e0\n\62\3\63\3\63\3\63"+
		"\3\63\3\64\3\64\7\64\u01e8\n\64\f\64\16\64\u01eb\13\64\4\u0178\u01cc\2"+
		"\65\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35"+
		"\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36"+
		";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65\3\2\n\4"+
		"\2\f\f\17\17\5\2\13\f\17\17\"\"\4\2,,\61\61\4\2--//\3\2\62;\3\2\60\60"+
		"\4\2C\\c|\6\2\62;C\\aac|\2\u01fb\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2"+
		"\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2"+
		"\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2"+
		"\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2"+
		"\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2"+
		"\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2"+
		"\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O"+
		"\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2"+
		"\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2"+
		"\3i\3\2\2\2\5{\3\2\2\2\7\u0089\3\2\2\2\t\u0091\3\2\2\2\13\u0097\3\2\2"+
		"\2\r\u00a3\3\2\2\2\17\u00ac\3\2\2\2\21\u00b7\3\2\2\2\23\u00c6\3\2\2\2"+
		"\25\u00c8\3\2\2\2\27\u00cb\3\2\2\2\31\u00d4\3\2\2\2\33\u00db\3\2\2\2\35"+
		"\u00e1\3\2\2\2\37\u00e6\3\2\2\2!\u00ef\3\2\2\2#\u00f6\3\2\2\2%\u00ff\3"+
		"\2\2\2\'\u010c\3\2\2\2)\u0118\3\2\2\2+\u011e\3\2\2\2-\u012e\3\2\2\2/\u0136"+
		"\3\2\2\2\61\u0138\3\2\2\2\63\u013d\3\2\2\2\65\u0142\3\2\2\2\67\u014b\3"+
		"\2\2\29\u0152\3\2\2\2;\u015b\3\2\2\2=\u0162\3\2\2\2?\u0167\3\2\2\2A\u0170"+
		"\3\2\2\2C\u0172\3\2\2\2E\u0180\3\2\2\2G\u018c\3\2\2\2I\u0192\3\2\2\2K"+
		"\u0194\3\2\2\2M\u0196\3\2\2\2O\u019c\3\2\2\2Q\u01a4\3\2\2\2S\u01aa\3\2"+
		"\2\2U\u01ac\3\2\2\2W\u01ae\3\2\2\2Y\u01b4\3\2\2\2[\u01b6\3\2\2\2]\u01b9"+
		"\3\2\2\2_\u01c4\3\2\2\2a\u01c8\3\2\2\2c\u01df\3\2\2\2e\u01e1\3\2\2\2g"+
		"\u01e5\3\2\2\2ij\7h\2\2jk\7w\2\2kl\7p\2\2lm\7e\2\2mn\7k\2\2no\7q\2\2o"+
		"p\7p\2\2pq\7a\2\2qr\7r\2\2rs\7t\2\2st\7k\2\2tu\7p\2\2uv\7e\2\2vw\7k\2"+
		"\2wx\7r\2\2xy\7c\2\2yz\7n\2\2z\4\3\2\2\2{|\7h\2\2|}\7k\2\2}~\7p\2\2~\177"+
		"\7a\2\2\177\u0080\7r\2\2\u0080\u0081\7t\2\2\u0081\u0082\7k\2\2\u0082\u0083"+
		"\7p\2\2\u0083\u0084\7e\2\2\u0084\u0085\7k\2\2\u0085\u0086\7r\2\2\u0086"+
		"\u0087\7c\2\2\u0087\u0088\7n\2\2\u0088\6\3\2\2\2\u0089\u008a\7h\2\2\u008a"+
		"\u008b\7w\2\2\u008b\u008c\7p\2\2\u008c\u008d\7e\2\2\u008d\u008e\7k\2\2"+
		"\u008e\u008f\7q\2\2\u008f\u0090\7p\2\2\u0090\b\3\2\2\2\u0091\u0092\7j"+
		"\2\2\u0092\u0093\7c\2\2\u0093\u0094\7e\2\2\u0094\u0095\7g\2\2\u0095\u0096"+
		"\7t\2\2\u0096\n\3\2\2\2\u0097\u0098\7h\2\2\u0098\u0099\7k\2\2\u0099\u009a"+
		"\7p\2\2\u009a\u009b\7a\2\2\u009b\u009c\7h\2\2\u009c\u009d\7w\2\2\u009d"+
		"\u009e\7p\2\2\u009e\u009f\7e\2\2\u009f\u00a0\7k\2\2\u00a0\u00a1\7q\2\2"+
		"\u00a1\u00a2\7p\2\2\u00a2\f\3\2\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5\7g"+
		"\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9"+
		"\7p\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab\7t\2\2\u00ab\16\3\2\2\2\u00ac\u00ad"+
		"\7g\2\2\u00ad\u00ae\7u\2\2\u00ae\u00af\7v\2\2\u00af\u00b0\7t\2\2\u00b0"+
		"\u00b1\7w\2\2\u00b1\u00b2\7e\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7w\2\2"+
		"\u00b4\u00b5\7t\2\2\u00b5\u00b6\7c\2\2\u00b6\20\3\2\2\2\u00b7\u00b8\7"+
		"h\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb\7a\2\2\u00bb\u00bc"+
		"\7g\2\2\u00bc\u00bd\7u\2\2\u00bd\u00be\7v\2\2\u00be\u00bf\7t\2\2\u00bf"+
		"\u00c0\7w\2\2\u00c0\u00c1\7e\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3\7w\2\2"+
		"\u00c3\u00c4\7t\2\2\u00c4\u00c5\7c\2\2\u00c5\22\3\2\2\2\u00c6\u00c7\7"+
		"?\2\2\u00c7\24\3\2\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca\7k\2\2\u00ca\26"+
		"\3\2\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7v\2\2\u00ce"+
		"\u00cf\7q\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1\7e\2\2\u00d1\u00d2\7g\2\2"+
		"\u00d2\u00d3\7u\2\2\u00d3\30\3\2\2\2\u00d4\u00d5\7h\2\2\u00d5\u00d6\7"+
		"k\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8\7a\2\2\u00d8\u00d9\7u\2\2\u00d9\u00da"+
		"\7k\2\2\u00da\32\3\2\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd\7k\2\2\u00dd\u00de"+
		"\7a\2\2\u00de\u00df\7p\2\2\u00df\u00e0\7q\2\2\u00e0\34\3\2\2\2\u00e1\u00e2"+
		"\7r\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4\7t\2\2\u00e4\u00e5\7c\2\2\u00e5"+
		"\36\3\2\2\2\u00e6\u00e7\7h\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9\7p\2\2\u00e9"+
		"\u00ea\7a\2\2\u00ea\u00eb\7r\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7t\2\2"+
		"\u00ed\u00ee\7c\2\2\u00ee \3\2\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1\7p\2"+
		"\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4\7t\2\2\u00f4\u00f5"+
		"\7q\2\2\u00f5\"\3\2\2\2\u00f6\u00f7\7o\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9"+
		"\7g\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc\7t\2\2\u00fc"+
		"\u00fd\7c\2\2\u00fd\u00fe\7u\2\2\u00fe$\3\2\2\2\u00ff\u0100\7h\2\2\u0100"+
		"\u0101\7k\2\2\u0101\u0102\7p\2\2\u0102\u0103\7a\2\2\u0103\u0104\7o\2\2"+
		"\u0104\u0105\7k\2\2\u0105\u0106\7g\2\2\u0106\u0107\7p\2\2\u0107\u0108"+
		"\7v\2\2\u0108\u0109\7t\2\2\u0109\u010a\7c\2\2\u010a\u010b\7u\2\2\u010b"+
		"&\3\2\2\2\u010c\u010d\7u\2\2\u010d\u010e\7g\2\2\u010e\u010f\7n\2\2\u010f"+
		"\u0110\7g\2\2\u0110\u0111\7e\2\2\u0111\u0112\7e\2\2\u0112\u0113\7k\2\2"+
		"\u0113\u0114\7q\2\2\u0114\u0115\7p\2\2\u0115\u0116\7c\2\2\u0116\u0117"+
		"\7t\2\2\u0117(\3\2\2\2\u0118\u0119\7g\2\2\u0119\u011a\7p\2\2\u011a\u011b"+
		"\7v\2\2\u011b\u011c\7t\2\2\u011c\u011d\7g\2\2\u011d*\3\2\2\2\u011e\u011f"+
		"\7h\2\2\u011f\u0120\7k\2\2\u0120\u0121\7p\2\2\u0121\u0122\7a\2\2\u0122"+
		"\u0123\7u\2\2\u0123\u0124\7g\2\2\u0124\u0125\7n\2\2\u0125\u0126\7g\2\2"+
		"\u0126\u0127\7e\2\2\u0127\u0128\7e\2\2\u0128\u0129\7k\2\2\u0129\u012a"+
		"\7q\2\2\u012a\u012b\7p\2\2\u012b\u012c\7c\2\2\u012c\u012d\7t\2\2\u012d"+
		",\3\2\2\2\u012e\u012f\7f\2\2\u012f\u0130\7g\2\2\u0130\u0131\7h\2\2\u0131"+
		"\u0132\7g\2\2\u0132\u0133\7e\2\2\u0133\u0134\7v\2\2\u0134\u0135\7q\2\2"+
		"\u0135.\3\2\2\2\u0136\u0137\7<\2\2\u0137\60\3\2\2\2\u0138\u0139\7e\2\2"+
		"\u0139\u013a\7c\2\2\u013a\u013b\7u\2\2\u013b\u013c\7q\2\2\u013c\62\3\2"+
		"\2\2\u013d\u013e\7n\2\2\u013e\u013f\7g\2\2\u013f\u0140\7g\2\2\u0140\u0141"+
		"\7t\2\2\u0141\64\3\2\2\2\u0142\u0143\7k\2\2\u0143\u0144\7o\2\2\u0144\u0145"+
		"\7r\2\2\u0145\u0146\7t\2\2\u0146\u0147\7k\2\2\u0147\u0148\7o\2\2\u0148"+
		"\u0149\7k\2\2\u0149\u014a\7t\2\2\u014a\66\3\2\2\2\u014b\u014c\7t\2\2\u014c"+
		"\u014d\7q\2\2\u014d\u014e\7o\2\2\u014e\u014f\7r\2\2\u014f\u0150\7g\2\2"+
		"\u0150\u0151\7t\2\2\u01518\3\2\2\2\u0152\u0153\7e\2\2\u0153\u0154\7c\2"+
		"\2\u0154\u0155\7t\2\2\u0155\u0156\7c\2\2\u0156\u0157\7e\2\2\u0157\u0158"+
		"\7v\2\2\u0158\u0159\7g\2\2\u0159\u015a\7t\2\2\u015a:\3\2\2\2\u015b\u015c"+
		"\7e\2\2\u015c\u015d\7c\2\2\u015d\u015e\7f\2\2\u015e\u015f\7g\2\2\u015f"+
		"\u0160\7p\2\2\u0160\u0161\7c\2\2\u0161<\3\2\2\2\u0162\u0163\7t\2\2\u0163"+
		"\u0164\7g\2\2\u0164\u0165\7c\2\2\u0165\u0166\7n\2\2\u0166>\3\2\2\2\u0167"+
		"\u0168\7d\2\2\u0168\u0169\7q\2\2\u0169\u016a\7q\2\2\u016a\u016b\7n\2\2"+
		"\u016b\u016c\7g\2\2\u016c\u016d\7c\2\2\u016d\u016e\7p\2\2\u016e\u016f"+
		"\7q\2\2\u016f@\3\2\2\2\u0170\u0171\7\60\2\2\u0171B\3\2\2\2\u0172\u0173"+
		"\7\61\2\2\u0173\u0174\7,\2\2\u0174\u0178\3\2\2\2\u0175\u0177\13\2\2\2"+
		"\u0176\u0175\3\2\2\2\u0177\u017a\3\2\2\2\u0178\u0179\3\2\2\2\u0178\u0176"+
		"\3\2\2\2\u0179\u017b\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u017c\7,\2\2\u017c"+
		"\u017d\7\61\2\2\u017d\u017e\3\2\2\2\u017e\u017f\b\"\2\2\u017fD\3\2\2\2"+
		"\u0180\u0181\7\61\2\2\u0181\u0182\7\61\2\2\u0182\u0186\3\2\2\2\u0183\u0185"+
		"\n\2\2\2\u0184\u0183\3\2\2\2\u0185\u0188\3\2\2\2\u0186\u0184\3\2\2\2\u0186"+
		"\u0187\3\2\2\2\u0187\u0189\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a\b#"+
		"\2\2\u018aF\3\2\2\2\u018b\u018d\t\3\2\2\u018c\u018b\3\2\2\2\u018d\u018e"+
		"\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0190\3\2\2\2\u0190"+
		"\u0191\b$\2\2\u0191H\3\2\2\2\u0192\u0193\7*\2\2\u0193J\3\2\2\2\u0194\u0195"+
		"\7+\2\2\u0195L\3\2\2\2\u0196\u0197\7#\2\2\u0197N\3\2\2\2\u0198\u0199\7"+
		"?\2\2\u0199\u019d\7?\2\2\u019a\u019b\7#\2\2\u019b\u019d\7?\2\2\u019c\u0198"+
		"\3\2\2\2\u019c\u019a\3\2\2\2\u019dP\3\2\2\2\u019e\u01a5\7>\2\2\u019f\u01a0"+
		"\7>\2\2\u01a0\u01a5\7?\2\2\u01a1\u01a2\7@\2\2\u01a2\u01a5\7?\2\2\u01a3"+
		"\u01a5\7@\2\2\u01a4\u019e\3\2\2\2\u01a4\u019f\3\2\2\2\u01a4\u01a1\3\2"+
		"\2\2\u01a4\u01a3\3\2\2\2\u01a5R\3\2\2\2\u01a6\u01a7\7(\2\2\u01a7\u01ab"+
		"\7(\2\2\u01a8\u01a9\7~\2\2\u01a9\u01ab\7~\2\2\u01aa\u01a6\3\2\2\2\u01aa"+
		"\u01a8\3\2\2\2\u01abT\3\2\2\2\u01ac\u01ad\7=\2\2\u01adV\3\2\2\2\u01ae"+
		"\u01af\7.\2\2\u01afX\3\2\2\2\u01b0\u01b5\t\4\2\2\u01b1\u01b2\7,\2\2\u01b2"+
		"\u01b5\7,\2\2\u01b3\u01b5\7\'\2\2\u01b4\u01b0\3\2\2\2\u01b4\u01b1\3\2"+
		"\2\2\u01b4\u01b3\3\2\2\2\u01b5Z\3\2\2\2\u01b6\u01b7\t\5\2\2\u01b7\\\3"+
		"\2\2\2\u01b8\u01ba\t\6\2\2\u01b9\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb"+
		"\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01bf\t\7"+
		"\2\2\u01be\u01c0\t\6\2\2\u01bf\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1"+
		"\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2^\3\2\2\2\u01c3\u01c5\t\6\2\2"+
		"\u01c4\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7"+
		"\3\2\2\2\u01c7`\3\2\2\2\u01c8\u01cc\7$\2\2\u01c9\u01cb\13\2\2\2\u01ca"+
		"\u01c9\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cc\u01ca\3\2"+
		"\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01cc\3\2\2\2\u01cf\u01d0\7$\2\2\u01d0"+
		"b\3\2\2\2\u01d1\u01d2\7x\2\2\u01d2\u01d3\7g\2\2\u01d3\u01d4\7t\2\2\u01d4"+
		"\u01d5\7f\2\2\u01d5\u01d6\7c\2\2\u01d6\u01d7\7f\2\2\u01d7\u01d8\7g\2\2"+
		"\u01d8\u01d9\7t\2\2\u01d9\u01e0\7q\2\2\u01da\u01db\7h\2\2\u01db\u01dc"+
		"\7c\2\2\u01dc\u01dd\7n\2\2\u01dd\u01de\7u\2\2\u01de\u01e0\7q\2\2\u01df"+
		"\u01d1\3\2\2\2\u01df\u01da\3\2\2\2\u01e0d\3\2\2\2\u01e1\u01e2\7)\2\2\u01e2"+
		"\u01e3\t\b\2\2\u01e3\u01e4\7)\2\2\u01e4f\3\2\2\2\u01e5\u01e9\t\b\2\2\u01e6"+
		"\u01e8\t\t\2\2\u01e7\u01e6\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01e7\3\2"+
		"\2\2\u01e9\u01ea\3\2\2\2\u01eah\3\2\2\2\u01eb\u01e9\3\2\2\2\20\2\u0178"+
		"\u0186\u018e\u019c\u01a4\u01aa\u01b4\u01bb\u01c1\u01c6\u01cc\u01df\u01e9"+
		"\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}