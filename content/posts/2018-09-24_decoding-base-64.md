Title: Decoding Base 64
Date: 2018-09-24

As a core Python developer, I recently worked on [bug #33770: "base64 throws 'incorrect padding' exception when the issue is NOT with the padding"](https://bugs.python.org/issue33770). It turns out that in addition to failing due to invalid characters or missing padding, decodeing base 64 can also fail due to invalid length.

The reason: When encoding with base64, the number of output data bytes (not including '=' padding bytes) may be 0, 2, or 3 more than a multiple of 4, **but never 1**:

Input      | Output       | Length (mod 4)
---------- | ------------ |:-------------:
`""`       | `""`         |       0
`"a"`      | `"YQ=="`     |       2
`"ab"`     | `"YWI="`     |       3
`"abc"`    | `"YWJj"`     |       0
`"abcd"`   | `"YWJjZA=="` |       2
`"abcde"`  | `"YWJjZGU="` |       3
`"abcdef"` | `"YWJjZGVm"` |       0

When attempting to decode base64-encoded data, if the number of data bytes is 1 more than a multiple of 4, there is no possible input that could have resulted in such output. Therefore, such inputs should be rejected as invalid.

## Final Thoughts

Storing or transferring data using *only* base64 encoding is **a bad idea**. A more appropriate format would include some facilities for error detection and/or correction, such as being able to tell whether the encoded data has been truncated. Unfortunately, I can't think of anything nearly as ubiquitous as base64 that includes even basic error detection features. Maybe it's time to create something like this?
