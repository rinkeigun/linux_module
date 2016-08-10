/* fuga.h */
#ifndef FUGA_H
#define FUGA_H

struct hoge_t; /* 前方宣言 */

typedef struct fuga_t
{
	struct hoge_t* hoge;
} Fuga;

#endif

