from preprocess_seroetr import utils

__version__="0.0.6"

def get_word_counts(x):
	return utils._get_word_counts(x)

def get_char_counts(x):
	return utils._get_char_counts(x)

def get_average_word_len(x):
	return utils._get_average_word_len(x)

def get_stopwords_counts(x):
	return utils._get_stopwords_counts(x)

def get_hashtag_counts(x):
	return utils._get_hashtag_counts(x)

def get_mentions_counts(x):
	return utils._get_mentions_counts(x)

def get_digit_counts(x):
	return utils._get_digit_counts(x)

def get_mentions_counts(x):
	return utils._get_mentions_counts(x)

def get_uppercase_counts(x):
	return utils._get_uppercase_counts(x)

def get_cont_to_exp(x):
	return utils._get_cont_to_exp(x)

def get_emails(x):
	return utils._get_emails(x)

def get_urls(x):
	return utils._get_urls(x)

def remove_urls(x):
	return utils._remove_urls(x)

def remove_rt(x):
	return utils._remove_rt(x)

def remove_special_chars(x):
	return utils._remove_special_chars(x)

def remove_html_tags(x):
	return utils._remove_html_tags(x)

def remove_accented_chars(x):
	return utils._remove_accented_chars(x)

def remove_stopwords(x):
	return utils._remove_stopwords(x)

def make_base(x):
	return utils._make_base(x)

def get_value_counts(df, col):
	return utils._get_value_counts(df, col)

def remove_common_words(x, freq, n=20):
	return utils._remove_common_words(x, freq, n)

def remove_rare_words(x, freq, n=20):
	return utils._remove_rare_words(x, freq, n)

def spelling_correction(x):
	return utils._spelling_correction(x)
