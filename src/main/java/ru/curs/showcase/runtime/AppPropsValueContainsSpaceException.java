package ru.curs.showcase.runtime;

import ru.curs.showcase.app.api.ExceptionType;
import ru.curs.showcase.util.exception.BaseException;

/**
 * Исключение, генерируемое в случае если значение из файла app.properties
 * конкретной userdata содержит пробел.
 * 
 */
public class AppPropsValueContainsSpaceException extends BaseException {
	private static final long serialVersionUID = 2423174720757028625L;

	private static final String ERROR_MES =
		"Userdata '%s'. Файл app.properties содержит параметр %s, в значении которого (%s) присутствует пробел.";

	public AppPropsValueContainsSpaceException(final String aUserDataId, final String param,
			final String value) {
		super(ExceptionType.USER, String.format(ERROR_MES, aUserDataId, param, value));

	}
}
