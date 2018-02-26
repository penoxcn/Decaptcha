#include <string.h>
#include "decaptcha.h"
#include "baseapi.h"

using namespace tesseract;

Decaptcha::Decaptcha(const char *datapath, const char *language)
{
	aApi = new TessBaseAPI;
	if(datapath!=NULL && language!=NULL) {
		Init(datapath,language);
	}
}

Decaptcha::~Decaptcha()
{
	delete ((TessBaseAPI *)aApi);
}

void Decaptcha::Init(const char *datapath, const char *language)
{
	((TessBaseAPI *)aApi)->Init(datapath, language);
	((TessBaseAPI *)aApi)->SetVariable("tessedit_char_whitelist", "0123456789");
	((TessBaseAPI *)aApi)->SetVariable("tessedit_write_ratings", "1");
	((TessBaseAPI *)aApi)->SetVariable("tessedit_write_output", "0");
	((TessBaseAPI *)aApi)->SetVariable("tessedit_write_raw_output", "0");
	((TessBaseAPI *)aApi)->SetVariable("tessedit_write_txt_map", "0");
}

void Decaptcha::SetCharList(const char* chs)
{
	((TessBaseAPI *)aApi)->SetVariable("tessedit_char_whitelist", chs);
}

void Decaptcha::End()
{
	((TessBaseAPI *)aApi)->End();
}

void Decaptcha::SetVariable(const char *name, const char *value)
{
	((TessBaseAPI *)aApi)->SetVariable(name, value);
}

char *Decaptcha::Recognize(const /*unsigned*/ char* imagedata,
                      int bytes_per_pixel, int bytes_per_line,
                      int left, int top, int width, int height)
{
	return ((TessBaseAPI *)aApi)->TesseractRect((const unsigned char *)imagedata,bytes_per_pixel,bytes_per_line,left,top,width,height);
}
