Title: Decoding Base 64 is Surprisingly Complex
Date: 2018-09-24

As a core Python developer, I recently worked on [bug #33770: "base64 throws 'incorrect padding' exception when the issue is NOT with the padding"](https://bugs.python.org/issue33770). It turns out that in addition to failing due to invalid characters or missing padding, base64-decoding can also fail due to invalid length.

<!---When encoding some data with base64, every output byte encodes up to 6 bits of the input data. Since the input is made up of 8-bit characters, i.e. bytes, this means that each 3 input bytes are encoded as 4 output bytes. What if the input's length isn't a multiple of 3?--->

<!---1. If it is 1 more than a multiple of 3, then the first 6 bits are encoded in one output byte, and the last 2 bits are encoded in another.--->
<!---2. If it is 2 more than a multiple of 3, then the first 12 bit are encoded in two output bytes, and the last 4 bits are encoded in another.--->

<!---This result is that the number of output bytes may be 0, 2, or 3 more than a multiple of 4. *But never 1 more than a multiple of 4!*--->

It turns out that the number of output data bytes (not including '=' padding bytes) may be 0, 2, or 3 more than a multiple of 4, **but never 1**:

Input       | Output        | Length (mod 4)
----------- | ------------- |:-------------:
`b''`       | `b''`         |       0
`b'a'`      | `b'YQ=='`     |       2
`b'ab`      | `b'YWI='`     |       3
`b'abc'`    | `b'YWJj'`     |       0
`b'abcd'`   | `b'YWJjZA=='` |       2
`b'abcde'`  | `b'YWJjZGU='` |       3
`b'abcdef'` | `b'YWJjZGVm'` |       0

Therefore, when attempting to decode base64-encoded data, if the number of data bytes is 1 more than a multiple of 4, there is no possible input that could have resulted in such output.

## Final Thoughts

Storing or transferring data using *only* base64 encoding is **a bad idea**. A more appropriate format would include some facilities for error detection and/or correction. Unfortunately, I can't think of anything nearly as ubiquitous as base64 that includes even basic error detection features. Maybe it's time to create something like this?
