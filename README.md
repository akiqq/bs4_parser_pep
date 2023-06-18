# Проект парсинг

## Описание проекта:
###  Проект работающий в разных режимах, с подключённым  логированием и обработкой ошибок, помогающий быть в курсе новостей в мире Python. Он выполняет 4 основных функции:

 1. Собирает ссылки на статьи о нововведениях в Python, переходит по ним и забирает информацию об авторах и редакторах статей.
 2. Собирает информацию о статусах версий Python.
 3. Скачивает архив с актуальной документацией.
 4. Парсит данные обо всех документах PEP:
     * Cохраняет результат в табличном виде в csv-файл.
     * Выводит таблицу с 2-мя колонками «Статус», «Количество» а так же выводит «Total»(общее количество PEP).

## Используемые технологии:
### * Python
### * BeautifulSoup4 - библиотека для парсинга.
### * Prettytable - библиотека для отображения табличных данных.

## Инструкция по развёртыванию проекта:
1. Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:akiqq/bs4_parser_pep.git
```
```
cd bs4_parser_pep
```
2. Создать и активировать виртуальное окружение:
```
pytnon -m venv venv
source venv/Scripts/activate
```

3. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
   * При необходимости обновить pip
   ```
   python3 -m pip install --upgrade pip
   ```

## Примеры команд:
* Вывод ссылок o нововведениях в Python:
```
python main.py whats-new
```
* Создание csv файла с таблицей:
```
python main.py pep -o file
```
* Создание таблицы о статусах версий:


## Примеры работы парсера:

* Вывод ссылок o нововведениях в Python:
```
python main.py whats-new


"18.06.2023 19:03:15 - [INFO] - Парсер запущен!"
"18.06.2023 19:03:15 - [INFO] - Аргументы командной строки: Namespace(mode='whats-new', clear_cache=False, output=None)"
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:01<00:00, 12.44it/s]
Ссылка на статью Заголовок Редактор, Автор
https://docs.python.org/3/whatsnew/3.11.html What’s New In Python 3.11¶  Release 3.11.4  Date June 17, 2023  Editor Pablo Galindo Salgado
https://docs.python.org/3/whatsnew/3.10.html What’s New In Python 3.10¶  Editor Pablo Galindo Salgado
https://docs.python.org/3/whatsnew/3.9.html What’s New In Python 3.9¶  Editor Łukasz Langa
https://docs.python.org/3/whatsnew/3.8.html What’s New In Python 3.8¶  Editor Raymond Hettinger
https://docs.python.org/3/whatsnew/3.7.html What’s New In Python 3.7¶  Editor Elvis Pranskevichus <elvis@magic.io>
https://docs.python.org/3/whatsnew/3.6.html What’s New In Python 3.6¶  Editors Elvis Pranskevichus <elvis@magic.io>, Yury Selivanov <yury@magic.io>
https://docs.python.org/3/whatsnew/3.5.html What’s New In Python 3.5¶  Editors Elvis Pranskevichus <elvis@magic.io>, Yury Selivanov <yury@magic.io>
https://docs.python.org/3/whatsnew/3.4.html What’s New In Python 3.4¶  Author R. David Murray <rdmurray@bitdance.com> (Editor)
https://docs.python.org/3/whatsnew/3.3.html What’s New In Python 3.3¶  PEP 405 - Python Virtual EnvironmentsPEP written by Carl Meyer; implementation by Carl Meyer and Vinay Sajip
https://docs.python.org/3/whatsnew/3.2.html What’s New In Python 3.2¶  Author Raymond Hettinger
https://docs.python.org/3/whatsnew/3.1.html What’s New In Python 3.1¶  Author Raymond Hettinger
https://docs.python.org/3/whatsnew/3.0.html What’s New In Python 3.0¶  Author Guido van Rossum
https://docs.python.org/3/whatsnew/2.7.html What’s New in Python 2.7¶  Author A.M. Kuchling (amk at amk.ca)
https://docs.python.org/3/whatsnew/2.6.html What’s New in Python 2.6¶  Author A.M. Kuchling (amk at amk.ca)
https://docs.python.org/3/whatsnew/2.5.html What’s New in Python 2.5¶  Author A.M. Kuchling
https://docs.python.org/3/whatsnew/2.4.html What’s New in Python 2.4¶  Author A.M. Kuchling
https://docs.python.org/3/whatsnew/2.3.html What’s New in Python 2.3¶  Author A.M. Kuchling
https://docs.python.org/3/whatsnew/2.2.html What’s New in Python 2.2¶  Author A.M. Kuchling
https://docs.python.org/3/whatsnew/2.1.html What’s New in Python 2.1¶  Author A.M. Kuchling
https://docs.python.org/3/whatsnew/2.0.html What’s New in Python 2.0¶  Author A.M. Kuchling and Moshe Zadka
"18.06.2023 19:03:17 - [INFO] - Парсер завершил работу."
```

* Создание таблицы о статусах версий:
```
python main.py latest-versions -o pretty

