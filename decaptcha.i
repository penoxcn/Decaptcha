%module decaptcha
%{
#include "decaptcha.h"
%}

class Decaptcha {
private:
	void *aApi;
public:
	Decaptcha(const char *datapath=NULL, const char *language=NULL);
	~Decaptcha();
	void SetCharList(const char* chs);
	void SetVariable(const char *name, const char *value);
	void Init(const char *datapath, const char *language);
	void End();
  char *Recognize(const /*unsigned*/ char* imagedata,
                      int bytes_per_pixel, int bytes_per_line,
                      int left, int top, int width, int height);
};