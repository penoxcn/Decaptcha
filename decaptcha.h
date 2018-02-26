#include <stdlib.h>

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
 /**
   * Recognize a rectangle from an image and return the result as a string.
   * May be called many times for a single Init.
   * Currently has no error checking.
   * Greyscale of 8 and color of 24 or 32 bits per pixel may be given.
   * Palette color images will not work properly and must be converted to
   * 24 bit.
   * Binary images of 1 bit per pixel may also be given but they must be
   * byte packed with the MSB of the first byte being the first pixel, and a
   * 1 represents WHITE. For binary images set bytes_per_pixel=0.
   * The recognized text is returned as a char* which is coded
   * as UTF8 and must be freed with the delete [] operator.
   *
   * Note that TesseractRect is the simplified convenience interface.
   * For advanced uses, use SetImage, (optionally) SetRectangle, Recognize,
   * and one or more of the Get*Text functions below.
   */
  //char* TesseractRect(const unsigned char* imagedata,
   //                   int bytes_per_pixel, int bytes_per_line,
   //                   int left, int top, int width, int height);
	char *Recognize(const /*unsigned*/ char* imagedata,
                      int bytes_per_pixel, int bytes_per_line,
                      int left, int top, int width, int height);
};