"18.06.2023 19:04:32 - [INFO] - Парсер запущен!"
"18.06.2023 19:04:32 - [INFO] - Аргументы командной строки: Namespace(mode='latest-versions', clear_cache=False, output='pretty')"
+--------------------------------------+----------------------------+--------+
| Ссылка на документацию               | Версия                     | Статус |
+--------------------------------------+----------------------------+--------+
| https://docs.python.org/3.13/        | ('3.13', 'in development') |        |
| https://docs.python.org/3.12/        | ('3.12', 'pre-release')    |        |
| https://docs.python.org/3.11/        | ('3.11', 'stable')         |        |
| https://docs.python.org/3.10/        | ('3.10', 'security-fixes') |        |
| https://docs.python.org/3.9/         | ('3.9', 'security-fixes')  |        |
| https://docs.python.org/3.8/         | ('3.8', 'security-fixes')  |        |
| https://docs.python.org/3.7/         | ('3.7', 'security-fixes')  |        |
| https://docs.python.org/3.6/         | ('3.6', 'EOL')             |        |
| https://docs.python.org/3.5/         | ('3.5', 'EOL')             |        |
| https://docs.python.org/2.7/         | ('2.7', 'EOL')             |        |
| https://www.python.org/doc/versions/ | All versions               |        |
+--------------------------------------+----------------------------+--------+
"18.06.2023 19:04:32 - [INFO] - Парсер завершил работу."
```

* Вывод данных о всех документах PEP:
```
python main.py whats-new

