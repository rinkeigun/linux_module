// コールバックを管理する構造体
typedef struct {
    void *a;
    void (*callback)(void *);
} callback_t;

// コールバックさせたい関数
void g( void *a )
{
    printf("%s\n", (char *)a);
}


// コールバックを初期化登録する関数
int setcallback( callback_t **pp, void (*callback)(void *), void *a )
{
    callback_t *p;
    
    p = malloc( sizeof(callback_t) );
    p->a = a;
    p->callback = callback;
    *pp = p;
    
    return 0;
}

// コールバックの登録を開放する関数
int unsetcallback( callback_t *p )
{
    free(p);
    return 0;
}

// 実際にコールバックする関数
int runcallback( callback_t *p )
{
    (p->callback)( p->a );
    return 0;
}



//-----------------------------------------
// メイン
char *hoge="abcde";
main()
{
    callback_t *p;
 
    setcallback( &p, g, (void *)hoge ); // ★コールバック関数を登録する
   
    runcallback( p );                   // ★コールバック関数を呼んでもらう

    unsetcallback( p );                 // ★後始末

    return 0;
}
