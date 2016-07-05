/*
   2016/07/05	Huiqun.Lin
   install libcurl4-openssl-dev
   wget http://www.digip.org/jansson/releases/jansson-2.7.tar.gz
   tar xvf janssion-2.7.tar.gz
   ./configure
   make
   sudo make install

   gcc  c_json.c -l curl -l jansson

   export LD_LIBRARY_PATH=/usr/local/lib

	./a.out
*/
#include <assert.h>
#include <string.h>
#include <memory.h>
#include <curl/curl.h>
#include <jansson.h>

typedef struct {
   char* data;   // response data from server
   size_t size;  // response size of data
 } MEMFILE;

 MEMFILE*
 memfopen() {
   MEMFILE* mf = (MEMFILE*) malloc(sizeof(MEMFILE));
   if (mf) {
     mf->data = NULL;
     mf->size = 0;
   }
   return mf;
 }

void
 memfclose(MEMFILE* mf) {
   if (mf->data) free(mf->data);
   free(mf);
 }

size_t
 memfwrite(char* ptr, size_t size, size_t nmemb, void* stream) {
   MEMFILE* mf = (MEMFILE*) stream;
   int block = size * nmemb;
   if (!mf) return block; // through
   if (!mf->data)
     mf->data = (char*) malloc(block);
   else
     mf->data = (char*) realloc(mf->data, mf->size + block);
   if (mf->data) {
     memcpy(mf->data + mf->size, ptr, block);
     mf->size += block;
   }
   return block;
 }

char*
 memfstrdup(MEMFILE* mf) {
   char* buf;
   if (mf->size == 0) return NULL;
   buf = (char*) malloc(mf->size + 1);
   memcpy(buf, mf->data, mf->size);
   buf[mf->size] = 0;
   return buf;
 }

int
 main() {
   CURL* curl;
   MEMFILE* mf = NULL;
   char* js = NULL;
   int i;

   mf = memfopen();

   curl = curl_easy_init();
   curl_easy_setopt(curl, CURLOPT_URL, "https://api.github.com/legacy/repos/search/unko");
   curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0);
   curl_easy_setopt(curl, CURLOPT_WRITEDATA, mf);
   curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, memfwrite);
   curl_easy_perform(curl);
   curl_easy_cleanup(curl);

   js = memfstrdup(mf);
   memfclose(mf);

   json_error_t error;
   json_t *result = json_loads(js, 0, &error);
   if (result == NULL) {
     fputs(error.text, stderr);
     goto leave;
   }
   json_t *repositories = json_object_get(result, "repositories");
   json_t *repository;
   json_array_foreach(repositories, i, repository) {
     printf("%s/%s: %s\n",
       json_string_value(json_object_get(repository, "username")),
       json_string_value(json_object_get(repository, "name")),
       json_string_value(json_object_get(repository, "description")));
   }

   json_decref(result);
leave:
   free(js);
 }