"18.06.2023 19:07:57 - [INFO] - Парсер запущен!"
"18.06.2023 19:07:57 - [INFO] - Аргументы командной строки: Namespace(mode='pep', clear_cache=False, output=None)"
 36%|█████████████████████████████████████████████████████████████████▉                                                                                                                       | 219/614 [02:33<04:44,  1.39it/s]"18.06.2023 19:10:32 - [INFO] - Несовпадающий статус:https://peps.python.org/pep-0401Статус в карточке: April Fool!Ожидаемые статусы: ('Rejected',)"
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 614/614 [07:06<00:00,  1.44it/s]
PEP PEP Title Status
1 PEP Purpose and Guidelines Active
2 Procedure for Adding New Modules Active
3 Guidelines for Handling Bug Reports Withdrawn
4 Deprecation of Standard Modules Active
5 Guidelines for Language Evolution Active
6 Bug Fix Releases Active
7 Style Guide for C Code Active
8 Style Guide for Python Code Active
9 Sample Plaintext PEP Template Withdrawn
10 Voting Guidelines Active
11 CPython platform support Active
12 Sample reStructuredText PEP Template Active
13 Python Language Governance Active
20 The Zen of Python Active
42 Feature Requests Withdrawn
100 Python Unicode Integration Final
101 Doing Python Releases 101 Active
102 Doing Python Micro Releases Superseded
103 Collecting information about git Withdrawn
160 Python 1.6 Release Schedule Final
200 Python 2.0 Release Schedule Final
201 Lockstep Iteration Final
202 List Comprehensions Final
203 Augmented Assignments Final
204 Range Literals Rejected
205 Weak References Final
206 Python Advanced Library Withdrawn
207 Rich Comparisons Final
208 Reworking the Coercion Model Final
209 Multi-dimensional Arrays Withdrawn
210 Decoupling the Interpreter Loop Rejected
211 Adding A New Outer Product Operator Rejected
212 Loop Counter Iteration Rejected
213 Attribute Access Handlers Deferred
214 Extended Print Statement Final
215 String Interpolation Superseded
216 Docstring Format Rejected
217 Display Hook for Interactive Use Final
218 Adding a Built-In Set Object Type Final
219 Stackless Python Deferred
220 Coroutines, Generators, Continuations Rejected
221 Import As Final
222 Web Library Enhancements Deferred
223 Change the Meaning of x Escapes Final
224 Attribute Docstrings Rejected
225 Elementwise/Objectwise Operators Rejected
226 Python 2.1 Release Schedule Final
227 Statically Nested Scopes Final
228 Reworking Python’s Numeric Model Withdrawn
229 Using Distutils to Build Python Final
230 Warning Framework Final
231 __findattr__() Rejected
232 Function Attributes Final
233 Python Online Help Deferred
234 Iterators Final
235 Import on Case-Insensitive Platforms Final
236 Back to the __future__ Final
237 Unifying Long Integers and Integers Final
238 Changing the Division Operator Final
239 Adding a Rational Type to Python Rejected
240 Adding a Rational Literal to Python Rejected
241 Metadata for Python Software Packages Superseded
242 Numeric Kinds Rejected
243 Module Repository Upload Mechanism Withdrawn
244 The directive statement Rejected
245 Python Interface Syntax Rejected
246 Object Adaptation Rejected
247 API for Cryptographic Hash Functions Final
248 Python Database API Specification v1.0 Final
249 Python Database API Specification v2.0 Final
250 Using site-packages on Windows Final
251 Python 2.2 Release Schedule Final
252 Making Types Look More Like Classes Final
253 Subtyping Built-in Types Final
254 Making Classes Look More Like Types Rejected
255 Simple Generators Final
256 Docstring Processing System Framework Rejected
257 Docstring Conventions Active
258 Docutils Design Specification Rejected
259 Omit printing newline after newline Rejected
260 Simplify xrange() Final
261 Support for “wide” Unicode characters Final
262 A Database of Installed Python Packages Rejected
263 Defining Python Source Code Encodings Final
264 Future statements in simulated shells Final
265 Sorting Dictionaries by Value Rejected
266 Optimizing Global Variable/Attribute Access Withdrawn
267 Optimized Access to Module Namespaces Deferred
268 Extended HTTP functionality and WebDAV Rejected
269 Pgen Module for Python Deferred
270 uniq method for list objects Rejected
271 Prefixing sys.path by command line option Rejected
272 API for Block Encryption Algorithms v1.0 Final
273 Import Modules from Zip Archives Final
274 Dict Comprehensions Final
275 Switching on Multiple Values Rejected
276 Simple Iterator for ints Rejected
277 Unicode file name support for Windows NT Final
278 Universal Newline Support Final
279 The enumerate() built-in function Final
280 Optimizing access to globals Deferred
281 Loop Counter Iteration with range and xrange Rejected
282 A Logging System Final
283 Python 2.3 Release Schedule Final
284 Integer for-loops Rejected
285 Adding a bool type Final
286 Enhanced Argument Tuples Deferred
287 reStructuredText Docstring Format Active
288 Generators Attributes and Exceptions Withdrawn
289 Generator Expressions Final
290 Code Migration and Modernization Active
291 Backward Compatibility for the Python 2 Standard Library Final
292 Simpler String Substitutions Final
293 Codec Error Handling Callbacks Final
294 Type Names in the types Module Rejected
295 Interpretation of multiline string constants Rejected
296 Adding a bytes Object Type Withdrawn
297 Support for System Upgrades Rejected
298 The Locked Buffer Interface Withdrawn
299 Special __main__() function in modules Rejected
301 Package Index and Metadata for Distutils Final
302 New Import Hooks Final
303 Extend divmod() for Multiple Divisors Rejected
304 Controlling Generation of Bytecode Files Withdrawn
305 CSV File API Final
306 How to Change Python’s Grammar Withdrawn
307 Extensions to the pickle protocol Final
308 Conditional Expressions Final
309 Partial Function Application Final
310 Reliable Acquisition/Release Pairs Rejected
311 Simplified Global Interpreter Lock Acquisition for Extensions Final
312 Simple Implicit Lambda Deferred
313 Adding Roman Numeral Literals to Python Rejected
314 Metadata for Python Software Packages 1.1 Superseded
315 Enhanced While Loop Rejected
316 Programming by Contract for Python Deferred
317 Eliminate Implicit Exception Instantiation Rejected
318 Decorators for Functions and Methods Final
319 Python Synchronize/Asynchronize Block Rejected
320 Python 2.4 Release Schedule Final
321 Date/Time Parsing and Formatting Withdrawn
322 Reverse Iteration Final
323 Copyable Iterators Deferred
324 subprocess - New process module Final
325 Resource-Release Support for Generators Rejected
326 A Case for Top and Bottom Values Rejected
327 Decimal Data Type Final
328 Imports: Multi-Line and Absolute/Relative Final
329 Treating Builtins as Constants in the Standard Library Rejected
330 Python Bytecode Verification Rejected
331 Locale-Independent Float/String Conversions Final
332 Byte vectors and String/Unicode Unification Rejected
333 Python Web Server Gateway Interface v1.0 Final
334 Simple Coroutines via SuspendIteration Withdrawn
335 Overloadable Boolean Operators Rejected
336 Make None Callable Rejected
337 Logging Usage in the Standard Library Deferred
338 Executing modules as scripts Final
339 Design of the CPython Compiler Withdrawn
340 Anonymous Block Statements Rejected
341 Unifying try-except and try-finally Final
342 Coroutines via Enhanced Generators Final
343 The “with” Statement Final
344 Exception Chaining and Embedded Tracebacks Superseded
345 Metadata for Python Software Packages 1.2 Superseded
346 User Defined (“with”) Statements Withdrawn
347 Migrating the Python CVS to Subversion Final
348 Exception Reorganization for Python 3.0 Rejected
349 Allow str() to return unicode strings Rejected
350 Codetags Rejected
351 The freeze protocol Rejected
352 Required Superclass for Exceptions Final
353 Using ssize_t as the index type Final
354 Enumerations in Python Superseded
355 Path - Object oriented filesystem paths Rejected
356 Python 2.5 Release Schedule Final
357 Allowing Any Object to be Used for Slicing Final
358 The “bytes” Object Final
359 The “make” Statement Withdrawn
360 Externally Maintained Packages Final
361 Python 2.6 and 3.0 Release Schedule Final
362 Function Signature Object Final
363 Syntax For Dynamic Attribute Access Rejected
364 Transitioning to the Py3K Standard Library Withdrawn
365 Adding the pkg_resources module Rejected
366 Main module explicit relative imports Final
367 New Super Superseded
368 Standard image protocol and class Deferred
369 Post import hooks Withdrawn
370 Per user site-packages directory Final
371 Addition of the multiprocessing package to the standard library Final
372 Adding an ordered dictionary to collections Final
373 Python 2.7 Release Schedule Final
374 Choosing a distributed VCS for the Python project Final
375 Python 3.1 Release Schedule Final
376 Database of Installed Python Distributions Final
377 Allow __enter__() methods to skip the statement body Rejected
378 Format Specifier for Thousands Separator Final
379 Adding an Assignment Expression Withdrawn
380 Syntax for Delegating to a Subgenerator Final
381 Mirroring infrastructure for PyPI Withdrawn
382 Namespace Packages Rejected
383 Non-decodable Bytes in System Character Interfaces Final
384 Defining a Stable ABI Final
385 Migrating from Subversion to Mercurial Final
386 Changing the version comparison module in Distutils Superseded
387 Backwards Compatibility Policy Active
389 argparse - New Command Line Parsing Module Final
390 Static metadata for Distutils Rejected
391 Dictionary-Based Configuration For Logging Final
392 Python 3.2 Release Schedule Final
393 Flexible String Representation Final
394 The “python” Command on Unix-Like Systems Active
395 Qualified Names for Modules Withdrawn
396 Module Version Numbers Rejected
397 Python launcher for Windows Final
398 Python 3.3 Release Schedule Final
399 Pure Python/C Accelerator Module Compatibility Requirements Final
400 Deprecate codecs.StreamReader and codecs.StreamWriter Deferred
401 BDFL Retirement April Fool!
402 Simplified Package Layout and Partitioning Rejected
403 General purpose decorator clause (aka “@in” clause) Deferred
404 Python 2.8 Un-release Schedule Final
405 Python Virtual Environments Final
406 Improved Encapsulation of Import State Withdrawn
407 New release cycle and introducing long-term support versions Deferred
408 Standard library __preview__ package Rejected
409 Suppressing exception context Final
410 Use decimal.Decimal type for timestamps Rejected
411 Provisional packages in the Python standard library Superseded
412 Key-Sharing Dictionary Final
413 Faster evolution of the Python Standard Library Withdrawn
414 Explicit Unicode Literal for Python 3.3 Final
415 Implement context suppression with exception attributes Final
416 Add a frozendict builtin type Rejected
417 Including mock in the Standard Library Final
418 Add monotonic time, performance counter, and process time functions Final
419 Protecting cleanup statements from interruptions Deferred
420 Implicit Namespace Packages Final
421 Adding sys.implementation Final
422 Simpler customisation of class creation Withdrawn
423 Naming conventions and recipes related to packaging Deferred
424 A method for exposing a length hint Final
425 Compatibility Tags for Built Distributions Final
426 Metadata for Python Software Packages 2.0 Withdrawn
427 The Wheel Binary Package Format 1.0 Final
428 The pathlib module – object-oriented filesystem paths Final
429 Python 3.4 Release Schedule Final
430 Migrating to Python 3 as the default online documentation Final
431 Time zone support improvements Superseded
432 Restructuring the CPython startup sequence Withdrawn
433 Easier suppression of file descriptor inheritance Superseded
434 IDLE Enhancement Exception for All Branches Active
435 Adding an Enum type to the Python standard library Final
436 The Argument Clinic DSL Final
437 A DSL for specifying signatures, annotations and argument converters Rejected
438 Transitioning to release-file hosting on PyPI Superseded
439 Inclusion of implicit pip bootstrap in Python installation Rejected
440 Version Identification and Dependency Specification Final
441 Improving Python ZIP Application Support Final
442 Safe object finalization Final
443 Single-dispatch generic functions Final
444 Python Web3 Interface Deferred
445 Add new APIs to customize Python memory allocators Final
446 Make newly created file descriptors non-inheritable Final
447 Add __getdescriptor__ method to metaclass Deferred
448 Additional Unpacking Generalizations Final
449 Removal of the PyPI Mirror Auto Discovery and Naming Scheme Final
450 Adding A Statistics Module To The Standard Library Final
451 A ModuleSpec Type for the Import System Final
452 API for Cryptographic Hash Functions v2.0 Final
453 Explicit bootstrapping of pip in Python installations Final
454 Add a new tracemalloc module to trace Python memory allocations Final
455 Adding a key-transforming dictionary to collections Rejected
456 Secure and interchangeable hash algorithm Final
457 Notation For Positional-Only Parameters Final
458 Secure PyPI downloads with signed repository metadata Accepted
459 Standard Metadata Extensions for Python Software Packages Withdrawn
460 Add binary interpolation and formatting Withdrawn
461 Adding % formatting to bytes and bytearray Final
462 Core development workflow automation for CPython Withdrawn
463 Exception-catching expressions Rejected
464 Removal of the PyPI Mirror Authenticity API Final
465 A dedicated infix operator for matrix multiplication Final
466 Network Security Enhancements for Python 2.7.x Final
467 Minor API improvements for binary sequences Draft
468 Preserving the order of **kwargs in a function. Final
469 Migration of dict iteration code to Python 3 Withdrawn
470 Removing External Hosting Support on PyPI Final
471 os.scandir() function – a better and faster directory iterator Final
472 Support for indexing with keyword arguments Rejected
473 Adding structured data to built-in exceptions Rejected
474 Creating forge.python.org Withdrawn
475 Retry system calls failing with EINTR Final
476 Enabling certificate verification by default for stdlib http clients Final
477 Backport ensurepip (PEP 453) to Python 2.7 Final
478 Python 3.5 Release Schedule Final
479 Change StopIteration handling inside generators Final
480 Surviving a Compromise of PyPI: End-to-end signing of packages Draft
481 Migrate CPython to Git, Github, and Phabricator Withdrawn
482 Literature Overview for Type Hints Final
483 The Theory of Type Hints Final
484 Type Hints Final
485 A Function for testing approximate equality Final
486 Make the Python Launcher aware of virtual environments Final
487 Simpler customisation of class creation Final
488 Elimination of PYO files Final
489 Multi-phase extension module initialization Final
490 Chain exceptions at C level Rejected
491 The Wheel Binary Package Format 1.9 Deferred
492 Coroutines with async and await syntax Final
493 HTTPS verification migration tools for Python 2.7 Final
494 Python 3.6 Release Schedule Final
495 Local Time Disambiguation Final
496 Environment Markers Rejected
497 A standard mechanism for backward compatibility Rejected
498 Literal String Interpolation Final
499 python -m foo should bind sys.modules[‘foo’] in addition to sys.modules[‘__main__’] Deferred
500 A protocol for delegating datetime methods to their tzinfo implementations Rejected
501 General purpose string interpolation Deferred
502 String Interpolation - Extended Discussion Rejected
503 Simple Repository API Final
504 Using the System RNG by default Withdrawn
505 None-aware operators Deferred
506 Adding A Secrets Module To The Standard Library Final
507 Migrate CPython to Git and GitLab Rejected
508 Dependency specification for Python Software Packages Final
509 Add a private version to dict Superseded
510 Specialize functions with guards Rejected
511 API for code transformers Rejected
512 Migrating from hg.python.org to GitHub Final
513 A Platform Tag for Portable Linux Built Distributions Superseded
514 Python registration in the Windows registry Active
515 Underscores in Numeric Literals Final
516 Build system abstraction for pip/conda etc Rejected
517 A build-system independent format for source trees Final
518 Specifying Minimum Build System Requirements for Python Projects Final
519 Adding a file system path protocol Final
520 Preserving Class Attribute Definition Order Final
521 Managing global context via ‘with’ blocks in generators and coroutines Withdrawn
522 Allow BlockingIOError in security sensitive APIs Rejected
523 Adding a frame evaluation API to CPython Final
524 Make os.urandom() blocking on Linux Final
525 Asynchronous Generators Final
526 Syntax for Variable Annotations Final
527 Removing Un(der)used file types/extensions on PyPI Final
528 Change Windows console encoding to UTF-8 Final
529 Change Windows filesystem encoding to UTF-8 Final
530 Asynchronous Comprehensions Final
531 Existence checking operators Withdrawn
532 A circuit breaking protocol and binary operators Deferred
533 Deterministic cleanup for iterators Deferred
534 Improved Errors for Missing Standard Library Modules Deferred
535 Rich comparison chaining Deferred
536 Final Grammar for Literal String Interpolation Deferred
537 Python 3.7 Release Schedule Active
538 Coercing the legacy C locale to a UTF-8 based locale Final
539 A New C-API for Thread-Local Storage in CPython Final
540 Add a new UTF-8 Mode Final
541 Package Index Name Retention Final
542 Dot Notation Assignment In Function Header Rejected
543 A Unified TLS API for Python Withdrawn
544 Protocols: Structural subtyping (static duck typing) Accepted
545 Python Documentation Translations Final
546 Backport ssl.MemoryBIO and ssl.SSLObject to Python 2.7 Rejected
547 Running extension modules using the -m option Deferred
548 More Flexible Loop Control Rejected
549 Instance Descriptors Rejected
550 Execution Context Withdrawn
551 Security transparency in the Python runtime Withdrawn
552 Deterministic pycs Final
553 Built-in breakpoint() Final
554 Multiple Interpreters in the Stdlib Draft
555 Context-local variables (contextvars) Withdrawn
556 Threaded garbage collection Deferred
557 Data Classes Final
558 Defined semantics for locals() Deferred
559 Built-in noop() Rejected
560 Core support for typing module and generic types Accepted
561 Distributing and Packaging Type Information Final
562 Module __getattr__ and __dir__ Final
563 Postponed Evaluation of Annotations Accepted
564 Add new time functions with nanosecond resolution Final
565 Show DeprecationWarning in __main__ Final
566 Metadata for Python Software Packages 2.1 Final
567 Context Variables Final
568 Generator-sensitivity for Context Variables Deferred
569 Python 3.8 Release Schedule Active
570 Python Positional-Only Parameters Final
571 The manylinux2010 Platform Tag Superseded
572 Assignment Expressions Final
573 Module State Access from C Extension Methods Final
574 Pickle protocol 5 with out-of-band data Final
575 Unifying function/method classes Withdrawn
576 Rationalize Built-in function classes Withdrawn
577 Augmented Assignment Expressions Withdrawn
578 Python Runtime Audit Hooks Accepted
579 Refactoring C functions and methods Final
580 The C call protocol Rejected
581 Using GitHub Issues for CPython Accepted
582 Python local packages directory Rejected
583 A Concurrency Memory Model for Python Withdrawn
584 Add Union Operators To dict Final
585 Type Hinting Generics In Standard Collections Final
586 Literal Types Accepted
587 Python Initialization Configuration Final
588 GitHub Issues Migration Plan Draft
589 TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys Accepted
590 Vectorcall: a fast calling protocol for CPython Accepted
591 Adding a final qualifier to typing Accepted
592 Adding “Yank” Support to the Simple API Final
593 Flexible function and variable annotations Accepted
594 Removing dead batteries from the standard library Final
595 Improving bugs.python.org Withdrawn
596 Python 3.9 Release Schedule Active
597 Add optional EncodingWarning Final
598 Introducing incremental feature releases Withdrawn
599 The manylinux2014 Platform Tag Superseded
600 Future ‘manylinux’ Platform Tags for Portable Linux Built Distributions Final
601 Forbid return/break/continue breaking out of finally Rejected
602 Annual Release Cycle for Python Accepted
603 Adding a frozenmap type to collections Draft
604 Allow writing union types as X | Y Accepted
605 A rolling feature release stream for CPython Rejected
606 Python Compatibility Version Rejected
607 Reducing CPython’s Feature Delivery Latency Final
608 Coordinated Python release Rejected
609 Python Packaging Authority (PyPA) Governance Active
610 Recording the Direct URL Origin of installed distributions Final
611 The one million limit Withdrawn
612 Parameter Specification Variables Accepted
613 Explicit Type Aliases Accepted
614 Relaxing Grammar Restrictions On Decorators Final
615 Support for the IANA Time Zone Database in the Standard Library Accepted
616 String methods to remove prefixes and suffixes Final
617 New PEG parser for CPython Accepted
618 Add Optional Length-Checking To zip Final
619 Python 3.10 Release Schedule Active
620 Hide implementation details from the C API Withdrawn
621 Storing project metadata in pyproject.toml Final
622 Structural Pattern Matching Superseded
623 Remove wstr from Unicode Final
624 Remove Py_UNICODE encoder APIs Final
625 Filename of a Source Distribution Accepted
626 Precise line numbers for debugging and other tools. Final
627 Recording installed projects Final
628 Add math.tau Final
629 Versioning PyPI’s Simple API Final
630 Isolating Extension Modules Final
631 Dependency specification in pyproject.toml based on PEP 508 Superseded
632 Deprecate distutils module Accepted
633 Dependency specification in pyproject.toml using an exploded TOML table Rejected
634 Structural Pattern Matching: Specification Accepted
635 Structural Pattern Matching: Motivation and Rationale Final
636 Structural Pattern Matching: Tutorial Final
637 Support for indexing with keyword arguments Rejected
638 Syntactic Macros Draft
639 Improving License Clarity with Better Package Metadata Draft
640 Unused variable syntax Rejected
641 Using an underscore in the version portion of Python 3.10 compatibility tags Rejected
642 Explicit Pattern Syntax for Structural Pattern Matching Rejected
643 Metadata for Package Source Distributions Final
644 Require OpenSSL 1.1.1 or newer Final
645 Allow writing optional types as x? Withdrawn
646 Variadic Generics Accepted
647 User-Defined Type Guards Accepted
648 Extensible customizations of the interpreter at startup Rejected
649 Deferred Evaluation Of Annotations Using Descriptors Accepted
650 Specifying Installer Requirements for Python Projects Withdrawn
651 Robust Stack Overflow Handling Rejected
652 Maintaining the Stable ABI Final
653 Precise Semantics for Pattern Matching Draft
654 Exception Groups and except* Accepted
655 Marking individual TypedDict items as required or potentially-missing Accepted
656 Platform Tag for Linux Distributions Using Musl Final
657 Include Fine Grained Error Locations in Tracebacks Final
658 Serve Distribution Metadata in the Simple Repository API Accepted
659 Specializing Adaptive Interpreter Draft
660 Editable installs for pyproject.toml based builds (wheel based) Final
661 Sentinel Values Draft
662 Editable installs via virtual wheels Rejected
663 Standardizing Enum str(), repr(), and format() behaviors Rejected
664 Python 3.11 Release Schedule Active
665 A file format to list Python dependencies for reproducibility of an application Rejected
666 Reject Foolish Indentation Rejected
667 Consistent views of namespaces Draft
668 Marking Python base environments as “externally managed” Accepted
669 Low Impact Monitoring for CPython Accepted
670 Convert macros to functions in the Python C API Final
671 Syntax for late-bound function argument defaults Draft
672 Unicode-related Security Considerations for Python Active
673 Self Type Accepted
674 Disallow using macros as l-values Deferred
675 Arbitrary Literal String Type Accepted
676 PEP Infrastructure Process Active
677 Callable Type Syntax Rejected
678 Enriching Exceptions with Notes Accepted
679 Allow parentheses in assert statements Draft
680 tomllib: Support for Parsing TOML in the Standard Library Accepted
681 Data Class Transforms Accepted
682 Format Specifier for Signed Zero Final
683 Immortal Objects, Using a Fixed Refcount Accepted
684 A Per-Interpreter GIL Accepted
685 Comparison of extra names for optional distribution dependencies Accepted
686 Make UTF-8 mode default Accepted
687 Isolating modules in the standard library Accepted
688 Making the buffer protocol accessible in Python Accepted
689 Unstable C API tier Final
690 Lazy Imports Rejected
691 JSON-based Simple API for Python Package Indexes Accepted
692 Using TypedDict for more precise **kwargs typing Accepted
693 Python 3.12 Release Schedule Active
694 Upload 2.0 API for Python Package Repositories Draft
695 Type Parameter Syntax Accepted
696 Type defaults for TypeVarLikes Draft
697 Limited C API for Extending Opaque Types Final
698 Override Decorator for Static Typing Accepted
699 Remove private dict version field added in PEP 509 Accepted
700 Additional Fields for the Simple API for Package Indexes Accepted
701 Syntactic formalization of f-strings Accepted
702 Marking deprecations using the type system Draft
703 Making the Global Interpreter Lock Optional in CPython Draft
704 Require virtual environments by default for package installers Withdrawn
705 TypedMapping: Type Hints for Mappings with a Fixed Set of Keys Draft
706 Filter for tarfile.extractall Final
707 A simplified signature for __exit__ and __aexit__ Rejected
708 Extending the Repository API to Mitigate Dependency Confusion Attacks Draft
709 Inlined comprehensions Accepted
710 Recording the provenance of installed packages Draft
711 PyBI: a standard format for distributing Python Binaries Draft
712 Adding a “converter” parameter to dataclasses.field Draft
713 Callable Modules Draft
714 Rename dist-info-metadata in the Simple API Draft
715 Disabling bdist_egg distribution uploads on PyPI Draft
754 IEEE 754 Floating Point Special Values Rejected
801 Reserved Active
3000 Python 3000 Final
3001 Procedure for reviewing and improving standard library modules Withdrawn
3002 Procedure for Backwards-Incompatible Changes Final
3003 Python Language Moratorium Final
3099 Things that will Not Change in Python 3000 Final
3100 Miscellaneous Python 3.0 Plans Final
3101 Advanced String Formatting Final
3102 Keyword-Only Arguments Final
3103 A Switch/Case Statement Rejected
3104 Access to Names in Outer Scopes Final
3105 Make print a function Final
3106 Revamping dict.keys(), .values() and .items() Final
3107 Function Annotations Final
3108 Standard Library Reorganization Final
3109 Raising Exceptions in Python 3000 Final
3110 Catching Exceptions in Python 3000 Final
3111 Simple input built-in in Python 3000 Final
3112 Bytes literals in Python 3000 Final
3113 Removal of Tuple Parameter Unpacking Final
3114 Renaming iterator.next() to iterator.__next__() Final
3115 Metaclasses in Python 3000 Final
3116 New I/O Final
3117 Postfix type declarations Rejected
3118 Revising the buffer protocol Final
3119 Introducing Abstract Base Classes Final
3120 Using UTF-8 as the default source encoding Final
3121 Extension Module Initialization and Finalization Accepted
3122 Delineation of the main module Rejected
3123 Making PyObject_HEAD conform to standard C Final
3124 Overloading, Generic Functions, Interfaces, and Adaptation Deferred
3125 Remove Backslash Continuation Rejected
3126 Remove Implicit String Concatenation Rejected
3127 Integer Literal Support and Syntax Final
3128 BList: A Faster List-like Type Rejected
3129 Class Decorators Final
3130 Access to Current Module/Class/Function Rejected
3131 Supporting Non-ASCII Identifiers Final
3132 Extended Iterable Unpacking Final
3133 Introducing Roles Rejected
3134 Exception Chaining and Embedded Tracebacks Final
3135 New Super Final
3136 Labeled break and continue Rejected
3137 Immutable Bytes and Mutable Buffer Final
3138 String representation in Python 3000 Final
3139 Cleaning out sys and the “interpreter” module Rejected
3140 str(container) should call str(item), not repr(item) Rejected
3141 A Type Hierarchy for Numbers Final
3142 Add a “while” clause to generator expressions Rejected
3143 Standard daemon process library Deferred
3144 IP Address Manipulation Library for the Python Standard Library Final
3145 Asynchronous I/O For subprocess.Popen Withdrawn
3146 Merging Unladen Swallow into CPython Withdrawn
3147 PYC Repository Directories Final
3148 futures - execute computations asynchronously Final
3149 ABI version tagged .so files Final
3150 Statement local namespaces (aka “given” clause) Deferred
3151 Reworking the OS and IO exception hierarchy Final
3152 Cofunctions Rejected
3153 Asynchronous IO support Superseded
3154 Pickle protocol version 4 Final
3155 Qualified name for classes and functions Final
3156 Asynchronous IO Support Rebooted: the “asyncio” Module Final
3333 Python Web Server Gateway Interface v1.0.1 Final
8000 Python Language Governance Proposal Overview Final
8001 Python Governance Voting Process Final
8002 Open Source Governance Survey Final
8010 The Technical Leader Governance Model Rejected
8011 Python Governance Model Lead by Trio of Pythonistas Rejected
8012 The Community Governance Model Rejected
8013 The External Council Governance Model Rejected
8014 The Commons Governance Model Rejected
8015 Organization of the Python community Rejected
8016 The Steering Council Model Accepted
8100 January 2019 Steering Council election Final
8101 2020 Term Steering Council election Final
8102 2021 Term Steering Council election Final
8103 2022 Term Steering Council election Final
8104 2023 Term Steering Council election Active
PEP in total = 614
Active in total = 31
April Fool! in total = 1
Accepted in total = 49
Deferred in total = 37
Draft in total = 25
Final in total = 273
Provisional in total = 0
Rejected in total = 122
Superseded in total = 20
Withdrawn in total = 56
"18.06.2023 19:15:05 - [INFO] - Парсер завершил работу."
```